import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc
# import dash
import pandas as pd
import plotly.express as px

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



df = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv", usecols = ['iso_code', 'continent', 'location', 'date', 'total_cases', 'new_cases','total_deaths', 'new_deaths','total_vaccinations','people_vaccinated', 'people_fully_vaccinated'])
df["date"] = pd.to_datetime(df["date"])
available_countries = df['location'].unique()


card_content0 = [
    dbc.CardHeader("Toatal Cases"),
    dbc.CardBody(
        [
            html.H5(id="tccard", children=[]),
            html.P(
                "Peoples are affected",
                className="card-text",
            ),
        ]
    ),
]

card_content = [
    dbc.CardHeader("Vaccinated"),
    dbc.CardBody(
        [
            html.H5(id='vaccinecard',children=[]),
            html.P(
                "Peoples are vaccinated",
                className="card-text",
            ),
        ]
    ),
]

card_content1 = [
    dbc.CardHeader("Deaths"),
    dbc.CardBody(
        [
            html.H5(id='deathcard',children=[]),
            html.P(
                "Peoples are died",
                className="card-text",
            ),
        ]
    ),
]


app = DjangoDash('coviddash',external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div(

    children=[
        html.H1(children="Covid-19 Latest Updates",style={"text-align":"center"},),

        html.P(children="This is worldwide details of covid-19.Some country not updating there data, it make our graph blank",style={"text-align":"center"}),

        html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card(card_content, color="success", inverse=True)),
                dbc.Col(dbc.Card(card_content0, color="warning", inverse=True)),
                dbc.Col(dbc.Card(card_content1, color="danger", inverse=True)),
            ],
            className="mb-4",
        ),
         ]
),
    html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.Div(
        dcc.Dropdown(
        id='clientside-graph-country',
        options=[
            {'label': country, 'value': country}
            for country in available_countries
        ],
        value='World'
        ),
        )),
         dbc.Col(html.Div(
        dcc.Dropdown(
            id='type-select',
            style={"max-widht":"100%"},
            options=[
                {'label':'Deaths','value':'total_deaths'},
                {'label':'Vaccinated','value':'total_vaccinations'},
                {'label':'Total Cases','value':'total_cases'},

            ],
            value='total_cases',
            placeholder="Select type",
        ),
        )),
     ]
        ),
    ]
),
        dcc.Graph(
        id='clientside-graph',
                ),
        html.P(children="This project is completly made in html css and plotly dash",style={"text-align":"center"}),
        
    ]
)


@app.callback (
    [Output(component_id='deathcard',component_property='children'),
    Output('vaccinecard','children'),
    Output('tccard','children'),
    Output(component_id='clientside-graph',component_property='figure')],
    [Input(component_id='clientside-graph-country',component_property='value'),
    Input(component_id='type-select',component_property='value')],
)
def dun(op,typ):
    dff= df[df["location"]==op]
    dvalue=int(dff["total_deaths"].iloc[-2])
    vvalue=int(dff["total_vaccinations"].iloc[-2])
    tvalue=int(dff["total_cases"].iloc[-2])
    fig=px.line(dff, x='date', y=typ, title="{}".format(typ).capitalize().replace("_"," ")+" report in {}".format(op),height=600)
    fig.update_layout(title_x=0.5, plot_bgcolor='#fff',paper_bgcolor='#fff', xaxis_title="Date", yaxis_title="{}".format(typ).capitalize().replace("_"," "))
    return dvalue,vvalue,tvalue,fig

