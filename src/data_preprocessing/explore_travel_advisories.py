import json
import os
import pandas as pd

# Path to the JSON file
file_path = os.path.join("data", "raw", "travel_advisories.json")

# Load the JSON data
with open(file_path, 'r') as f:
    data = json.load(f)

# Extract the relevant part of the data
advisories = data['data']

# Create a list to store the processed data
records = []

for country_code, details in advisories.items():
    record = {
        "Country": details['name'],
        "Continent": details['continent'],
        "Risk Score": details['advisory']['score'],
        "Advisory Message": details['advisory']['message'],
        "Last Updated": details['advisory']['updated'],
        "Source": details['advisory']['source']
    }
    records.append(record)

# Convert the list of records into a DataFrame
df = pd.DataFrame(records)

# Display the first few rows of the DataFrame
print(df.head())

# Save the DataFrame to a CSV file for further use
output_path = os.path.join("data", "processed", "travel_advisories.csv")
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)

print(f"Processed data saved to {output_path}")
