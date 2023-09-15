import streamlit as st
import pandas as pd
import os 
import warnings

# Ignore warnings
warnings.filterwarnings("ignore")

st.title(':bar_chart: Super Store') 
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

# File upload
fl = st.file_uploader(":file_folder: Upload a file", type=(["csv","txt","xlsx","xls"]))


