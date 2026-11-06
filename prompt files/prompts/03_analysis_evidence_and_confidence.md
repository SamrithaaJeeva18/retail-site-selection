# 03_analysis_evidence_and_confidence.md

**Project:** Retail Location Intelligence Platform  
**Document:** Analysis, Evidence and Confidence Framework  
**Version:** 1.0  
**Status:** Proposed baseline — subject to project approval

## 1. Purpose and authority

This document defines the principles governing analytical methods, evidence interpretation, uncertainty, confidence assessment, and location suitability evaluation within the Retail Location Intelligence Platform.

Its purpose is to ensure that analytical outputs are reproducible, explainable, geographically valid, and supported by appropriate evidence.

This document applies to research interpretation, geospatial processing, comparative analysis, model development, visualisations, and user-facing recommendations.

It operates under `01_master_instructions.md` and uses the research and validation requirements defined in `02_research_and_data_framework.md`.

No analytical result may be presented as more precise, reliable, or conclusive than its supporting evidence permits.

## 2. Fundamental analytical distinctions

The platform must distinguish the following concepts.

| Concept | Meaning |
|---|---|
| Data quality | Characteristics of a dataset, including completeness, accuracy, consistency, recency, coverage, and suitability |
| Data confidence | Degree of justified confidence in the reliability of particular data or observations |
| Analysis confidence | Degree of justified confidence in an analytical result, considering input evidence, methodology, assumptions, uncertainty, and validation |
| Location suitability | Extent to which a location meets the organisation's approved assessment objectives and evaluation criteria |
| Data availability | Whether information exists and can be accessed for the intended purpose |
| Evidence sufficiency | Whether the available evidence adequately supports a particular conclusion |

These concepts must remain separate in data structures, analytical logic, reports, and the user interface.

**High data or analysis confidence does not establish commercial suitability. High apparent suitability does not establish that the conclusion is reliable.**

A location may be suitable but poorly evidenced, or reliably assessed as unsuitable.

## 3. Evidence classification and traceability

### 3.1 Information classification

Every material analytical input and output must be identifiable as one or more of the following:

- Verified observed data.
- User-provided information.
- Published research findings.
- Estimates or projections.
- Derived or calculated values.
- Modelled outputs.
- Interpretations or hypotheses.
- Unverified information.
- Missing or unavailable information.

User-provided information must not automatically be labelled independently verified.

Derived values must retain links to their inputs and transformation methods.

### 3.2 Evidence provenance

Material analytical claims must be traceable to their supporting sources, reference periods, transformations, assumptions, and analytical procedures.

Where multiple datasets contribute to a result, the platform must preserve sufficient lineage to identify the contributing inputs.

Evidence conflicts, missing sources, and material limitations must be disclosed rather than silently resolved.

### 3.3 Evidence strength

Evaluate evidence in relation to its intended use, considering source credibility, measurement quality, geographic relevance, temporal relevance, methodological transparency, representativeness, and independent corroboration where available.

Do not invent evidence-strength scores, grades, or thresholds without an approved framework.

## 4. Analytical methodology selection

### 4.1 Problem-driven analysis

Select analytical methods based on the configured business question, available evidence, geographic context, and required decision outputs.

Potential approaches include:

- Descriptive statistics and exploratory data analysis.
- Geographic distribution and spatial concentration analysis.
- Distance, proximity, and accessibility analysis.
- Network-based travel distance or time analysis.
- Catchment and service-area analysis.
- Market coverage and spatial gap analysis.
- Competitor and commercial-context analysis.
- Multi-location comparison.
- Statistical or predictive modelling where justified.

These are candidate capabilities, not automatically approved or universally applicable methods.

### 4.2 Method justification

Before implementing a material analytical method, document:

1. The question it is intended to answer.
2. Required inputs and their availability.
3. Methodological assumptions and limitations.
4. Relevant supporting research or technical evidence.
5. Geographic and temporal applicability.
6. Validation approach.
7. Expected outputs and appropriate interpretation.
8. Approval status where required.

Do not select a method solely because it is technically available or visually impressive.

### 4.3 Machine learning

