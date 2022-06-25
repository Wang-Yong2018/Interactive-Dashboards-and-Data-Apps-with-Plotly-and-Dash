# this is dash learning scrip of interfactive with pandas data

import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
from pathlib import Path
from  functools import lru_cache
from timeit import timeit

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


@lru_cache()
def get_poverty_data_fast():
	data_path = Path('data/PovStatsData.csv')
	# csv_name = data_path.glob('*poverty.csv')
	df = pd.read_csv(data_path)
	
	return df
poverty_data = get_poverty_data_fast()

@app.callback(Output('report', 'children'),
			Input('country', 'value'))
def display_country_report(country):
	if country is None:
		return ''
	filtered_df = poverty_data[(poverty_data['Country Name'] == country) &
							(poverty_data['Indicator Name']=='Population, total')]
	population= filtered_df.loc[:, '2010'].values[0]
	return [html.H3(country), f'The population of {country} in 2010 was {population:,.0f}.']


app.layout = html.Div(children=[
    html.H1('Poverty And Equity Database',
            style={'color': 'blue',
                   'fontSize': '40px'}),
    html.H2('The World Bank'),
    html.P("Key Facts:"),
    dbc.Tabs([
        dbc.Tab([
            html.Ul([
                html.Br(),
                html.Li("Number of Economies: 170"),
                html.Li("Temporal Coverage: 1974 - 2019"),
                html.Li('Last Update: March 18, 2020'),
                html.Li([
                    'Source: ',
                    html.A('https://datacatalog.worldbank.org/dataset/poverty-and-Equity',
                           href='https://datacatalog.worldbank.org/dataset/poverty-and-equity-database'),
                ]),


            ]),
        ], label='Key Facts'),
        dbc.Tab([
            html.Ul([
                html.Br(),
                html.Br(),
                html.Li(
                    "Book title: Interfactive Dashboards and Data Apps with plotly Dash"),
                html.Li(['GitHub repo: ',
                         html.A('https://github.com/PacktPublishing/Interactive-Dashboard',
                                href='https://github.com/PackPublishing/Interactive-Dashboarding'),
                         ])
            ])
        ], label='Project Info'),
        dbc.Tab([
            html.Ul([
                html.Div([dcc.Dropdown(id='country',
                options=[{'label': country, 'value': country}
                    for country in poverty_data['Country Name'].unique()]
                         ),
                html.Div(id='report')
                ])
            ]),
            ], label='Poverty_data'),
])
])


if __name__ == '__main__':
    app.run_server(debug=True)
