import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAQ_API_KEY")

BASE_URL = "https://api.openaq.org/v3"

RAW_DATA_DIR = "data/raw"


def fetch_latest_data(location_id):

    url = f"{BASE_URL}/locations/{location_id}/latest"

    headers = {
        "X-API-Key": API_KEY
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to OpenAQ API.")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP Error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Request Error: {error}")

    return None


def save_raw_data(data, location_id):

    os.makedirs(RAW_DATA_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"location_{location_id}_{timestamp}.json"

    filepath = os.path.join(
        RAW_DATA_DIR,
        filename
    )

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"Raw data saved to: {filepath}")


if __name__ == "__main__":

    location_id = 8118

    data = fetch_latest_data(location_id)

    if data:
        save_raw_data(data, location_id)