# Retail Location Intelligence Platform — Documentation Guide

**Document:** Project Documentation Index and AI Context Guide  
**Version:** 1.0  
**Status:** Supporting documentation guide

## 1. Purpose

This README explains the project documentation structure, document responsibilities, instruction hierarchy, and context-selection rules for AI-assisted development.

It is a navigation and reference guide, not an additional source of business requirements.

The Retail Location Intelligence Platform is an organisation-independent, configurable, evidence-driven application for assessing potential physical business locations.

Development is supported by Google AI Studio and other approved tools, with technical and analytical decisions governed by the project documentation.

## 2. Active project documents

All active project instruction documents are located in the `prompts/` directory.

| File | Primary responsibility |
|---|---|
| `00_platform_overview.md` | Platform purpose, identity, objectives, scope, and governing principles |
| `01_master_instructions.md` | Project leadership, AI behaviour, instruction hierarchy, quality standards, and approvals |
| `02_research_and_data_framework.md` | Research methodology, data requirements, sources, licensing, validation, and research deliverables |
| `03_analysis_evidence_and_confidence.md` | Analytical integrity, evidence sufficiency, data confidence, analysis confidence, and suitability |
| `04_project_workflow_and_deliverables.md` | Project lifecycle, workstreams, deliverables, milestones, decision gates, and reporting |
| `05_user_requirements_and_assessment_workflow.md` | User requirements, roles, assessment journey, and expected application behaviour |
| `06_functional_requirements_and_ui_ux.md` | Functional specifications, application structure, interface behaviour, usability, and acceptance criteria |
| `07_technical_architecture_and_data_management.md` | Technology stack, frontend, backend, database, APIs, GIS, integrations, and data management |
| `08_security_testing_and_deployment.md` | Security, privacy, testing, validation, deployment, monitoring, and production readiness |

These documents collectively define the proposed project foundation.

A document being present does not mean that every proposed technical or business decision has been approved, implemented, or tested.

## 3. Historical reference material

The original research document is stored separately:

`../reference/data_source_identification_original.md`

This document preserves the initial research requirements, background, and historical project context.

It may be consulted for requirements traceability, research coverage, and clarification.

It is not an additional active instruction document and must not automatically override the current approved project requirements.

If an important historical requirement appears to be missing, identify the discrepancy and recommend a controlled correction rather than silently changing the active specifications.

## 4. Instruction hierarchy

Apply the instruction and approval hierarchy defined in `01_master_instructions.md`.

In general:

1. Follow the latest explicit user approvals and decisions within their applicable scope.
2. Follow the governing instructions in `01_master_instructions.md`.
3. Apply the relevant subject-specific requirements in documents 00–08.
4. Respect approved architecture, methodology, and configuration decisions.
5. Treat provisional recommendations and examples as unapproved until confirmed.
6. Use historical references for context, not as competing instructions.

When documents appear inconsistent, identify the conflict and its impact before making consequential changes.

Do not silently replace approved decisions.

## 5. AI context-selection rules

Use only the documentation necessary for the current task.

Always preserve the essential governing constraints from `01_master_instructions.md`.

Read additional documents according to task relevance.

| Task | Primary documents |
|---|---|
| Understand platform purpose and scope | 00, 01 |
| Plan research or investigate data sources | 01, 02, 03 |
| Evaluate data quality, evidence, or analytical methods | 01, 02, 03 |
| Plan workstreams, deliverables, or milestones | 01, 04 |
| Define user journeys and requirements | 01, 05 |
| Design interfaces and application functionality | 01, 05, 06 |
| Develop frontend components | 01, 06, 07 |
| Develop backend APIs and database structures | 01, 05, 07, 08 |
| Implement geographic processing or analysis | 01, 02, 03, 07 |
| Implement authentication or access controls | 01, 07, 08 |
| Perform testing and quality assurance | 01, 05, 06, 07, 08 |
| Prepare deployment or production operations | 01, 07, 08 |
| Review the complete foundation | 00–08 and the historical reference where relevant |

These are starting points, not rigid restrictions.

Load another document when its requirements materially affect the task.

Do not repeatedly load every document, the entire codebase, or the historical reference when a smaller relevant context is sufficient.

If a required file is unavailable, request it or state the limitation. Never claim to have read inaccessible content.

## 6. AI-assisted implementation workflow

For each implementation task:

1. Identify the relevant approved requirements and decisions.
2. Inspect the affected code, schemas, and interfaces.
3. Identify dependencies, constraints, and potential risks.
4. Propose a focused implementation approach.
5. Obtain approval where required.
6. Implement the smallest coherent, testable change.
7. Run relevant validation and tests where tools are available.
8. Report actual results, failures, limitations, and unresolved items.
9. Update relevant project records only when justified.

Avoid unnecessarily rewriting working components or creating duplicate implementations.

Do not introduce hard-coded organisation identities, competitors, scoring criteria, weights, catchment distances, or other unapproved business assumptions.

Do not fabricate datasets, analytical outputs, integrations, research findings, or test results.

## 7. Project ownership and professional responsibilities

The AI development partner is expected to act proactively across:

- Project leadership and solution architecture.
- Business requirements and retail location intelligence.
- Geospatial analysis and GIS engineering.
- Data research, engineering, and data science.
- AI/ML engineering where justified.
- Frontend, backend, and database development.
- UI/UX design and accessibility.
- Security, testing, and deployment planning.
- AI prompt and context engineering.

Responsibilities include identifying risks, maintaining consistency, recommending technically sound solutions, and preventing avoidable rework.

Consequential business decisions, material methodology choices, significant requirement changes, and financial commitments remain subject to user approval.

## 8. Decision and implementation status

Distinguish clearly between:

- Proposed.
- Approved.
- Implemented.
- Tested.
- Validated.
- Deferred.
- Blocked.

A recommended technology is not automatically an approved dependency.

Generated code is not automatically working code.

A functioning interface is not proof of correct analytical behaviour.

Research findings are not verified merely because an AI model presents them confidently.

Maintain traceability between relevant requirements, implementation tasks, evidence, tests, and decisions.

## 9. Documentation maintenance

The nine active documents form the project foundation.

Maintain them through controlled, targeted amendments rather than unnecessary rewrites.

Before changing an established requirement:

1. Identify the affected document and section.
2. Explain the reason and impact.
3. Check related requirements and dependencies.
4. Determine whether approval is required.
5. Make the smallest complete correction.
6. Record consequential changes where appropriate.

Do not reopen settled decisions without a genuine requirement change, verified defect, material new evidence, or justified technical dependency.

## 10. Governing principle

**Use the right project context for the right task, preserve approved requirements, and build the platform incrementally with verifiable evidence.**

The objective is a reliable, secure, maintainable, organisation-independent Retail Location Intelligence Platform—not merely a collection of prompts or a visually convincing prototype.