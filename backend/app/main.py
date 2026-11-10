from uuid import UUID

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select, text
from sqlalchemy.orm import Session

from .database import get_db, get_tenant_db
from .models import Assessment

app = FastAPI(title='Retail Site Selection API', version='0.1.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/health')
def health() -> dict[str, str]:
    return {
        'status': 'ok',
        'service': 'retail-site-selection-api',
        'environment': 'development',
    }


@app.get('/health/database')
def database_health(db: Session = Depends(get_db)) -> dict[str, str]:
    db.execute(text('SELECT 1'))
    return {'status': 'ok', 'database': 'connected'}


@app.get('/api/assessments')
def list_assessments() -> list[dict[str, str]]:
    return [
        {
            'name': 'Central Colombo expansion',
            'region': 'Colombo District',
            'status': 'Ready for analysis',
            'confidence': 'Moderate',
        },
        {
            'name': 'Kandy showroom review',
            'region': 'Kandy District',
            'status': 'Draft',
            'confidence': 'Pending',
        },
        {
            'name': 'Galle outlet coverage',
            'region': 'Galle District',
            'status': 'Results available',
            'confidence': 'High',
        },
    ]


@app.get('/api/organizations/{organization_id}/assessments')
def list_organization_assessments(
    organization_id: UUID,
    db: Session = Depends(get_tenant_db),
) -> list[dict[str, int | str]]:
    assessments = db.scalars(
        select(Assessment)
        .where(Assessment.organization_id == organization_id)
        .order_by(Assessment.id)
    ).all()
    return [
        {
            'id': assessment.id,
            'name': assessment.name,
            'status': assessment.status,
        }
        for assessment in assessments
    ]
