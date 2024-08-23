# **Travel Safety Recommender System 🌍**

### **Live Demo**: [Travel Safety Recommender](https://regmibhuwan-travel-safety-recommender-srcdashboard-biqsxm.streamlit.app/)

## **Overview**

The **Travel Safety Recommender System** is an interactive web application that provides personalized travel safety recommendations based on global travel advisories. Built with data science and machine learning principles, this application helps users make informed decisions about their travel plans by analyzing real-time advisory data, user preferences, and geographic factors.


---

## **Features**

- **Interactive Map**: Visualize travel safety recommendations on an interactive world map with real-time updates.
- **User Preferences**: Tailor recommendations based on user-selected continents and specific concerns (e.g., health, political risks).
- **Real-Time Advisory Data**: Integrates live data feeds to provide up-to-date safety recommendations.
- **Scalable Deployment**: Hosted on Streamlit Cloud for easy access and sharing.
- **Intuitive Dashboard**: Built using Streamlit, offering a clean and user-friendly interface.

---

## **Technology Stack**

- **Frontend & Backend**: [Streamlit](https://streamlit.io/) – Rapid prototyping of data-driven web apps.
- **Mapping & Visualization**: [Folium](https://python-visualization.github.io/folium/) – Interactive maps powered by Leaflet.js.
- **Geocoding**: [Geopy](https://geopy.readthedocs.io/en/stable/) – Geocoding of country names to latitude and longitude.
- **Data Handling**: [Pandas](https://pandas.pydata.org/) – Efficient data manipulation and analysis.
- **Deployment**: [Streamlit Community Cloud](https://streamlit.io/cloud) – Seamless deployment of Streamlit apps.

---

## **Installation**

### **Step 1: Clone the Repository**

git clone https://github.com/regmibhuwan/travel-safety-recommender.git
cd travel-safety-recommender**```

### **Step 2: Set Up the Virtual Environment**

python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate 

### ** Step 3: Install Dependencies**

pip install -r requirements.txt

### ** Step 4: Run the Application Locally**

streamlit run src/dashboard.py

## How It Works
- Data Collection: Fetches the latest travel advisories using APIs, processes the data, and geocodes countries to include latitude and longitude.

- Data Processing: Preprocesses raw data to generate a structured CSV file with risk levels, advisory messages, and geospatial data.

- Recommendation Engine: Uses user inputs (preferred continent, specific concerns) to filter and present personalized travel safety recommendations.

- Interactive Dashboard: Displays recommendations on a world map with clickable markers to view detailed advisories.

## Live Deployment
The app is deployed on Streamlit Cloud, making it accessible from anywhere without the need for local installation. Check out the live demo here: Travel Safety Recommender.

## Challenges and Future Improvements
- Real-Time Data Integration: Integrating live data sources for continuous updates is a challenge, but this project sets the foundation for future enhancements.

- Scalability: Currently optimized for small to medium datasets; could be expanded for larger, more complex data sets.

- Enhanced Personalization: Future iterations could incorporate machine learning to predict user preferences based on historical data.
  
## Contribution
Contributions are welcome! If you have any suggestions or improvements, feel free to fork the repository and create a pull request.

