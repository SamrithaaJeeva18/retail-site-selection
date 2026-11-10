from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, ForeignKeyConstraint, Index, Numeric, String, Text, UniqueConstraint, and_
from sqlalchemy.dialects.postgresql import UUID as PostgreSQLUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from geoalchemy2 import Geography
from geoalchemy2.elements import WKBElement

from .database import Base


class Organization(Base):
    __tablename__ = 'organizations'

    id: Mapped[UUID] = mapped_column(PostgreSQLUUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(255), nullable=False)


class BusinessProfile(Base):
    __tablename__ = 'business_profiles'
    __table_args__ = (UniqueConstraint('id', 'organization_id', name='uq_business_profiles_id_org'),)

    id: Mapped[int] = mapped_column(primary_key=True)
    organization_id: Mapped[UUID] = mapped_column(
        PostgreSQLUUID(as_uuid=True),
        ForeignKey('organizations.id'),
        nullable=False,
        index=True,
    )
    organisation_name: Mapped[str] = mapped_column(String(255), nullable=False)
    business_type: Mapped[str | None] = mapped_column(String(255), nullable=True)
    outlet_format: Mapped[str | None] = mapped_column(String(255), nullable=True)

    assessments: Mapped[list['Assessment']] = relationship(
        back_populates='business_profile',
        primaryjoin=lambda: and_(
            BusinessProfile.id == Assessment.business_profile_id,
            BusinessProfile.organization_id == Assessment.organization_id,
        ),
        foreign_keys=lambda: [Assessment.business_profile_id, Assessment.organization_id],
    )


class Assessment(Base):
    __tablename__ = 'assessments'
    __table_args__ = (
        UniqueConstraint('id', 'organization_id', name='uq_assessments_id_org'),
        ForeignKeyConstraint(
            ['business_profile_id', 'organization_id'],
            ['business_profiles.id', 'business_profiles.organization_id'],
            name='fk_assessments_profile_org',
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    organization_id: Mapped[UUID] = mapped_column(
        PostgreSQLUUID(as_uuid=True),
        ForeignKey('organizations.id'),
        nullable=False,
        index=True,
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    objective: Mapped[str | None] = mapped_column(Text, nullable=True)
    geographic_scope: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(64), default='draft', nullable=False)
    business_profile_id: Mapped[int | None] = mapped_column(nullable=True)

    business_profile: Mapped[BusinessProfile | None] = relationship(
        back_populates='assessments',
        primaryjoin=lambda: and_(
            Assessment.business_profile_id == BusinessProfile.id,
            Assessment.organization_id == BusinessProfile.organization_id,
        ),
        foreign_keys=lambda: [Assessment.business_profile_id, Assessment.organization_id],
    )
    candidate_sites: Mapped[list['CandidateSite']] = relationship(
        back_populates='assessment',
        primaryjoin=lambda: and_(
            Assessment.id == CandidateSite.assessment_id,
            Assessment.organization_id == CandidateSite.organization_id,
        ),
        foreign_keys=lambda: [CandidateSite.assessment_id, CandidateSite.organization_id],
    )


class CandidateSite(Base):
    __tablename__ = 'candidate_sites'
    __table_args__ = (
        ForeignKeyConstraint(
            ['assessment_id', 'organization_id'],
            ['assessments.id', 'assessments.organization_id'],
            name='fk_candidate_sites_assessment_org',
        ),
        Index('idx_candidate_sites_geog', 'geog', postgresql_using='gist'),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    organization_id: Mapped[UUID] = mapped_column(
        PostgreSQLUUID(as_uuid=True),
        ForeignKey('organizations.id'),
        nullable=False,
        index=True,
    )
    assessment_id: Mapped[int | None] = mapped_column(nullable=True)
    site_name: Mapped[str] = mapped_column(String(255), nullable=False)
    geog: Mapped[WKBElement | None] = mapped_column(
        Geography(geometry_type='POINT', srid=4326, spatial_index=False),
        nullable=True,
    )
    confidence_score: Mapped[float | None] = mapped_column(Numeric(5, 2), nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    assessment: Mapped[Assessment | None] = relationship(
        back_populates='candidate_sites',
        primaryjoin=lambda: and_(
            CandidateSite.assessment_id == Assessment.id,
            CandidateSite.organization_id == Assessment.organization_id,
        ),
        foreign_keys=lambda: [CandidateSite.assessment_id, CandidateSite.organization_id],
    )
