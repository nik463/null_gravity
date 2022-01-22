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



df = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv", usecols = ['iso_code', 'continent', 'location', 'date', 'total_cases', 'new_cases','total_deaths', 'new_deaths','total_vaccinations','people_vaccinated', 'people_fully_vaccinated'])
df["date"] = pd.to_datetime(df["date"])
available_countries = df['location'].unique()

app = DjangoDash('SimpleExample1') 


app.layout = html.Div(

    children=[
        html.H1(children="covid latest updates",),

        html.P(children="this is worldwide details of covid-19.from this you can generate variius details",),

        dcc.Dropdown(
        id='clientside-graph-country',
        options=[
            {'label': country, 'value': country}
            for country in available_countries
        ],
        value='Canada'
        ),
        dcc.Graph(
        id='clientside-graph',
    ),


    ]
)


@app.callback (
    Output(component_id='clientside-graph',component_property='figure'),
    Input(component_id='clientside-graph-country',component_property='value'),
)
def dun(op):
    dff= df[df["location"]==op]
    fig=px.line(dff, x='date', y=["total_cases","total_deaths"], title="Total Case Of {}".format(op))
    fig.update_layout(title_x=0.5, plot_bgcolor='#F2DFCE',paper_bgcolor='#fff', xaxis_title="Date")
    return fig