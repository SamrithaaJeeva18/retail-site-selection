"""Add organization ownership and PostgreSQL row-level security.

Revision ID: 20261110_tenant_rls
Revises: 20261109_initial
Create Date: 2026-11-10
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = '20261110_tenant_rls'
down_revision = '20261109_initial'
branch_labels = None
depends_on = None


TENANT_TABLES = ('business_profiles', 'assessments', 'candidate_sites')


def _require_empty_tenant_tables() -> None:
    connection = op.get_bind()
    for table_name in TENANT_TABLES:
        has_rows = connection.scalar(
            sa.text(f'SELECT EXISTS (SELECT 1 FROM {table_name} LIMIT 1)')
        )
        if has_rows:
            raise RuntimeError(
                f'{table_name} contains data. Assign each existing record to an approved '
                'organization before applying tenant isolation.'
            )


def _create_application_role() -> None:
    op.execute(
        """
        DO $$
        BEGIN
            IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'retail_site_app') THEN
                CREATE ROLE retail_site_app
                    NOLOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE NOBYPASSRLS;
            ELSIF EXISTS (
                SELECT 1
                FROM pg_roles
                WHERE rolname = 'retail_site_app'
                  AND (rolcanlogin OR rolsuper OR rolbypassrls)
            ) THEN
                RAISE EXCEPTION
                    'Role retail_site_app exists with unsafe attributes; review it before migration.';
            END IF;
        END
        $$;
        """
    )


def _enable_tenant_rls(table_name: str) -> None:
    op.execute(sa.text(f'ALTER TABLE {table_name} ENABLE ROW LEVEL SECURITY'))
    op.execute(sa.text(f'ALTER TABLE {table_name} FORCE ROW LEVEL SECURITY'))
    op.execute(
        sa.text(
            f"""
            CREATE POLICY {table_name}_organization_isolation
            ON {table_name}
            FOR ALL
            USING (
                organization_id =
                NULLIF(current_setting('app.current_organization_id', true), '')::uuid
            )
            WITH CHECK (
                organization_id =
                NULLIF(current_setting('app.current_organization_id', true), '')::uuid
            )
            """
        )
    )


def upgrade() -> None:
    _require_empty_tenant_tables()

    op.drop_constraint(
        'assessments_business_profile_id_fkey',
        'assessments',
        type_='foreignkey',
    )
    op.drop_constraint(
        'candidate_sites_assessment_id_fkey',
        'candidate_sites',
        type_='foreignkey',
    )

    op.create_table(
        'organizations',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
    )
    op.add_column(
        'business_profiles',
        sa.Column('organization_id', postgresql.UUID(as_uuid=True), nullable=False),
    )
    op.add_column(
        'assessments',
        sa.Column('organization_id', postgresql.UUID(as_uuid=True), nullable=False),
    )
    op.add_column(
        'candidate_sites',
        sa.Column('organization_id', postgresql.UUID(as_uuid=True), nullable=False),
    )

    op.create_foreign_key(
        'fk_business_profiles_organization',
        'business_profiles',
        'organizations',
        ['organization_id'],
        ['id'],
    )
    op.create_foreign_key(
        'fk_assessments_organization',
        'assessments',
        'organizations',
        ['organization_id'],
        ['id'],
    )
    op.create_foreign_key(
        'fk_candidate_sites_organization',
        'candidate_sites',
        'organizations',
        ['organization_id'],
        ['id'],
    )

    op.create_unique_constraint(
        'uq_business_profiles_id_org',
        'business_profiles',
        ['id', 'organization_id'],
    )
    op.create_unique_constraint(
        'uq_assessments_id_org',
        'assessments',
        ['id', 'organization_id'],
    )
    op.create_foreign_key(
        'fk_assessments_profile_org',
        'assessments',
        'business_profiles',
        ['business_profile_id', 'organization_id'],
        ['id', 'organization_id'],
    )
    op.create_foreign_key(
        'fk_candidate_sites_assessment_org',
        'candidate_sites',
        'assessments',
        ['assessment_id', 'organization_id'],
        ['id', 'organization_id'],
    )

    for table_name in TENANT_TABLES:
        op.create_index(
            f'ix_{table_name}_organization_id',
            table_name,
            ['organization_id'],
        )

    _create_application_role()
    op.execute('GRANT SELECT ON organizations TO retail_site_app')
    op.execute(
        'GRANT SELECT, INSERT, UPDATE, DELETE '
        'ON business_profiles, assessments, candidate_sites TO retail_site_app'
    )
    op.execute(
        'GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO retail_site_app'
    )

    op.execute('ALTER TABLE organizations ENABLE ROW LEVEL SECURITY')
    op.execute('ALTER TABLE organizations FORCE ROW LEVEL SECURITY')
    op.execute(
        """
        CREATE POLICY organizations_member_read
        ON organizations
        FOR SELECT
        USING (id = NULLIF(current_setting('app.current_organization_id', true), '')::uuid)
        """
    )
    for table_name in TENANT_TABLES:
        _enable_tenant_rls(table_name)


def downgrade() -> None:
    connection = op.get_bind()
    for table_name in TENANT_TABLES:
        has_rows = connection.scalar(
            sa.text(f'SELECT EXISTS (SELECT 1 FROM {table_name} LIMIT 1)')
        )
        if has_rows:
            raise RuntimeError(
                f'{table_name} contains tenant data. Export or migrate it before rollback.'
            )
    if connection.scalar(sa.text('SELECT EXISTS (SELECT 1 FROM organizations LIMIT 1)')):
        raise RuntimeError('organizations contains data. Export it before rollback.')

    op.execute('DROP POLICY IF EXISTS organizations_member_read ON organizations')
    op.execute('ALTER TABLE organizations DISABLE ROW LEVEL SECURITY')
    for table_name in TENANT_TABLES:
        op.execute(
            sa.text(
                f'DROP POLICY IF EXISTS {table_name}_organization_isolation ON {table_name}'
            )
        )
        op.execute(sa.text(f'ALTER TABLE {table_name} DISABLE ROW LEVEL SECURITY'))
        op.drop_index(f'ix_{table_name}_organization_id', table_name=table_name)

    op.drop_constraint(
        'fk_candidate_sites_assessment_org',
        'candidate_sites',
        type_='foreignkey',
    )
    op.drop_constraint(
        'fk_assessments_profile_org',
        'assessments',
        type_='foreignkey',
    )
    op.drop_constraint('uq_assessments_id_org', 'assessments', type_='unique')
    op.drop_constraint('uq_business_profiles_id_org', 'business_profiles', type_='unique')
    op.drop_constraint(
        'fk_candidate_sites_organization',
        'candidate_sites',
        type_='foreignkey',
    )
    op.drop_constraint(
        'fk_assessments_organization',
        'assessments',
        type_='foreignkey',
    )
    op.drop_constraint(
        'fk_business_profiles_organization',
        'business_profiles',
        type_='foreignkey',
    )
    op.drop_column('candidate_sites', 'organization_id')
    op.drop_column('assessments', 'organization_id')
    op.drop_column('business_profiles', 'organization_id')
    op.drop_table('organizations')
    op.create_foreign_key(
        'assessments_business_profile_id_fkey',
        'assessments',
        'business_profiles',
        ['business_profile_id'],
        ['id'],
    )
    op.create_foreign_key(
        'candidate_sites_assessment_id_fkey',
        'candidate_sites',
        'assessments',
        ['assessment_id'],
        ['id'],
    )
