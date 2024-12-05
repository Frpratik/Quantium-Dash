import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd
 
# Read the sales data
df = pd.read_csv('output/soul_food_sales.csv')
 
# Ensure the 'date' field is in datetime format
df['date'] = pd.to_datetime(df['date'])
 
# Sort the data by date
df = df.sort_values('date')
 
# Create the Dash app
app = dash.Dash(__name__)
 
# Define the layout of the app
app.layout = html.Div([
    # Header
    html.H1("Soul Foods Pink Morsel Sales Visualizer"),
    
    # Line chart to visualize sales over time
    dcc.Graph(
        id='sales-line-chart',
        figure={
            'data': [
                go.Scatter(
                    x=df['date'],
                    y=df['sales'],
                    mode='lines',
                    name='Sales'
                )
            ],
            'layout': go.Layout(
                title='Sales of Pink Morsels Over Time',
                xaxis={'title': 'Date'},
                yaxis={'title': 'Sales ($)'},
                hovermode='closest'
            )
        }
    )
])
 
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)