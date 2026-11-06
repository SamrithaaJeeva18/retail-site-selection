# 04_project_workflow_and_deliverables.md

**Project:** Retail Location Intelligence Platform  
**Document:** Project Workflow and Deliverables  
**Version:** 1.0  
**Status:** Proposed baseline — subject to project approval

## 1. Purpose

This document defines the development lifecycle, workstreams, stage deliverables, dependencies, review requirements, and approval gates for the Retail Location Intelligence Platform.

The project must progress systematically from requirements and evidence-based research through architecture, implementation, validation, and deployment.

The objective is to deliver a reliable, configurable, user-friendly, and maintainable web application that supports defensible retail location assessments.

This document governs project execution. It must be interpreted alongside:

- `00_platform_overview.md` — platform purpose and boundaries.
- `01_master_instructions.md` — governing instructions and approval authority.
- `02_research_and_data_framework.md` — research, sources, data quality, and access.
- `03_analysis_evidence_and_confidence.md` — analytical methods, uncertainty, confidence, and suitability.
- `05–08` — application requirements, design, architecture, security, testing, and deployment.

Do not duplicate detailed requirements from these documents.

## 2. Project leadership and responsibilities

The AI development partner shall proactively perform the roles of project lead, geospatial solution architect, research lead, requirements analyst, UI/UX designer, software developer, and testing coordinator, within its available capabilities.

Responsibilities include:

1. Plan and coordinate the project lifecycle.
2. Identify requirements, dependencies, risks, and unresolved decisions.
3. Recommend technically and analytically defensible approaches.
4. Maintain consistency across documents, implementation, and outputs.
5. Challenge weak assumptions and unsuitable design choices.
6. Produce implementation-ready specifications and development instructions.
7. Develop and validate functionality where tools and environments permit.
8. Communicate progress, limitations, and next actions clearly.
9. Prevent unnecessary repetition and avoidable rework.

The user retains final approval authority over consequential business decisions, major methodology choices, material requirement changes, financial commitments, and production deployment.

AI-generated plans, code, reports, or recommendations must not be represented as verified, executed, or approved unless that has occurred.

## 3. Workstream structure

The project contains two coordinated workstreams.

### Workstream A — Business, research, and data

Responsible for:

- Business requirements and assessment objectives.
- Research questions and evidence requirements.
- Data category identification and prioritisation.
- Source discovery, verification, and access assessment.
- Data quality, geographic coverage, and limitations.
- Research literature and methodological evidence.
- Analytical readiness and data gaps.
- Business and methodological approval requirements.

### Workstream B — Application design and development

Responsible for:

- Functional and non-functional requirements.
- Guided user workflows and UI/UX.
- System and geospatial architecture.
- Configuration and data management.
- Mapping and analytical functionality.
- Security and access management.
- Implementation, integration, and testing.
- Deployment and operational maintenance.

### Coordination rules

The workstreams may progress iteratively where dependencies permit.

Application design may begin using documented requirements while research continues. However, unverified data, unapproved methodologies, or unresolved business assumptions must not be embedded as established functionality.

Technical feasibility does not establish analytical or commercial validity.

Changes in either workstream must be evaluated for effects on the other.

## 4. Project lifecycle

The project follows eight coordinated stages.

| Stage | Primary objective |
|---|---|
| 1. Foundation and requirements | Establish the platform's purpose, constraints, workflows, and requirements |
| 2. Research and data feasibility | Determine evidence availability, quality, access, and analytical readiness |
| 3. Solution and UX design | Define architecture, interfaces, data structures, and user journeys |
| 4. Implementation planning | Establish a feasible build sequence and acceptance criteria |
| 5. Application development | Implement approved functionality incrementally |
| 6. Verification and validation | Test functionality, geospatial operations, analytical integrity, and usability |
| 7. Deployment preparation and release | Verify operational readiness and obtain deployment approval |
| 8. Maintenance and improvement | Monitor, correct, maintain, and extend the platform responsibly |

These stages establish dependencies, not a requirement to complete all research before any technical prototyping.

## 5. Stage 1 — Foundation and requirements

### Objective

Establish a coherent, sufficiently complete project foundation before substantial application development.

### Activities

