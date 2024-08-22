import pandas as pd
import os
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# Define user preferences
user_preferences = {
    "risk_tolerance": 2,  # 0 = very risk-averse, 5 = very risk-tolerant
    "preferred_continent": "EU",  # User prefers to travel in Europe
    "concerned_about": "health"  # User is particularly concerned about health risks
}

# Load the processed travel advisories data
file_path = os.path.join("data", "processed", "travel_advisories.csv")
df = pd.read_csv(file_path)

# Initialize geolocator
geolocator = Nominatim(user_agent="travel-safety-recommender")

# Function to get latitude and longitude
def get_lat_lon(country):
    try:
        location = geolocator.geocode(country, timeout=10)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except GeocoderTimedOut:
        return None, None

# Apply the geocoding function to each country
df['Latitude'], df['Longitude'] = zip(*df['Country'].apply(get_lat_lon))

# Define the function to generate recommendations with user preferences
def generate_recommendation(row):
    recommendation = ""
    
    # First, check if the destination is on the user's preferred continent
    continent_preference = row['Continent'] == user_preferences['preferred_continent']
    
    # Adjust recommendation based on risk score and user risk tolerance
    if row['Risk Score'] >= user_preferences['risk_tolerance'] + 2:
        if "political" in row['Advisory Message'].lower() and user_preferences['concerned_about'] == "political":
            recommendation = "Not Recommended for Travel - Political Unrest (User Concern)"
        elif "health" in row['Advisory Message'].lower() and user_preferences['concerned_about'] == "health":
            recommendation = "Not Recommended for Travel - Health Risk (User Concern)"
        else:
            recommendation = "Not Recommended for Travel"
    elif row['Risk Score'] >= user_preferences['risk_tolerance'] and continent_preference:
        recommendation = "Travel with Caution - Preferred Continent"
    elif row['Risk Score'] >= user_preferences['risk_tolerance']:
        recommendation = "Travel with Caution"
    else:
        if continent_preference:
            recommendation = "Safe to Travel - Preferred Continent"
        else:
            recommendation = "Safe to Travel"
    
    return recommendation, row['Advisory Message']


# Apply the recommendation function to each row
df['Recommendation'], df['Details'] = zip(*df.apply(generate_recommendation, axis=1))

# Save the recommendations to a new CSV file
output_path = os.path.join("outputs", "personalized_recommendations.csv")
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)

print(f"Personalized recommendations generated and saved to {output_path}")
