# 02_research_and_data_framework.md

**Project:** Retail Location Intelligence Platform  
**Document:** Research and Data Framework  
**Version:** 1.0  
**Status:** Proposed baseline — subject to project approval

## 1. Purpose and scope

This document defines the framework for identifying, evaluating, accessing, validating, and preparing data and research evidence for the Retail Location Intelligence Platform.

The framework supports evidence-based retail location assessments while remaining independent of any particular organisation, industry, geographic market, or deployment.

Research must establish what information is needed, what is actually available, whether it is reliable and legally usable, and what conclusions it can support.

This document governs research and data preparation. Analytical confidence, suitability assessment, and interpretation are governed by `03_analysis_evidence_and_confidence.md`. Project-wide instructions and approvals are governed by `01_master_instructions.md`.

## 2. Research objectives

Research activities shall:

1. Identify data and evidence relevant to the configured business objectives and geographic scope.
2. Investigate credible primary and secondary data sources.
3. Determine geographic coverage, reporting periods, granularity, availability, and update frequency.
4. Verify data provenance, credibility, methodology, access conditions, and permitted uses.
5. Assess completeness, accuracy, consistency, timeliness, and geographic suitability.
6. Identify relevant academic research and established analytical methods.
7. Document data gaps, limitations, uncertainties, and conflicts.
8. Determine whether available evidence is sufficient for the proposed analyses.
9. Recommend defensible data acquisition, preparation, and validation approaches.
10. Produce traceable research outputs that can inform platform design and subsequent assessments.

Research findings must distinguish confirmed availability from potential or unverified sources.

## 3. Research scope and configuration

### 3.1 Organisation-independent framework

The platform must not assume that every organisation requires the same data categories, indicators, competitors, customer segments, or analytical methods.

Research requirements shall be derived from the configured:

- Organisation and business profile.
- Industry, products, services, and outlet format.
- Assessment objectives.
- Geographic scope.
- Existing business network, where available.
- Relevant market and competitor definitions.
- Approved assessment requirements and constraints.

The initial deployment may focus on Sri Lanka and D. Samson & Sons (Pvt) Ltd., but those details must remain deployment-specific rather than permanent platform assumptions.

### 3.2 Research boundaries

Before research begins, establish the assessment's geographic extent, relevant time period, required geographic resolution, business context, and intended analytical outputs.

Where requirements are unclear, record the uncertainty and obtain clarification when it materially affects research scope, cost, legality, or analytical validity.

Do not silently broaden scope or introduce unapproved business assumptions.

## 4. Candidate data categories

The following categories form an initial research checklist, not a mandatory or exhaustive set of universal location-selection factors.

| Category | Potential research coverage |
|---|---|
| Competitor locations | Relevant competitor outlets, branch locations, operating status, formats, and market presence |
| Retail and commercial activity | Retail chains, shopping centres, commercial establishments, and activity concentrations |
| Supermarkets and anchors | Supermarkets and other potentially relevant destination or anchor establishments |
| Financial institutions | Banks, branches, ATMs, and other financial services where relevant |
| Pedestrian activity | Observed or estimated footfall, pedestrian movement, and associated coverage limitations |
| Road traffic and accessibility | Road networks, traffic observations, transport connectivity, travel conditions, and access |
| Population | Population distribution, density, demographic composition, and relevant geographic units |
| Income and purchasing power | Credible income, expenditure, socioeconomic, or purchasing-power indicators |
| Existing outlet network | Authorised organisation-specific locations, coverage, formats, and relevant operational information |
| Additional contextual indicators | Land use, employment, development activity, public transport, site characteristics, or other justified variables |

For each category:

- Establish its relevance to the specific assessment.
- Identify candidate sources and available fields.
- Check coverage, recency, geographic granularity, and reliability.
- Determine whether data represent direct observations, estimates, proxies, or modelled values.
- Document limitations and suitability for intended use.
- Exclude or defer categories that lack sufficient relevance or defensible evidence.

The presence of a category in this checklist does not authorise its automatic use in a suitability model.

Specific competitor names, retail brands, and business classifications must come from user configuration or a verified, reviewable discovery process.

## 5. Data source identification and verification

### 5.1 Source discovery

Investigate sources appropriate to the configured geography and requirements, including:

- Official government statistics, censuses, surveys, and administrative records.
- National and local geographic or planning authorities.
- Authoritative open-data portals and geospatial repositories.
- Official organisation and business-location records.
- Licensed commercial data providers.
- Documented mapping, geocoding, and routing services.
- Peer-reviewed publications and credible technical research.
- Authorised internal organisational datasets.

Source selection must be based on relevance, credibility, coverage, and permitted use—not convenience alone.

### 5.2 Source verification

For every material source, establish where possible:

