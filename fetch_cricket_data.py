import os
import requests
import mysql.connector
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API credentials
API_KEY = os.getenv("API_KEY")
API_HOST = os.getenv("API_HOST")

# MySQL credentials
DB_NAME = os.getenv("DB_NAME")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", 3306))

# Cricbuzz API endpoint
url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"
headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": API_HOST
}

# Fetch recent matches
try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    data = response.json()
except Exception as e:
    print(f"Error fetching data from API: {e}")
    exit()

# ✅ Correct data parsing
matches = []
for match_type in data.get("typeMatches", []):
    for series in match_type.get("seriesMatches", []):
        series_info = series.get("seriesAdWrapper", {})
        series_name = series_info.get("seriesName", "Unknown Series")
        
        for match in series_info.get("matches", []):
            info = match.get("matchInfo", {})
            match_desc = info.get("matchDesc", "Unknown Match")
            team1 = info.get("team1", {}).get("teamName", "TBD")
            team2 = info.get("team2", {}).get("teamName", "TBD")
            status = info.get("status", "N/A")

            matches.append((series_name, match_desc, team1, team2, status))

# Create DataFrame
df = pd.DataFrame(matches, columns=["series", "match_desc", "team1", "team2", "status"])
print("Fetched matches:\n", df)

# Insert into MySQL
try:
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USERNAME,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DB_PORT
    )
    cursor = conn.cursor()

    # Create table if not exists
    create_table_query = """
    CREATE TABLE IF NOT EXISTS recent_matches (
        id INT AUTO_INCREMENT PRIMARY KEY,
        series VARCHAR(255),
        match_desc VARCHAR(255),
        team1 VARCHAR(100),
        team2 VARCHAR(100),
        status TEXT
    );
    """
    cursor.execute(create_table_query)

    # Clear old data
    cursor.execute("DELETE FROM recent_matches")

    # Insert new data
    insert_query = """
    INSERT INTO recent_matches (series, match_desc, team1, team2, status)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.executemany(insert_query, matches)
    conn.commit()
    print("✅ Data inserted successfully into recent_matches table.")

except mysql.connector.Error as err:
    print(f"MySQL error: {err}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
