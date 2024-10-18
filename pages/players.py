"""
COMPARATIF DE JOUEURS PAGE LAYOUT
"""

from dash import dcc, html, register_page, dash_table, callback, Output, Input
import plotly.express as px
from utils.transform_data import get_rookies_seniors, get_df_nba
import pandas as pd 
import dash_bootstrap_components as dbc 

df_nba = get_df_nba()

register_page(__name__, path='/players')  # Define players route

df_rookies, df_seniors = get_rookies_seniors()


# PLAYERS LAYOUT
layout = html.Div([
    html.H1("Comparatif par joueurs"),
    dbc.Container([
        dbc.Row([
            dbc.Col([ 
                dcc.Dropdown(df_rookies["Joueur"], '', id='rookie-dropdown', placeholder="Rookies", multi=True),
                dash_table.DataTable(
                    pd.DataFrame().to_dict('records'), 
                    [{"name": i, "id": i} for i in df_rookies.columns],
                    id="table-rookies",
                    style_table={'overflowY': 'auto'},
                    style_header={'fontSize': '10px' }
                )
            ], width=6),
            dbc.Col([
                dcc.Dropdown(df_seniors["Joueur"], '', id='senior-dropdown', placeholder="Seniors", multi=True),
                dash_table.DataTable(
                    pd.DataFrame().to_dict('records'), 
                    [{"name": i, "id": i} for i in df_seniors.columns],
                    id="table-seniors",
                    style_table={'overflowY': 'auto', },
                     style_header={'fontSize': '10px' }
                ),
            ], width=6),        
        ], justify="between")
    ], style={'margin': 0 ,'width': '100%', 'max-width': '98%'} ),
])


# CB Dropdown rookies
@callback(
    Output('table-rookies', 'data'),
    Input('rookie-dropdown', 'value')
)
def update_output_table_rookies(rookie_names):
    df = []
    if rookie_names:
        rookies = df_rookies[df_rookies["Joueur"].isin(rookie_names)]
        df.append(rookies)
    if df:
        df_filter = pd.concat(df)
    else:
        df_filter = pd.DataFrame()
    return df_filter.to_dict('records')


# CB Dropdown senior
@callback(
    Output('table-seniors', 'data'),
    Input('senior-dropdown', 'value')
)
def update_output_table_senior(senior_names):
    df = []
    if senior_names:
        seniors = df_seniors[df_seniors["Joueur"].isin(senior_names)]
        df.append(seniors)
        
    if df:
        df_filter = pd.concat(df)
    else:
        df_filter = pd.DataFrame()

    return df_filter.to_dict('records')
