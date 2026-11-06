# Prompt 01: Data Source Identification and Validation
## Retail Site Selection Project — Sri Lanka

## 1. Role and Responsibilities

Act as a senior data scientist, geospatial analyst, and research analyst specialising in retail location intelligence, commercial site selection, and evidence-based business decision-making.

Your task is to identify, research, and evaluate reliable data sources required to develop a data-driven retail showroom location selection solution for **D. Samson & Sons (Pvt) Ltd. in Sri Lanka**.

Assume that the person using this prompt is at the initial stage of the project and may not have prior knowledge of geospatial analysis, retail site selection, data collection, or statistical research. Therefore, explain technical concepts in simple, clear language without sacrificing accuracy.

Do not begin by recommending a machine learning model or producing location rankings. First establish what data is required, where it can be obtained, how reliable it is, and whether it is sufficiently complete for the intended analysis.

---

## 2. Project Background

The objective is to identify and evaluate potential areas for future company showroom locations across Sri Lanka.

A suitable showroom location should be evaluated using multiple factors rather than a single indicator. These may include:

- The locations of competing retailers and major retail chains.
- The locations of supermarkets and other relevant commercial establishments.
- The distribution and concentration of banks and financial institutions, where relevant.
- Population density and the distribution of people across different areas.
- Consumer income or other credible indicators of local purchasing power.
- Road networks, traffic conditions, and accessibility.
- Pedestrian or customer footfall, where reliable data is available.
- The locations of existing company showrooms, outlets, dealers, franchises, and other relevant network locations.
- Other relevant factors supported by credible research or verified data.

These factors may help explain the commercial characteristics of an area. However, their presence alone does not prove that an area will generate high sales or be profitable.

The purpose of this stage is to establish a trustworthy data foundation for subsequent geospatial analysis and potential location evaluation.

## 3. Primary Objective of This Task

Identify the most relevant and credible data sources for every required data category.

For each source, determine:

1. What information it provides.
2. Why the information matters to retail site selection.
3. Which geographic areas it covers.
4. Whether it provides point locations, geographic boundaries, numerical measurements, or other data formats.
5. The most recent available observation or publication date.
6. Whether consecutive years of historical data are available.
7. Whether the data can be accessed, downloaded, licensed, or obtained through an API.
8. Whether the data is sufficiently accurate and detailed for the intended analysis.
9. What limitations, biases, or missing information may affect its usefulness.
10. How the information could eventually be used in the project.

Do not assume that every requested dataset exists, is publicly available, or can be obtained at the required geographic resolution. Verify these points through research.

---

## 4. Required Data Categories

### 4.1 Competitor Showroom Locations

**What this means:** Geographic locations of businesses that compete with the company's retail offering.

Investigate potential sources such as Google Maps, official company websites, official store locators, and other credible business directories.

Research relevant competitors and retail chains, including the following examples where applicable:

- Bata
- Cool Planet
- Odel
- Nolimit
- Fashion Bug

These are initial examples, not a confirmed or exhaustive competitor list. Assess whether each business is genuinely relevant to the company's retail offering before including it.

For each potential source, investigate whether the following information is available:

- Business or showroom name.
- Geographic coordinates (latitude and longitude).
- Full address and locality.
- Store category or business type.
- Current operational status.
- Date on which the information was collected or last verified.
- Source URL and supporting evidence.

Determine whether Google Maps provides the necessary information through permitted access methods, such as the official Google Maps Platform APIs, or whether another reliable source is more suitable.

Do not assume that every location visible on a map is currently operational. Investigate methods for checking whether locations are open, closed, duplicated, relocated, or incorrectly classified.

### 4.2 Major Retail Chains and Commercial Establishments

Identify relevant major retailers and commercial establishments that may help describe the commercial activity of an area.

Potential examples include:

- Large retail chains.
- Department stores.
- Shopping centres and malls.
- Clothing and footwear retailers.
- Other retail businesses relevant to the company's products.

Investigate official store locators, business directories, mapping services, and other credible sources.

Explain how the distribution of these establishments could help identify commercial centres or retail clusters.

Do not treat the number of nearby businesses as direct proof of showroom demand. Assess whether these businesses attract a similar customer segment or serve a relevant market.

### 4.3 Supermarket Locations

Investigate the geographic distribution of major supermarket chains in Sri Lanka.

Potential examples include:

- Keells.
- Cargills Food City.
- Laughs Supermarkets.

These are examples to investigate, not a requirement to include every branch without verification.

Determine whether branch-level locations can be obtained from official store locators, mapping services, or other credible sources.

