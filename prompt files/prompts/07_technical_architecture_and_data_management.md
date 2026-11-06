**Project:** Retail Location Intelligence Platform  
**Document:** Technical Architecture and Data Management  
**Version:** 1.0  
**Status:** Proposed architecture — technology decisions pending final approval and compatibility testing

## 1. Purpose and scope

This document establishes the proposed technical architecture, technology stack, application components, database strategy, geospatial processing, API integration, AI usage, and data management requirements.

The architecture must support a configurable, secure, scalable, maintainable, and user-friendly retail location intelligence web application.

The platform must remain independent of any particular organisation, industry, geographic market, or data provider.

This document implements the requirements established in files 00–06. Security testing and deployment procedures are further defined in `08_security_testing_and_deployment.md`.

## 2. Architectural principles

The solution shall follow these principles:

1. Separate frontend, backend, data storage, and analytical processing responsibilities.
2. Keep business configuration separate from application code.
3. Maintain strict organisational data isolation.
4. Use appropriate geospatial technologies and spatial data structures.
5. Separate source data, validated data, derived data, and analytical results.
6. Preserve source provenance, assessment configuration, and analytical reproducibility.
7. Use modular, maintainable components and documented interfaces.
8. Avoid unnecessary infrastructure and premature microservices.
9. Support asynchronous processing for long-running operations.
10. Use approved, supported, compatible technology versions.
11. Avoid dependence on a single AI model or external data provider where practical.
12. Prevent unsupported analytical conclusions and fabricated outputs.

The preferred initial architecture is a **modular monolith with a separate web frontend**, rather than a distributed microservices architecture.

This reduces operational complexity while preserving clear boundaries for future expansion.

## 3. Proposed technology stack

The following stack is the recommended starting point, subject to final compatibility verification and approval.

| Layer | Recommended technology | Purpose |
|---|---|---|
| Frontend language | TypeScript | Type-safe web application development |
| Frontend framework | React | Component-based user interface |
| Frontend tooling | Vite | Development and production build tooling |
| UI styling | Tailwind CSS | Consistent, responsive styling |
| UI components | Accessible React component library | Reusable interface elements |
| Mapping | MapLibre GL JS | Interactive map rendering |
| Backend language | Python | APIs, data processing, and geospatial analysis |
| Backend framework | FastAPI | Application API and backend services |
| Primary database | PostgreSQL | Persistent relational information |
| Spatial extension | PostGIS | Spatial storage, indexing, and queries |
| Database access | SQLAlchemy and appropriate PostgreSQL driver | Application data access |
| Database migrations | Alembic | Controlled schema changes |
| Geospatial libraries | Shapely, GeoPandas, pyproj | Geographic operations and data preparation |
| Temporary processing | PostgreSQL staging structures and temporary files | Intermediate processing |
| Cache / queue infrastructure | Redis, if justified | Caching and background-job coordination |
| AI services | Gemini API, where justified | Optional AI-assisted features |
| Development support | Google AI Studio | AI-assisted development and prototyping |
| Containerisation | Docker, where appropriate | Reproducible environments |

These are architectural recommendations, not claims that the complete stack has been installed, integrated, or tested.

### 3.1 Frontend selection

**Preferred:** React with TypeScript and Vite.

Reasons:

- Component reuse across dashboard, assessment wizard, maps, and results.
- Strong suitability for interactive application workflows.
- Clear separation between presentation and backend analytical services.
- Flexible integration with mapping and visualisation libraries.

Next.js remains an alternative if server-side rendering, integrated server functionality, or other specific requirements justify it.

Do not introduce a second frontend framework without a documented reason.

### 3.2 Backend selection

**Preferred:** Python with FastAPI.

Reasons:

- Suitable for structured application APIs.
- Integration with Python geospatial and data-analysis libraries.
- Clear separation of business logic from frontend code.
- Support for validation, background processing, and documented API contracts.

The backend must be the authoritative execution layer for protected data access, approved analytical calculations, and consequential business operations.

### 3.3 Database selection

**Preferred:** PostgreSQL with PostGIS.

PostgreSQL shall manage relational application data, while PostGIS provides spatial data types, spatial indexes, and geographic query capabilities.

MySQL is a viable relational alternative but is not the preferred initial choice because the platform requires substantial spatial functionality.

