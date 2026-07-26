import streamlit as st
import pandas as pd
@st.cache_data
def load_data():
    athlete = pd.read_csv("data/athlete_events.csv.zip")
    regions = pd.read_csv("data/noc_regions.csv.zip")
    athlete = athlete.drop_duplicates()
    athlete = athlete.merge(regions,on="NOC",how="left")
    athlete["region"] = athlete["region"].fillna("Unknown")
    return athlete
