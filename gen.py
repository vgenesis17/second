import streamlit as st
import plotly.express as px
import pandas as pd
import os 
import warnings
warnings.filter("ignore")

st.title(':bar_chart: Super Store') 
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

fl = st.file_uploader(":file_folder: Upload a file", type=(["csv","txt","xlsx","xls"]))

# Assuming you have a DataFrame named df
col1, col2 = st.columns(2)

# Check if the DataFrame has an "Order Date" column
if "Order Date" in df.columns:
    df["Order_Date"] = pd.to_datetime(df["Order Date"])
    
    # Getting the min and max date in the "Order_Date" column
    startDate = df["Order_Date"].min()
    endDate = df["Order_Date"].max()
    
    # Display the min and max dates
    col1.write(f"Start Date: {startDate}")
    col2.write(f"End Date: {endDate}")
else:
    st.write("The 'Order Date' column does not exist in the DataFrame.")
