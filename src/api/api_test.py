import os
import requests
from dotenv import load_dotenv

load_dotenv()

Api_KEY=os.getenv("f2717c9c02baa000a92c3987b9615ed78dcbadbb5b5108816a1e5ec6a44c0b5d")

url="https://api.openaq.org/v3/locations/8118"
headers={
    "X-API-Key":"f2717c9c02baa000a92c3987b9615ed78dcbadbb5b5108816a1e5ec6a44c0b5d"
}

reponse=requests.get(url,headers=headers)
print("status code:",reponse.status_code)

data=reponse.json()
print(data)