Assess how supermarket locations might serve as indicators of established commercial activity, accessibility, or customer movement.

Clearly distinguish between a supermarket's location and measured customer footfall. Do not infer actual visitor numbers unless a credible dataset provides them.

### 4.4 Banks and Financial Institutions

Investigate the locations of banks, bank branches, and other relevant financial institutions.

Potential sources include official bank branch locators, regulatory publications, official datasets, and mapping services.

Determine whether branch-level geographic information is available and whether it can be collected consistently across Sri Lanka.

Explain how banks might help identify established commercial areas or service centres. However, assess whether their presence is genuinely relevant to the company's retail site selection objective.

Do not assume that areas with more bank branches necessarily have higher retail sales, higher consumer income, or greater customer footfall.

### 4.5 Pedestrian and Customer Footfall

**What this means:** The number of people passing through or visiting a particular location during a defined period.

Investigate whether credible pedestrian footfall or visitor-count data is available for Sri Lankan commercial areas.

Research potential sources such as:

- Official urban planning or transport studies.
- Published pedestrian-count surveys.
- Commercial mobility or location-intelligence datasets.
- Shopping-centre or retail-property reports.
- Academic research containing measured footfall data.
- Other legitimate sources that explicitly measure pedestrian or visitor activity.

For every source, determine:

- Whether the data measures pedestrians, vehicle movements, visits, or mobile-device-derived movement estimates.
- The geographic coverage and measurement locations.
- The observation dates and time periods.
- The methodology used to estimate or measure footfall.
- Whether the data represents actual counts, estimates, samples, or modelled values.
- Whether historical observations are available for consecutive years.
- Whether access requires payment, licensing, or permission.
- Whether the dataset is representative of the target locations.

Do not label general business density, map popularity, search interest, or nearby establishment counts as measured footfall.

If reliable footfall data cannot be obtained, document this limitation and investigate whether suitable alternative indicators exist. Explain their weaknesses clearly.

### 4.6 Road Traffic and Accessibility

Investigate data sources that describe road traffic, transport connectivity, and accessibility.

Potential sources may include official transport authorities, road agencies, published traffic surveys, transport research, and permitted mapping or routing services.

Determine whether data is available for:

- Road network geometry.
- Road classifications.
- Traffic volume or vehicle counts.
- Traffic congestion or travel-time estimates.
- Connectivity between commercial areas.
- Accessibility from surrounding population centres.

For traffic volume, identify whether the data represents actual vehicle counts, estimated traffic levels, or modelled conditions.

For routing and travel-time services, document whether the information represents current, typical, or historical traffic conditions.

Investigate whether consistent historical observations exist for consecutive years and whether the data is available at a sufficiently detailed geographic level.

Explain why road traffic and pedestrian footfall are different measures. High vehicle traffic does not automatically imply high pedestrian activity, easy parking, convenient access, or strong retail demand.

### 4.7 Population Density and Population Distribution

Investigate reliable sources for population data across Sri Lanka.

Prioritise official statistical publications and datasets from the Department of Census and Statistics Sri Lanka and other relevant authoritative institutions. Consider credible international datasets only where their methods, coverage, and suitability can be assessed.

Research the availability of:

- Total population by geographic area.
- Population density.
- Population distribution across districts, divisions, and smaller administrative areas, where available.
- Census reference dates.
- Annual population estimates or projections.
- Historical population figures for consecutive years.
- Geographic boundary files required to map the data.

For each source, establish the geographic unit used, such as a district, divisional secretariat division, grama niladhari division, or another defined area.

Do not compare population figures from different geographic boundaries as though they represent identical areas.

Distinguish observed census counts from estimates and projections. Document the reference year, methodology, and limitations of each dataset.

Assess whether the geographic resolution is sufficiently detailed for showroom site selection. District-level population figures, for example, may be too broad to distinguish between individual commercial locations.

### 4.8 Consumer Income and Purchasing Power

Investigate credible data sources that can help estimate differences in consumer income or purchasing power across Sri Lanka.

Start by researching relevant publications and datasets from the Central Bank of Sri Lanka and the Department of Census and Statistics Sri Lanka. Investigate other authoritative sources where appropriate.

Consider whether the available data includes:

- Household income.
- Household expenditure.
- Per-capita income or expenditure measures.
- Income distribution.
- Poverty-related indicators.
- Regional economic indicators.
- Other defensible proxies for local purchasing power.

Determine whether the figures are available nationally, by province, district, divisional area, or another geographic unit.

For every dataset, identify the reference period, publication date, geographic resolution, currency, units, and whether the figures are nominal or adjusted for inflation.