Avoid operating multiple primary relational databases without a justified requirement.

## 4. Technology version and compatibility management

### 4.1 Technology selection policy

The platform shall use stable, supported, maintainable, and mutually compatible technologies.

Technology selection must consider:

- Functional and analytical requirements.
- Geospatial processing capabilities.
- Security and maintenance support.
- Frontend and backend compatibility.
- Database and extension compatibility.
- Development and deployment environments.
- Dependency availability and installation reliability.
- Long-term maintainability.
- Operational complexity and cost.

### 4.2 Recommended technology baseline

The following technology baseline defines the recommended components without prescribing fixed software versions.

Use the latest stable, officially supported, security-maintained, and mutually compatible versions available at the time of implementation, subject to verification and approval.

Exact versions shall be selected, tested, documented, and locked during the technical proof of concept and implementation process.

| Component | Recommended baseline | Decision status |
|---|---|---|
| Frontend language | TypeScript, maintained stable release | Recommended; exact version pending |
| Frontend framework | Stable, supported React release | Recommended; exact version pending |
| Frontend build tooling | Vite, compatible stable release | Recommended; exact version pending |
| Node.js runtime | Supported Active LTS or Maintenance LTS release compatible with selected tooling | Recommended; exact version pending |
| UI styling | Tailwind CSS, compatible stable release | Recommended; exact version pending |
| UI component library | Accessible React-compatible component library | Selection pending |
| Mapping library | MapLibre GL JS, compatible stable release | Recommended; exact version pending |
| Backend language | Stable, supported Python release compatible with the selected backend and geospatial dependencies | Recommended; exact version pending |
| Backend framework | FastAPI, compatible stable release | Recommended; exact version pending |
| API data validation | Pydantic, compatible with selected FastAPI | Recommended |
| Database | Stable, supported PostgreSQL release | Recommended; exact version pending |
| Spatial database extension | Stable PostGIS release compatible with the selected PostgreSQL version | Recommended; exact version pending |
| Database access | SQLAlchemy and compatible PostgreSQL driver | Recommended |
| Database migrations | Alembic, compatible with SQLAlchemy | Recommended |
| Geospatial processing | GeoPandas, Shapely, pyproj and required dependencies | Recommended; versions pending |
| Spatial database operations | PostGIS functions and spatial indexes | Recommended |
| Temporary processing | PostgreSQL staging structures and controlled temporary files | Recommended |
| Background processing | Appropriate worker mechanism when justified | Implementation pending |
| Caching and queue infrastructure | Redis only when justified | Deferred |
| AI integration | Gemini API or another approved service, where justified | Optional |
| Development environment | Google AI Studio and an appropriate executable development environment | Proposed |
| Containerisation | Docker where appropriate | Recommended for reproducibility |
| Hosting | Provider selected through technical and operational evaluation | Undecided |

The baseline must not be interpreted as an approved production dependency manifest.

### 4.3 Version-selection rationale

**Frontend**

Select an officially supported Node.js LTS release compatible with the chosen React, TypeScript, Vite, and frontend dependencies.

Verify runtime, package, and build compatibility before locking exact versions.

**Backend**

Select a stable, officially supported Python release compatible with FastAPI, the selected database drivers, and the required geospatial libraries.

Verify compatibility with GeoPandas, Shapely, pyproj, and relevant native dependencies before finalising the Python version.

Do not assume that the newest Python release is automatically the most suitable choice.

**Database**

Select a stable, officially supported PostgreSQL release with a compatible, maintained PostGIS extension.

Verify the selected combination using official compatibility documentation.

Actual installation, extension activation, spatial functionality, migration compatibility, and performance must be tested before final approval.

**Mapping**

MapLibre GL JS is the preferred interactive mapping library.

Map style providers, tile services, geographic datasets, attribution, licensing, and usage restrictions require separate evaluation.

**Geospatial processing**

GeoPandas, Shapely, pyproj, and relevant dependencies must be selected as a compatible group.

Where required, verify compatibility with native geographic libraries such as GEOS, PROJ, and GDAL.

Do not independently pin conflicting geospatial dependencies.

### 4.4 Compatibility verification requirements

Before substantial implementation, conduct a focused technical proof of concept covering:

