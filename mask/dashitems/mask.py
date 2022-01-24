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

               
    ]
)

    html.Div([
    dcc.Upload(
        id='upload-image',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-image-upload'),
])
