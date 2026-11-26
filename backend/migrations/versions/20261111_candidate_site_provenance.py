"""Add user-provided provenance notes to candidate sites.

Revision ID: 20261111_candidate_provenance
Revises: 20261110_tenant_rls
Create Date: 2026-11-11
"""

from alembic import op
import sqlalchemy as sa


revision = '20261111_candidate_provenance'
down_revision = '20261110_tenant_rls'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'candidate_sites',
        sa.Column('provenance_note', sa.Text(), nullable=True),
    )


def downgrade() -> None:
    op.drop_column('candidate_sites', 'provenance_note')
