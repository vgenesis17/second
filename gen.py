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

if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_xlsx(filename)
else:
    os.chdir(r"C:\Users\genesis.villagracia\Downloads")
    df = pd.read_xlsx("Sample - Superstore.xlsx")


#Defines Columns  
col1,col2 = st.columns ((2))
df["Order_Date"] = pd.to_datetime(df["Order Date"])



#getting max and min date in this column
startDate = pd.to_datetime(df["Order Date"]).min()
endDate = pd.to_datetime(df["Order Date"]).max()
#DisplayToColumns

with col1:
     date1 = pd.to_datetime(st.date_input("Start Date", startDate))
with col2:
     date2 = pd.to_datetime(st.date_input("End Date", endDate))
    
df = df[(df["Order Date"] >= date1) & (df["Order Date"] <= date2)].copy()







