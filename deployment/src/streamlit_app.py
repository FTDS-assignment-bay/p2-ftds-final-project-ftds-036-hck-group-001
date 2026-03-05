import streamlit as st

st.set_page_config(
    page_title="DemandSense AI",
    layout="wide"
)

import eda
import prediction

page = st.sidebar.selectbox(
    "Choose page",
    ("EDA", "Prediction")
)

if page == "EDA":
    eda.run()
else:
    prediction.run()