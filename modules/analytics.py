def medal_tally(df, year="Overall", country="Overall"):
    temp_df = df.dropna(subset=["Medal"])
    if year != "Overall":
        temp_df = temp_df[temp_df["Year"] == year]
    if country != "Overall":
        temp_df = temp_df[temp_df["region"] == country]
    tally = (temp_df.groupby("region")["Medal"].count().reset_index().rename(columns={"region": "Country","Medal": "Total Medals"})
        .sort_values("Total Medals",ascending=False))
    return tally
def year_list(df):
    years = sorted(df["Year"].dropna().unique().tolist())
    return ["Overall"] + years

def country_list(df):
    countries = sorted(df["region"].dropna().unique().tolist())
    return ["Overall"] + countries

def country_list_only(df):
    return sorted(df["region"].dropna().unique().tolist())

def country_yearwise_medals(df, country):
    temp = df[(df["region"] == country) &(df["Medal"].notna())]
    trend = (temp.groupby("Year").size().reset_index(name="Medals"))
    return trend

def country_top_sports(df, country):
    temp = df[(df["region"] == country) &(df["Medal"].notna())]
    sports = (temp.groupby("Sport").size().reset_index(name="Medals")
    .sort_values("Medals", ascending=False).head(10))
    return sports

def country_top_athletes(df, country):
    temp = df[(df["region"] == country) & (df["Medal"].notna())]
    athletes = (temp.groupby("Name").size().reset_index(name="Medals").sort_values("Medals", ascending=False).head(10))
    return athletes

def country_statistics(df, country):
    temp = df[df["region"] == country]
    return {"Olympics": temp["Year"].nunique(),
    "Athletes": temp["Name"].nunique(),
    "Sports": temp["Sport"].nunique(),
    "Events": temp["Event"].nunique(),
    "Medals": temp["Medal"].notna().sum()}

def athlete_list(df):
    return sorted(df["Name"].dropna().unique().tolist())

def athlete_statistics(df, athlete):
    temp = df[df["Name"] == athlete]
    return {"Olympics": temp["Year"].nunique(),
        "Sports": temp["Sport"].nunique(),
        "Events": temp["Event"].nunique(),
        "Gold": (temp["Medal"] == "Gold").sum(),
        "Silver": (temp["Medal"] == "Silver").sum(),
        "Bronze": (temp["Medal"] == "Bronze").sum(),
        "Total": temp["Medal"].notna().sum()}

def athlete_timeline(df, athlete):
    temp = df[df["Name"] == athlete]
    return (temp.groupby("Year").size().reset_index(name="Events"))

def athlete_medals(df, athlete):
    temp = df[(df["Name"] == athlete) & (df["Medal"].notna())]
    return (temp.groupby("Medal").size().reset_index(name="Count"))

def athlete_records(df, athlete):
    temp = df[df["Name"] == athlete]
    return temp[[
            "Year",
            "City",
            "Sport",
            "Event",
            "Team",
            "Age",
            "Medal"]
    ].sort_values("Year")

def sports_list(df):
    return sorted(df["Sport"].dropna().unique().tolist())

def sport_statistics(df, sport):
    temp = df[df["Sport"] == sport]
    return {
        "Olympics": temp["Year"].nunique(),
        "Countries": temp["region"].nunique(),
        "Athletes": temp["Name"].nunique(),
        "Events": temp["Event"].nunique(),
        "Medals": temp["Medal"].notna().sum()
    }

def sport_participation(df, sport):
    temp = df[df["Sport"] == sport]
    return (temp.groupby("Year")["Name"].nunique().reset_index(name="Athletes"))

def sport_top_countries(df, sport):
    temp = df[(df["Sport"] == sport) &(df["Medal"].notna())]
    return (temp.groupby("region").size().reset_index(name="Medals").sort_values("Medals", ascending=False).head(10))

def sport_top_athletes(df, sport):
    temp = df[(df["Sport"] == sport) & (df["Medal"].notna())]
    return (temp.groupby("Name").size().reset_index(name="Medals").sort_values("Medals", ascending=False).head(10))

def sport_medal_distribution(df, sport):
    temp = df[(df["Sport"] == sport) & (df["Medal"].notna())]
    return (temp.groupby("Medal").size().reset_index(name="Count"))