Machine learning is not a default requirement.

Consider it only when the analytical problem, sufficient relevant data, evaluation design, and expected benefits justify its use.

Do not assume that machine learning automatically improves location-selection accuracy.

Predictive outputs must be distinguished from observations and accompanied by appropriate validation and uncertainty information.

## 5. Geographic analytical integrity

### 5.1 Spatial methods

All geographic operations must use appropriate coordinate systems, geometries, spatial resolution, and validated input data.

Distinguish:

- Straight-line distance.
- Road-network distance.
- Travel distance.
- Travel time.
- Geographic proximity.
- Accessibility.

These measures are not interchangeable.

### 5.2 Catchment analysis

Catchment boundaries and methods must reflect the approved assessment requirements and available evidence.

Possible approaches include geographic buffers, network service areas, travel-time areas, and other justified methods.

Do not invent universal catchment radii, travel-time thresholds, or customer reach assumptions.

### 5.3 Spatial limitations

Consider boundary effects, aggregation bias, geographic coverage gaps, coordinate uncertainty, and differences between administrative units and actual market behaviour.

Do not present highly aggregated information as precise site-level evidence.

Geographic visualisations must accurately reflect the underlying spatial data and methodology.

## 6. Population, market potential, and customer interpretation

The platform must distinguish total population, potential customer population, observed customer base, and catchment population.

Population counts or density alone must not be interpreted as actual demand, sales potential, or customer conversion.

Where relevant, investigate credible evidence concerning demographics, purchasing power, consumer behaviour, accessibility, and market characteristics.

Any derived market-potential indicator must have a documented method, justified assumptions, and appropriate evidence.

Do not invent customer conversion rates, expenditure patterns, market-share estimates, or demand relationships.

## 7. Data confidence framework

### 7.1 Objective

Data confidence communicates how reliably a dataset, observation, or indicator can support its intended use.

It must consider relevant evidence such as:

- Source credibility and provenance.
- Accuracy and validation findings.
- Completeness and representativeness.
- Geographic coverage and precision.
- Temporal relevance.
- Methodological reliability.
- Consistency and corroboration.
- Known uncertainty and limitations.

### 7.2 Assessment requirements

The platform must support explicit data-confidence assessments.

However, the numerical formula, categorical scale, aggregation method, and thresholds are not predefined.

These must be researched, justified, documented, validated where possible, and approved before operational use.

Until such a framework is approved, use transparent descriptive assessments with supporting evidence rather than invented confidence percentages.

### 7.3 Missing and uncertain information

Missing information must not automatically receive a numerical zero or be treated as evidence of poor market conditions.

Distinguish unknown, unavailable, unverified, outdated, and invalid data.

Confidence reporting must explain the reason for uncertainty and its consequences for the intended analysis.

## 8. Analysis confidence framework

### 8.1 Objective

Analysis confidence communicates how strongly the available evidence and analytical process support a particular result.

It must account for:

- Confidence in contributing data.
- Coverage and completeness of required inputs.
- Suitability of the analytical method.
- Assumptions and sensitivity to those assumptions.
- Geographic and temporal validity.
- Validation and independent corroboration.
- Uncertainty, missing evidence, and known limitations.

### 8.2 Assessment requirements

Analysis confidence must be assessed separately from data confidence and location suitability.

Do not assume that averaging input confidence values produces valid analysis confidence.

Any formal confidence calculation, scale, aggregation rule, or threshold requires methodological justification and approval.

Where quantitative assessment is not defensible, report evidence-based qualitative limitations and uncertainty.

### 8.3 Confidence interpretation

Confidence measures the reliability of a conclusion, not whether that conclusion is favourable.

The interface and reports must prevent users from confusing high confidence with high commercial attractiveness.

## 9. Location suitability and comparative evaluation

### 9.1 Suitability definition

Location suitability is determined by how well a candidate location meets the organisation's configured and approved business requirements.

Relevant factors, eligibility conditions, comparison methods, and business priorities must be configurable or derived through an explicitly approved process.

### 9.2 Evaluation methods

Potential approaches may include:

