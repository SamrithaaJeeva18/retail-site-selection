import os
from pathlib import Path
from typing import Generator
from uuid import UUID

from dotenv import load_dotenv
from fastapi import Depends
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from .auth import Principal, require_organization_access

load_dotenv(Path(__file__).resolve().parents[2] / '.env')

database_url = os.getenv('APP_DATABASE_URL')
if not database_url:
    raise RuntimeError('APP_DATABASE_URL must be set for the application database connection.')

engine = create_engine(database_url, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_tenant_db(
    organization_id: UUID = Depends(require_organization_access),
    db: Session = Depends(get_db),
) -> Generator[Session, None, None]:
    db.execute(
        text("SELECT set_config('app.current_organization_id', :organization_id, true)"),
        {'organization_id': str(organization_id)},
    )
    yield db
