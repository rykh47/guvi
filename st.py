import streamlit as st
import sqlite3
import pandas as pd
from datetime import date

conn = sqlite3.connect('nasa_asteroids.db')

# --- Custom CSS for styling ---
st.markdown(
    """
    <style>
    .main-header {
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .header-icon {
        font-size: 2rem;
        vertical-align: middle;
    }
    .sidebar-section {
        margin-bottom: 2rem;
    }
    .sidebar-title {
        font-weight: bold;
        font-size: 1.2rem;
        margin-bottom: 0.5rem;
    }
    .filter-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 2rem;
    }
    .filter-label {
        font-size: 0.95rem;
        color: #666;
    }
    .highlight-btn {
        background-color: #ff4b4b !important;
        color: white !important;
        border-radius: 5px;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Sidebar Navigation ---
st.sidebar.markdown('<div class="sidebar-section sidebar-title">Asteroid Approaches</div>', unsafe_allow_html=True)
st.sidebar.button('Filter Criteria', key='filter', help='Filter asteroids', use_container_width=True)
st.sidebar.markdown('<div class="sidebar-section">Queries</div>', unsafe_allow_html=True)

# --- Main Header ---
st.markdown('<div class="main-header">🚀 NASA Asteroid Tracker <span class="header-icon">🪐</span></div>', unsafe_allow_html=True)

# --- Filters in Main Area ---
st.markdown('<div class="filter-card">', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<span class="filter-label">Min Magnitude</span>', unsafe_allow_html=True)
    min_mag = st.number_input("", min_value=10.0, max_value=32.41, value=12.0, step=0.01, key='min_mag')
    st.markdown('<span class="filter-label">Min Estimated Distance (km)</span>', unsafe_allow_html=True)
    min_dist = st.number_input(" ", min_value=0.0, max_value=4.43, value=0.0, step=0.01, key='min_dist')
    st.markdown('<span class="filter-label">Min Estimated Diameter (km)</span>', unsafe_allow_html=True)
    min_diam = st.number_input("  ", min_value=0.0, max_value=19.33, value=0.0, step=0.01, key='min_diam')

with col2:
    st.markdown('<span class="filter-label">Max Magnitude</span>', unsafe_allow_html=True)
    max_mag = st.number_input("   ", min_value=10.0, max_value=32.41, value=32.41, step=0.01, key='max_mag')
    st.markdown('<span class="filter-label">Max Estimated Distance (km)</span>', unsafe_allow_html=True)
    max_dist = st.number_input("    ", min_value=0.0, max_value=4.43, value=4.43, step=0.01, key='max_dist')
    st.markdown('<span class="filter-label">Max Estimated Diameter (km)</span>', unsafe_allow_html=True)
    max_diam = st.number_input("     ", min_value=0.0, max_value=19.33, value=19.33, step=0.01, key='max_diam')

with col3:
    st.markdown('<span class="filter-label">Relative_velocity_kmph Range</span>', unsafe_allow_html=True)
    rel_vel = st.slider(" ", 1441.21, 173071.85, (1441.21, 173071.85), key='rel_vel')
    st.markdown('<span class="filter-label">Astronomical Unit</span>', unsafe_allow_html=True)
    au = st.slider("  ", 0.0, 9.59, (0.0, 9.59), key='au')
    st.markdown('<span class="filter-label">Only Show Potentially Hazardous</span>', unsafe_allow_html=True)
    hazardous = st.selectbox("   ", ["All", "Yes", "No"], key='hazardous')

with col4:
    st.markdown('<span class="filter-label">Start Date</span>', unsafe_allow_html=True)
    start_date = st.date_input("    ", value=date(2014, 1, 1), key='start_date')
    st.markdown('<span class="filter-label">End Date</span>', unsafe_allow_html=True)
    end_date = st.date_input("     ", value=date(2015, 4, 13), key='end_date')

st.markdown('</div>', unsafe_allow_html=True)

# --- Filter Button ---
if st.button('Filter', key='filter_btn'):
    filter_query = f'''
    SELECT a.name, c.close_approach_date, c.relative_velocity_kmph, a.estimated_diameter_min_km, a.is_potentially_hazardous_asteroid
    FROM asteroids a
    JOIN close_approach c ON a.id = c.neo_reference_id
    WHERE 1=1
    AND a.absolute_magnitude_h BETWEEN {min_mag} AND {max_mag}
    AND c.relative_velocity_kmph BETWEEN {rel_vel[0]} AND {rel_vel[1]}
    AND a.estimated_diameter_min_km BETWEEN {min_diam} AND {max_diam}
    AND c.miss_distance_kilometers BETWEEN {min_dist} AND {max_dist}
    AND c.close_approach_date BETWEEN '{start_date}' AND '{end_date}'
    '''
    if hazardous == "Yes":
        filter_query += " AND a.is_potentially_hazardous_asteroid = 1"
    elif hazardous == "No":
        filter_query += " AND a.is_potentially_hazardous_asteroid = 0"
    filtered_df = pd.read_sql_query(filter_query, conn)
    st.header("Filtered Asteroids")
    st.dataframe(filtered_df)

# --- Query Section (below filters) ---
st.markdown('---')
query_options = {
    "Asteroid Approach Count": '''
        SELECT a.name, COUNT(*) as approach_count
        FROM asteroids a
        JOIN close_approach c ON a.id = c.neo_reference_id
        GROUP BY a.name
        ORDER BY approach_count DESC
        LIMIT 20
    ''',
    "Top 10 Fastest Asteroids": '''
        SELECT a.name, MAX(c.relative_velocity_kmph) as max_velocity
        FROM asteroids a
        JOIN close_approach c ON a.id = c.neo_reference_id
        GROUP BY a.name
        ORDER BY max_velocity DESC
        LIMIT 10
    ''',
    "Hazardous Asteroids (>3 approaches)": '''
        SELECT a.name, COUNT(*) as approach_count
        FROM asteroids a
        JOIN close_approach c ON a.id = c.neo_reference_id
        WHERE a.is_potentially_hazardous_asteroid = 1
        GROUP BY a.name
        HAVING approach_count > 3
        ORDER BY approach_count DESC
    '''
}
selected_query = st.selectbox("Select a Query", list(query_options.keys()))
df = pd.read_sql_query(query_options[selected_query], conn)
st.dataframe(df)

conn.close()