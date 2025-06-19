import sqlite3
import pandas as pd
import json
with open('NASA_NEO_Insights/neo_cleaned.json', 'r') as f:
    records = json.load(f)

df = pd.DataFrame(records)

df.to_json('NASA_NEO_Insights/neo_cleaned.json', orient='records', indent=4)

conn = sqlite3.connect('nasa_asteroids.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS asteroids (
    id INTEGER,
    name TEXT,
    absolute_magnitude_h FLOAT,
    estimated_diameter_min_km FLOAT,
    estimated_diameter_max_km FLOAT,
    is_potentially_hazardous_asteroid BOOLEAN
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS close_approach (
    neo_reference_id INTEGER,
    close_approach_date DATE,
    relative_velocity_kmph FLOAT,
    astronomical FLOAT,
    miss_distance_km FLOAT,
    miss_distance_lunar FLOAT,
    orbiting_body TEXT
)
''')

# Insert unique asteroids
asteroids = df[['id', 'name', 'absolute_magnitude_h', 'estimated_diameter_min_km',
                'estimated_diameter_max_km', 'is_potentially_hazardous_asteroid']].drop_duplicates()
asteroids.to_sql('asteroids', conn, if_exists='append', index=False)

# Insert close approach data
close_approach = df[['neo_reference_id', 'close_approach_date', 'relative_velocity_kmph',
                     'astronomical', 'miss_distance_km', 'miss_distance_lunar', 'orbiting_body']]
close_approach.to_sql('close_approach', conn, if_exists='append', index=False)

conn.commit()
conn.close()
print("Database populated from JSON.")