Distinguish national economic statistics from local household income measurements. A national income indicator cannot automatically be assigned to an individual town or showroom catchment area.

If direct local income data is unavailable, investigate alternative indicators only when their relationship to purchasing power is supported by credible evidence. Clearly explain the limitations of each proxy.

Do not invent local income estimates or claim that a particular area has wealthier consumers without supporting evidence.

### 4.9 Existing Company Network Locations

Investigate the internal data required to represent the company's existing network.

This may include:

- Existing showrooms.
- Company-owned outlets.
- Dealers.
- Franchises.
- Other relevant distribution or retail locations.

This information is expected to require internal company records or authorised input from relevant departments.

Identify the fields required for each location, including location name or identifier, address, geographic coordinates, outlet type, operational status, and relevant opening or closure dates where available.

Determine whether additional internal information, such as sales performance or customer coverage, is available and appropriate for the project.

Explain how the existing network can help assess geographic coverage, potential overlap, underserved areas, and possible conflicts between proposed locations and current operations.

Do not assume that every nearby existing outlet makes a proposed location unsuitable. Any exclusion or penalty must be based on an explicitly defined business rule and supporting evidence.

Treat internal company data as confidential and recommend appropriate access controls.

### 4.10 Other Relevant Commercial and Geographic Indicators

Identify additional variables that could materially improve location evaluation.

Potential areas to investigate include:

- Shopping-centre locations.
- Employment and business concentrations.
- Public transport connectivity.
- Parking availability.
- Major roads and intersections.
- Urban development and land-use patterns.
- Relevant commercial property information.
- Tourist or visitor activity where relevant.
- Competitor concentration and market coverage.
- Other factors identified in credible retail location research.

Do not collect additional variables merely because they are available. Explain the business relevance of each proposed variable and assess its reliability, geographic resolution, and cost of acquisition.

Separate essential datasets from optional datasets so that the project can proceed even if some optional information is unavailable.

---

## 5. Geographic Scope

The intended geographic scope is Sri Lanka.

Investigate data sources that cover the country as a whole or provide sufficiently detailed information for relevant towns and commercial areas.

For each source, document whether coverage is:

- Nationwide.
- Limited to selected districts or cities.
- Available only for specific locations.
- Incomplete or uneven across the country.

Identify any geographic coverage gaps that could bias comparisons between regions.

Where multiple datasets are combined, investigate whether they use compatible coordinate reference systems, geographic boundaries, and location identifiers.

Do not assume that a dataset with nationwide coverage is automatically accurate at individual showroom level.

---

## 6. Data Recency and Consecutive-Year Analysis

The project requires recent information and, wherever available, historical data covering consecutive years.

Follow these instructions:

1. Identify the latest available data at the time of research.
2. Record the actual observation period, not merely the date on which a report or webpage was published.
3. Investigate whether the same variable is available for consecutive years.
4. Collect or document multiple years where the source provides comparable observations.
5. Record gaps in annual coverage, changes in methodology, and changes in geographic boundaries.
6. Distinguish between the latest observed values, estimates, forecasts, and projections.
7. Check whether older datasets remain useful for variables that change slowly, such as administrative boundaries, while clearly documenting their age.
8. Explain when historical data is unavailable or not comparable across years.

Do not impose an arbitrary number of years without considering the source and business purpose. Recommend an appropriate historical period for each data category and explain the reasoning.

Do not combine different years of data as though all observations describe the same point in time. If datasets refer to different periods, explain the potential impact on the analysis.

Do not describe a dataset as the latest available unless its date has been verified against the source.

---

## 7. Research Papers and Published Studies

Conduct a targeted review of credible research papers and published studies relevant to retail location selection, geospatial analysis, customer footfall, accessibility, population density, purchasing power, and commercial clustering.

Prioritise:

- Peer-reviewed journal articles.
- Academic conference papers with identifiable publication details.
- University or institutional research.
- Official government and transport studies.
- Credible international organisation reports.
- Other authoritative research with transparent methodology.

For each relevant study, record:

- Full title.
- Author or responsible institution.
- Publication year.
- Country or geographic area studied.
- Research objective.
- Data sources and methods used.
- Key findings, including numerical results where explicitly reported.
- Limitations acknowledged by the authors.
- Relevance to the Sri Lankan project.
- DOI or stable source URL, where available.

Use research papers to understand which variables and methods may be relevant and why.

Do not assume that findings from another country apply directly to Sri Lanka. Explain differences in geography, consumer behaviour, retail structure, transport systems, and data availability that may affect transferability.

