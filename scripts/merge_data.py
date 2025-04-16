# scripts/merge_data.py
import json, pandas as pd, os

# --- Load FBI Data ---
with open("data/fbi_crime.json") as f:
    fbi_raw = json.load(f)

monthly_rates = fbi_raw["rates"]["United States Arrests"]

# Convert to dataframe
fbi_df = pd.DataFrame(list(monthly_rates.items()), columns=["month_year", "arrest_rate"])
fbi_df["Year"] = fbi_df["month_year"].str[-4:].astype(int)

# Compute average arrest rate by year
fbi_yearly = fbi_df.groupby("Year").agg({"arrest_rate": "mean"}).reset_index()
fbi_yearly.rename(columns={"arrest_rate": "avg_arrest_rate"}, inplace=True)

# --- Load Census Multi-Year Data ---
with open("data/census_multi_year.json") as f:
    census_raw = json.load(f)

census_df = pd.DataFrame(census_raw)

# Convert to correct types
census_df["Year"] = census_df["Year"].astype(int)
census_df["employed_population"] = census_df["employed_population"].astype(int)
census_df["median_income"] = census_df["median_income"].astype(int)
census_df["pct_insured"] = census_df["pct_insured"].astype(float)
census_df["pct_below_poverty"] = census_df["pct_below_poverty"].astype(float)
census_df["unemployment_rate"] = census_df["unemployment_rate"].astype(float)

# --- Merge on Year ---
merged = pd.merge(fbi_yearly, census_df, on="Year", how="inner")

# --- Export ---
os.makedirs("results", exist_ok=True)
merged.to_csv("results/merged.csv", index=False)

# --- Log ---
os.makedirs("logs", exist_ok=True)
with open("logs/integration_log.md", "w") as f:
    f.write("- Averaged FBI monthly arrest rates per year (2012–2016)\n")
    f.write("- Merged with census socioeconomic data (multi-year, national)\n")
    f.write("- Variables: employed_population, median_income, pct_insured, pct_below_poverty, unemployment_rate\n")
    f.write(f"- Final dataset saved as results/merged.csv with {len(merged)} rows\n")

print("✅ Merged data saved to results/merged.csv")