- Confirm the organisation-independent platform objective.
- Define intended users and business use cases.
- Establish the guided assessment workflow.
- Identify functional and non-functional requirements.
- Define configurable versus data-driven versus system-controlled information.
- Identify analytical boundaries and prohibited assumptions.
- Document data, security, usability, and integration requirements.
- Identify major risks, dependencies, and unresolved decisions.
- Establish requirement traceability and acceptance criteria.

### Deliverables

- Approved platform overview and governing instructions.
- Research, analytical, and project workflow frameworks.
- User requirements and assessment workflow specification.
- Functional requirements and UI/UX specification.
- Initial technical and security requirements.
- Requirements register and decision log.

### Completion criteria

Requirements must be sufficiently clear, internally consistent, prioritised, and traceable to support architectural design.

Unresolved matters must be recorded with their impact and decision owner.

Do not claim that requirements are complete solely because the Markdown documents have been written.

## 6. Stage 2 — Research and data feasibility

### Objective

Establish which evidence and datasets can legitimately support the intended assessments.

### Activities

- Investigate relevant data categories and research literature.
- Identify and verify credible sources.
- Evaluate data access, licensing, cost, and technical constraints.
- Assess geographic and temporal coverage.
- Examine quality, completeness, precision, and consistency.
- Identify gaps, conflicts, and limitations.
- Investigate defensible analytical methods.
- Determine which proposed capabilities are supported by available evidence.

### Deliverables

- Research findings summary.
- Data source and access register.
- Research evidence and methodology register.
- Data availability and coverage assessment.
- Data quality and validation findings.
- Geographic and temporal gap assessment.
- Analytical feasibility and readiness assessment.
- Prioritised acquisition and research recommendations.

### Completion criteria

Each proposed material analysis must have a documented evidence-readiness status.

Research completion does not require every possible dataset to be available. It requires a defensible understanding of what is available, missing, restricted, or unsuitable.

Unsupported analytical capabilities must remain deferred, limited, or explicitly experimental.

## 7. Stage 3 — Solution architecture and UI/UX design

### Objective

Design an understandable, reusable, secure, and technically feasible web platform.

### Activities

- Define system components and responsibilities.
- Evaluate technology choices against actual requirements.
- Design user journeys, navigation, and screen structure.
- Define configuration, data storage, and analytical boundaries.
- Design spatial data structures and processing workflows.
- Plan mapping, search, comparison, and reporting capabilities.
- Define integrations and external service dependencies.
- Establish error handling, loading states, and missing-data behaviour.
- Design evidence, confidence, and limitations presentation.
- Evaluate accessibility, responsiveness, and maintainability.

### Deliverables

- Solution architecture specification.
- User journey and screen specifications.
- UI/UX design principles and interaction requirements.
- Data model and configuration design.
- Geospatial processing and integration design.
- Security and deployment architecture proposals.
- Architecture decision records for consequential choices.

### Completion criteria

The design must support the approved requirements without hard-coded organisation-specific business logic.

Major technical choices must be justified, dependencies identified, and material trade-offs presented for approval.

Google AI Studio may support development, but its capabilities must not be confused with the architecture or production runtime of the final application.

## 8. Stage 4 — Implementation planning

### Objective

Convert the approved design into manageable, testable development work.

### Activities

- Identify dependencies and implementation order.
- Define an initial viable release scope.
- Break features into incremental work packages.
- Establish requirement-to-feature traceability.
- Define acceptance criteria and validation procedures.
- Identify required datasets, credentials, services, and environments.
- Separate essential functionality from optional enhancements.
- Record implementation risks and unresolved prerequisites.

### Deliverables

- Prioritised development backlog.
- Incremental implementation plan.
- Acceptance criteria for planned features.
- Testing strategy and initial test cases.
- Dependency and risk register.
- Release scope proposal.

### Completion criteria

Each development work package must have a clear purpose, expected behaviour, dependencies, and means of verification.

Do not implement speculative features merely to make the application appear comprehensive.

## 9. Stage 5 — Application development

### Objective

Implement the platform incrementally while preserving approved requirements and system integrity.

### Development principles

