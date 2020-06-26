import dash_html_components as html
from dash.dependencies import Input, Output
import os
import dash_bootstrap_components as dbc
from app import app, UPLOAD_DIRECTORY
import layouts
import callbacks

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

server = app.server # Heroku needs this in index.py for it to work

app.config.suppress_callback_exceptions = True

if __name__ == '__main__':
    app.run_server(debug=True)
