"""
COMPARATIF D'EQUIPES PAGE LAYOUT
"""

from dash import dcc, html, register_page, dash_table, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
from utils.transform_data import get_lst_caracts, get_lst_postes, get_df_nba
import pandas as pd 

register_page(__name__, path='/teams')  # Define Teams Page route

lst_caracts = get_lst_caracts()
lst_postes = get_lst_postes()
df_nba = get_df_nba()

# Team Page Layout
layout = html.Div([
    html.H1("Comparatif par Equipes"),
    dbc.Container([
        dbc.Row([
            dbc.Col([ 
                dcc.Dropdown(lst_caracts, '', id='caracts-dropdown', placeholder="Caractéristiques"), 
            ], width=11),
            dcc.Graph(id="plot-caract"),
            dcc.Slider(id = 'slider_poste',
                      min = 0,
                      max = len(lst_postes),
                      marks={ i: poste for i, poste in enumerate(lst_postes)},
                      step = None)
        ], justify="between")
    ], style={'margin': 0 ,'width': '100%', 'max-width': '98%'} ),
])


# CB Dropdown Caracts
@callback(
    Output("plot-caract", "figure"), 
    [
        Input("caracts-dropdown", "value"),
        Input("slider_poste", "value")
    ]
)
def update_bar_chart(caract, poste):
    
    df_filtered = df_nba.copy()
    
    # Empty by default
    if caract == "":
        return px.bar()  
    print(poste)
    # Filter 1-6
    if poste :
        df_filtered = df_filtered[df_filtered['Poste'] == lst_postes[poste]]

    # Update bar plot
    df_filter = df_filtered.groupby('Equipe')[caract].sum().reset_index().head(5)
    df_filter = df_filter.sort_values(by=caract, ascending=False)
    fig = px.bar(df_filter, x="Equipe", y=caract, color="Equipe", barmode="group")
    
    return fig
