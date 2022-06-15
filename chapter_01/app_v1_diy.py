import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.DARKLY]
                )

app.layout = html.Div([
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
                ])

            ]),
        ], label='Key Facts'),
        dbc.Tab([
            html.Ul([
                html.Br(),
                html.Li(
                    "Book title: Interfactive Dashboards and Data Apps with plotly Dash"),
                html.Li(['GitHub repo: ',
                         html.A('https://github.com/PacktPublishing/Interactive-Dashboard',
                                href='https://github.com/PackPublishing/Interactive-Dashboarding'),
                         ])
            ])
        ], label='Project Info')
    ])

])

if __name__ == '__main__':
    app.run_server(debug=True)