1. React, TypeScript, Vite, and Node.js installation and build compatibility.
2. React integration with MapLibre GL JS.
3. Python and FastAPI installation and runtime compatibility.
4. FastAPI integration with SQLAlchemy and the selected PostgreSQL driver.
5. PostgreSQL installation and PostGIS extension activation.
6. Spatial table creation, indexing, and geographic queries.
7. GeoPandas, Shapely, pyproj, and native dependency compatibility.
8. Frontend-to-backend API communication.
9. Backend-to-database communication.
10. Database migration execution and rollback considerations.
11. Basic organisation-scoped data access.
12. Geographic data ingestion, coordinate transformation, and validation.
13. Development environment reproducibility.
14. Relevant security and dependency checks.

Use a small, clearly labelled synthetic dataset for technical testing.

A successful package installation alone does not establish full compatibility.

### 4.5 Exact dependency manifest

After the proof of concept, maintain an implementation dependency manifest recording:

- Technology or package name.
- Selected exact version.
- Runtime and operating system.
- Relevant compatibility requirements.
- Official release or documentation reference.
- Verification date.
- Installation and test status.
- Known limitations.
- Upgrade considerations.
- Approval status.

Record the actual versions installed and tested rather than copying unverified package numbers from AI-generated suggestions.

Use the relevant package managers and dependency lockfiles to preserve reproducibility.

### 4.6 Dependency and environment control

Maintain:

- Frontend package manifest and lockfile.
- Backend dependency manifest and resolved versions.
- Python runtime version specification.
- Node.js runtime version specification.
- PostgreSQL and PostGIS version records.
- Database migration history.
- Container configuration where applicable.
- Development and deployment environment documentation.

Use consistent dependency versions across relevant development, testing, and production environments.

Do not introduce automatic major-version upgrades without compatibility and regression testing.

### 4.7 Version changes and approval

Technology upgrades must be evaluated according to:

- Security requirements.
- Maintenance and support status.
- Compatibility.
- Functional impact.
- Geospatial processing correctness.
- Migration requirements.
- Deployment impact.
- Testing results.

Minor maintenance updates may follow the approved dependency management process.

Major architecture changes, database migrations with consequential effects, or significant runtime changes require documented impact assessment and appropriate approval.

### 4.8 Technology verification status

The initial architecture has been selected at the recommendation level.

The following activities remain outstanding:

- Exact dependency resolution and pinning.
- Full-stack installation and execution.
- Python geospatial compatibility testing.
- Frontend and mapping integration testing.
- PostgreSQL/PostGIS installation and spatial validation.
- Authentication and organisation-isolation implementation.
- Background-processing evaluation.
- Hosting and deployment selection.
- End-to-end technical verification.

Do not describe these activities as completed until execution evidence is available.

The architecture may proceed to a controlled technical proof of concept, but production readiness requires the additional validation and approval processes defined in `08_security_testing_and_deployment.md`.

## 5. Logical system architecture

The application shall consist of the following logical components.

### 5.1 Frontend application

Responsible for:

- Authentication-related user interactions.
- Dashboard and assessment navigation.
- Guided assessment forms.
- Geographic selection and map interaction.
- Market and competitor configuration.
- Data-readiness presentation.
- Results and comparisons.
- Evidence and confidence explanations.
- Reporting and authorised administrative interfaces.

The frontend must not be the authoritative location for sensitive calculations, database credentials, or privileged business logic.

### 5.2 Backend application

Responsible for:

- API request handling and validation.
- Authentication verification and authorisation.
- Organisation and assessment management.
- Business configuration management.
- Data access and source management.
- Geospatial and analytical orchestration.
- Evidence and confidence records.
- Assessment result persistence.
- Report generation.
- Audit and operational events.

Backend modules should remain logically separated even when deployed as one application.

### 5.3 Data processing and analytical services

Responsible for:

- Data ingestion and validation.
- Geocoding and spatial transformation.
- Spatial queries and derived indicators.
- Approved analytical calculations.
- Data-readiness checks.
- Long-running processing tasks.
- Analytical result generation and validation.

Where necessary, resource-intensive tasks should run in separate workers rather than blocking ordinary API requests.

### 5.4 Persistent data layer

Responsible for storing approved organisational, operational, geographic, research, and assessment records.

