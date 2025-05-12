

# scripts/merge_data.py
import pandas as pd
import os

# --- Load FBI Monthly CSV ---
fbi_df = pd.read_csv("data/fbi_monthly.csv")  # Make sure this file exists

# --- Load Census Monthly CSV ---
census_df = pd.read_csv("data/census_monthly_data.csv")  # Make sure this file exists

# --- Merge on Year and Month ---
merged = pd.merge(fbi_df, census_df, on=["Year", "Month"], how="inner")

# --- Clean Columns ---
# Drop duplicate or unnecessary columns
merged.drop(columns=["NAME", "us", "population"], inplace=True)

# Optional: reorder columns
cols = ["Year", "Month", "arrest_rate", "employed_population", "unemployment_rate",
        "median_income", "pct_below_poverty", "pct_insured"]
merged = merged[cols]

# --- Save ---
os.makedirs("results", exist_ok=True)
merged.to_csv("results/merged.csv", index=False)

print("✅ Monthly merged dataset saved to results/merged.csv")
