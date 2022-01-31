import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc
import dash
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']




app = DjangoDash('mask',external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div(

    children=[
        html.H3(children="Did you weared mask???",style={"text-align":"center"},),

        html.Br(),

        html.H6(children="This is just demonstration of app using mask model",style={"text-align":"center"}),

        html.Br(),
        
        html.H6(children="please upload your picture",style={"text-align":"center"}),

        html.Br(),

               
    ],
),