Verify reported numerical findings against the original paper whenever possible. Do not invent research results, misrepresent statistical relationships, or cite a paper that has not been verified.

Clearly distinguish between a study's reported findings and your own interpretation of how those findings might apply to this project.

---

## 8. Source Verification and Evidence Standards

Every proposed data source must be supported by verifiable evidence.

Prioritise primary sources, including official government portals, official statistical publications, official company websites, documented APIs, and original research publications.

Secondary sources may be used when they provide useful additional evidence, but their origin and reliability must be assessed.

For each source:

- Provide the exact source name.
- Provide a direct URL to the relevant dataset, publication, documentation, or official page.
- State what the source actually confirms.
- Record the publication date and data reference period where available.
- Identify the organisation responsible for producing the data.
- Explain whether the data is directly downloadable, available through an API, accessible only through a portal, obtainable by request, or available commercially.
- Record access restrictions, licence conditions, costs, and relevant terms of use where verifiable.
- Identify any claims that could not be independently verified.

Do not rely solely on search-engine snippets, unverified summaries, or AI-generated descriptions.

If a source is inaccessible, do not pretend to have inspected its contents. State what remains unverified and recommend a practical way to obtain or confirm the information.

If no reliable source is found for a requirement, explicitly report that result and identify the remaining research gap.

---

## 9. Data Quality Assessment Before Analysis

Data quality must be evaluated before the datasets are used for geospatial analysis or location recommendations.

For each dataset, establish a validation checklist covering the following areas.

### 9.1 Completeness

Check whether required fields are populated and whether important geographic areas or time periods are missing.

### 9.2 Accuracy

Determine whether the information can be verified against the original source or another credible reference.

For geographic data, investigate whether coordinates correspond to the actual business or observation location.

### 9.3 Consistency

Check whether names, categories, geographic units, measurement units, date formats, and other fields are defined consistently across records and datasets.

### 9.4 Duplicates

Investigate duplicate businesses, repeated records, duplicate coordinates, and multiple listings referring to the same physical location.

Do not automatically delete records merely because they share similar names or coordinates. Confirm whether they represent genuine duplicates or separate businesses.

### 9.5 Timeliness

Record when the information was observed, collected, updated, or published. Identify data that may be outdated for the intended use.

### 9.6 Geographic Resolution

Determine whether the dataset is sufficiently detailed for the intended question. Identify cases where aggregated statistics cannot support conclusions about individual sites.

### 9.7 Methodological Reliability

Understand how the figures were collected, measured, estimated, or modelled. Flag datasets whose methodology is unclear.

### 9.8 Comparability Across Years

Check whether definitions, collection methods, geographic boundaries, and measurement units remain consistent across the selected years.

### 9.9 Licensing and Permitted Use

Confirm whether the data may legally and practically be accessed, stored, processed, combined, and used for the intended internal business purpose.

### 9.10 Confidence and Limitations

Document unresolved quality issues, assumptions, uncertainties, and potential biases. Recommend whether each dataset is suitable, conditionally suitable, or unsuitable for the intended analysis.

Do not begin the substantive location analysis until the key datasets have been assessed and material quality issues have been documented.

---

## 10. Rules for Google Maps and Other Online Data

When investigating Google Maps or other online mapping services, determine the permitted and technically supported method of obtaining the required information.

Investigate official APIs, documented export options, official business directories, and other legitimate alternatives.

Do not assume that information visible on a website is automatically available for unrestricted bulk collection or commercial reuse.

Do not recommend bypassing access controls, anti-bot protections, authentication restrictions, or contractual limitations.

Assess API availability, pricing, usage limits, licensing, attribution requirements, and data-retention restrictions using current official documentation where relevant.

Where a proposed source cannot provide reliable or permitted access to the required data, identify an alternative and explain any trade-offs in coverage, accuracy, freshness, or cost.

---

## 11. Rules Against Unsupported Claims

Follow these requirements throughout the research:

- Never invent data, statistics, citations, URLs, publication dates, or research findings.
- Never claim that a dataset exists or is available for download without verifying the claim.
- Never treat an estimate as an observed measurement.
- Never treat business density as a direct measurement of footfall.
- Never assume that high vehicle traffic means high pedestrian traffic or strong retail demand.
- Never infer local consumer income directly from national-level statistics without a defensible methodology.
- Never assume that a competitor's presence proves that an area is commercially attractive for this company.
- Never assume that competitor concentration is always beneficial or always harmful.
- Never assume that proximity to an existing company outlet makes a proposed location unsuitable without a defined business rule.
- Clearly separate verified facts, reasonable interpretations, hypotheses, and unresolved questions.
- Cite the source supporting each material factual claim and numerical finding.
- State explicitly when evidence is insufficient to reach a conclusion.

