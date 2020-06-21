import dash
from flask import Flask, send_from_directory

import dash_bootstrap_components as dbc

UPLOAD_DIRECTORY = "uploaded"

<<<<<<< HEAD
=======
# Normally, Dash creates its own Flask server internally. By creating our own,
# we can create a route for downloading files directly:

>>>>>>> 05fc6e0149f5bfdd61a86e1025e195d1ecacf5df
server = Flask(__name__)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], server=server)

# --  x
@app.callback(
    Output('opt-dropdown', 'options'),
    [Input("upload-data", "filename")],
)
def update_dropdown(uploaded_filenames):
    return [
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}]

# -- Download Handler Reactions --- #


@server.route("/download/<path:path>")
def download(path):
    """Serve a file from the upload directory."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)
<<<<<<< HEAD
=======


@app.callback(
    Output("file-list", "children"),
    [Input("upload-data", "filename"),
     Input("upload-data", "contents")],
)
def update_output(uploaded_filenames, uploaded_file_contents):
    """Save uploaded files and regenerate the file list."""

    if uploaded_filenames is not None and uploaded_file_contents is not None:
        for name, data in zip(uploaded_filenames, uploaded_file_contents):
            save_file(name, data)

    files = uploaded_files()

    if len(files) == 0:
        return [html.Li("No files yet!")]
    else:
        return [html.Li(file_download_link(filename)) for filename in files]



@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return page_create
    elif pathname == "/page-2":
        return html.P("This is the content of page 2")
    elif pathname == "/page-3":
        return page_update
    elif pathname == "/page-4":
        return page_delete
    elif pathname == "/page-5":
        return page_view
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(port=8888, debug=True)
>>>>>>> 05fc6e0149f5bfdd61a86e1025e195d1ecacf5df
