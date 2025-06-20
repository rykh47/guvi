# 🚀 NASA Near-Earth Object (NEO) Tracking & Insights using Public API

This project tracks and analyzes NASA Near-Earth Objects (NEOs) using the official NASA public API. It provides a **Streamlit dashboard** for interactive filtering, querying, and visualization of asteroid approach data.

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

## 📊 Streamlit Application Features

### 1. **Asteroid Approaches (Filter Criteria)**
- **Filter asteroids** by:
  - Estimated diameter (min/max)
  - Relative velocity
  - Astronomical units (AU)
  - Lunar distance (LD)
  - Potentially hazardous status
  - Date range
- **View filtered results** in a sortable, searchable table.

### 2. **Asteroid Queries**
- Choose from a rich set of **predefined SQL queries** to answer questions such as:
  - How many times each asteroid has approached Earth
  - Average velocity of each asteroid
  - Top 10 fastest asteroids
  - Hazardous asteroids with frequent approaches
  - Closest approaches, fastest speeds, and more
- **Extra sample queries** included for deeper insights:
  - Average miss distance for hazardous asteroids
  - All approaches in a specific year
  - Asteroids with smallest/large diameters
  - Distribution of approaches per year
  - Earliest/latest approach dates
  - ...and more!

### 3. **Custom SQL Query Box**
- **Write and execute your own SQL queries** directly in the dashboard to explore the data and derive your own insights.

### 4. **Debugging Data Stats**
- Optionally display sample data and statistics for debugging or exploration.

---

## 🚦 How To Use the Streamlit Dashboard

1. **Install dependencies**  
   Make sure you have Python 3 and install requirements:
   ```sh
   pip install streamlit pandas requests
   ```

2. **Data Extraction**  
   Run `api_requests.py` to fetch and save NEO data from NASA API to `nasa.json`.

3. **Data Cleaning**  
   Run `data_cleance.py` to clean `nasa.json` and export the results to `neo_cleaned.json`.

4. **Database Population**  
   Run your database script (e.g., `sqlite3.py` or similar) to create and populate `nasa_asteroids.db` from the cleaned JSON.

5. **Launch the Dashboard**  
   Run the Streamlit app:
   ```sh
   streamlit run nasa_streamlit.py
   ```

6. **Explore the Features**
   - Use the **sidebar** to switch between "Filter Criteria" and "Asteroid Queries".
   - In **Filter Criteria**, set your filters and click "Filter" to see matching asteroids.
   - In **Asteroid Queries**, select a predefined question to view results instantly.
   - Try the **custom SQL query** box to write your own queries and analyze the data further.

---

## 💡 Example Use Cases

- Identify potentially hazardous asteroids that have approached Earth multiple times.
- Find the fastest or largest asteroids in the dataset.
- Analyze trends in asteroid approaches over time.
- Explore the data with your own custom SQL queries for unique insights.

---

## 📚 Learning Outcomes

- Practice data extraction, cleaning, and storage using real-world NASA data.
- Learn to build interactive dashboards with Streamlit.
- Develop SQL skills by exploring and analyzing a real asteroid dataset.
- Gain experience in data-driven storytelling and scientific inquiry.

---

## 🛰️ Credits

- Data: [NASA NEO API](https://api.nasa.gov/)
- Dashboard: Built with Streamlit

