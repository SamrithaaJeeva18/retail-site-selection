# Retail Location Intelligence Platform — Implementation Master

**Purpose:** Operational instructions for AI-assisted Phase 1 implementation. This file does not replace or amend the frozen foundation documents.

## 1. Authority and project boundaries

- The GitHub repository is the source of truth for code, documents, decisions, and progress.
- `prompts/01_master_instructions.md` governs project-wide behaviour. `prompts/00_platform_overview.md` establishes the product purpose. Files `02`–`08` define specialist requirements. `prompts/readme.md` explains their roles. If repository paths differ, discover the actual paths rather than guessing.
- Follow the frozen foundation. Do not rewrite it or introduce requirements without an identified contradiction, verified defect, or approved change.
- The platform is organisation-independent. Do not hard-code organisation, industry, geography, competitors, scoring criteria, weights, thresholds, catchments, or unapproved business assumptions.
- Distinguish user configuration, verified data, and system-controlled operations. Keep data confidence, analysis confidence, and suitability separate.
- Never invent sources, metrics, analytical results, tests, integration success, or completion status.
- Significant business methodology, security architecture, provider commitments, and paid-service choices require explicit user approval.

## 2. Context loading and token discipline

1. At session start, read this file and `implementation/current_task.md` (if present). Consult the foundation README or headings to locate the relevant source documents.
2. Read only the sections of foundation documents relevant to the current task; follow cross-references where necessary. Do not automatically ingest all nine files.
3. Treat the existing foundation master as governing authority, but avoid repeatedly copying its full text into each prompt. If repository access cannot retrieve a required section, say so and request the specific content.
4. Before coding, state the task, required files/sections, assumptions, planned changes, and verification criteria in a concise summary.
5. Work in one bounded task at a time. Avoid unrelated refactors, broad document rewrites, and unnecessary dependencies.
6. Reuse code and project context already present; avoid regenerating entire files when a focused patch is sufficient.
7. Maintain a brief task log with file changes, commands/tests actually run, outcomes, blockers, and next action. Do not claim tests were run unless execution evidence exists.

## 3. Task-based document routing

- **Project setup and dependency compatibility:** `00`, `01`, `07`, relevant `08` controls.
- **Assessment workflow and UI:** `00`, `05`, `06`, relevant `07` architecture.
- **Map and geospatial interactions:** `05`, `06`, `07`; consult `02` for data-source constraints.
- **Database, identity, tenancy and protected APIs:** `07`, `08`, relevant `05`/`06` requirements. Resolve identity and tenant-isolation design before implementing protected organisation-specific operations.
- **Research, data ingestion and external providers:** `02`, `03`, `07`, `08`.
- **Evidence, confidence and analytical output:** `03`, `05`, `06`, `07`.
- **Testing and deployment:** `07`, `08`, plus acceptance criteria for the current feature.

The numbers above refer to files under `prompts/`; use exact filenames from the repository. Read additional sections only when the task requires them.

## 4. Proposed Phase 1 technical boundaries

- Candidate frontend: React, TypeScript, Vite and MapLibre GL JS.
- Candidate backend: Python with FastAPI.
- Candidate spatial persistence: PostgreSQL with PostGIS; SQLAlchemy/Alembic as proposed.
- Use stable, supported, security-maintained, mutually compatible dependencies; select, verify, record and lock exact versions during implementation.
- Prefer a modular monolith. Do not substitute a Node.js-only backend, non-spatial database, commercial service, or AI-based scoring for the proposed architecture without a documented rationale and approval.
- Google AI Studio may be used for code generation and supported previews. Verify its actual repository access, runtime and sync capabilities; use VS Code/local or other approved environments to run components not supported in the AI Studio environment.
- Use synthetic, clearly labelled test data for the POC. Do not use confidential organisation data or unlicensed third-party data.
- Do not add Redis, distributed workers, paid hosting, or paid APIs until justified and approved.

## 5. Implementation order and gates

**P1.1 — Repository and environment:** Verify repository access, inspect structure, set up frontend/backend/database scaffolding, environment examples, ignore rules, and dependency manifests. No secrets in Git.

**P1.2 — Compatibility:** Demonstrate frontend build, API startup, PostGIS extension and spatial query, database migration, and frontend-to-backend communication. Record actual command output.

**P1.3 — Security design:** Record authentication-provider options and tenant-isolation design, obtain approval for consequential choices, then test organisation-scoped access before protected features.

**P1.4 — Initial application:** Build an application shell, guided assessment navigation, and map interaction using synthetic data; do not fabricate suitability rankings or confidence scores.

**P1.5 — Integration and verification:** Run applicable tests, document results and limitations, resolve critical issues, and prepare a Phase 2 backlog.

Production readiness is a separate gate governed by file `08`.

## 6. Response and change-control contract

For each task, respond concisely with:

1. **Task and governing references** — exact foundation sections consulted.
2. **Plan** — bounded steps and any approval needed.
3. **Changes** — exact files created/modified; do not modify unrelated files.
4. **Verification** — commands executed, results observed, and tests not run.
5. **Status and next task** — complete, partial, or blocked, with evidence.

If GitHub integration, execution, or an external provider is inaccessible, state the limitation. Never imply that generated code has been committed, synced, installed, or tested without verification.
