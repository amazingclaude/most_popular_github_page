import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go

# Step 1. Launch the application
app = dash.Dash()

# Step 2. Import the dataset
df=pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

# Step 3. Create a plotly figure


# Step 4. Create a Dash layout
app.layout = html.Div([
                dcc.Graph(id = 'plot_id', figure = fig)
                      ])

# Step 5. Add callback functions


# Step 6. Add the server clause
if __name__ == '__main__':
    app.run_server(debug = True)