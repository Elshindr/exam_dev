"""
LAUNCHER APP
"""
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc 
from dash import page_container

# Init Dash
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Navbar everywhere
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),  # URL redirection
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dcc.Link("Home", href='/', className="nav-link")),
            dbc.NavItem(dcc.Link("Comparatif de joueurs", href='/players', className="nav-link")),
            dbc.NavItem(dcc.Link("Comparatif d'équipes", href='/teams', className="nav-link")),
        ],
        brand="NBA Metrics (2013)",
        color="primary",
        dark=True,
    ),
    
    # Actual page content
    page_container
])

# Launcher app
if __name__ == '__main__':
    app.run_server(debug=True)
