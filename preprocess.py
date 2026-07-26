import pandas as pd

def load_data():
    athlete = pd.read_csv("data/athlete_events.csv")
    region = pd.read_csv("data/noc_regions.csv")
    df = athlete.drop_duplicates()
    df = df.merge(region, on="NOC", how="left")
    df["region"] = df["region"].fillna("Unknown")
    return df

def medal_data(df):
    return df.dropna(subset=["Medal"])