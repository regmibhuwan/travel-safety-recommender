import requests
import json
import os

def fetch_travel_advisories():
    url = "https://www.travel-advisory.info/api"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        save_data(data, "travel_advisories.json")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

def save_data(data, filename):
    directory = os.path.join("data", "raw")
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {filepath}")

if __name__ == "__main__":
    fetch_travel_advisories()
