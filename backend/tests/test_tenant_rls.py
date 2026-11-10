import os
import unittest
from pathlib import Path
from uuid import uuid4

from dotenv import dotenv_values
from sqlalchemy import create_engine, text


@unittest.skipUnless(
    os.getenv('RUN_DATABASE_SECURITY_TESTS') == '1',
    'Set RUN_DATABASE_SECURITY_TESTS=1 to run live PostgreSQL RLS tests.',
)
class TenantRlsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        environment = dotenv_values(Path(__file__).resolve().parents[2] / '.env')
        database_url = environment.get('DATABASE_URL')
        if not database_url:
            raise RuntimeError('DATABASE_URL is required for the live RLS tests.')
        cls.engine = create_engine(database_url, future=True)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.engine.dispose()

    def setUp(self) -> None:
        self.organization_a = uuid4()
        self.organization_b = uuid4()
        self.profile_a = f'test-profile-{self.organization_a}'
        self.profile_b = f'test-profile-{self.organization_b}'
        self.assessment_a = f'test-assessment-{self.organization_a}'
        self.assessment_b = f'test-assessment-{self.organization_b}'
        self.site_a = f'test-site-{self.organization_a}'
        self.site_b = f'test-site-{self.organization_b}'

        with self.engine.begin() as connection:
            connection.execute(
                text('INSERT INTO organizations (id, name) VALUES (:id, :name)'),
                [
                    {'id': self.organization_a, 'name': self.profile_a},
                    {'id': self.organization_b, 'name': self.profile_b},
                ],
            )
            profile_a_id = connection.scalar(
                text(
                    'INSERT INTO business_profiles (organization_id, organisation_name) '
                    'VALUES (:organization_id, :name) RETURNING id'
                ),
                {'organization_id': self.organization_a, 'name': self.profile_a},
            )
            profile_b_id = connection.scalar(
                text(
                    'INSERT INTO business_profiles (organization_id, organisation_name) '
                    'VALUES (:organization_id, :name) RETURNING id'
                ),
                {'organization_id': self.organization_b, 'name': self.profile_b},
            )
            assessment_a_id = connection.scalar(
                text(
                    'INSERT INTO assessments (organization_id, name, business_profile_id) '
                    'VALUES (:organization_id, :name, :profile_id) RETURNING id'
                ),
                {
                    'organization_id': self.organization_a,
                    'name': self.assessment_a,
                    'profile_id': profile_a_id,
                },
            )
            assessment_b_id = connection.scalar(
                text(
                    'INSERT INTO assessments (organization_id, name, business_profile_id) '
                    'VALUES (:organization_id, :name, :profile_id) RETURNING id'
                ),
                {
                    'organization_id': self.organization_b,
                    'name': self.assessment_b,
                    'profile_id': profile_b_id,
                },
            )
            connection.execute(
                text(
                    'INSERT INTO candidate_sites (organization_id, assessment_id, site_name) '
                    'VALUES (:organization_id, :assessment_id, :site_name)'
                ),
                [
                    {
                        'organization_id': self.organization_a,
                        'assessment_id': assessment_a_id,
                        'site_name': self.site_a,
                    },
                    {
                        'organization_id': self.organization_b,
                        'assessment_id': assessment_b_id,
                        'site_name': self.site_b,
                    },
                ],
            )

    def tearDown(self) -> None:
        with self.engine.begin() as connection:
            connection.execute(
                text('DELETE FROM candidate_sites WHERE organization_id IN (:a, :b)'),
                {'a': self.organization_a, 'b': self.organization_b},
            )
            connection.execute(
                text('DELETE FROM assessments WHERE organization_id IN (:a, :b)'),
                {'a': self.organization_a, 'b': self.organization_b},
            )
            connection.execute(
                text('DELETE FROM business_profiles WHERE organization_id IN (:a, :b)'),
                {'a': self.organization_a, 'b': self.organization_b},
            )
            connection.execute(
                text('DELETE FROM organizations WHERE id IN (:a, :b)'),
                {'a': self.organization_a, 'b': self.organization_b},
            )

    def _visible_values(self, table_name: str, column_name: str, organization_id=None) -> set[str]:
        with self.engine.connect() as connection:
            with connection.begin():
                connection.execute(text('SET LOCAL ROLE retail_site_app'))
                if organization_id is not None:
                    connection.execute(
                        text(
                            "SELECT set_config('app.current_organization_id', :organization_id, true)"
                        ),
                        {'organization_id': str(organization_id)},
                    )
                result = connection.execute(
                    text(f'SELECT {column_name} FROM {table_name}')
                )
                return {row[0] for row in result}

    def test_current_organization_sees_only_its_rows(self) -> None:
        table_values = (
            ('organizations', 'name', self.profile_a, self.profile_b),
            ('business_profiles', 'organisation_name', self.profile_a, self.profile_b),
            ('assessments', 'name', self.assessment_a, self.assessment_b),
            ('candidate_sites', 'site_name', self.site_a, self.site_b),
        )
        for table_name, column_name, value_a, value_b in table_values:
            with self.subTest(table=table_name, organization='a'):
                self.assertEqual(
                    self._visible_values(table_name, column_name, self.organization_a),
                    {value_a},
                )
            with self.subTest(table=table_name, organization='b'):
                self.assertEqual(
                    self._visible_values(table_name, column_name, self.organization_b),
                    {value_b},
                )

    def test_missing_tenant_context_sees_no_rows(self) -> None:
        for table_name, column_name in (
            ('organizations', 'name'),
            ('business_profiles', 'organisation_name'),
            ('assessments', 'name'),
            ('candidate_sites', 'site_name'),
        ):
            with self.subTest(table=table_name):
                self.assertEqual(self._visible_values(table_name, column_name), set())

    def test_application_database_role_is_not_privileged(self) -> None:
        from app.database import SessionLocal

        with SessionLocal() as session:
            is_privileged = session.scalar(
                text(
                    'SELECT rolsuper OR rolbypassrls '
                    'FROM pg_roles WHERE rolname = current_user'
                )
            )
        self.assertFalse(is_privileged)

    def test_tenant_database_dependency_sets_rls_context(self) -> None:
        from app.database import SessionLocal, get_tenant_db

        session = SessionLocal()
        tenant_session = get_tenant_db(self.organization_a, session)
        next(tenant_session)
        try:
            names = set(
                session.scalars(text('SELECT organisation_name FROM business_profiles'))
            )
        finally:
            tenant_session.close()
            session.close()
        self.assertEqual(names, {self.profile_a})

    def test_insert_for_another_organization_is_rejected(self) -> None:
        from sqlalchemy.exc import DBAPIError

        with self.engine.connect() as connection:
            with connection.begin():
                connection.execute(text('SET LOCAL ROLE retail_site_app'))
                connection.execute(
                    text(
                        "SELECT set_config('app.current_organization_id', :organization_id, true)"
                    ),
                    {'organization_id': str(self.organization_a)},
                )
                savepoint = connection.begin_nested()
                with self.assertRaises(DBAPIError):
                    connection.execute(
                        text(
                            'INSERT INTO business_profiles (organization_id, organisation_name) '
                            'VALUES (:organization_id, :name)'
                        ),
                        {
                            'organization_id': self.organization_b,
                            'name': 'unauthorized-test-row',
                        },
                    )
                savepoint.rollback()

    def test_cross_organization_relationship_is_rejected(self) -> None:
        from sqlalchemy.exc import DBAPIError

        with self.assertRaises(DBAPIError):
            with self.engine.begin() as connection:
                connection.execute(
                    text(
                        'INSERT INTO assessments (organization_id, name, business_profile_id) '
                        'SELECT :organization_id, :name, id FROM business_profiles '
                        'WHERE organization_id = :other_organization_id'
                    ),
                    {
                        'organization_id': self.organization_a,
                        'name': 'unauthorized-cross-organization-assessment',
                        'other_organization_id': self.organization_b,
                    },
                )


if __name__ == '__main__':
    unittest.main()
