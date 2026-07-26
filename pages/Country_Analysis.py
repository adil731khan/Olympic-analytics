import streamlit as st
from modules.data_loader import load_data
from modules.analytics import (country_list_only,country_statistics,country_yearwise_medals,country_top_sports,country_top_athletes)
from modules.charts import (line_chart,horizontal_bar)
from modules.layout import (load_css,sidebar)
from modules.ui import (page_title,metric_card)

st.set_page_config(page_title="Country Analysis",layout="wide")
load_css()
sidebar()

df = load_data()
page_title("Country Analysis","Analyze Olympic performance of a selected country.")

countries = country_list_only(df)
country = st.selectbox("Select Country",countries,index=None,placeholder="Search country...")
if country is None:
    st.warning("Please select a country.")
    st.stop()
stats = country_statistics(df, country)

c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    metric_card("Olympics", stats["Olympics"])
with c2:
    metric_card("Athletes", stats["Athletes"])
with c3:
    metric_card("Sports", stats["Sports"])
with c4:
    metric_card("Events", stats["Events"])
with c5:
    metric_card("Medals", stats["Medals"])

st.markdown("## Medal Trend")
trend = country_yearwise_medals(df, country)
fig = line_chart(trend,"Year","Medals",f"{country} Medal Trend")
st.pyplot(fig)

left, right = st.columns(2)
with left:
    st.subheader("Top Sports")
    sports = country_top_sports(df, country)
    fig = horizontal_bar(sports,"Medals","Sport","Top Sports")
    st.pyplot(fig)

with right:
    st.subheader("Top Athletes")
    athletes = country_top_athletes(df, country)
    st.dataframe(athletes,use_container_width=True,hide_index=True,height=400)