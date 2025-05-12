# Data Dictionary

## Raw Input Files:

### `data/fbi_monthly.csv`
| Column   | Type    | Description                                        |
| -------- | ------- | ---------------------------------------------------|
| **Year**   | integer | Calendar year (e.g. 2012)                        |
| **Month**  | integer | Calendar month (1–12)                            |
| **Arrests**| integer | Number of arrests reported by the FBI that month |

### `data/census_multi_year.csv`
| Column                 | Type    | Description                                            |
| ---------------------- | ------- | ------------------------------------------------------ |
| **Year**               | integer | Calendar year (e.g. 2012)                              |
| **employed_population**| integer | Total employed individuals in that year                |
| **unemployment_rate**  | float   | Percentage of the population unemployed                |
| **median_income**      | integer | Median household income in USD                         |
| **pct_below_poverty**  | float   | Percentage of population below the poverty line        |
| **pct_insured**        | float   | Percentage of population with health insurance         |

## Derived Output Files

### `results/merged.csv`
| Column                 | Type    | Description                                                        |
| ---------------------- | ------- | ------------------------------------------------------------------ |
| **Year**               | integer | Calendar year                                                      |
| **Month**              | integer | Calendar month within that year (1–12)                             |
| **arrest_rate**        | float   | Monthly arrest rate (per 100 k population)                         |
| **employed_population**| integer | Employed population for that year                                  |
| **unemployment_rate**  | float   | Unemployment rate for that year                                    |
| **median_income**      | integer | Median household income for that year                              |
| **pct_below_poverty**  | float   | Percentage below poverty line for that year                        |
| **pct_insured**        | float   | Percentage insured for that year                                   |

### `results/merged_profile.csv`
| Column   | Type    | Description                                |
| -------- | ------- | ------------------------------------------ |
| **variable** | string  | Name of the variable being summarized  |
| **count**    | integer | Number of non-missing observations     |
| **mean**     | float   | Mean of the variable                   |
| **std**      | float   | Standard deviation                     |
| **min**      | numeric | Minimum value                          |
| **25%**      | numeric | 25th percentile                        |
| **50%**      | numeric | Median (50th percentile)               |
| **75%**      | numeric | 75th percentile                        |
| **max**      | numeric | Maximum value                          |

### `results/cleaned_data.csv`
| Column                 | Type    | Description                                                       |
| ---------------------- | ------- | ----------------------------------------------------------------- |
| **Year**               | integer | Calendar year                                                     |
| **avg_arrest_rate**    | float   | Yearly average arrest rate                                        |
| **employed_population**| integer | Total employed population (summed or averaged per script logic)   |
| **unemployment_rate**  | float   | Yearly average unemployment rate                                  |
| **median_income**      | float   | Yearly average median household income                            |
| **pct_below_poverty**  | float   | Yearly average percentage below poverty                           |
| **pct_insured**        | float   | Yearly average percentage insured                                 |

### `results/descriptive_stats.csv`
| Column | Type    | Description                               |
| ------ | ------- | ----------------------------------------- |
| **index** | string  | Variable name                          |
| **count** | integer | Number of observations                 |
| **mean**  | float   | Mean value                             |
| **std**   | float   | Standard deviation                     |
| **min**   | numeric | Minimum value                          |
| **25%**   | numeric | 25th percentile                        |
| **50%**   | numeric | Median (50th percentile)               |
| **75%**   | numeric | 75th percentile                        |
| **max**   | numeric | Maximum value                          |

## Visualization Files

- **`results/correlation_matrix.png`**  
  Heatmap of the correlation matrix between numeric columns in `cleaned_data.csv`.

- **`results/arrest_rate_trend.png`**  
  Line chart showing the trend of yearly arrest rates over time.

- **`results/unemployment_rate_trend.png`**  
  Line chart showing the trend of yearly unemployment rates over time.