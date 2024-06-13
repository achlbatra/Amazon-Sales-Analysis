import streamlit as st
import matplotlib
matplotlib.use('Agg')  # Use Agg backend for non-interactive environments
import matplotlib.pyplot as plt
import pandas as pd

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

courier_status = st.sidebar.multiselect('Courier Status', options=['Shipped','Unshipped'], default=['Shipped','Unshipped'])

# Heading of the dashboard
st.markdown(" # ***Amazon Sales Analysis - Dashboard***")
st.write('Welcome to the Amazon Sales Analysis Dashboard! This interactive tool provides a comprehensive view of sales performance based on various metrics and categories. Explore trends over time, analyze category-wise performance, and gain insights into customer behavior with intuitive visualizations.\n')
st.markdown('##### Key Features:')
st.write('1. Sales Trends Over Time: Visualize the growth trajectory of our sales and identify seasonal patterns.\n',
        '2. Category Performance: Evaluate the performance of different product categories in terms of quantity sold and revenue generated.\n'
        '3. B2B Analysis: Understand the impact of business-to-business transactions on our overall sales.\n'
        '4. Geographical Insights: Explore sales data across states and cities to pinpoint regional trends and opportunities.\n\n'
        'Navigate through different sections to uncover actionable insights that drive business decisions and optimize our sales strategy.\n\n'
        "Let's dive into the data and unlock valuable insights to enhance our Amazon sales performance!")
# Filtered data based on user input
filtered = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]
if category:
    filtered = filtered[filtered['Category'].isin(category)]
if courier_status:
    filtered = filtered[filtered['Courier Status'].isin(['Shipped','Unshipped'])]

################################# Sales trend based on category ###############################################
st.header('Sales Trend Based on Category')
st.write('Explore the dynamic trends in our Amazon sales over time. This plot reveals the ebb and flow of sales quantities, highlighting peak periods and identifying trends that impact our revenue.')
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

st.markdown('#### Conclusions:\n')
st.write('Our sales exhibit consistent growth throughout the year, with notable peaks during promotional periods and the holiday season. Understanding these trends allows us to anticipate demand and optimize inventory management effectively.')

####################################### Category performance ########################################
st.header('Category Performance')
st.write("Delve into the performance of different product categories. This visualization showcases which categories drive the highest sales quantities and revenue, providing insights into our product portfolio's strengths and opportunities.")
category_per = filtered.groupby('Category').agg({'Qty':'sum', 'Amount':'sum'}).reset_index()

# Display bar chart for Quantity
st.subheader('Quantity Sold per Category')
st.bar_chart(category_per.set_index('Category')['Qty'])

# Display bar chart for Amount
st.subheader('Total Amount Sold per Category')
st.bar_chart(category_per.set_index('Category')['Amount'])

st.markdown('#### Conclusions:\n')
st.write("Categories ***Sets*** and ***Kurta*** leads in sales quantity, as well as higher revenue due to larger order values. Category ***Western Dresses*** shows promising growth potential, highlighting opportunities for expansion and product diversification.")

##################################### Sales performance based on state ###############################

#standardising state data
st.header('Sales distribution based on Amount')
st.write('Gain a geographical perspective on our sales distribution across states and cities. This plot identifies regional trends, helping us tailor marketing strategies and operational tactics to maximize sales in specific regions.')

