"""
HOME PAGE LAYOUT
"""
from dash import html, register_page
import dash_bootstrap_components as dbc 
register_page(__name__, path='/')  # Register Home Page route

# Home Page Layout
layout = html.Div([
            dbc.Container([
                html.H1("Bienvenue!"),
                html.P('Ici, on aime les metrics et surtout la NBA de 2013!'),
                
                dbc.Row([
                    dbc.Col([ 
                        dbc.Card(
                            dbc.CardBody([
                                html.H4("Comparatif des joueurs", className="card-title"),
                                html.H6("Saison 2013-2014", className="card-subtitle"),
                                html.P(
                                    "Tableaux récapitulatif entre rookies et seniors",
                                     className="card-text",
                                ),
                                dbc.CardLink("Voir", href="/players"),
                            ])
                        ),
                    ], width=6),
                     dbc.Col([ 
                        dbc.Card(
                            dbc.CardBody([
                                html.H4("Comparatif d'équipes", className="card-title"),
                                html.H6("Saisons 2013-2014", className="card-subtitle"),
                                html.P(
                                    "Some quick example text to build on the card title and make "
                                    "up the bulk of the card's content.",
                                     className="card-text",
                                ),
                                dbc.CardLink("Voir", href="/teams"),
                            ])
                        ),
                    ], width=6),     
                ], 
                justify="between") 
            ], 
                style={'margin': 0 ,'width': '100%', 'max-width': '98%'}
            ),
])
    