# IS477 Project Plan

---

### **Overview**

For our final project, the overall goal is to explore the relationship between national crime rates and key socioeconomic indicators across the United States from 2012 to 2016. More specifically, we want to explore how trends in different crimes such as violent and property crime correlate with macroeconomic variables such as employment rates, healthcare access, and industry sectors. Our two datasets originate from public-domain government sources: the **FBI Crime Data Explorer** and the **U.S. Census Bureau's American Community Survey (ACS)**. Using these two datasets, we plan to analyze correlations and patterns in national crime fluctuations that will help inform policy and urban design.

In the project, we’ll automate the end-to-end workflow using **Snakemake**. All data will be programmatically acquired, processed through **Python scripts**, and visualized to answer our research questions.

---

### **Research Questions**

1. **How have national crime rates (violent/property) changed from 2012 to 2016, and how do they correlate with macroeconomic indicators such as employment, healthcare access, and industry classification?**

2. **Are there noticeable shifts in crime trends following major national events? Do these changes align with shifts in socioeconomic indicators?**

3. **Which national-level social indicators most closely track or predict changes in crime rates over time?**

---

### **Team Roles and Responsibilities**

#### **Eric**
- Write all data acquisition scripts which include:
  - **FBI API integration** using Python's `requests` module.
  - **Census data import** via direct download or API.
- Implement **SHA256 integrity checks** using Python’s `hashlib` library.
- Create documentation with steps for someone else to acquire the data.
- Perform data merging and integration using Python or SQL.
- Create scripts to profile, assess quality, and clean data using either Python or SQL.

#### **Greg**
- Develop all data analysis and/or visualization scripts using Python (**pandas**, **seaborn/matplotlib**).
- Implement the complete **Snakemake** workflow to automate data ingestion, cleaning, analysis, and output generation.
- Conduct exploratory data analysis and correlation studies.
- Build final charts and figures to support findings.
- Write reproducibility documentation and handle metadata using **Schema.org/DataCite** standards.
- Ensure licensing and citation requirements are met.
- Maintain version control through **GitHub**.
- Create and manage `requirements.txt`, `.gitignore`, Box file upload, and other environment files.

---

### **Datasets**

1. **FBI Crime Data (API)**
   - **Source:** FBI Crime Data Explorer API
   - **Format:** CSV files accessed via API endpoints or downloadable ZIP archives
   - **Fields:** Year, Population, Violent Crime, Property Crime, and various offense subtypes
   - **Granularity:** National-level totals aggregated by year  
     [FBI Crime Data Explorer](https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/docApi)
   - **License:** Public domain (CC0)

