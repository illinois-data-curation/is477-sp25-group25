# fetch_fbi_data.py
import os
import requests
import hashlib
from dotenv import load_dotenv
load_dotenv()  # Load .env file
print("FBI KEY:", os.getenv("FBI_API_KEY"))

FBI_KEY = os.getenv("FBI_API_KEY")
url = url = f"https://api.usa.gov/crime/fbi/cde/arrest/agency/USA/all?type=counts&from=01-2012&to=12-2016&API_KEY={FBI_KEY}"


r = requests.get(url)
os.makedirs("data", exist_ok=True)

with open("data/fbi_crime.json", "w") as f:
    f.write(r.text)

sha = hashlib.sha256(r.content).hexdigest()
with open("data/fbi_crime.sha256", "w") as f:
    f.write(f"{sha}  fbi_crime.json")
