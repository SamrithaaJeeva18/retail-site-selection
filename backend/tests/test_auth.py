from datetime import datetime, timedelta, timezone
from types import SimpleNamespace
import unittest
from uuid import uuid4

import jwt
from cryptography.hazmat.primitives.asymmetric import rsa
from fastapi import HTTPException

from app.auth import OIDCSettings, Principal, decode_access_token, require_organization_access


class StaticJwksClient:
    def __init__(self, key: object) -> None:
        self.key = key

    def get_signing_key_from_jwt(self, token: str) -> SimpleNamespace:
        return SimpleNamespace(key=self.key)


class OidcTokenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        cls.public_key = cls.private_key.public_key()
        cls.settings = OIDCSettings(
            issuer='https://identity.example.test/realms/retail',
            audience='retail-site-selection-api',
            jwks_url='https://identity.example.test/realms/retail/protocol/openid-connect/certs',
            organization_claim='organization_ids',
        )

    def _token(self, claims: dict[str, object]) -> str:
        now = datetime.now(timezone.utc)
        token_claims = {
            'iss': self.settings.issuer,
            'aud': self.settings.audience,
            'sub': 'user-123',
            'iat': now,
            'exp': now + timedelta(minutes=5),
            **claims,
        }
        return jwt.encode(token_claims, self.private_key, algorithm='RS256', headers={'kid': 'test'})

    def test_valid_token_produces_organization_principal(self) -> None:
        organization_id = uuid4()
        principal = decode_access_token(
            self._token({'organization_ids': [str(organization_id)]}),
            self.settings,
            StaticJwksClient(self.public_key),
        )
        self.assertEqual(principal.subject, 'user-123')
        self.assertEqual(principal.organization_ids, frozenset({organization_id}))

    def test_wrong_audience_is_rejected(self) -> None:
        token = self._token({'organization_ids': [str(uuid4())], 'aud': 'other-api'})
        with self.assertRaises(HTTPException) as error:
            decode_access_token(token, self.settings, StaticJwksClient(self.public_key))
        self.assertEqual(error.exception.status_code, 401)

    def test_missing_organization_claim_is_rejected(self) -> None:
        with self.assertRaises(HTTPException) as error:
            decode_access_token(self._token({}), self.settings, StaticJwksClient(self.public_key))
        self.assertEqual(error.exception.status_code, 403)

    def test_user_cannot_select_an_unassigned_organization(self) -> None:
        assigned = uuid4()
        unassigned = uuid4()
        principal = Principal(subject='user-123', organization_ids=frozenset({assigned}))
        with self.assertRaises(HTTPException) as error:
            require_organization_access(unassigned, principal)
        self.assertEqual(error.exception.status_code, 403)


if __name__ == '__main__':
    unittest.main()
