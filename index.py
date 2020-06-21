import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import os
import dash_bootstrap_components as dbc
from styles import CONTENT_STYLE
from app import app, UPLOAD_DIRECTORY
from layouts import page_create, page_view, page_update, page_sidebar, page_delete
import callbacks

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id="url"),
    html.Div(id="page-content", style=CONTENT_STYLE),
    page_sidebar
])

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



if __name__ == '__main__':
    app.run_server(debug=True)