If evidence is incomplete, report the uncertainty instead of filling the gap with an unsupported assumption.

---

## 12. Required Deliverables

Present the results in the following order.

### Deliverable 1: Executive Summary

Provide a concise explanation of the research findings, the strongest available data sources, the major data gaps, and the most important constraints affecting the project.

### Deliverable 2: Data Source Register

Create a structured table containing:

| Field | Required information |
|---|---|
| Data category | The type of information required |
| Specific variables | The exact fields or measurements needed |
| Source name | The organisation, platform, dataset, or publication |
| Direct source URL | A verifiable link to the relevant resource |
| Geographic coverage | The areas covered |
| Latest observation period | The most recent period actually represented |
| Historical coverage | Whether consecutive-year data exists |
| Geographic resolution | The smallest area or location represented |
| Access method | Download, API, request, commercial licence, or other verified method |
| Cost and restrictions | Verified costs, licence terms, or access limitations |
| Quality concerns | Missing data, accuracy issues, bias, or methodological concerns |
| Intended use | How the data may support site selection |
| Evidence status | Verified, partially verified, or unverified |

Use separate rows when sources provide materially different datasets or versions.

### Deliverable 3: Data Requirements and Priorities

Classify the required datasets into:

- **Essential:** Data needed to perform the initial defensible analysis.
- **Important:** Data that could materially improve evaluation if available.
- **Optional:** Data that may provide additional context but is not essential to begin.

Explain the reason for each classification. Do not label a dataset essential solely because it is mentioned in this prompt; assess its actual contribution to the project.

### Deliverable 4: Consecutive-Year Availability Assessment

Summarise the historical coverage of each major variable, the latest verified observation period, any missing years, and whether comparisons across years are methodologically appropriate.

### Deliverable 5: Research Evidence Summary

Summarise verified research papers and official studies, their relevant findings, the strength of the evidence, and their applicability or limitations for Sri Lanka.

### Deliverable 6: Data Quality and Validation Plan

Specify the checks required before analysis, the data fields that must be validated, the likely quality risks, and the conditions under which a dataset should be accepted, conditionally accepted, or rejected.

### Deliverable 7: Data Gaps and Recommended Next Steps

Identify information that could not be obtained, sources that require permission or payment, and any internal company data that must be requested.

Recommend practical next steps in order of priority. Do not proceed to model development or final location rankings at this stage.

---

## 13. Communication and Presentation Requirements

Assume the reader is encountering this project for the first time.

- Explain unfamiliar technical terms in plain English when first introduced.
- Explain what each data category means, why it matters, and how it might be used.
- Provide enough detail for a beginner to understand the findings without needing to interpret unexplained technical terminology.
- Use concise explanations, descriptive headings, tables, and clearly labelled evidence.
- Avoid unnecessary jargon, vague statements, and repetitive explanations.
- Include exact figures, units, dates, and geographic coverage whenever these are supported by verified evidence.
- Provide direct links so that the reader can independently inspect important sources.
- Do not overwhelm the reader with large quantities of low-value information. Prioritise sources according to relevance, reliability, accessibility, and usefulness.

## 14. Final Instructions

Conduct the research systematically and use current, verifiable sources wherever possible.

The immediate objective is to establish **what data is available, where it comes from, how reliable it is, how recent it is, and whether it is suitable for retail site selection in Sri Lanka**.

Do not skip any required data category without explaining why. If a category cannot be adequately researched, identify the gap explicitly.

Do not proceed directly to building a predictive model, assigning weights, ranking locations, or making expansion recommendations. Those decisions belong to later project stages, after the available data has been understood and validated.

All findings must be supported by facts, figures, and traceable evidence. Clearly document assumptions, limitations, uncertainty, and unresolved questions. Never invent findings unsupported by evidence.

# File structure 
Area	My assessment
Project context	Correctly separated from research instructions
Data categories	Should remain together because they define what information the solution needs
Geographic scope and recency	Sensible to combine because both influence dataset suitability
Research and verification	Related responsibilities, suitable for one document
Data quality	Important enough to have its own document
Data access and licensing	Should be separately identifiable because of API and legal restrictions
Evidence integrity	Should be explicit and reinforced by the Master Instructions
Deliverables	Correctly separated from research methodology
Communication	Useful as a common reporting standard
Research constraints	Important for preventing the AI from moving prematurely into modelling and ranking