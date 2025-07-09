# 📊 Coffee Sales Interactive Dashboard (Streamlit)
import streamlit as st
import pandas as pd
import plotly.express as px

# ============================
# Load & preprocess data
# ============================
df = pd.read_csv('index.csv')
df['date'] = pd.to_datetime(df['date'])
df['datetime'] = pd.to_datetime(df['datetime'])
df['hour'] = df['datetime'].dt.hour
df['day_of_week'] = df['datetime'].dt.day_name()
df['card'] = df['card'].fillna('CASH')

st.title("☕ Coffee Sales Dashboard")
st.markdown("Created by Ambrose Henry")

# ============================
# Coffee Selection
# ============================
coffee_types = df['coffee_name'].unique()
selected_coffee = st.selectbox("Select Coffee Type:", coffee_types)

filtered = df[df['coffee_name'] == selected_coffee]

# ============================
# Daily Sales Trend
# ============================
trend = filtered.groupby('date')['money'].sum().reset_index()
fig_trend = px.line(
    trend,
    x='date',
    y='money',
    title=f'Daily Sales Trend for {selected_coffee}',
    markers=True
)
st.plotly_chart(fig_trend, use_container_width=True)

# ============================
# Sales by Hour
# ============================
hourly = filtered.groupby('hour')['money'].sum().reset_index()
fig_hour = px.bar(
    hourly,
    x='hour',
    y='money',
    title=f'Sales by Hour for {selected_coffee}',
    labels={'hour': 'Hour of Day', 'money': 'Sales ($)'}
)
st.plotly_chart(fig_hour, use_container_width=True)

# ============================
# Payment Method Pie
# ============================
pie = filtered['cash_type'].value_counts().reset_index()
pie.columns = ['cash_type', 'count']
if pie.empty:
    pie = pd.DataFrame({'cash_type': ['No Data'], 'count': [1]})
fig_pie = px.pie(
    pie,
    names='cash_type',
    values='count',
    title=f'Payment Method Split for {selected_coffee}'
)
st.plotly_chart(fig_pie, use_container_width=True)