state_mapping = {
    'ANDAMAN & NICOBAR': 'Andaman & Nicobar',
    'ANDHRA PRADESH': 'Andhra Pradesh',
    'APO': 'Andhra Pradesh',  # Assuming APO is an abbreviation for Andhra Pradesh
    'AR': 'Arunachal Pradesh',
    'ARUNACHAL PRADESH': 'Arunachal Pradesh',
    'ARUNACHAL PRADESH': 'Arunachal Pradesh',
    'ARUNACHAL PRADESH': 'Arunachal Pradesh',
    'ASSAM': 'Assam',
    'BIHAR': 'Bihar',
    'BIHAR': 'Bihar',
    'CHANDIGARH': 'Chandigarh',
    'CHHATTISGARH': 'Chhattisgarh',
    'CHANDIGARH': 'Chandigarh',
    'DADRA AND NAGAR': 'Dadra and Nagar Haveli',
    'DELHI': 'Delhi',
    'DELHI': 'Delhi',
    'GOA': 'Goa',
    'GOA': 'Goa',
    'GUJARAT': 'Gujarat',
    'HARYANA': 'Haryana',
    'HIMACHAL PRADESH': 'Himachal Pradesh',
    'JAMMU & KASHMIR': 'Jammu & Kashmir',
    'JHARKHAND': 'Jharkhand',
    'KARNATAKA': 'Karnataka',
    'KERALA': 'Kerala',
    'LADAKH': 'Ladakh',
    'LAKSHADWEEP': 'Lakshadweep',
    'MADHYA PRADESH': 'Madhya Pradesh',
    'MAHARASHTRA': 'Maharashtra',
    'MANIPUR': 'Manipur',
    'MEGHALAYA': 'Meghalaya',
    'MIZORAM': 'Mizoram',
    'NAGALAND': 'Nagaland',
    'NL': 'Nagaland',
    'NEW DELHI': 'Delhi',  # Assuming New Delhi is considered part of Delhi
    'ODISHA': 'Odisha',
    'ODISHA': 'Odisha',
    'ORISSA': 'Odisha',
    'PB': 'Punjab',
    'PUDUCHERRY': 'Puducherry',
    'PUNJAB': 'Punjab',
    'PONDICHERRY': 'Puducherry',
    'PUDUCHERRY': 'Puducherry',
    'PUNJAB': 'Punjab',
    'PUNJAB/MOHALI/ZIRAKPUR': 'Punjab',  # Assuming Mohali/Zirakpur are part of Punjab
    'RAJASTHAN': 'Rajasthan',
    'RJ': 'Rajasthan',
    'RAJASTHAN': 'Rajasthan',
    'RAJASTHAN': 'Rajasthan',
    'RAJASTHAN': 'Rajasthan',
    'SIKKIM': 'Sikkim',
    'SIKKIM': 'Sikkim',
    'TAMIL NADU': 'Tamil Nadu',
    'TELANGANA': 'Telangana',
    'TRIPURA': 'Tripura',
    'UTTAR PRADESH': 'Uttar Pradesh',
    'UTTARAKHAND': 'Uttarakhand',
    'WEST BENGAL': 'West Bengal',
    'BIHAR': 'Bihar',
    'DELHI': 'Delhi',
    'GOA': 'Goa',
    'ODISHA': 'Odisha',
    'PUNJAB': 'Punjab',
    'RAJASTHAN': 'Rajasthan',
    'RAJASTHAN': 'Rajasthan'
}

filtered['ship-state'] = filtered['ship-state'].str.strip().str.title().replace(state_mapping)

state_sales = filtered.groupby(['ship-state']).agg({'Amount': 'sum'}).reset_index()

# Sort by amount and select top 10 states
top_10_states_amt = state_sales.sort_values(by='Amount', ascending=False).head(10)

fig2, ax = plt.subplots()
ax.pie(top_10_states_amt['Amount'], labels = top_10_states_amt['ship-state'], autopct='%1.1f%%')
ax.set_title('Top 10 earning States')
ax.axis('equal')
st.pyplot(fig2)

st.markdown('#### Conclusions:\n')
st.write('Sales are concentrated in major urban centers, with opportunities for growth identified in emerging markets. Tailoring marketing strategies and distribution channels to regional preferences can enhance sales performance and market penetration.')
############################################### B2B distribution ########################################

st.header('B2B/B2C Analysis')
st.write('Analyze the impact of business-to-business (B2B) transactions on our sales ecosystem. This plot illuminates how B2B transactions contribute to our overall revenue, offering insights into our commercial relationships and customer segments.')

b2b_count = filtered[filtered['B2B']==True].shape[0]
b2c_count = filtered[filtered['B2B']==False].shape[0]

var = ['B2B', 'B2C']
cnt = [b2b_count, b2c_count]

fig3, ax = plt.subplots()
ax.bar(var,cnt)
st.pyplot(fig3)
st.markdown('#### Conclusions:\n')
st.write('Business-to-business (B2B) transactions play a significant role in our sales ecosystem, underscoring the importance of catering to corporate clients and understanding their purchasing behaviors.')

