import os
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Protocol
from uuid import UUID

import jwt
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import PyJWKClient

load_dotenv(Path(__file__).resolve().parents[2] / '.env')


@dataclass(frozen=True)
class OIDCSettings:
    issuer: str
    audience: str
    jwks_url: str
    organization_claim: str

    @classmethod
    def from_environment(cls) -> 'OIDCSettings | None':
        issuer = os.getenv('OIDC_ISSUER')
        audience = os.getenv('OIDC_AUDIENCE')
        if not issuer or not audience:
            return None

        return cls(
            issuer=issuer,
            audience=audience,
            jwks_url=os.getenv(
                'OIDC_JWKS_URL',
                f'{issuer.rstrip("/")}/protocol/openid-connect/certs',
            ),
            organization_claim=os.getenv('OIDC_ORGANIZATION_CLAIM', 'organization_ids'),
        )


@dataclass(frozen=True)
class Principal:
    subject: str
    organization_ids: frozenset[UUID]


class SigningKey(Protocol):
    key: object


class JwksProvider(Protocol):
    def get_signing_key_from_jwt(self, token: str) -> SigningKey: ...


bearer_scheme = HTTPBearer(auto_error=False)


def decode_access_token(
    token: str,
    settings: OIDCSettings,
    jwks_client: JwksProvider,
) -> Principal:
    try:
        signing_key = jwks_client.get_signing_key_from_jwt(token)
        claims = jwt.decode(
            token,
            signing_key.key,
            algorithms=['RS256'],
            audience=settings.audience,
            issuer=settings.issuer,
            options={'require': ['exp', 'iat', 'sub']},
            leeway=30,
        )
    except jwt.PyJWTError as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid bearer token.',
            headers={'WWW-Authenticate': 'Bearer'},
        ) from error

    subject = claims.get('sub')
    if not isinstance(subject, str) or not subject:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid bearer token.')

    raw_organizations = claims.get(settings.organization_claim)
    if isinstance(raw_organizations, str):
        raw_organizations = [raw_organizations]
    if not isinstance(raw_organizations, list) or not raw_organizations:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='No organization membership is present.')

    try:
        organization_ids = frozenset(UUID(value) for value in raw_organizations)
    except (TypeError, ValueError, AttributeError) as error:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Organization membership is invalid.') from error

    return Principal(subject=subject, organization_ids=organization_ids)


@lru_cache(maxsize=4)
def _jwks_client(url: str) -> PyJWKClient:
    return PyJWKClient(url)


def get_current_principal(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
) -> Principal:
    if credentials is None or credentials.scheme.lower() != 'bearer':
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Bearer authentication is required.',
            headers={'WWW-Authenticate': 'Bearer'},
        )

    settings = OIDCSettings.from_environment()
    if settings is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='OIDC authentication is not configured.',
        )

    try:
        return decode_access_token(
            credentials.credentials,
            settings,
            _jwks_client(settings.jwks_url),
        )
    except jwt.PyJWKClientError as error:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='The OIDC signing keys are unavailable.',
        ) from error


def require_organization_access(
    organization_id: UUID,
    principal: Principal = Depends(get_current_principal),
) -> UUID:
    if organization_id not in principal.organization_ids:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='The authenticated user is not a member of this organization.',
        )
    return organization_id
