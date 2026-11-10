import json
import os
import socket
import threading
import time
import unittest
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, quote
from urllib.request import Request, urlopen
from uuid import UUID, uuid4

from dotenv import dotenv_values
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
import uvicorn
from sqlalchemy import create_engine, text

from app.auth import OIDCSettings, get_current_principal, require_organization_access


@unittest.skipUnless(
    os.getenv('RUN_KEYCLOAK_INTEGRATION_TESTS') == '1',
    'Set RUN_KEYCLOAK_INTEGRATION_TESTS=1 to run live Keycloak tests.',
)
class KeycloakIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.issuer = os.environ.get('OIDC_ISSUER')
        cls.audience = os.environ.get('OIDC_AUDIENCE')
        cls.client_id = os.environ.get('KEYCLOAK_TEST_CLIENT_ID')
        cls.negative_client_id = os.environ.get('KEYCLOAK_NEGATIVE_CLIENT_ID')
        cls.member_username = os.environ.get('KEYCLOAK_TEST_MEMBER_USERNAME')
        cls.member_password = os.environ.get('KEYCLOAK_TEST_MEMBER_PASSWORD')
        cls.unassigned_username = os.environ.get('KEYCLOAK_TEST_UNASSIGNED_USERNAME')
        cls.unassigned_password = os.environ.get('KEYCLOAK_TEST_UNASSIGNED_PASSWORD')
        cls.organization_id = os.environ.get('KEYCLOAK_TEST_ORGANIZATION_ID')
        cls.other_organization_id = os.environ.get('KEYCLOAK_OTHER_ORGANIZATION_ID')

        required = (
            cls.issuer,
            cls.audience,
            cls.client_id,
            cls.negative_client_id,
            cls.member_username,
            cls.member_password,
            cls.unassigned_username,
            cls.unassigned_password,
            cls.organization_id,
            cls.other_organization_id,
        )
        if not all(required):
            raise RuntimeError('Keycloak integration test settings are incomplete in the local environment.')

        cls.settings = OIDCSettings.from_environment()
        if cls.settings is None:
            raise RuntimeError('OIDC_ISSUER and OIDC_AUDIENCE must be configured.')
        cls.organization_id = UUID(cls.organization_id)
        cls.other_organization_id = UUID(cls.other_organization_id)

        database_url = dotenv_values(Path(__file__).resolve().parents[2] / '.env').get('DATABASE_URL')
        if not database_url:
            raise RuntimeError('DATABASE_URL is required for Keycloak API integration tests.')
        cls._database_engine = create_engine(database_url, future=True)
        cls.addClassCleanup(cls._database_engine.dispose)
        cls._member_assessment_name = f'keycloak-api-test-{uuid4()}'
        cls._other_assessment_name = f'keycloak-api-test-{uuid4()}'
        cls._member_organization_name = f'keycloak-api-test-org-{uuid4()}'
        cls._other_organization_name = f'keycloak-api-test-org-{uuid4()}'
        cls._seed_api_test_data()
        cls.addClassCleanup(cls._remove_api_test_data)

        from app.main import app

        cls._api_server = uvicorn.Server(
            uvicorn.Config(app, log_level='error', access_log=False)
        )
        cls._api_socket = socket.socket()
        cls._api_socket.bind(('127.0.0.1', 0))
        cls._api_socket.listen()
        cls._api_url = f'http://127.0.0.1:{cls._api_socket.getsockname()[1]}'
        cls._api_thread = threading.Thread(
            target=cls._api_server.run,
            kwargs={'sockets': [cls._api_socket]},
            daemon=True,
        )
        cls.addClassCleanup(cls._stop_api_server)
        cls._api_thread.start()
        deadline = time.monotonic() + 10
        while not cls._api_server.started and cls._api_thread.is_alive():
            if time.monotonic() >= deadline:
                cls._api_server.should_exit = True
                cls._api_thread.join(timeout=5)
                raise RuntimeError('The API server did not start for Keycloak integration tests.')
            time.sleep(0.05)

    @classmethod
    def _seed_api_test_data(cls) -> None:
        organization_names = {
            cls.organization_id: cls._member_organization_name,
            cls.other_organization_id: cls._other_organization_name,
        }
        assessment_names = {
            cls.organization_id: cls._member_assessment_name,
            cls.other_organization_id: cls._other_assessment_name,
        }
        with cls._database_engine.begin() as connection:
            existing_organizations = set(
                connection.scalars(
                    text('SELECT id FROM organizations WHERE id IN (:member, :other)'),
                    {'member': cls.organization_id, 'other': cls.other_organization_id},
                )
            )
            for organization_id, name in organization_names.items():
                if organization_id not in existing_organizations:
                    connection.execute(
                        text('INSERT INTO organizations (id, name) VALUES (:id, :name)'),
                        {'id': organization_id, 'name': name},
                    )
                connection.execute(
                    text(
                        'INSERT INTO assessments (organization_id, name, status) '
                        'VALUES (:organization_id, :name, :status)'
                    ),
                    {
                        'organization_id': organization_id,
                        'name': assessment_names[organization_id],
                        'status': 'draft',
                    },
                )

    @classmethod
    def _remove_api_test_data(cls) -> None:
        with cls._database_engine.begin() as connection:
            connection.execute(
                text('DELETE FROM assessments WHERE name IN (:member, :other)'),
                {
                    'member': cls._member_assessment_name,
                    'other': cls._other_assessment_name,
                },
            )
            connection.execute(
                text(
                    'DELETE FROM organizations '
                    'WHERE (id = :member_id AND name = :member_name) '
                    'OR (id = :other_id AND name = :other_name)'
                ),
                {
                    'member_id': cls.organization_id,
                    'member_name': cls._member_organization_name,
                    'other_id': cls.other_organization_id,
                    'other_name': cls._other_organization_name,
                },
            )

    @classmethod
    def _stop_api_server(cls) -> None:
        cls._api_server.should_exit = True
        cls._api_thread.join(timeout=10)
        if cls._api_thread.is_alive():
            raise RuntimeError('The API server did not stop after Keycloak integration tests.')

    @classmethod
    def _access_token(cls, username: str, password: str, client_id: str) -> str:
        token_url = f'{cls.issuer.rstrip("/")}/protocol/openid-connect/token'
        request = Request(
            token_url,
            data=urlencode(
                {
                    'grant_type': 'password',
                    'client_id': client_id,
                    'username': username,
                    'password': password,
                    'scope': 'openid',
                }
            ).encode(),
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            method='POST',
        )
        try:
            with urlopen(request, timeout=10) as response:
                token_response = json.load(response)
        except HTTPError as error:
            raise RuntimeError(
                f'Keycloak token request failed with HTTP {error.code}; verify local test-client credentials and grants.'
            ) from error
        except URLError as error:
            raise RuntimeError('Keycloak token endpoint is not reachable at the configured issuer.') from error

        access_token = token_response.get('access_token')
        if not isinstance(access_token, str) or not access_token:
            raise RuntimeError('Keycloak returned no access token.')
        return access_token

    @classmethod
    def _member_token(cls, client_id: str | None = None) -> str:
        return cls._access_token(
            cls.member_username,
            cls.member_password,
            client_id or cls.client_id,
        )

    @classmethod
    def _unassigned_token(cls) -> str:
        return cls._access_token(
            cls.unassigned_username,
            cls.unassigned_password,
            cls.client_id,
        )

    @classmethod
    def _api_get(cls, organization_id: UUID, token: str | None = None) -> tuple[int, object]:
        request = Request(
            f'{cls._api_url}/api/organizations/{quote(str(organization_id))}/assessments',
            headers={'Authorization': f'Bearer {token}'} if token else {},
        )
        try:
            with urlopen(request, timeout=10) as response:
                return response.status, json.load(response)
        except HTTPError as error:
            with error:
                return error.code, json.load(error)

    @staticmethod
    def _principal(token: str):
        return get_current_principal(
            HTTPAuthorizationCredentials(scheme='Bearer', credentials=token)
        )

    def test_keycloak_issued_token_is_accepted_for_assigned_organization(self) -> None:
        principal = self._principal(self._member_token())
        self.assertIn(self.organization_id, principal.organization_ids)
        self.assertEqual(
            require_organization_access(self.organization_id, principal),
            self.organization_id,
        )

    def test_keycloak_issued_token_without_api_audience_is_rejected(self) -> None:
        with self.assertRaises(HTTPException) as error:
            self._principal(self._member_token(self.negative_client_id))
        self.assertEqual(error.exception.status_code, 401)

    def test_keycloak_issued_token_without_membership_is_forbidden(self) -> None:
        with self.assertRaises(HTTPException) as error:
            self._principal(self._unassigned_token())
        self.assertEqual(error.exception.status_code, 403)

    def test_member_cannot_access_a_different_organization(self) -> None:
        principal = self._principal(self._member_token())
        with self.assertRaises(HTTPException) as error:
            require_organization_access(self.other_organization_id, principal)
        self.assertEqual(error.exception.status_code, 403)

    def test_api_lists_assessments_for_an_assigned_organization(self) -> None:
        status, response = self._api_get(
            self.organization_id,
            self._member_token(),
        )
        self.assertEqual(status, 200)
        self.assertIsInstance(response, list)
        self.assertEqual(
            [assessment['name'] for assessment in response],
            [self._member_assessment_name],
        )

    def test_api_rejects_a_member_for_another_organization(self) -> None:
        status, _ = self._api_get(
            self.other_organization_id,
            self._member_token(),
        )
        self.assertEqual(status, 403)

    def test_api_rejects_a_user_without_organization_membership(self) -> None:
        status, _ = self._api_get(
            self.organization_id,
            self._unassigned_token(),
        )
        self.assertEqual(status, 403)

    def test_api_rejects_a_token_without_the_api_audience(self) -> None:
        status, _ = self._api_get(
            self.organization_id,
            self._member_token(self.negative_client_id),
        )
        self.assertEqual(status, 401)

    def test_api_rejects_requests_without_a_bearer_token(self) -> None:
        status, _ = self._api_get(self.organization_id)
        self.assertEqual(status, 401)


if __name__ == '__main__':
    unittest.main()
