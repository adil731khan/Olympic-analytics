import streamlit as st

def metric_card(title, value, color="#2563EB"):
    st.markdown(
        f"""
        <div style="
            background:white;
            padding:18px;
            border-radius:12px;
            border-left:6px solid {color};
            box-shadow:0 2px 8px rgba(0,0,0,.08);
            text-align:center;
            margin-bottom:15px">
            <h4 style="margin:0;color:#64748B;">{title}</h4>
            <h2 style="margin-top:10px;color:{color};">{value}</h2>
        </div>
        """,unsafe_allow_html=True)

def page_title(title, subtitle):
    st.markdown(
        f"""
        <div style="
            background:#2563EB;
            padding:20px;
            border-radius:12px;
            color:white;
            margin-bottom:25px">
            <h1 style="margin:0;">{title}</h1>
            <p style="margin-top:8px;">{subtitle}</p>
        </div>
        """,unsafe_allow_html=True)
