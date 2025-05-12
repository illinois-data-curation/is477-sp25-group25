
import os
import requests
import hashlib
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
CENSUS_KEY = os.getenv("CENSUS_API_KEY")

# Years and fields to pull
years = [2012, 2013, 2014, 2015, 2016]
variables = {
    "DP03_0005E": "employed_population",
    "DP03_0062E": "unemployment_rate",
    "DP03_0088E": "median_income",
    "DP03_0096PE": "pct_below_poverty",
    "DP03_0099PE": "pct_insured"
}
var_str = ",".join(["NAME"] + list(variables.keys()))

data = []
for year in years:
    url = f"https://api.census.gov/data/{year}/acs/acs1/profile?get={var_str}&for=us:*&key={CENSUS_KEY}"
    r = requests.get(url)
    if r.status_code == 200:
        raw = r.json()
        headers = raw[0]
        values = raw[1]
        row = dict(zip(headers, values))
        row["Year"] = year
        data.append(row)
    else:
        print(f"Failed for {year}: {r.status_code}")

df = pd.DataFrame(data)
df.rename(columns=variables, inplace=True)

# Save JSON + CSV
os.makedirs("data", exist_ok=True)
df.to_json("data/census_multi_year.json", orient="records")
df.to_csv("data/census_multi_year.csv", index=False)

# Hash check
sha = hashlib.sha256(open("data/census_multi_year.csv", "rb").read()).hexdigest()
with open("data/census_multi_year.sha256", "w") as f:
    f.write(f"{sha}  census_multi_year.csv")

print("Census data from 2012–2016 saved to data/census_multi_year.csv")
print(f"Successfully pulled {len(data)} years of data")

# Expand each year's data across 12 months
expanded_data = []
for _, row in df.iterrows():
    for month in range(1, 13):
        new_row = row.copy()
        new_row["Month"] = month
        expanded_data.append(new_row)

expanded_df = pd.DataFrame(expanded_data)

# Save the expanded data
expanded_df.to_csv("data/census_multi_year.csv", index=False)
