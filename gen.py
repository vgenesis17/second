import streamlit as st
import mymodel as m
st.write("""#First App *world!*""")
window = st.slider("Forcast Prediction (days)")
st.write(m.run(window=window))

