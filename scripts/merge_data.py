# scripts/merge_data.py
import json, pandas as pd, os

# --- Load FBI JSON ---
with open("data/fbi_crime.json") as f:
    raw = json.load(f)
monthly_rates = raw["rates"]["United States Arrests"]

# Extract and average by year
fbi_df = pd.DataFrame(list(monthly_rates.items()), columns=["month_year", "arrest_rate"])
fbi_df["Year"] = fbi_df["month_year"].str[-4:].astype(int)
fbi_df["arrest_rate"] = pd.to_numeric(fbi_df["arrest_rate"], errors="coerce")

fbi_yearly = fbi_df.groupby("Year").agg({"arrest_rate": "mean"}).reset_index()
fbi_yearly.rename(columns={"arrest_rate": "avg_arrest_rate"}, inplace=True)

# --- Load Census CSV ---
census_df = pd.read_csv("data/census_multi_year.csv")

# --- Merge ---
merged = pd.merge(fbi_yearly, census_df, on="Year", how="inner")
merged.drop(columns=["NAME", "us"], inplace=True)
merged["avg_arrest_rate"] = merged["avg_arrest_rate"].round(1)

# --- Save ---
os.makedirs("results", exist_ok=True)
merged.to_csv("results/merged.csv", index=False)

print("✅ Merged CSV saved to results/merged.csv")
