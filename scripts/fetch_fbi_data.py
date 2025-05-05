
import os
import requests
import hashlib
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
FBI_KEY = os.getenv("FBI_API_KEY")

url = f"https://api.usa.gov/crime/fbi/cde/arrest/agency/USA/all?type=counts&from=01-2012&to=12-2016&API_KEY={FBI_KEY}"
r = requests.get(url)
data = r.json()

rates = data["rates"]["United States Arrests"]
populations = data["populations"]["population"]["United States"]

records = []
for month_year in rates:
    rate = rates[month_year]
    population = populations[month_year]
    month, year = month_year.split("-")
    records.append({
        "Year": int(year),
        "Month": int(month),
        "arrest_rate": rate,
        "population": population
    })
    

fbi_df = pd.DataFrame(records)
fbi_df.sort_values(by=["Year", "Month"], inplace=True)

os.makedirs("data", exist_ok=True)
fbi_df.to_csv("data/fbi_monthly.csv", index=False)

sha = hashlib.sha256(open("data/fbi_monthly.csv", "rb").read()).hexdigest()
with open("data/fbi_monthly.sha256", "w") as f:
    f.write(f"{sha}  fbi_monthly.csv")

print("✅ FBI monthly data saved to data/fbi_monthly.csv")
