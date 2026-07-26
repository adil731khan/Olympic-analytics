import streamlit as st
from pathlib import Path

def load_css():
    css_path = Path("assets/style.css")
    if css_path.exists():
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

def sidebar():
    st.sidebar.title("Olympic Analytics")
    st.sidebar.markdown("---")
    st.sidebar.write("Interactive dashboard for Olympic Games analysis.")
    st.sidebar.markdown("---")
    st.sidebar.info(
        """
Dataset

1896–2016 Olympic Games
        """)