The database must enforce appropriate integrity constraints and organisational access boundaries.

## 6. Logical data model

The initial logical data model should include the following entities or equivalent structures.

| Entity group | Responsibility |
|---|---|
| Organisations | Organisation identity and configuration |
| Users and memberships | User identity, organisation membership, and roles |
| Business profiles | Industry, products, services, and outlet context |
| Assessments | Assessment identity, purpose, status, and ownership |
| Assessment configurations | Versioned objectives, preferences, and geographic scope |
| Candidate locations | User-defined or system-derived locations and their provenance |
| Competitor configurations | Assessment-specific relevant competitors and categories |
| Geographic reference data | Boundaries, geographic units, and spatial references |
| Source registry | Source identity, access conditions, and provenance |
| Dataset registry | Dataset versions, coverage, validation, and permitted use |
| Geographic features | Spatial records and relevant attributes |
| Analytical methods | Method identity, versions, and approval status |
| Analysis jobs | Execution requests, status, failures, and processing metadata |
| Analysis results | Calculated outputs, inputs, assumptions, and validation |
| Confidence assessments | Data and analysis confidence records |
| Suitability assessments | Results produced using approved suitability methods |
| Reports | Generated assessment outputs and relevant metadata |
| Audit records | Consequential user, configuration, and system actions |

This is a logical design, not a final physical database schema.

Primary keys, foreign keys, indexes, constraints, retention policies, and physical table structures must be specified during database implementation.

## 7. Organisation isolation and configuration management

### 7.1 Organisational boundaries

Organisation-specific data must be logically isolated.

Every organisation-owned record must be associated with the appropriate organisational context.

The backend must enforce access permissions for reads, writes, exports, and analytical operations.

Frontend filtering alone is insufficient.

### 7.2 Shared and private information

Distinguish:

- Platform-wide reference data.
- Public or licensed geographic datasets.
- Organisation-specific business records.
- Assessment-specific configuration.
- Private or restricted datasets.
- System-generated analytical outputs.

Shared datasets must not expose confidential organisation-specific information.

### 7.3 Configuration management

Store business settings as structured, validated data.

Do not hard-code:

- Organisation identity.
- Competitor lists.
- Industries or products.
- Geographic scope.
- Evaluation criteria.
- Weights or thresholds.
- Catchment parameters.
- Scoring formulas.
- Data-provider credentials.

System defaults may be used only where technically necessary and must not silently impose unapproved business assumptions.

### 7.4 Physical database design and migration controls

The physical database schema shall be developed from the logical entities defined in Section 6, using PostgreSQL, PostGIS, SQLAlchemy, and Alembic.

**Schema design requirements**

- Define tables, primary keys, foreign keys, relationships, data types, and appropriate constraints.
- Use unique identifiers and enforce referential integrity.
- Apply indexes based on actual query requirements, including spatial indexes where appropriate.
- Include timestamps, ownership information, and lifecycle statuses where justified.
- Preserve dataset, configuration, method, and result version references required for analytical reproducibility.
- Distinguish platform-wide reference data from organisation-owned and assessment-specific data.
- Avoid unnecessary tables, duplicated records, and premature database complexity.

**Organisation isolation**

- Every organisation-owned record must have a verifiable organisation association, directly or through an enforced parent relationship.
- The backend must authenticate users and authorise access according to their organisation membership and permissions.
- Organisation identifiers supplied by clients must never be trusted without server-side verification.
- Apply PostgreSQL Row-Level Security (RLS) as defence in depth for applicable tenant-owned tables, using a reviewed and tested database access context.
- Define explicit policies for authorised platform administration and genuinely shared reference data.
- Ensure background jobs, exports, reports, and analytical queries follow the same isolation requirements.
- Test attempts to access another organisation's records, including through related objects and indirect API requests.

RLS must supplement, not replace, application-level authorisation. Its policy design, database roles, and connection-handling behaviour must be verified before production use.

**Database migrations**

- Use Alembic to manage version-controlled schema changes.
- Review migration scripts before execution.
- Test migrations against representative development and testing databases.
- Protect existing data during schema changes.
- Document backup, recovery, and rollback or forward-recovery procedures for consequential migrations.
- Do not modify production schemas manually outside an authorised emergency procedure.
- Maintain consistent migration versions across deployment environments.

