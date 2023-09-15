import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title for your Streamlit app
st.title('Data Manipulation and Visualization with Streamlit')

# Upload a CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Check if a file is uploaded
if uploaded_file is not None:
    # Load the data into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the raw data
    st.subheader("Raw Data")
    st.write(df)

    # Data manipulation
    st.subheader("Data Manipulation")

    # Select columns for manipulation
    selected_columns = st.multiselect("Select Columns", df.columns)

    if selected_columns:
        # Filter the DataFrame based on selected columns
        filtered_df = df[selected_columns]

        # Display the filtered data
        st.write(filtered_df)

        # Calculate summary statistics
        st.subheader("Summary Statistics")
        st.write(filtered_df.describe())

        # Data visualization
        st.subheader("Data Visualization")

        # Choose a type of chart
        chart_type = st.selectbox("Select a Chart Type", ["Bar Chart", "Histogram"])

        if chart_type == "Bar Chart":
            # Group data by one of the selected columns and count occurrences
            group_column = st.selectbox("Select a Column for Grouping", selected_columns)
            if group_column:
                chart_data = filtered_df[group_column].value_counts()
                st.bar_chart(chart_data)

        elif chart_type == "Histogram":
            # Select a column for the histogram
            hist_column = st.selectbox("Select a Column for Histogram", selected_columns)
            if hist_column:
                st.set_option('deprecation.showPyplotGlobalUse', False)
                sns.histplot(filtered_df[hist_column], kde=True)
                plt.xlabel(hist_column)
                plt.ylabel("Frequency")
                st.pyplot()

# Add some explanation or instructions
st.markdown("### Instructions:")
st.markdown("- Upload a CSV file.")
st.markdown("- Select columns for manipulation.")
st.markdown("- Choose a chart type for visualization.")

# Footer
st.text("Sample Streamlit App for Data Manipulation and Visualization")

