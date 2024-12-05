import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output
 
# Read the sales data
df = pd.read_csv('output/soul_food_sales.csv')
 
# Ensure the 'date' field is in datetime format
df['date'] = pd.to_datetime(df['date'])
 
# Create the Dash app
app = dash.Dash(__name__)
 
# Define the layout of the app
app.layout = html.Div(
    style={
        'font-family': 'Arial, sans-serif',
        'background-color': '#f4f4f9',
        'padding': '20px',
        'color': '#333'
    },
    children=[
        # Header
        html.H1(
            "Soul Foods Pink Morsel Sales Visualizer",
            style={
                'text-align': 'center',
                'color': '#4CAF50',
                'margin-bottom': '40px'
            }
        ),
        
        # Radio button for region selection
        html.Div(
            children=[
                html.Label(
                    "Select Region:",
                    style={
                        'font-size': '18px',
                        'font-weight': 'bold',
                        'margin-bottom': '10px'
                    }
                ),
                dcc.RadioItems(
                    id='region-selector',
                    options=[
                        {'label': 'North', 'value': 'north'},
                        {'label': 'East', 'value': 'east'},
                        {'label': 'South', 'value': 'south'},
                        {'label': 'West', 'value': 'west'},
                        {'label': 'All', 'value': 'all'}
                    ],
                    value='all',
                    labelStyle={'display': 'block', 'margin': '5px 0'},
                    style={'padding': '10px', 'font-size': '16px'}
                ),
            ],
            style={
                'margin-bottom': '30px',
                'text-align': 'center',
            }
        ),
        
        # Line chart to visualize sales over time
        dcc.Graph(
            id='sales-line-chart',
            style={
                'border': '2px solid #ddd',
                'border-radius': '10px',
                'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.1)',
            }
        ),
    ]
)
 
# Define the callback to update the line chart based on the selected region
@app.callback(
    Output('sales-line-chart', 'figure'),
    [Input('region-selector', 'value')]
)
def update_line_chart(selected_region):
    # Filter the data based on the selected region
    if selected_region != 'all':
        filtered_df = df[df['region'] == selected_region]
    else:
        filtered_df = df
 
    # Sort the filtered data by date
    filtered_df = filtered_df.sort_values('date')
 
    # Create the figure
    figure = {
        'data': [
            go.Scatter(
                x=filtered_df['date'],
                y=filtered_df['sales'],
                mode='lines',
                name='Sales'
            )
        ],
        'layout': go.Layout(
            title=f'Sales of Pink Morsels in {selected_region.capitalize()} Region' if selected_region != 'all' else 'Sales of Pink Morsels Across All Regions',
            xaxis={'title': 'Date'},
            yaxis={'title': 'Sales ($)'},
            hovermode='closest',
            plot_bgcolor='#f4f4f9',
            paper_bgcolor='#ffffff',
        )
    }
 
    return figure
 
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)