import pandas as pd
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", 3306))

# Load CSV
df = pd.read_csv("recent_matches.csv")  # Rename your uploaded file accordingly

# Connect to MySQL
conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USERNAME,
    password=DB_PASSWORD,
    database=DB_NAME,
    port=DB_PORT
)

cursor = conn.cursor()

# Create table if not exists
create_query = """
CREATE TABLE IF NOT EXISTS recent_matches (
    id INT AUTO_INCREMENT PRIMARY KEY,
    series VARCHAR(255),
    match_desc VARCHAR(255),
    team1 VARCHAR(100),
    team2 VARCHAR(100),
    status TEXT
)
"""
cursor.execute(create_query)

# Clear existing data (optional)
cursor.execute("DELETE FROM recent_matches")

# Insert data
insert_query = """
INSERT INTO recent_matches (series, match_desc, team1, team2, status)
VALUES (%s, %s, %s, %s, %s)
"""

for _, row in df.iterrows():
    cursor.execute(insert_query, (
        row['series'],
        row['match_desc'],
        row['team1'],
        row['team2'],
        row['status']
    ))

conn.commit()
cursor.close()
conn.close()

print("✅ CSV data inserted into MySQL successfully.")
