# 🚀 NASA Near-Earth Object (NEO) Tracking & Insights using Public API

This project tracks and analyzes NASA Near-Earth Objects (NEOs) using the official NASA public API. It provides a Streamlit dashboard for interactive filtering, querying, and visualization of asteroid approach data.

---

## 📦 Project Structure

```mini_project/```   
```└── NASA_NEO_Insights/```  
```  └── db/```   
 ```         ├── nasa.json              # Raw data from NASA API  ```    
 ```         ├── neo_cleaned.json       # Cleaned data in JSON format  ```   
 ```         ├── nasa_asteroids.db      # SQLite database with asteroid and approach data  ```  
 ```   ├── api_requests.py        # Fetches NEO data from NASA API and saves as nasa.json  ```    
 ```   ├── data_cleance.py        # Cleans nasa.json and exports as neo_cleaned.json  ```   
 ```   ├── nasa_streamlit.py      # Main Streamlit dashboard  ```  
 ```   ├── readme.md              # Project-specific README  ```  
 ```   └── __pycache__/           # Python cache files  ```  

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
- Cleans and stores data in JSON and SQLite database
- Interactive Streamlit dashboard:
  - Filter asteroids by magnitude, diameter, velocity, distance, date, and hazard status
  - Predefined queries (e.g., top approaches, fastest asteroids, hazardous asteroids)
  - Data visualization in tabular format

---

## 🚦 How It Works

1. **Data Extraction**  
   Run `api_requests.py` to fetch and save NEO data from NASA API to `nasa.json`.

2. **Data Cleaning**  
   Run `data_cleance.py` to clean `nasa.json` and export the results to `neo_cleaned.json`.

3. **Database Population**  
   Run your database script (e.g., `sqlite3.py` or similar) to create and populate `nasa_asteroids.db` from the cleaned JSON.

4. **Dashboard**  
   Run `nasa_streamlit.py` with Streamlit to launch the interactive dashboard:
   ```sh
   streamlit run nasa_streamlit.py
   ```

---

