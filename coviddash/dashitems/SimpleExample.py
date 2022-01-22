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

app = DjangoDash('SimpleExample')   # replaces dash.Dash

app.layout = html.Div([
    dcc.RadioItems(
        id='dropdown-color',
        options=[{'label': c, 'value': c.lower()} for c in ['Red', 'Green', 'Blue']],
        value='red'
    ),
    html.Div(id='output-color'),
    dcc.RadioItems(
        id='dropdown-size',
        options=[{'label': i,
                  'value': j} for i, j in [('L','large'), ('M','medium'), ('S','small')]],
        value='medium'
    ),
    html.Div(id='output-size')

])

@app.callback(
    dash.dependencies.Output('output-color', 'children'),
    [dash.dependencies.Input('dropdown-color', 'value')])
def callback_color(dropdown_value):
    return "The selected color is %s." % dropdown_value

@app.callback(
    dash.dependencies.Output('output-size', 'children'),
    [dash.dependencies.Input('dropdown-color', 'value'),
     dash.dependencies.Input('dropdown-size', 'value')])
def callback_size(dropdown_color, dropdown_size):
    return "The chosen T-shirt is a %s %s one." %(dropdown_size,
                                                  dropdown_color)



########################################################


df = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv", usecols = ['iso_code', 'continent', 'location', 'date', 'total_cases', 'new_cases','total_deaths', 'new_deaths','total_vaccinations','people_vaccinated', 'people_fully_vaccinated'])
df["date"] = pd.to_datetime(df["date"])
df.sort_values('date',inplace=True)
# df['total_cases'] = int(df['total_cases'])

def get_country_list():
    return df.location.unique()

def getdropdown(countrylst):
    dropdownlist = []
    for i in sorted(countrylst):
        tmp_dict = {'label':i,'value':i}
        dropdownlist.append(tmp_dict)
    return dropdownlist


app = DjangoDash('SimpleExample1') 


app.layout = html.Div(

    children=[
        html.H1(children="covid latest updates",),

        html.P(children="this is worldwide details of covid-19.from this you can generate variius details",),

        dcc.Dropdown(
            id='drop-down',
            options=getdropdown(get_country_list()),
            value='India'
        ),

        dcc.Graph(

            figure={
                "data": [
                    {
                        "x": df["date"],
                        "y": df["total_cases"],
                        "type":"lines",

                    },
                ],
                "layout": {"title":"Covid details"},
            },
        ),
    ]
)