- Publisher or responsible organisation.
- Dataset or publication title.
- Original source URL, DOI, or stable identifier.
- Publication date and underlying observation/reference period.
- Geographic coverage and resolution.
- Data collection and production methodology.
- Available fields, formats, and access mechanisms.
- Update frequency and known limitations.
- Licence, access restrictions, and permitted uses.
- Date accessed and verification status.

A search result, catalogue entry, documentation page, or advertised dataset is not proof that usable data have been obtained.

Distinguish **discovered**, **verified**, **accessible**, **retrieved**, **validated**, and **approved for use** statuses.

### 5.3 Source preference

Prefer authoritative, methodologically transparent, geographically appropriate, and sufficiently recent sources.

Where sources disagree, compare their definitions, dates, coverage, methodology, and underlying observations before selecting or combining them.

Do not assume that an official source is automatically complete, current, or suitable for every analytical purpose.

## 6. Research literature and methodological evidence

Identify relevant academic papers, technical publications, and credible industry research addressing retail location intelligence, spatial analysis, market potential, accessibility, catchment analysis, competitor effects, and other assessment-specific topics.

Evaluate each material publication for:

- Authorship, publisher, publication venue, and date.
- Research question and methodology.
- Data sources, geographic context, and sample characteristics.
- Findings, assumptions, limitations, and validation.
- Relevance and transferability to the configured business and geography.

Maintain a clear distinction between published findings and methods proposed for this platform.

A method demonstrated in another country, sector, or period must not be treated as locally validated without further justification.

Do not invent references, findings, statistical relationships, or methodological endorsements.

Research evidence may inform candidate methods, but material analytical decisions require the approvals defined in the master instructions.

## 7. Geographic scope and spatial data requirements

### 7.1 Geographic coverage

Research shall consider the configured country, region, administrative units, cities, towns, selected areas, or user-defined boundaries.

Assess whether sources cover the entire requested area or only selected locations.

Record missing geographic areas explicitly. Do not infer that an establishment, road, population group, or activity is absent merely because it is missing from a dataset.

### 7.2 Spatial integrity

For spatial datasets, inspect:

- Coordinate reference system and coordinate validity.
- Geographic accuracy and geocoding quality.
- Administrative boundary definitions and versions.
- Spatial resolution and aggregation level.
- Duplicate, incomplete, ambiguous, or incorrectly positioned records.
- Compatibility between datasets and time periods.

Use documented coordinate transformations and spatial operations.

Distinguish straight-line distance, road-network distance, travel time, and accessibility. Do not substitute one for another without an explicitly justified method.

### 7.3 Geographic compatibility

Where datasets use different boundaries, geographic units, or resolutions, document the differences and assess whether defensible harmonisation is possible.

Do not imply neighbourhood-level or site-level precision from district-level or otherwise aggregated data.

## 8. Data recency and temporal consistency

For each source, record the actual reference period separately from the publication, retrieval, and update dates.

Classify values appropriately as historical observations, current observations, estimates, projections, forecasts, or unknown.

Assess whether:

- Data are sufficiently recent for the intended decision.
- Different sources represent comparable time periods.
- Historical series use consistent definitions and boundaries.
- Consecutive-year data are genuinely available where needed.
- Changes in collection methods affect comparability.

Do not invent a universal recency threshold or automatically reject older data. Determine acceptable recency according to the indicator, rate of change, intended use, and approved requirements.

Where only outdated information exists, disclose its age and implications.

## 9. Data access, licensing, and responsible use

### 9.1 Access assessment

Investigate appropriate acquisition methods, including official downloads, documented APIs, licensed services, approved data transfers, and authorised internal access.

For each proposed method, record relevant authentication, quotas, costs, coverage, technical constraints, and maintenance considerations.

Do not assume an API, downloadable dataset, or automated integration exists without verification.

### 9.2 Legal and contractual requirements

Before operational use, verify applicable:

- Licensing and reuse permissions.
- Commercial-use and redistribution restrictions.
- Attribution obligations.
- API and platform terms.
- Storage, caching, retention, and sharing restrictions.
- Privacy and confidentiality requirements.
- Applicable access and security obligations.

Public availability does not establish permission for commercial reuse, scraping, redistribution, or persistent storage.

Do not bypass access restrictions, authentication controls, or contractual limitations.

### 9.3 Internal and sensitive information

Treat organisation-provided data as authorised, potentially confidential information.

Record ownership, permitted purposes, access controls, and relevant retention requirements.

Use only approved internal datasets. Do not assume that confidential organisational records are publicly accessible or available to other platform users.

Credentials and API secrets must not be embedded in research documents, source code, or exposed client-side configuration.

### 9.4 Unavailable or restricted sources

