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
        html.H1(children="covid latest updates",style={"text-align":"center"},),

        html.P(children="This is worldwide details of covid-19.Some country not updating there data, it make our graph blank",style={"text-align":"center"}),
    
        dcc.Dropdown(
        id='clientside-graph-country',
        style={"max-width":"50%"},
        options=[
            {'label': country, 'value': country}
            for country in available_countries
        ],
        value='World'
        ),
        dcc.Dropdown(
            id='type-select',
            style={"max-width":"50%"},
            options=[
                {'label':'Deaths','value':'total_deaths'},
                {'label':'Vaccinated','value':'total_vaccinations'},
                {'label':'Total Cases','value':'total_cases'},

            ],
            value='total_cases',
            placeholder="Select type",
        ),
        dcc.Graph(
        id='clientside-graph',
                ),


    ]
)


@app.callback (
    Output(component_id='clientside-graph',component_property='figure'),
    [Input(component_id='clientside-graph-country',component_property='value'),
    Input(component_id='type-select',component_property='value')],
)
def dun(op,typ):
    dff= df[df["location"]==op]
    fig=px.line(dff, x='date', y=typ, title="{}".format(typ).capitalize().replace("_"," ")+" report in {}".format(op))
    fig.update_layout(title_x=0.5, plot_bgcolor='#fff',paper_bgcolor='#fff', xaxis_title="Date", yaxis_title="{}".format(typ).capitalize().replace("_"," "))
    return fig