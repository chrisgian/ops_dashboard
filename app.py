import dash
from flask import Flask, send_from_directory

import dash_bootstrap_components as dbc

UPLOAD_DIRECTORY = "uploaded"

server = Flask(__name__)

app = dash.Dash(
    external_stylesheets=[dbc.themes.SIMPLEX], 
    server=server,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}]
    )


@server.route("/download/<path:path>")
def download(path):
    """Serve a file from the upload directory."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


