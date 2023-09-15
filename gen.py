import streamlit as st
import pandas as pd
import plotly.express as px

# Load data from a CSV file (place your data in the 'data/' directory)
@st.cache  # Cache the loaded data to improve performance
def load_data():
    data = pd.read_csv("data/sample_data.csv")  # Adjust the file name as needed
    return data

# Create a Streamlit app
def main():
    st.title("Sample Streamlit Data Visualization")
    st.sidebar.header("Settings")

    # Load the data
    data = load_data()

    # Sidebar options for data manipulation
    st.sidebar.subheader("Data Manipulation")
    selected_column = st.sidebar.selectbox("Select a column:", data.columns)
    
    # Filter the data based on user selection
    filtered_data = data[data[selected_column] > st.sidebar.slider(f"Filter by {selected_column}", min_value=0, max_value=data[selected_column].max())]

    # Display the filtered data
    st.subheader("Filtered Data")
    st.write(filtered_data)

    # Data visualization
    st.subheader("Data Visualization")
    chart_type = st.selectbox("Select a chart type:", ["Bar Chart", "Scatter Plot"])
    
    if chart_type == "Bar Chart":
        st.write("### Bar Chart")
        fig = px.bar(data, x="Category", y="Sales", title="Sales by Category")
        st.plotly_chart(fig)

    elif chart_type == "Scatter Plot":
        st.write("### Scatter Plot")
        fig = px.scatter(data, x="Profit", y="Sales", color="Category", title="Profit vs. Sales")
        st.plotly_chart(fig)

if __name__ == "__main__":
    main()
