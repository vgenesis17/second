import streamlit as st
import plotly.express as px
import panda as pd
import os 
import warnings
warnings.filterwanings('ignore')
st.title('Super Store') 
st.text_input('Search')

st.set_page_config(page_title="Superstore!",page_icon=":bar_chart:",layout="wide")


