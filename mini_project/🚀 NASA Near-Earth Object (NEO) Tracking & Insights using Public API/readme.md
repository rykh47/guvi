# 🚀 NASA Near-Earth Object (NEO) Tracking & Insights using Public API

This project tracks and analyzes NASA Near-Earth Objects (NEOs) using the official NASA public API. It provides a Streamlit dashboard for interactive filtering, querying, and visualization of asteroid approach data.

---

## 📦 Project Structure

mini_project/ └── 🚀 NASA Near-Earth Object (NEO) Tracking & Insights using Public API/   
&nbsp;&nbsp;&nbsp;&nbsp;                   ├── nasa_asteroids.db # SQLite database with asteroid and approach data   
&nbsp;&nbsp;&nbsp;&nbsp;                   ├── nasa_streamlit.py # Main Streamlit dashboard   
&nbsp;&nbsp;&nbsp;&nbsp;                   ├── nasa.json # Raw data from NASA API    
&nbsp;&nbsp;&nbsp;&nbsp;                   ├── readme.md # Project-specific README    
&nbsp;&nbsp;&nbsp;&nbsp;                   ├── sqlite3.py # Script to populate SQLite DB from JSON  

---

## 🛠️ Technologies Used

- **Python 3**
- **Pandas**: Data manipulation and cleaning
- **Requests**: Fetching data from NASA API
- **Streamlit**: Interactive dashboard and UI
- **SQLite3**: Local database for efficient querying
- **NASA NEO API**: Data source for asteroid approaches

---

## 📊 Features

- Fetches NEO data from NASA’s public API
- Cleans and stores data in CSV and SQLite database
- Interactive Streamlit dashboard:
  - Filter asteroids by magnitude, diameter, velocity, distance, date, and hazard status
  - Predefined queries (e.g., top approaches, fastest asteroids, hazardous asteroids)
  - Data visualization in tabular format

---

## 🚦 How It Works

1. **Data Extraction**  
   Run `requests.py` to fetch and save NEO data from NASA API to `neo_cleaned.csv`.

2. **Database Population**  
   Run `sqlite3.py` to create and populate `nasa_asteroids.db` from the CSV.

3. **Dashboard**  
   Run `nasa_streamlit.py` with Streamlit to launch the interactive dashboard:
   ```sh
   streamlit run st.py