When a useful source cannot be accessed or licensed, document the restriction and investigate legitimate alternatives.

A proxy or substitute dataset must be identified as such, with its limitations and applicability assessed before use.

## 10. Data quality and validation

### 10.1 Quality dimensions

Evaluate datasets against relevant dimensions:

- **Completeness:** Missing records, fields, locations, periods, and coverage.
- **Accuracy:** Reliability of values, coordinates, classifications, and measurements.
- **Consistency:** Compatible definitions, formats, units, and relationships.
- **Uniqueness:** Duplicate or overlapping records and entities.
- **Timeliness:** Observation dates, updates, and currency.
- **Geographic suitability:** Spatial precision, coverage, and resolution.
- **Methodological reliability:** Collection procedures, sampling, estimation, and known biases.
- **Representativeness:** Whether observed data reasonably reflect the intended population or geography.
- **Usability:** Appropriate fields, formats, documentation, and lawful access.

Validation requirements must reflect the data type and intended analysis.

### 10.2 Validation activities

As applicable:

1. Inspect schema, field definitions, units, formats, and metadata.
2. Check missing, malformed, duplicated, and inconsistent records.
3. Validate geographic coordinates and boundary relationships.
4. Check date fields, temporal coverage, and comparability.
5. Examine implausible values and outliers without automatically deleting them.
6. Cross-check important records or aggregates against independent credible evidence where feasible.
7. Inspect classification and entity-matching errors.
8. Record validation findings, corrections, exclusions, and unresolved issues.
9. Preserve traceability to original data.

Cleaning must not silently change the meaning of source records.

### 10.3 Quality outcomes

Classify each dataset's readiness for a specified use as, for example, suitable, conditionally suitable, unsuitable, or not yet assessed.

These are descriptive workflow states, not invented numerical quality scores.

Document the rationale and any conditions for use.

Detailed confidence assessment and the relationship between data quality, analytical confidence, and location suitability are governed by `03_analysis_evidence_and_confidence.md`.

## 11. Population and market interpretation

Research must distinguish:

- Total population.
- Potential customer population.
- Observed customer base.
- Catchment population.

These concepts must not be treated as interchangeable.

Population totals alone do not establish demand, customer conversion, purchasing power, or commercial attractiveness.

Any segmentation, catchment estimation, market potential, or demand-related inference must use a documented and justified method supported by appropriate evidence.

Do not assume a universal customer segment, catchment radius, spending pattern, or conversion rate.

## 12. Data preparation and provenance

Before analytical use, define appropriate preparation procedures for each approved dataset.

These may include standardisation, geocoding, deduplication, spatial joins, boundary harmonisation, temporal alignment, entity matching, and derived-variable creation.

Maintain traceability from original source records to prepared datasets and derived outputs.

Record, where applicable:

- Source and dataset version.
- Retrieval date and acquisition method.
- Original and transformed schemas.
- Cleaning and transformation steps.
- Matching or geocoding assumptions.
- Records excluded or modified and reasons.
- Validation outcomes and unresolved limitations.

Preserve original data where permitted and operationally appropriate.

Avoid destructive transformations and undocumented changes.

## 13. Research registers and required outputs

Research must produce structured, reusable, evidence-based records and a clear research report. The outputs must establish what data is required, what is available, how reliable and recent it is, whether it can be lawfully used, and what gaps remain.

### 13.1 Research registers

Maintain the following records throughout the research process.

**Data Source Register**

For each material source, record:

- Data category and specific variables.
- Source name, publisher, and direct source URL or identifier.
- Geographic coverage and resolution.
- Latest observation period and historical availability.
- Access method, cost, licensing, and usage restrictions.
- Data quality, methodology, and known limitations.
- Intended analytical use.
- Verification, retrieval, validation, and approval status.

**Research Evidence Register**

Record relevant academic publications, technical studies, methodologies, findings, limitations, geographic applicability, and supporting references.

**Data Availability and Gap Register**

Track available, partially available, inaccessible, outdated, unsuitable, and unverified information, including geographic and temporal gaps, alternative sources, and implications for planned analyses.

These registers must remain traceable to their underlying evidence and consistent with the research report.

### 13.2 Mandatory research deliverables

The initial research stage must produce the following seven identifiable deliverables.

**Deliverable 1 — Executive Summary**

Provide a concise overview of:

- Overall research findings.
- Strongest verified and relevant data sources.
- Available data categories.
- Major geographic, temporal, and quality limitations.
- Access, licensing, cost, and technical restrictions.
- Important information gaps.
- Recommended next steps.

Do not claim that the evidence is sufficient for location selection unless that conclusion has been established.

**Deliverable 2 — Data Source Register**

Present the identified sources in a structured table.

