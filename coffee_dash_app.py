# 📊 Coffee Sales Interactive Dashboard (Dash)
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
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

# ============================
# Start Dash App
# ============================
app = dash.Dash(__name__)
app.title = "Coffee Sales Dashboard"

# App Layout
app.layout = html.Div([
    html.H1("☕ Coffee Sales Dashboard", style={'textAlign': 'center'}),

    html.Div([
        html.Label("Select Coffee Type:"),
        dcc.Dropdown(
            id='coffee-dropdown',
            options=[{'label': coffee, 'value': coffee} for coffee in df['coffee_name'].unique()],
            value=df['coffee_name'].unique()[0]
        ),
    ], style={'width': '50%', 'margin': 'auto'}),

    dcc.Graph(id='sales-trend'),
    dcc.Graph(id='sales-by-hour'),
    dcc.Graph(id='payment-method-pie'),

    # ✅ Creator footer
    html.Div(
        "Created by Ambrose Henry",
        style={
            'textAlign': 'center',
            'marginTop': '50px',
            'color': '#888',
            'fontSize': '14px'
        }
    )
])

# Callbacks

@app.callback(
    Output('sales-trend', 'figure'),
    Input('coffee-dropdown', 'value')
)
def update_sales_trend(selected_coffee):
    filtered = df[df['coffee_name'] == selected_coffee]
    trend = filtered.groupby('date')['money'].sum().reset_index()
    fig = px.line(
        trend,
        x='date',
        y='money',
        title=f'Daily Sales Trend for {selected_coffee}',
        markers=True
    )
    return fig

@app.callback(
    Output('sales-by-hour', 'figure'),
    Input('coffee-dropdown', 'value')
)
def update_sales_by_hour(selected_coffee):
    filtered = df[df['coffee_name'] == selected_coffee]
    hourly = filtered.groupby('hour')['money'].sum().reset_index()
    fig = px.bar(
        hourly,
        x='hour',
        y='money',
        title=f'Sales by Hour for {selected_coffee}',
        labels={'hour': 'Hour of Day', 'money': 'Sales ($)'}
    )
    return fig

@app.callback(
    Output('payment-method-pie', 'figure'),
    Input('coffee-dropdown', 'value')
)
def update_payment_method(selected_coffee):
    filtered = df[df['coffee_name'] == selected_coffee]
    pie = filtered['cash_type'].value_counts().reset_index()
    pie.columns = ['cash_type', 'count']

    if pie.empty:
        pie = pd.DataFrame({
            'cash_type': ['No Data'],
            'count': [1]
        })

    fig = px.pie(
        pie,
        names='cash_type',
        values='count',
        title=f'Payment Method Split for {selected_coffee}'
    )
    return fig

# Run App
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8080, debug=True)

