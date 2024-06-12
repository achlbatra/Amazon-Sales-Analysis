import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
@st.cache_data
def load_data():
    df = pd.read_csv('Amazon Sale Report.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# Creating the sidebar for filters
st.sidebar.header('Filters')

start_date = st.sidebar.date_input('Start date', min_value=df['Date'].min(), max_value=df['Date'].max())
end_date = st.sidebar.date_input('End date', min_value=start_date, max_value=df['Date'].max())

category = st.sidebar.multiselect('Categories', options=df['Category'].unique(), default=df['Category'].unique())

courier_status = st.sidebar.multiselect('Courier Status', options=df['Courier Status'].dropna().unique(), default=df['Courier Status'].dropna().unique())

# Heading of the dashboard
st.markdown(" # ***Amazon Sales Analysis - Dashboard***")

# Filtered data based on user input
filtered = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]
if category:
    filtered = filtered[filtered['Category'].isin(category)]
if courier_status:
    filtered = filtered[filtered['Courier Status'].isin(courier_status)]

################################# Sales trend based on category ###############################################
st.header('Sales Trend Based on Category')

# Grouping based on date and category
sales_trend = filtered.groupby(['Date', 'Category']).agg({'Qty': 'sum', 'Amount': 'sum'}).reset_index()

# Initializes a Matplotlib figure and axes object for plotting
fig, ax = plt.subplots()

for ctg in category:
    data = sales_trend[sales_trend['Category'] == ctg]
    ax.plot(data['Date'], data['Qty'], label=ctg)

# Rotate the x-axis labels for better readability
plt.xticks(rotation=90)

ax.set_xlabel('Date')
ax.set_ylabel('Quantity Sold')

# Position the legend outside the plot
ax.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout to make space for the legend
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(fig)

####################################### Category performance ########################################
st.header('Category Performance')

category_per = filtered.groupby('Category').agg({'Qty':'sum', 'Amount':'sum'}).reset_index()

# Display bar chart for Quantity
st.subheader('Quantity Sold per Category')
st.bar_chart(category_per.set_index('Category')['Qty'])

# Display bar chart for Amount
st.subheader('Total Amount Sold per Category')
st.bar_chart(category_per.set_index('Category')['Amount'])

