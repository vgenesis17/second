import streamlit as st
st.title(':bar_chart: Super Store') 
st.text_input('Search')

fl = st.file_uploader(":file_folder: Upload a file",type(["csv","txt","xlsx","xls"])
if fl is not None:
     filename=fl.name
     st.write(filename)
     df=pd.read_csv(filename, encoding = "ISO-8859-1")
else:
    df = pd.read_csv("Superstore.csv", encoding = "ISO-8859-1")