Include the data category, variables, source identity, direct reference, geographic coverage and resolution, observation period, historical availability, access method, cost, licensing restrictions, quality concerns, intended use, and evidence status.

Distinguish discovered sources from verified, accessible, retrieved, validated, and approved datasets.

**Deliverable 3 — Data Requirements and Priorities**

Identify the data required for the configured business objectives and geographic scope.

For each relevant category, explain:

- Required variables and their intended purpose.
- Business and analytical relevance.
- Availability and suitability.
- Dependencies and limitations.
- Proposed research or acquisition priority.

Priorities must be justified by the assessment requirements and available evidence. Do not invent business priorities or automatically treat every category as mandatory.

**Deliverable 4 — Consecutive-Year Availability Assessment**

Assess whether historical data are available for consecutive years where relevant to the intended analysis.

Document:

- Available observation years and periods.
- Missing years or discontinuities.
- Geographic coverage and resolution.
- Changes in definitions, boundaries, or collection methods.
- Temporal comparability.
- Suitability for trend analysis.

Distinguish the observation period from the publication or retrieval date.

Do not claim that consecutive-year data exist without verifying the relevant records.

**Deliverable 5 — Research Evidence Summary**

Summarise relevant verified evidence, including:

- Authoritative data sources and publications.
- Relevant academic and technical research.
- Research methods and findings.
- Geographic and business applicability.
- Assumptions, limitations, and conflicting evidence.
- Implications for possible future analytical methods.

Clearly distinguish published findings, verified facts, proposed methods, and untested assumptions.

**Deliverable 6 — Data Quality and Validation Plan**

Define the checks required before using relevant datasets.

Address:

- Completeness and missing values.
- Accuracy and consistency.
- Duplicates and entity matching.
- Geographic validity and resolution.
- Temporal consistency and recency.
- Outliers and implausible observations.
- Methodological reliability and representativeness.
- Provenance and transformation traceability.
- Validation responsibilities and unresolved issues.

Specify the expected validation approach and record actual validation results separately.

Do not describe a dataset as validated when the checks have not been performed.

**Deliverable 7 — Data Gaps and Recommended Next Steps**

Identify unresolved data and research requirements.

For each significant gap, document:

- Missing or inadequate information.
- Affected data category or analytical requirement.
- Consequences for the proposed assessment.
- Potential authorised sources or alternatives.
- Required permissions, resources, or decisions.
- Recommended next action and dependencies.

Recommendations must be prioritised and justified.

Do not proceed to unsupported suitability scoring, predictive modelling, or location rankings merely because the research report has been produced.

### 13.3 Research report structure

Present the final initial-stage research report in the following order:

1. Executive Summary.
2. Data Source Register.
3. Data Requirements and Priorities.
4. Consecutive-Year Availability Assessment.
5. Research Evidence Summary.
6. Data Quality and Validation Plan.
7. Data Gaps and Recommended Next Steps.

Supporting registers, detailed evidence, and supplementary technical information may be included as appendices or linked records.

All seven deliverables must remain identifiable, even where some findings are incomplete or unavailable.

### 13.4 Research output quality requirements

All research outputs must:

- Address relevant data categories without silently omitting difficult areas.
- Use consistent terminology, source identities, dates, and evidence statuses.
- Distinguish verified, partially verified, unverified, estimated, and unavailable information.
- Provide traceable references for material factual claims.
- Clearly disclose missing evidence, limitations, and uncertainty.
- Avoid unsupported analytical or commercial conclusions.
- Remain understandable to both technical and business stakeholders.
- Identify decisions requiring approval.
- Remain reusable across organisations and geographic markets.

The research framework and seven-deliverable structure define the initial research stage. Detailed project-stage responsibilities and handoffs remain governed by `04_project_workflow_and_deliverables.md`.

## 14. Research completion and analytical readiness

Research is not complete merely because sources have been listed.

Before a dataset is used for a material analytical conclusion, establish that:

1. Its source and provenance are documented.
2. Access and intended use are permitted.
3. Its geographic and temporal coverage are understood.
4. Relevant quality checks have been performed.
5. Its limitations and uncertainty are recorded.
6. Its suitability for the intended analytical operation has been assessed.
7. Any consequential assumptions or methodological decisions have been approved.

Readiness is **specific to the proposed analysis**, not a blanket certification of a dataset.

Insufficient data must lead to an explicitly limited or deferred analysis—not fabricated completeness, unsupported scores, or unjustified recommendations.

## 15. Governing principle

**Research must establish the credibility, availability, permitted use, and analytical suitability of evidence before that evidence is used to support retail location decisions.**

The platform must remain capable of reporting that evidence is incomplete or that an assessment cannot yet be supported.

No source, indicator, method, or conclusion should be presented as verified unless the corresponding verification has actually occurred.