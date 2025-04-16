
import os, requests, hashlib, json
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
CENSUS_KEY = os.getenv("CENSUS_API_KEY")

# Years and fields to pull
years = [2012, 2013, 2014, 2015, 2016]
variables = ["S2301_C01_001E", "S1901_C01_012E"]  # employment + income
var_str = ",".join(["NAME"] + variables)

data = []
for year in years:
    url = f"https://api.census.gov/data/{year}/acs/acs5/subject?get={var_str}&for=us:*&key={CENSUS_KEY}"
    r = requests.get(url)
    if r.status_code == 200:
        raw = r.json()
        headers = raw[0]
        values = raw[1]
        row = dict(zip(headers, values))
        row["Year"] = year
        data.append(row)
    else:
        print(f"❌ Failed for {year}: {r.status_code}")

df = pd.DataFrame(data)
df.rename(columns={
    "S2301_C01_001E": "employed_population",
    "S1901_C01_012E": "median_income",
    "S2701_C01_001E": "pct_insured",
    "S1701_C03_001E": "pct_below_poverty",
    "DP03_0062E": "unemployment_rate"
}, inplace=True)


# Save JSON + CSV
os.makedirs("data", exist_ok=True)
df.to_json("data/census_multi_year.json", orient="records")
df.to_csv("data/census_multi_year.csv", index=False)

# Hash check
sha = hashlib.sha256(open("data/census_multi_year.csv", "rb").read()).hexdigest()
with open("data/census_multi_year.sha256", "w") as f:
    f.write(f"{sha}  census_multi_year.csv")

print("✅ Census data from 2012–2016 saved to data/census_multi_year.csv")
