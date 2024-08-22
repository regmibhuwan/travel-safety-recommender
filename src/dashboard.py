import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

# Load the personalized recommendations data
file_path = "outputs/personalized_recommendations.csv"
df = pd.read_csv(file_path)

# Set up the title of the dashboard
st.title("Travel Safety Recommendation System")

# User input for continent preference
continent = st.selectbox(
    "Select Preferred Continent:",
    df['Continent'].unique()
)

# User input for specific concerns
concern = st.selectbox(
    "Select Concern:",
    ["general", "health", "political"]
)

# Filter the recommendations based on user input
filtered_df = df[df['Continent'] == continent]

if concern != "general":
    filtered_df = filtered_df[filtered_df['Details'].str.contains(concern, case=False)]

# Create a map centered on the globe
m = folium.Map(location=[20, 0], zoom_start=2)

# Add markers to the map based on filtered data
for i, row in filtered_df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"{row['Country']}: {row['Recommendation']}\n{row['Details']}",
        icon=folium.Icon(color="blue")
    ).add_to(m)

# Display the map in the Streamlit app
folium_static(m)
