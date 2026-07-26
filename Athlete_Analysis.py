import streamlit as st
from modules.data_loader import load_data
from modules.analytics import (athlete_list,athlete_statistics,athlete_timeline,athlete_medals,athlete_records)
from modules.charts import (line_chart,pie_chart)
from modules.layout import (load_css,sidebar)
from modules.ui import (page_title,metric_card)
st.set_page_config(page_title="Athlete Analysis",layout="wide")
load_css()
sidebar()
df = load_data()
page_title("Athlete Analysis","Explore Olympic careers of athletes.")
country = st.selectbox("Country",sorted(df["region"].dropna().unique()))
athletes = sorted(df[df["region"] == country]["Name"].dropna().unique())
athlete = st.selectbox("Athlete",athletes)

if athlete is None:
    st.warning("Please select an athlete.")
    st.stop()

stats = athlete_statistics(df, athlete)
c1, c2, c3 = st.columns(3)
with c1:
    metric_card("Olympics", stats["Olympics"])
with c2:
    metric_card("Sports", stats["Sports"])
with c3:
    metric_card("Events", stats["Events"])
c4, c5, c6, c7 = st.columns(4)
with c4:
    metric_card("Gold", stats["Gold"], "#F59E0B")
with c5:
    metric_card("Silver", stats["Silver"], "#94A3B8")
with c6:
    metric_card("Bronze", stats["Bronze"], "#B45309")
with c7:
    metric_card("Total", stats["Total"], "#2563EB")
left, right = st.columns(2)
with left:
    st.subheader("Career Timeline")
    trend = athlete_timeline(df, athlete)
    fig = line_chart(trend,"Year","Events","Participation Trend")
    st.pyplot(fig)
with right:
    st.subheader("Medal Distribution")
    medals = athlete_medals(df, athlete)
    if len(medals):
        fig = pie_chart(medals,"Medal","Count","Medal Distribution")
        st.pyplot(fig)
    else:
        st.info("No medals available.")

st.subheader("Career Records")
records = athlete_records(df, athlete)
st.dataframe(records,use_container_width=True,hide_index=True,height=450)