**Implementation and verification**

The detailed physical schema, database relationships, RLS policies, and migration scripts shall be produced and tested during the database implementation stage.

Before approval, verify referential integrity, spatial operations, tenant isolation, migration execution, and data preservation.

The requirements in this subsection are mandatory design controls. They do not imply that the physical database schema or security policies have already been implemented.

## 8. Spatial database design

### 8.1 Spatial data types

Use appropriate PostGIS geometry or geography types according to the intended operations.

Spatial records should include valid geographic identifiers and coordinate reference information.

Use spatial indexes where appropriate.

### 8.2 Coordinate systems

Store and process spatial information using documented coordinate reference systems.

Select appropriate projected or geographic coordinate systems for each analytical operation.

Do not perform distance or area calculations using unsuitable coordinate assumptions.

### 8.3 Geographic integrity

Validate:

- Coordinate ranges.
- Geometry validity.
- Spatial reference compatibility.
- Duplicate or overlapping records.
- Administrative boundary relationships.
- Geocoding uncertainty.
- Geographic coverage and resolution.

### 8.4 Spatial analysis

Use PostGIS for suitable database-side spatial queries and Python geospatial libraries where more complex processing is justified.

Do not duplicate expensive spatial calculations unnecessarily.

Distinguish straight-line distances from road-network distances and travel times.

Network routing requires suitable road-network data or an authorised routing service; PostGIS alone does not establish driving-time estimates.

## 9. Data ingestion and processing architecture

### 9.1 Data lifecycle

Use the following conceptual data lifecycle:

1. Source identification and access approval.
2. Data acquisition.
3. Raw or staging storage.
4. Schema and quality validation.
5. Geographic and temporal validation.
6. Cleaning and transformation.
7. Approved dataset publication.
8. Analytical processing.
9. Result validation and storage.
10. Monitoring, updating, or retirement.

### 9.2 Data separation

Separate:

- Original source data.
- Temporary/staging data.
- Validated operational datasets.
- Derived analytical datasets.
- Assessment results.

Do not overwrite original evidence with transformed values.

### 9.3 Provenance

Maintain sufficient metadata to identify source versions, retrieval dates, transformations, validation results, and restrictions.

Analytical outputs must reference the datasets and methods used.

### 9.4 Data updates

Changes to datasets must not silently alter historical assessment results.

Support versioning or reproducible references to the source and configuration used for an assessment.

## 10. Temporary storage, caching, and background jobs

### 10.1 Temporary data

Use PostgreSQL staging tables, controlled temporary files, or equivalent mechanisms for intermediate processing.

Temporary data must have appropriate lifecycle, cleanup, access, and retention controls.

A separate temporary database is not mandatory.

### 10.2 Caching

Introduce caching when justified by measurable performance needs, repeated expensive queries, or external API limitations.

Redis is a candidate but is not required for the initial architecture.

Cached data must respect organisational permissions, source licences, freshness requirements, and invalidation rules.

### 10.3 Background processing

Long-running data ingestion, geographic processing, and analytical operations should not block normal application requests.

Use a persistent job record and an appropriate worker mechanism.

A dedicated queue system may be introduced when the initial execution approach becomes insufficient.

Job processing must support failure handling, retry controls, status reporting, and prevention of unintended duplicate operations.

## 11. API architecture

### 11.1 API principles

Use documented, versioned backend interfaces.

APIs must:

- Validate requests.
- Enforce authorisation.
- Return consistent response structures.
- Handle missing and invalid inputs.
- Avoid leaking confidential information.
- Provide meaningful error responses.
- Support appropriate pagination and filtering.
- Distinguish synchronous requests from asynchronous jobs.

### 11.2 Initial API domains

Potential API domains include:

- Authentication and user context.
- Organisations and profiles.
- Assessments and configurations.
- Geographic search and reference data.
- Candidate locations.
- Competitor and market configuration.
- Dataset availability and metadata.
- Analysis requests and job status.
- Results and comparisons.
- Evidence and confidence.
- Reports and exports.
- Administration and audit.

Exact endpoints, request schemas, and response contracts must be defined during implementation planning.

### 11.3 API security

Protected endpoints must verify authenticated identity and relevant permissions.

Never trust an organisation identifier or user role supplied by the browser without server-side authorisation.

