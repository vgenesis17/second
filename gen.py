import streamlit as st
import plotly.express as px
import pandas as pd
import os
st.title(':bar_chart: Super Store') 
st.text_input('Search')

fl = st.file_uploader(":file_folder: Upload a file",type(["csv","txt","xlsx","xls"])
if fl is not None:
     filename=fl.name
     st.write(filename)
     df=pd.read_csv(filename, encoding = "ISO-8859-1")
else:
     os.chdir(r"C:\Users\genesis.villagracia\Downloads")
    df = pd.read_xlsx("Sample - Superstore.xlsx", encoding = "ISO-8859-1")



