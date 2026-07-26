import streamlit as st
from modules.data_loader import load_data
from modules.analytics import (medal_tally,year_list,country_list)
from modules.layout import (load_css,sidebar)
from modules.ui import (page_title)
st.set_page_config(page_title="Medal Tally",layout="wide")
load_css()
sidebar()

df = load_data()
page_title("Medal Tally","Explore medal standings by year and country.")

left, right = st.columns(2)
with left:
    year = st.selectbox("Select Year",year_list(df))

with right:
    country = st.selectbox("Select Country",country_list(df))

table = medal_tally(df,year,country)
csv = table.to_csv(index=False).encode("utf-8")
st.download_button(label="Download Medal Tally",data=csv,file_name="medal_tally.csv",mime="text/csv")
st.dataframe(table,use_container_width=True,hide_index=True)