Apply appropriate rate limits, input validation, logging, and secure error handling.

## 12. External geographic and data services

The platform may integrate with authorised services for:

- Base maps.
- Geocoding and place search.
- Administrative boundaries.
- Road-network routing.
- Geographic reference data.
- Demographic and socioeconomic information.
- Commercial establishments.
- Licensed market intelligence.

Each integration must be evaluated for:

- Coverage and data quality.
- API availability and reliability.
- Licence and permitted use.
- Authentication requirements.
- Cost and usage limits.
- Storage and caching restrictions.
- Update frequency.
- Geographic suitability.
- Failure handling and alternatives.

Do not assume that a mapping provider supplies verified competitor, footfall, income, or customer-demand information.

Provider-specific integration logic should be isolated behind reusable service interfaces where practical.

## 13. Analytical engine architecture

### 13.1 Separation of responsibilities

Separate:

- Data retrieval and validation.
- Geographic processing.
- Indicator calculation.
- Confidence assessment.
- Suitability evaluation.
- Results interpretation and presentation.

### 13.2 Method governance

Every material analytical method must have a documented purpose, inputs, assumptions, version, validation status, and approval status.

Do not introduce arbitrary scoring, ranking, weighting, catchment, or exclusion logic.

### 13.3 Confidence architecture

Store data confidence, analysis confidence, and location suitability as distinct concepts.

Their calculations, if approved, must be independently traceable.

Do not infer analysis confidence by automatically averaging data-confidence values.

### 13.4 Missing evidence

Analytical services must handle missing, incomplete, outdated, and unsuitable data explicitly.

Unsupported outputs must be omitted, limited, or marked unavailable rather than fabricated.

### 13.5 Reproducibility

Each material analysis result should retain references to:

- Assessment configuration version.
- Input dataset versions.
- Analytical method version.
- Parameters and assumptions.
- Execution metadata.
- Validation findings.
- Relevant limitations.

## 14. AI and Google AI Studio integration

### 14.1 Development environment

Google AI Studio may be used to assist with:

- Application prototyping.
- Code generation.
- UI development.
- Technical problem-solving.
- Implementation planning.
- Test generation.
- Documentation support.

Generated code must still be reviewed, executed, and tested in an appropriate environment.

Do not assume that Google AI Studio automatically provides production hosting, persistent databases, backend workers, or all required integrations.

### 14.2 Runtime AI capabilities

Gemini or another approved AI service may support relevant features such as:

- Explaining analytical results.
- Summarising evidence.
- Assisting with research interpretation.
- Supporting natural-language interaction.
- Helping users understand configuration options.

These capabilities are optional and must be justified by requirements.

### 14.3 AI restrictions

AI must not independently invent:

- Competitor locations.
- Population or income figures.
- Geographic coordinates.
- Source references.
- Data-confidence scores.
- Analytical confidence.
- Suitability rankings.
- Unapproved analytical methods.

Deterministic calculations and approved geospatial operations must be performed by the appropriate backend analytical components.

AI-generated explanations must be grounded in retrieved, permitted, and traceable evidence.

### 14.4 AI security and cost

Keep API credentials server-side.

Do not expose confidential organisation data to external AI services without authorisation.

Apply suitable access controls, usage limits, logging, and cost monitoring.

### 14.5 Context and token efficiency

Use modular prompts and task-specific documentation.

Do not repeatedly submit every project document to the model.

Preserve essential governing constraints while supplying only relevant requirements, code, schemas, and decisions.

## 15. Security architecture boundaries

The system must enforce security across frontend, backend, database, external integrations, and analytical processing.

Architectural requirements include:

- Authentication and authorisation.
- Organisation-level data isolation.
- Least-privilege access.
- Secure credential management.
- Encrypted transport.
- Appropriate data protection.
- Input validation.
- Secure file handling.
- Auditability.
- Protection against common web application vulnerabilities.
- Controlled access to restricted datasets.

Detailed security controls, threat assessment, testing, and deployment requirements belong in file 08.

## 16. Deployment architecture considerations

The platform should support distinct development, testing, and production environments where appropriate.

The proposed deployable components are:

- Frontend web application.
- Backend API service.
- PostgreSQL/PostGIS database.
- Background worker when required.
- Controlled file or object storage where required.
- Optional cache/queue service.
- Approved external geographic and AI services.

