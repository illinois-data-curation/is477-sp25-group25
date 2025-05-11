# clean_data.py

#!/usr/bin/env python3
import os
import pandas as pd

def load_raw(path="results/merged.csv"):
    return pd.read_csv(path)

def clean(df):
    # 1. Drop rows missing core metrics
    df = df.dropna(subset=[
        "arrest_rate",
        "employed_population",
        "unemployment_rate"
    ])

    # 2. Fill non-critical gaps
    df["median_income"] = df["median_income"].fillna(df["median_income"].median())
    df["pct_below_poverty"] = df["pct_below_poverty"].fillna(0)
    df["pct_insured"]      = df["pct_insured"].fillna(0)

    # 3. Ensure numeric types
    num_cols = [
        "arrest_rate",
        "employed_population",
        "unemployment_rate",
        "median_income",
        "pct_below_poverty",
        "pct_insured"
    ]
    for col in num_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # 4. (Optional) roll monthly → yearly
    df_yearly = (
        df
        .assign(Year=df["Year"].astype(int))
        .groupby("Year", as_index=False)
        .agg({
            "arrest_rate":        "mean",
            "employed_population":"sum",
            "unemployment_rate":  "mean",
            "median_income":      "mean",
            "pct_below_poverty":  "mean",
            "pct_insured":        "mean"
        })
    )

    return df_yearly

def main():
    raw = load_raw()
    cleaned = clean(raw)
    os.makedirs("results", exist_ok=True)
    cleaned.to_csv("results/cleaned_data.csv", index=False)
    print(f"✅ Cleaned data → results/cleaned_data.csv ({len(cleaned)} rows)")

if __name__ == "__main__":
    main()