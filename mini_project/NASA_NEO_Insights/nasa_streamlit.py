import streamlit as st
import sqlite3
import pandas as pd
from datetime import date

conn = sqlite3.connect('NASA_NEO_Insights/db/nasa_asteroids.db')

# --- CSS ---
st.markdown(
    """
    <style>
    .main-header {
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 2rem;
        margin-top: 1rem;
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
        padding: 2rem 1.5rem 2rem 1.5rem;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 2.5rem;
        margin-top: 1rem;
        max-width: 100%;
    }
    .filter-label {
        font-size: 1rem;
        color: #666;
        margin-bottom: 0.3rem;
        display: block;
    }
    .stNumberInput, .stSlider, .stDateInput, .stSelectbox {
        margin-bottom: 1.2rem !important;
    }
    .highlight-btn {
        background-color: #ff4b4b !important;
        color: white !important;
        border-radius: 5px;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    @media (max-width: 900px) {
        .main-header {
            font-size: 2rem;
        }
        .filter-card {
            padding: 1rem 0.5rem 1rem 0.5rem;
        }
    }
    @media (max-width: 700px) {
        .main-header {
            font-size: 1.3rem;
        }
        .filter-card {
            padding: 0.5rem 0.2rem 0.5rem 0.2rem;
        }
        .stApp [data-testid="column"] {
            flex: 1 1 100% !important;
            min-width: 100% !important;
            max-width: 100% !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Sidebar  ---
st.sidebar.markdown('<div class="sidebar-section sidebar-title">Asteroid Approaches</div>', unsafe_allow_html=True)
st.sidebar.button('Filter Criteria', key='filter', help='Filter asteroids', use_container_width=True)
st.sidebar.markdown('<div class="sidebar-section">Queries</div>', unsafe_allow_html=True)

# --- Main Header ---
st.markdown('<div class="main-header">🚀 NASA Asteroid Tracker <span class="header-icon">🪐</span></div>', unsafe_allow_html=True)

# --- Filters in Main Area ---
st.markdown(
    """
    <style>
    .filter-flex {
        display: flex;
        flex-wrap: wrap;
        gap: 2rem;
        justify-content: space-between;
        align-items: flex-end;
    }
    .filter-item {
        min-width: 220px;
        flex: 1 1 220px;
        margin-bottom: 1.2rem;
    }
    @media (max-width: 900px) {
        .filter-flex {
            gap: 1rem;
        }
        .filter-item {
            min-width: 160px;
        }
    }
    @media (max-width: 700px) {
        .filter-flex {
            flex-direction: column;
            gap: 0.5rem;
        }
        .filter-item {
            min-width: 100%;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.container():
    # First row
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<span class="filter-label">Estimated Diameter Min (km)</span>', unsafe_allow_html=True)
        diam_min_range = st.slider(
            "Diameter Min (km)", 0.0, 5.0, (0.0, 5.0), step=0.001, key='diam_min_range'
        )
    with col2:
        st.markdown('<span class="filter-label">Estimated Diameter Max (km)</span>', unsafe_allow_html=True)
        diam_max_range = st.slider(
            "Diameter Max (km)", 0.0, 11.0, (0.0, 11.0), step=0.001, key='diam_max_range'
        )
    with col3:
        st.markdown('<span class="filter-label">Relative velocity (kmph)</span>', unsafe_allow_html=True)
        rel_vel = st.slider(
            "Relative velocity (kmph)", 1418, 190514, (1418, 190514), step=1, key='rel_vel'
        )

    # Second row
    col4, col5, col6 = st.columns(3)
    with col4:
        st.markdown('<span class="filter-label">Astronomical Units</span>', unsafe_allow_html=True)
        au_range = st.slider(
            "AU", 0.0, 0.5, (0.0, 0.5), step=0.001, key='au_range'
        )
    with col5:
        st.markdown('<span class="filter-label">Lunar Distance</span>', unsafe_allow_html=True)
        lunar_range = st.slider(
            "Lunar Distance", 0.02, 194.48, (0.02, 194.48), step=0.01, key='lunar_range'
        )
    with col6:
        st.markdown('<span class="filter-label">Potentially Hazardous</span>', unsafe_allow_html=True)
        hazardous = st.selectbox("Potentially Hazardous", ["All", "Yes", "No"], key='hazardous')

    # Third row
    col7, col8, col9 = st.columns(3)
    with col7:
        st.markdown('<span class="filter-label">Start Date</span>', unsafe_allow_html=True)
        start_date = st.date_input("Start Date", value=pd.to_datetime("2024-01-01"), key='start_date')
    with col8:
        st.markdown('<span class="filter-label">End Date</span>', unsafe_allow_html=True)
        end_date = st.date_input("End Date", value=pd.to_datetime("2025-08-17"), key='end_date')

    st.markdown('</div>', unsafe_allow_html=True)

st.write("")  

# --- Filter Button and Table Display ---
if 'filtered_df' not in st.session_state:
    # default filter
    filter_query = '''
    SELECT a.name, c.close_approach_date, c.relative_velocity_kmph, 
           a.estimated_diameter_min_km, a.estimated_diameter_max_km, 
           a.is_potentially_hazardous_asteroid
    FROM asteroids a
    JOIN close_approach c ON a.id = c.neo_reference_id
    '''
    st.session_state.filtered_df = pd.read_sql_query(filter_query, conn)

if st.button('Filter', key='filter_btn'):
    filter_query = f'''
    SELECT a.name, c.close_approach_date, c.relative_velocity_kmph, 
           a.estimated_diameter_min_km, a.estimated_diameter_max_km, 
           a.is_potentially_hazardous_asteroid
    FROM asteroids a
    JOIN close_approach c ON a.id = c.neo_reference_id
    WHERE 1=1
    AND a.estimated_diameter_min_km BETWEEN {diam_min_range[0]} AND {diam_min_range[1]}
    AND a.estimated_diameter_max_km BETWEEN {diam_max_range[0]} AND {diam_max_range[1]}
    AND c.relative_velocity_kmph BETWEEN {rel_vel[0]} AND {rel_vel[1]}
    AND c.astronomical BETWEEN {au_range[0]} AND {au_range[1]}
    AND c.miss_distance_lunar BETWEEN {lunar_range[0]} AND {lunar_range[1]}
    AND c.close_approach_date BETWEEN '{start_date}' AND '{end_date}'
    '''
    if hazardous == "Yes":
        filter_query += " AND a.is_potentially_hazardous_asteroid = 1"
    elif hazardous == "No":
        filter_query += " AND a.is_potentially_hazardous_asteroid = 0"
    st.session_state.filtered_df = pd.read_sql_query(filter_query, conn)

st.header("Filtered Asteroids")
if st.session_state.filtered_df.empty:
    st.info("No results found for the selected filters.")
else:
    st.dataframe(st.session_state.filtered_df, use_container_width=True)

st.divider()

# --- Query Section ---
st.markdown("### Quick Queries")
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
st.dataframe(df, use_container_width=True)

# --- Debugging Data Stats ---
if st.checkbox("Show data stats for debugging"):
    st.write("Asteroids sample:", pd.read_sql_query("SELECT * FROM asteroids LIMIT 5", conn))
    st.write("Close approach sample:", pd.read_sql_query("SELECT * FROM close_approach LIMIT 5", conn))
    st.write(pd.read_sql_query("SELECT MIN(estimated_diameter_min_km), MAX(estimated_diameter_min_km) FROM asteroids", conn))
    st.write(pd.read_sql_query("SELECT MIN(estimated_diameter_max_km), MAX(estimated_diameter_max_km) FROM asteroids", conn))
    st.write(pd.read_sql_query("SELECT MIN(relative_velocity_kmph), MAX(relative_velocity_kmph) FROM close_approach", conn))
    st.write(pd.read_sql_query("SELECT MIN(astronomical), MAX(astronomical) FROM close_approach", conn))
    st.write(pd.read_sql_query("SELECT MIN(miss_distance_lunar), MAX(miss_distance_lunar) FROM close_approach", conn))
    st.write(pd.read_sql_query("SELECT MIN(close_approach_date), MAX(close_approach_date) FROM close_approach", conn))
    st.write(pd.read_sql_query("SELECT a.id, c.neo_reference_id FROM asteroids a JOIN close_approach c ON a.id = c.neo_reference_id LIMIT 5", conn))

conn.close()