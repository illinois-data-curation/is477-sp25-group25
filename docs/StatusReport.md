# IS477 Status Report – April 15

## Overview

This report summarizes our progress on the final project titled "Analyzing Crime Trends and Socioeconomic Indicators in the United States (2012–2016)." Our work focuses on understanding how national arrest rates correlate with employment, income, health insurance, and poverty data. We are following the data curation lifecycle presented in class, with current efforts focused on dataset merging and resolving schema compatibility issues.

## Research Questions

1. How have national arrest rates (2012–2016) shifted, and how do they correlate with key socioeconomic indicators?  
2. Are certain indicators (e.g., poverty, unemployment) more predictive of changes in crime than others?  
3. Can national-level arrest trends help inform potential policy decisions around employment and healthcare access?

## Task Status Updates

| Task                                          | Owner | Status                                                                                                   |
|-----------------------------------------------|-------|-----------------------------------------------------------------------------------------------------------|
| Project Plan Submission (Apr 2)               | Both  | Submitted `ProjectPlan.md` including goals, dataset sources, GitHub repo structure, and timelines.       |
| FBI + Census Data Acquisition (Apr 4)         | Greg  | Scripts completed: `fetch_fbi_data.py` and `fetch_census_multi_year.py`. API keys handled via `.env`. Output stored with SHA256 hash logs. |
| Merge Datasets + Schema Alignment (Apr 6)     | Greg  | In progress. Encountered schema mismatches and API limitations such as missing or inconsistent variables. |
| Data Profiling & Cleaning (Apr 8)             | Greg  | Delayed until merge is resolved. Plan includes `pandas.describe()`, null checks, and type normalization. |
| Visualizations (Apr 10)                       | Eric  | Pending merge fix. Plan includes line plots and heatmaps using `matplotlib` and `seaborn`.               |
| Snakemake Workflow Setup (Apr 12)             | Eric  | Not started. Planned after merge is functional. Will include rule-based automation from fetch to analyze. |
| Reproducibility Packaging (Apr 14)            | Eric  | Not started. Will include `requirements.txt`, Box upload, and metadata documentation.                    |
| Interim Report Submission (Apr 15)            | Greg  | Completed.                                                                                               |

## Artifacts and Script Overview

- `scripts/fetch_fbi_data.py`: Downloads FBI arrest rate data via API, processes monthly values into yearly averages.  
- `scripts/fetch_census_multi_year.py`: Pulls ACS data for 2012–2016, including employment, income, and other indicators.  
- `data/*.sha256`: Contains integrity hash values for downloaded datasets.  
- `data/fbi_crime.json`, `data/census_multi_year.json`: Raw data retrieved from APIs.  
- `scripts/merge_data.py`: Merges datasets by year and handles type casting and alignment.  
- `logs/integration_log.md`: Logs integration steps, transformations, and encountered issues.

## Current Issues

- FBI data uses monthly date keys (e.g., "01-2012"), which require transformation to extract and average by year.  
- Several Census API variables are unavailable for certain years or return inconsistent data, requiring manual inspection.  
- Some columns expected from the API are missing or returned with nulls, causing compiler errors during type casting in `merge_data.py`.  
- Currently working to manually validate the returned columns per year and resolve the schema mismatches.

## Updated Timeline

| Date     | Task                                      | Status      | Notes                                                                 |
|----------|-------------------------------------------|-------------|-----------------------------------------------------------------------|
| Apr 16   | Finalize clean merge of FBI and Census    | On track    | Schema issues being resolved and variable names are being validated. |
| Apr 17   | Data profiling and summary stats          | Scheduled   | Includes null checks, dtype validation, and basic statistical output. |
| Apr 18   | Visualizations                            | Scheduled   | Line plots and correlation heatmaps. Stored in `results/`.           |
| Apr 19   | Snakemake automation                      | Scheduled   | Automate full workflow using Snakefile.                              |
| Apr 20   | Metadata packaging and archiving          | Scheduled   | Finalize metadata, citations, and Box upload.                        |
| Apr 23   | Final documentation and polish            | Scheduled   | Final README update and reproduction instructions.                   |
| Apr 25   | Zenodo archive + final submission         | Scheduled   | GitHub release, Zenodo DOI, and Canvas submission.                   |

## Changes to Project Plan

- The original `census_data.json` (single year) has been replaced with `census_multi_year.json` to cover 2012–2016.  
- Variables related to industry were removed in favor of more interpretable fields like poverty rate, income, and insurance coverage.  
- FBI data structure differed from documentation and required custom parsing logic for month-based keys in `merge_data.py`.  
- Column naming conflicts and API omissions introduced additional validation and debugging steps in the merge process.

## Summary

We have completed data acquisition and integrity verification. The merge process is underway but currently blocked by missing or inconsistent columns in the Census API and nested key formatting in the FBI JSON. We are actively resolving these issues through manual inspection and schema validation. Once resolved, we will proceed with profiling, visualization, and workflow automation. We remain on track for final delivery by May 1.