- Criteria-based comparison.
- Constraint or eligibility screening.
- Spatial coverage assessment.
- Multi-criteria decision analysis.
- Scenario comparison.
- Other evidence-supported approaches.

No method is automatically authorised by inclusion in this document.

### 9.3 Weights, scoring, and rankings

Do not invent or silently apply:

- Evaluation criteria.
- Criteria weights.
- Scoring scales or normalisation rules.
- Thresholds or exclusion conditions.
- Aggregation formulas.
- Rankings or recommendation rules.

Material evaluation methodology must be documented, justified, and approved.

User-configured preferences must be clearly distinguished from system-derived evidence.

### 9.4 Insufficient evidence

When required data or approved methods are unavailable, the platform must provide a limited assessment or explain why suitability cannot be determined.

Do not generate a definitive ranking or recommendation merely to produce a complete-looking result.

## 10. Uncertainty, sensitivity, and validation

### 10.1 Uncertainty

Identify material uncertainty arising from data limitations, measurement error, geographic assumptions, modelling choices, temporal differences, and missing evidence.

Explain uncertainty in terms relevant to the assessment rather than using unsupported numerical precision.

### 10.2 Sensitivity and scenarios

Where justified, assess how analytical results change under alternative defensible assumptions, parameter settings, or approved scenarios.

Do not introduce arbitrary scenario values as factual expectations.

Clearly label user-defined, research-supported, and hypothetical scenarios.

### 10.3 Validation

Apply appropriate validation to analytical outputs, which may include:

- Recalculation and consistency checks.
- Geographic and boundary checks.
- Comparison with independent evidence.
- Benchmarking against established methods.
- Sensitivity testing.
- Statistical evaluation where applicable.
- Review of anomalous or counterintuitive results.

Validation procedures must match the analytical method.

A technically successful calculation is not proof that the result is commercially meaningful or geographically valid.

## 11. Reproducibility and auditability

Material analytical outputs must retain sufficient information to reproduce or explain how they were generated.

Record, where applicable:

- Assessment configuration and approved methodology.
- Input datasets and versions.
- Source references and observation periods.
- Data preparation and transformations.
- Parameters and assumptions.
- Analytical procedures and software versions.
- Validation results.
- Limitations and approval status.

Preserve an appropriate history of consequential changes.

Do not silently alter historical assessment results when data or configuration changes.

## 12. User-facing interpretation and visualisation

The web application must communicate analytical findings clearly to users without requiring specialist GIS or data science knowledge.

Where relevant, outputs should provide:

- Geographic context and interactive maps.
- Clear indicator definitions and units.
- Source and observation-period information.
- Data availability and coverage.
- Data-confidence and analysis-confidence explanations.
- Suitability results only where supported by an approved method.
- Comparisons between locations.
- Material assumptions, uncertainty, and limitations.
- Explanations of why a result was produced.

Use understandable terminology, accessible visual design, and progressive disclosure of technical detail.

Do not display unsupported precision, misleading map symbols, unexplained scores, or fabricated recommendations.

The detailed interface design belongs in `06_functional_requirements_and_ui_ux.md`.

## 13. Analytical decision controls

Before an analytical capability is treated as operationally valid, confirm that:

1. Its business purpose is established.
2. Required inputs are available and appropriately validated.
3. Its methodology is documented and justified.
4. Consequential assumptions and parameters are approved.
5. Relevant geographic and temporal limitations are addressed.
6. Its outputs are validated appropriately.
7. Confidence and uncertainty are communicated accurately.
8. Its results can be traced to evidence and configuration.
9. Its interpretation does not exceed what the evidence supports.

Where these conditions are unmet, label the capability as proposed, experimental, incomplete, or unavailable, as appropriate.

Do not present an implemented algorithm as a validated decision-support method solely because the software runs.

## 14. Governing principle

**The platform must distinguish what the evidence shows, how reliably it supports an analytical conclusion, and whether a location meets approved business requirements.**

All analytical methods must be defensible, transparent, appropriately validated, and proportionate to the available evidence.

When a reliable conclusion cannot be established, the platform must communicate that limitation rather than inventing certainty.


