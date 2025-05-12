# scripts/manual_merge.py
import pandas as pd
import os

# Load datasets
fbi = pd.read_csv("data/fbi_monthly.csv")
census = pd.read_csv("data/census_multi_year.csv")

# Drop duplicate columns if needed
census = census.drop(columns=['NAME', 'us'], errors='ignore')

# Merge on Year + Month
merged = pd.merge(fbi, census, on=["Year", "Month"], how="inner")

# Save output
os.makedirs("results", exist_ok=True)
merged.to_csv("results/merged.csv", index=False)

print("✅ Manual merged dataset saved to results/merged.csv")