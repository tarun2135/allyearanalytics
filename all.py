import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objs as go

# Sample data
data = {
    'Academic Fees Paid': [75000, 90000, 65000, 35000, 25000, 90000, 65000, 25000, 90000, 35000,
                           25000, 75000, 35000, 25000, 25000, 25000, 35000, 75000, 90000, 35000,
                           25000, 25000, 35000, 75000, 35000, 65000, 25000, 35000, 25000, 35000,
                           75000, 65000, 25000, 25000, 65000, 75000, 25000, 35000, 25000, 65000,
                           25000, 90000, 75000, 90000, 35000, 25000, 65000, 25000, 25000, 90000,
                           75000],
    'Academic Due Fees': [50000, 35000, 60000, 90000, 100000, 35000, 60000, 100000, 35000, 90000,
                          100000, 50000, 90000, 100000, 100000, 100000, 90000, 50000, 35000, 90000,
                          100000, 100000, 90000, 50000, 90000, 60000, 100000, 90000, 100000, 90000,
                          50000, 60000, 100000, 100000, 60000, 50000, 100000, 90000, 100000, 60000,
                          100000, 35000, 50000, 35000, 90000, 100000, 60000, 100000, 100000, 35000,
                          50000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Center align the subheader text with smaller font size
st.markdown("<h2 style='text-align: center; font-size: 24px;'>Academic Fees Paid vs Academic Due Fees</h2>", unsafe_allow_html=True)

labels = [f"Student {i+1}" for i in range(len(df))]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, df['Academic Fees Paid'], width, label='Academic Fees Paid', color='blue')
rects2 = ax.bar(x + width/2, df['Academic Due Fees'], width, label='Academic Due Fees', color='green')

ax.set_xlabel('Students')
ax.set_ylabel('Fees')
ax.set_title('Academic Fees Comparison')
ax.set_xticks([])  # Remove x-axis tick labels
ax.legend()

# Display bar chart
st.pyplot(fig)

# Read the CSV file into a DataFrame
csv_file = r"C:\Users\lenovo\Desktop\ALLData.csv"
df = pd.read_csv(csv_file)

# Dropdown filter for branch
branch_filter = st.selectbox('Select Branch', ['CSE', 'ECE'])

# Filter DataFrame based on selected branch
filtered_df = df[df['Branch'] == branch_filter]

# Calculate total counts for each category
academic_paid_count = filtered_df['Academic Fees Paid'].notna().sum()
transportation_paid_count = filtered_df['Transportation Fees Paid'].notna().sum()
hostel_paid_count = filtered_df['Hostel Fees Paid'].notna().sum()

# Create labels and values for the pie chart
labels = ['Academic', 'Transportation', 'Hostel']
values = [academic_paid_count, transportation_paid_count, hostel_paid_count]

# Create pie chart
st.markdown("<h3 style='text-align: center; font-size: 20px;'>Overall Fees Paid In CSE,ECE Departments</h3>", unsafe_allow_html=True)
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

# Center align the graph
st.write(fig, width=600, height=400, use_container_width=True)
