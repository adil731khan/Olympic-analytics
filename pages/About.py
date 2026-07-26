import streamlit as st
from modules.layout import (load_css,sidebar)
from modules.ui import (page_title)
st.set_page_config(page_title="About",layout="wide")
load_css()
sidebar()
page_title("About This Project","Olympic Analytics Dashboard")
st.markdown("""
## Project Overview

This project is an interactive dashboard for analyzing Olympic Games data.

### Features

- Medal Tally
- Country Analysis
- Athlete Analysis
- Sports Analysis

### Technologies Used

- Python
- Streamlit
- Pandas
- Matplotlib
- NumPy

### Dataset

- athlete_events.csv
- noc_regions.csv
""")