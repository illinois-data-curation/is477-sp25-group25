import pandas as pd
import os

fbi_df = pd.read_csv("data/fbi_monthly.csv") 

census_df = pd.read_csv("data/census_monthly_data.csv")

merged = pd.merge(fbi_df, census_df, on=["Year", "Month"], how="inner")

merged.drop(columns=["NAME", "us", "population"], inplace=True)

cols = ["Year", "Month", "arrest_rate", "employed_population", "unemployment_rate",
        "median_income", "pct_below_poverty", "pct_insured"]
merged = merged[cols]

os.makedirs("results", exist_ok=True)
merged.to_csv("results/merged.csv", index=False)

print("✅ Monthly merged dataset saved to results/merged.csv")
