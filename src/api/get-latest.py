import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("f2717c9c02baa000a92c3987b9615ed78dcbadbb5b5108816a1e5ec6a44c0b5d")

url = "https://api.openaq.org/v3/locations/8118/latest"

headers = {
    "X-API-Key": "f2717c9c02baa000a92c3987b9615ed78dcbadbb5b5108816a1e5ec6a44c0b5d"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

data = response.json()

for record in data["results"]:
    print(record)