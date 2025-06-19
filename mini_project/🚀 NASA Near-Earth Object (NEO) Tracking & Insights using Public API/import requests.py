import requests
from datetime import datetime, timedelta
import time

API_KEY = 'HnfGx2LkyOqlZykr83ZhNH2CcL7jH2qPk7bQ80xW'  # Replace with your NASA API key
BASE_URL = 'https://api.nasa.gov/neo/rest/v1/feed'
start_date = datetime(2024, 1, 1)
records = []
max_records = 10000

def fetch_neo_data(start, end):
    url = f"{BASE_URL}?start_date={start}&end_date={end}&api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error:", response.text)
        return None
    return response.json()

while len(records) < max_records:
    end_date = start_date + timedelta(days=6)
    data = fetch_neo_data(start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
    if not data:
        break
    for date in data['near_earth_objects']:
        for obj in data['near_earth_objects'][date]:
            try:
                for approach in obj.get('close_approach_data', []):
                    record = {
                        'id': int(obj.get('id', 0)),
                        'neo_reference_id': int(obj.get('neo_reference_id', 0)),
                        'name': obj.get('name', ''),
                        'absolute_magnitude_h': float(obj.get('absolute_magnitude_h', 0)),
                        'estimated_diameter_min_km': float(obj['estimated_diameter']['kilometers']['estimated_diameter_min']),
                        'estimated_diameter_max_km': float(obj['estimated_diameter']['kilometers']['estimated_diameter_max']),
                        'is_potentially_hazardous_asteroid': bool(obj.get('is_potentially_hazardous_asteroid', False)),
                        'close_approach_date': datetime.strptime(approach.get('close_approach_date', '1900-01-01'), '%Y-%m-%d').date(),
                        'relative_velocity_kmph': float(approach['relative_velocity']['kilometers_per_hour']),
                        'astronomical': float(approach['miss_distance']['astronomical']),
                        'miss_distance_km': float(approach['miss_distance']['kilometers']),
                        'miss_distance_lunar': float(approach['miss_distance']['lunar']),
                        'orbiting_body': approach.get('orbiting_body', '')
                    }
                    records.append(record)
                    if len(records) >= max_records:
                        break
                if len(records) >= max_records:
                    break
            except Exception as e:
                continue
        if len(records) >= max_records:
            break
    # Pagination: move to next 7 days
    start_date = end_date + timedelta(days=1)
    time.sleep(1)  # Be polite to the API

import pandas as pd
df = pd.DataFrame(records)
df.to_csv('neo_cleaned.csv', index=False)
print(f"Extracted {len(df)} records.")