# Retail Site Selection

A data-driven retail location intelligence solution for evaluating potential showroom locations in Sri Lanka using geospatial analysis, commercial indicators, competitor insight, and existing outlet network coverage.

## Project status

This repository has been initialized as Phase 1 scaffolding for the proposed architecture:

- Frontend: React + TypeScript + Vite
- Backend: Python + FastAPI
- Database: PostgreSQL/PostGIS with SQLAlchemy/Alembic patterns
- Data model: synthetic, clearly labelled demo data only

## Repository structure

- `frontend/` — Vite React application shell and guided assessment UI
- `backend/` — FastAPI API and service layer
- `database/` — PostGIS initialisation support
- `prompt files/` — frozen foundation and implementation instructions
- `implementation/` — current task tracking

## Local development

1. Install frontend dependencies:
   npm install --prefix frontend
2. Install backend dependencies:
   py -3.12 -m venv backend/.venv
   backend/.venv/Scripts/python -m pip install -r backend/requirements.txt
3. Configure the local database:
   Copy `.env.example` to `.env`. Set `DATABASE_URL` to a PostgreSQL administrator URL for migrations and create the `retail_site_selection` database if needed.
4. Apply the schema and PostGIS extension:
   Set-Location backend
   .venv/Scripts/alembic upgrade head
5. Configure a restricted application database login:
   Create a non-superuser login role, grant it membership in `retail_site_app`, and set `APP_DATABASE_URL` to that login in `.env`. Do not run the application as the PostgreSQL administrator.
6. Configure Keycloak before enabling protected routes:
   Set `OIDC_ISSUER`, `OIDC_AUDIENCE`, and optionally `OIDC_JWKS_URL`. Configure access tokens with an `organization_ids` claim containing the user's authorized organization UUIDs.
7. Start the backend:
   Set-Location ..
   $env:PYTHONPATH = (Get-Location).Path
   backend/.venv/Scripts/python -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
8. Start the frontend:
   npm run dev --prefix frontend

## Notes

This scaffold intentionally avoids real organisation-specific data, paid integrations, and protected operational assumptions. It is a minimal implementation foundation aligned with the project’s governing instructions and technical architecture.

The tenant security migration adds organization ownership, cross-organization foreign-key constraints, and PostgreSQL row-level security. It refuses to migrate populated tenant tables without an explicit data-assignment plan. The application uses a separate restricted database URL so RLS is not bypassed by a superuser connection.

Run backend unit tests from `backend/` with:

```powershell
python -m unittest discover -s tests -v
```

To include the local PostgreSQL RLS integration tests, set `$env:RUN_DATABASE_SECURITY_TESTS = '1'` first. The OIDC tests use signed local test tokens; they do not establish that a Keycloak realm has been configured or reached.