2. **U.S. Census Socioeconomic Data (CSV/API)**
   - **Source:** ACS Data Profiles - Table DP03
   - **Format:** CSV (via [data.census.gov](https://data.census.gov) or Census API)
   - **Fields:** Employment status, industry, class of worker, income, healthcare coverage
   - **Granularity:** National-level aggregated statistics by year
   - **License:** Public domain (CC0)

---

### **Merge Strategy and Data Compatibility**

Although both datasets are national and aggregated by year, they originate from entirely different domains and offer distinct schemas. The FBI dataset focuses on crime incidence, while the ACS provides socioeconomic context. The only overlapping columns suitable for merging are **Year** and **Population**. This simplifies integration while still offering enough structural diversity to meet the "different schema" requirement. All merging will be performed using the `merge()` function in **Pandas**.

---

### **Project Timeline (Detailed)**

| **Date**   | **Task**                                                                          | **Responsibility** | **Description**                                                                                                                                                          |
|------------|-----------------------------------------------------------------------------------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Apr 2**  | Submit finalized project plan                                                     | **Both**           | Finalize goals, dataset selection, research questions, and repository setup                                                                                            |
| **Apr 4**  | Complete FBI/Census data acquisition scripts + integrity checks                   | **Eric**           | Use `requests` to query FBI and Census REST APIs, store data locally, generate SHA256 hash logs <br> [ACS Data Profiles](https://data.census.gov/table/ACSDP5Y2016.DP03) |
| **Apr 6**  | Merge datasets and document integration logic                                     | **Eric**           | Use `pandas.merge()` on **Year**, align schemas, document all transformations in `integration_log.md`                                                                  |
| **Apr 8**  | Clean datasets and complete data profiling/quality assessment                     | **Eric**           | Use pandas and `describe()`, count nulls, cast data types, remove anomalies                                                                                              |
| **Apr 10** | Conduct visual exploration and correlation analysis                               | **Greg**           | Generate line plots (crime vs. employment), heatmaps (correlation matrix), and exploratory pairplots                                                                     |
| **Apr 12** | Build Snakemake workflow to automate all steps                                    | **Greg**           | Define Snakemake rules for: fetch → clean → merge → analyze → visualize                                                                                                 |
| **Apr 14** | Package reproducibility files (`requirements.txt`, Box, metadata)                   | **Greg**           | Freeze Python environment (`pip freeze`), upload results to Box, generate `metadata.json` and data dictionary                                                             |
| **Apr 15** | Submit Interim Report                                                               | **Greg**           | Draft findings, progress, and planned adjustments in `StatusReport.md`                                                                                                   |
| **Apr 20** | Write licensing, citations, and finalize metadata                                   | **Greg**           | Add LICENSE, BibTeX citations, and complete metadata via DataCite format                                                                                                  |
| **Apr 23** | Final pass-through, README polish, link outputs                                   | **Greg**           | Polish documentation, write reproduction instructions, finalize visuals                                                                                                 |
| **Apr 25** | Archive release on Zenodo + DOI generation                                          | **Eric**           | Upload GitHub release to Zenodo, generate DOI, embed Zenodo badge in README                                                                                              |
| **May 1**  | Final project submission                                                            | **Both**           | Verify all final submission criteria are met                                                                                                                           |

---

### **Technical Stack**

- **Language:** Python 3.x
- **Libraries:** pandas, requests, matplotlib, seaborn, hashlib, snakemake
- **Data Acquisition:** REST API requests with logging and retry logic, parameterized by year and fields
- **Data Integrity:** SHA256 hash generation using `hashlib`, output stored in `checksums/` folder
- **Automation:** Snakemake rules (Snakefile) to ensure deterministic end-to-end runs
- **Visualization:** Seaborn/matplotlib for line plots (crime vs. employment), heatmaps (correlation matrix), pairplots (multivariate insights)
- **Reproducibility:** Outputs saved to `/results`, intermediate files ignored in `.gitignore`, Box used for large artifacts
- **Documentation:** Markdown for all logs, plus metadata in Schema.org or DataCite JSON format

---

### **Reproducibility Plan**

We’ll ensure our project meets the highest standard of reproducibility through the following practices:

- **Data Scripts:**  
  All data must be downloaded via RESTful API using Python scripts or manually downloaded with precise documentation and SHA256 hash validation.

- **Snakemake Workflow:**  
  A Snakefile will define all pipeline stages: fetch → integrity check → preprocessing → analysis → visualization.

- **Box Archive:**  
  Output data and intermediate files will be hosted externally via Box with shareable links in the README. These will not be committed to the GitHub repository.

- **README + Metadata:**  
  The README will include usage instructions, reproduction steps, dependency setup via `requirements.txt`, and a detailed directory structure. Metadata will follow Schema.org or DataCite.

- **Final Archival:**  
  Upon completion, the full project will be archived on Zenodo with an embedded DOI badge and citation support.

---

### **Final Deliverables**

- **GitHub Repository** containing:
  - Python scripts for data acquisition, merging, analysis, and visualization
  - Snakemake automation pipeline
  - `requirements.txt`, `.gitignore`, and environment logs
  - Metadata files (`metadata.json`, `datadictionary.md`)
  - Clean plots (.png, .svg) with annotations
- **Box Archive** with all outputs
- **Zenodo Repository** with archived bundle and DOI
- **Interim Report** (`StatusReport.md`) and final **README** (`README.md`)

---

### **Summary**

We will build a clean, automated workflow using **Snakemake** to explore how national crime trends relate to key socioeconomic indicators between 2012–2016. We will use public datasets, automate the pipeline with Snakemake, and document everything for full reproducibility.

---