1. Implement reusable, modular components.
2. Keep business configuration separate from application logic.
3. Preserve clear boundaries between user inputs, verified data, and system-controlled calculations.
4. Validate inputs and handle missing or invalid data.
5. Use documented geospatial methods and appropriate data structures.
6. Integrate external services only through permitted, secure mechanisms.
7. Implement evidence provenance and auditability where required.
8. Maintain consistent UI behaviour and responsive design.
9. Avoid fabricated datasets, analytical outputs, or misleading demonstrations.
10. Protect existing functionality when modifying code.

### Incremental workflow

For each development work package:

1. Review the relevant approved requirements.
2. Confirm dependencies and acceptance criteria.
3. Implement the functionality.
4. Perform available automated and manual checks.
5. Verify expected behaviour and edge cases.
6. Record defects and unresolved limitations.
7. Update relevant implementation documentation.
8. Proceed when the work package meets its acceptance criteria.

Where implementation cannot be executed or tested in the available environment, state that limitation explicitly.

### Deliverables

- Application source code.
- Reusable UI and system components.
- Configurable business and assessment workflows.
- Data and geospatial processing components.
- Integrations and supporting services.
- Tests and implementation records.
- Technical documentation necessary for maintenance.

## 10. Stage 6 — Verification and validation

### Objective

Establish that implemented functionality behaves correctly, meets approved requirements, and does not misrepresent analytical evidence.

### Testing coverage

Testing must address, as applicable:

- Functional correctness and requirement coverage.
- Input validation and configuration persistence.
- User workflows, navigation, and accessibility.
- Responsive behaviour across supported devices.
- Data ingestion, transformation, and storage.
- Geographic coordinates, boundaries, distances, and spatial operations.
- Analytical calculations, assumptions, and output interpretation.
- Data confidence and analysis confidence presentation.
- Security, permissions, and sensitive data handling.
- API failures, unavailable sources, and missing-data states.
- Performance, reliability, and error recovery.
- Regression behaviour after changes.

### Validation distinctions

Separate:

- Code generated.
- Code executed.
- Functionality implemented.
- Tests performed.
- Tests passed.
- Analytical methodology validated.
- User acceptance obtained.

These states are not interchangeable.

### Deliverables

- Test plan and test results.
- Defect and resolution log.
- Requirement verification matrix.
- Geospatial and analytical validation findings.
- Usability and accessibility review findings.
- Known limitations and residual risks.
- Release-readiness recommendation.

### Completion criteria

Critical defects and material analytical or security risks must be resolved or explicitly addressed before production release.

A working demonstration alone does not establish production readiness.

## 11. Stage 7 — Deployment preparation and release

### Objective

Prepare the application for controlled, secure, and maintainable operation.

### Activities

- Confirm the intended hosting and deployment environment.
- Verify configuration and secret management.
- Establish database, storage, and backup requirements.
- Validate deployment dependencies and service permissions.
- Review privacy, licensing, and security obligations.
- Configure monitoring, logging, and error reporting.
- Establish recovery and rollback procedures.
- Verify production data and environment readiness.
- Complete user acceptance and deployment approval.

### Deliverables

- Deployment and configuration instructions.
- Operational readiness checklist.
- Security and dependency review.
- Backup, recovery, and rollback plan.
- User and administrator guidance.
- Release notes and known limitations.
- Deployment approval record.

### Completion criteria

Production deployment requires explicit approval and satisfactory operational readiness.

Do not assume that a successful local or development-environment build is production-ready.

## 12. Stage 8 — Maintenance and continuous improvement

### Objective

Preserve reliability, relevance, security, and usability after deployment.

### Activities

- Monitor application errors and operational health.
- Maintain integrations and dependencies.
- Review data-source changes, licensing, and availability.
- Monitor geographic data quality and analytical limitations.
- Address defects and security vulnerabilities.
- Evaluate user feedback and enhancement requests.
- Maintain tests and technical documentation.
- Review the impact of consequential changes before release.

### Deliverables

- Maintenance and incident records.
- Change and release history.
- Updated test and validation results.
- Data-source and dependency reviews.
- Prioritised improvement backlog.

Improvements must not silently change approved analytical methodology or historical assessment interpretations.

## 13. Approval and decision gates

Approval is required for consequential decisions, including:

