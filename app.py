import os
import streamlit as st
import pandas as pd
import mysql.connector
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# MySQL connection settings
DB_NAME = os.getenv("DB_NAME")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))

# App config
st.set_page_config(
    page_title="🏏 Cricket Match Dashboard",
    page_icon="🏏",
    layout="wide"
)

# Title and intro
st.title("🏏 Recent Cricket Matches Dashboard")
st.markdown("This dashboard shows recent cricket matches fetched using the Cricbuzz API (via RapidAPI).")

# Connect to MySQL and fetch data
try:
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USERNAME,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DB_PORT
    )

    query = "SELECT series, match_desc, team1, team2, status FROM recent_matches ORDER BY id DESC;"
    df = pd.read_sql(query, conn)
    conn.close()

    # Show dataframe in Streamlit
    st.dataframe(df, use_container_width=True)

except mysql.connector.Error as err:
    st.error(f"Database connection failed: {err}")

# Sidebar footer
st.sidebar.title("About")
st.sidebar.info("Made with ❤️ by Ani | Powered by Streamlit + MySQL + Cricbuzz API")