Hosting must be selected according to operational requirements, security, geographic availability, maintenance, and cost.

Do not commit to a cloud provider or paid service without a justified recommendation and approval.

## 17. Performance and scalability

Design for realistic geographic datasets and interactive workflows.

Consider:

- Spatial indexing.
- Query optimisation.
- Efficient geographic data transfer.
- Pagination and filtering.
- Map-layer loading strategies.
- Background processing.
- Database connection management.
- Appropriate caching.
- Resource monitoring.
- Data growth and retention.

Do not invent performance guarantees without measured workloads and acceptance criteria.

The initial architecture should be simple enough to maintain while allowing justified scaling.

## 18. Testing and architecture verification

Technical stack and dependency compatibility shall be verified through the proof-of-concept requirements defined in Section 4.4.

In addition, architecture verification must establish that the proposed solution supports the platform's functional, analytical, security, and operational requirements.

The broader verification scope includes:
1. Authentication, authorisation, and organisation-level data isolation.
2. Data ingestion, validation, and controlled dataset publication.
3. Spatial data integrity and appropriate geographic calculations.
4. Analysis-job execution, status tracking, failure handling, and recovery.
5. Interactive map rendering and geographic data presentation.
6. Dataset provenance, method traceability, and analytical reproducibility.
7. Separation of data confidence, analysis confidence, and suitability.
8. Secure handling of credentials, restricted data, and external integrations.
9. Deployment feasibility, operational dependencies, and environment configuration.
10. Compliance with relevant approved functional and non-functional requirements.
Verification activities must be mapped to applicable requirements and acceptance criteria.

Record the evidence, outcomes, unresolved defects, and pending checks.

A successful technical proof of concept does not automatically establish production readiness. Detailed security, quality assurance, and deployment requirements remain governed by 08_security_testing_and_deployment.md.

## 19. Architecture decisions and unresolved items

Maintain architecture decision records for material choices.

Each record should contain:

- Decision identifier.
- Problem and requirements.
- Alternatives considered.
- Recommended option.
- Rationale and trade-offs.
- Risks and dependencies.
- Approval status.
- Verification or implementation status.

### Initial decisions requiring confirmation

| ID | Proposed decision | Status |
|---|---|---|
| ADR-01 | React + TypeScript + Vite frontend | Recommended |
| ADR-02 | Python + FastAPI backend | Recommended |
| ADR-03 | PostgreSQL + PostGIS primary database | Recommended |
| ADR-04 | Modular monolith architecture | Recommended |
| ADR-05 | MapLibre GL JS mapping | Recommended |
| ADR-06 | PostgreSQL staging before separate temporary infrastructure | Recommended |
| ADR-07 | Redis introduced only when justified | Deferred |
| ADR-08 | Cloud hosting and deployment provider | Undecided |
| ADR-09 | Authentication and identity provider | Undecided |
| ADR-10 | Background-job implementation | Undecided |
| ADR-11 | External mapping, routing, and data providers | Pending source and licence evaluation |
| ADR-12 | Exact dependency versions | Pending compatibility verification |

Do not present recommended decisions as approved or implemented.

## 20. Architecture acceptance criteria

The proposed architecture is ready for full implementation, beyond controlled technical proof-of-concept activities, when the following conditions have been sufficiently verified, documented, and approved:

1. The selected stack supports the approved functional requirements.
2. Critical technology compatibility has been verified.
3. The logical data model and organisational boundaries are established.
4. Geospatial storage and processing approaches are justified.
5. Data provenance and analytical reproducibility are supported.
6. Temporary storage and background-processing needs are addressed.
7. External service dependencies and restrictions are documented.
8. Security and access boundaries are clear.
9. Deployment feasibility has been assessed.
10. Material decisions and unresolved risks are recorded.
11. Consequential choices have received the required approval.
12. The implementation approach can be tested incrementally.

## 21. Governing principle

**The platform architecture must support trustworthy geographic analysis, reusable business configuration, secure data management, and a coherent user experience without unnecessary technical complexity.**

Technology selection must follow verified requirements and compatibility evidence.

A technically functioning application is not sufficient unless its data handling, analytical methods, security, and user-facing outputs are also defensible.