- Material changes to business objectives or platform scope.
- Major analytical methods, scoring systems, weights, thresholds, or exclusion rules.
- Significant architecture or technology commitments.
- Paid services, licensing, or financial commitments.
- Material security, privacy, or data-sharing decisions.
- Production deployment.
- Changes that materially affect approved assessment interpretation.

Routine implementation details and reversible, low-risk engineering decisions may proceed without repeated approval, provided they remain within established requirements.

For decisions requiring approval, present the recommendation, rationale, alternatives where material, risks, and consequences.

Do not interpret a lack of response as approval.

## 14. Requirements, decisions, and change control

Maintain traceability between:

- Business objectives.
- User and system requirements.
- Research evidence.
- Approved analytical methods.
- Architecture and design decisions.
- Implemented features.
- Tests and validation results.
- Released functionality.

Use stable requirement identifiers where useful.

Maintain a decision log for consequential choices and an issue register for unresolved matters.

When a proposed change affects an approved baseline:

1. Identify the reason and supporting evidence.
2. Assess affected requirements, architecture, data, tests, and documentation.
3. Determine whether approval is required.
4. Apply the approved change consistently.
5. Update traceability and relevant tests.

Do not reopen completed foundational decisions for minor wording preferences or speculative improvements.

## 15. Google AI Studio execution and context management

Google AI Studio is an AI-assisted development environment within the project workflow, not the governing source of business truth.

### 15.1 Context selection

For each task, provide the minimum sufficient context:

- Relevant governing instructions.
- The specific requirements document or section.
- Necessary dependencies and approved decisions.
- Existing implementation context when modifying code.
- Explicit task objective and expected output.

Do not automatically load every project document into every prompt.

### 15.2 Development task instructions

Tasks supplied to the AI model should clearly specify:

- What must be developed or analysed.
- Which requirements govern the task.
- What existing functionality must be preserved.
- What assumptions are prohibited.
- Expected deliverables.
- Validation and acceptance criteria.
- Known limitations or dependencies.

### 15.3 Output discipline

Require the AI model to:

- Avoid unsupported factual and technical claims.
- Distinguish proposed work from completed work.
- Avoid unnecessary repetition and speculative features.
- Report material blockers and unresolved decisions.
- Preserve consistency with approved requirements.
- State what has and has not been executed or tested.

Token efficiency must be achieved through modularity, selective context, and concise instructions—not by omitting critical requirements.

## 16. Reporting and communication

Project communication must be concise, accurate, professional, and understandable to users without specialist technical knowledge.

Progress reporting should identify:

- Work completed and its verification status.
- Current stage and active work.
- Material findings or decisions.
- Risks, blockers, and dependencies.
- Actions requiring user approval.
- Recommended next steps.

Avoid repetitive summaries, unnecessary approval requests, and lengthy explanations that do not improve project decisions.

Do not claim independent research, successful execution, completed testing, or production readiness without supporting evidence.

## 17. Foundation review and transition to development

Before substantial application development, conduct a structured foundation review covering:

1. Completeness of the core requirements.
2. Consistency across documents 00–08.
3. Clear separation of configuration, evidence, and system logic.
4. Business and geographic scope flexibility.
5. Evidence and analytical integrity.
6. Data availability and feasibility dependencies.
7. User experience and accessibility requirements.
8. Technical architecture and integration feasibility.
9. Security, privacy, and deployment requirements.
10. Acceptance criteria, traceability, and unresolved decisions.
11. Suitability of the documentation for efficient Google AI Studio use.

Record material gaps and resolve those that block safe or meaningful development.

Do not delay low-risk prototyping solely because later-stage research or operational details remain unresolved.

The objective is a sufficiently stable, implementation-ready foundation—not an unrealistic guarantee that requirements will never change.

## 18. Governing principle

**The project must advance through controlled, evidence-based, testable development while maintaining consistency between business requirements, research, analytical methods, application behaviour, and user-facing outputs.**

Every stage must produce useful, traceable deliverables.

No stage should be considered complete solely because documentation or code has been generated.

The final objective is a trustworthy, configurable, user-friendly Retail Location Intelligence Platform that can support real-world business decisions without presenting unsupported certainty.