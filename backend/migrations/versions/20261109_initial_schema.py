"""Initial schema for retail site selection data.

Revision ID: 20261109_initial
Revises:
Create Date: 2026-11-09 16:00:00.000000

"""

from alembic import op
from geoalchemy2 import Geography
import sqlalchemy as sa


revision = '20261109_initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute('CREATE EXTENSION IF NOT EXISTS postgis;')
    op.create_table(
        'business_profiles',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('organisation_name', sa.String(length=255), nullable=False),
        sa.Column('business_type', sa.String(length=255), nullable=True),
        sa.Column('outlet_format', sa.String(length=255), nullable=True),
    )
    op.create_table(
        'assessments',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('objective', sa.Text(), nullable=True),
        sa.Column('geographic_scope', sa.Text(), nullable=True),
        sa.Column('status', sa.String(length=64), nullable=False, server_default='draft'),
        sa.Column('business_profile_id', sa.Integer(), sa.ForeignKey('business_profiles.id'), nullable=True),
    )
    op.create_table(
        'candidate_sites',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('assessment_id', sa.Integer(), sa.ForeignKey('assessments.id'), nullable=True),
        sa.Column('site_name', sa.String(length=255), nullable=False),
        sa.Column('geog', Geography(geometry_type='POINT', srid=4326, spatial_index=False), nullable=True),
        sa.Column('confidence_score', sa.Numeric(precision=5, scale=2), nullable=True),
        sa.Column('notes', sa.Text(), nullable=True),
    )
    op.create_index(
        'idx_candidate_sites_geog',
        'candidate_sites',
        ['geog'],
        unique=False,
        postgresql_using='gist',
    )


def downgrade() -> None:
    op.drop_index('idx_candidate_sites_geog', table_name='candidate_sites')
    op.drop_table('candidate_sites')
    op.drop_table('assessments')
    op.drop_table('business_profiles')
