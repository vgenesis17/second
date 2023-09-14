import streamlit as st
import pandas as pd
import os 

st.title(':bar_chart: Super Store') 
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

fl = st.file_uploader(":file_folder: Upload a file", type=(["csv","txt","xlsx","xls"]))

#Defines Columns  
col1,col2 = st.columns ((2))
df["Order_Date"] = pd.to_datetime(df["Order Date"])
#getting max and min date in this column
StartDate = pd.to_datetime(df["Order Date"]).min()
EndDate = pd.to_datetime(df["Order Date"]).max()
#DisplayToColumns

with col1:
     date1 = pd.to_datetime(st.date_input("Start Date", StartDate))
with col2:
     date2 = pd.to_datetime(st.date_input("End Date", EndDate))
df = df[(df["Order Date"] >= date1) & (df["Order Date"] <= date2)
