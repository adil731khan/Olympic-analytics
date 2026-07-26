import streamlit as st
from modules.data_loader import load_data
from modules.analytics import (sports_list,sport_participation,sport_statistics,sport_top_countries,sport_top_athletes,sport_medal_distribution)
from modules.charts import (line_chart,horizontal_bar,pie_chart)
from modules.layout import (load_css,sidebar)
from modules.ui import (page_title,metric_card)
st.set_page_config(page_title="Sports Analysis",layout="wide")
load_css()
sidebar()

df = load_data()
page_title("Sports Analysis","Explore Olympic statistics by sport.")
sport = st.selectbox("Select Sport",sports_list(df),index=None,placeholder="Search sport...")
if sport is None:
    st.warning("Please select a sport.")
    st.stop()
stats = sport_statistics(df, sport)
c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    metric_card("Olympics", stats["Olympics"])
with c2:
    metric_card("Countries", stats["Countries"])
with c3:
    metric_card("Athletes", stats["Athletes"])
with c4:
    metric_card("Events", stats["Events"])
with c5:
    metric_card("Medals", stats["Medals"])
left, right = st.columns(2)
with left:
    st.subheader("Participation Trend")
    trend = sport_participation(df, sport)
    fig = line_chart(trend,"Year","Athletes","Athlete Participation")
    st.pyplot(fig)
with right:
    st.subheader("Medal Distribution")
    medals = sport_medal_distribution(df, sport)
    fig = pie_chart(medals,"Medal","Count","Medal Distribution")
    st.pyplot(fig)
st.divider()
left, right = st.columns(2)
with left:
    st.subheader("Top Countries")
    countries = sport_top_countries(df, sport)
    fig = horizontal_bar(countries,"Medals","region","Top Countries")
    st.pyplot(fig)
with right:
    st.subheader("Top Athletes")
    athletes = sport_top_athletes(df, sport)
    st.dataframe(athletes,use_container_width=True,hide_index=True,height=400)