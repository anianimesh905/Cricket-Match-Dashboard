import os
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
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
    # Build SQLAlchemy connection URL
    db_uri = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    # Create SQLAlchemy engine
    engine = create_engine(db_uri)

    # Define your query
    query = "SELECT series, match_desc, team1, team2, status FROM recent_matches ORDER BY id DESC;"

    # Read from MySQL using SQLAlchemy engine
    df = pd.read_sql(query, con=engine)
    
    # Show dataframe in Streamlit
    st.dataframe(df, use_container_width=True)

except Exception as err:
    st.error(f"Database connection failed: {err}")

# Sidebar footer
st.sidebar.title("About")
st.sidebar.info("Made with ❤️ by Ani | Powered by Streamlit + MySQL + Cricbuzz API")
