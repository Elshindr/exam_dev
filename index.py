import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px  
app = dash.Dash(__name__)

if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0')