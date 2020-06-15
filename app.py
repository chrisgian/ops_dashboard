"""
This app creates a simple sidebar layout using inline style arguments and the
dbc.Nav component.

dcc.Location is used to track the current location. There are two callbacks,
one uses the current location to render the appropriate page content, the other
uses the current location to toggle the "active" properties of the navigation
links.

For more details on building multi-page Dash applications, check out the Dash
documentation: https://dash.plot.ly/urls
"""
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Markdown text


#  App instantiate
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}


sidebar = html.Div(
    [
        dcc.Markdown(
            '''
            # Prototype App: Sidebar
            [Dash Core Components Example: Sidebar Layout](https://dash-bootstrap-components.opensource.faculty.ai/examples/simple-sidebar/)
            '''),
        html.Hr(),

        dbc.Nav(
            [
                html.Div(['Explore']),
                dbc.NavLink("View Existing", href="/page-5", id="page-5-link"),
                html.Div(['Data Management']),
                dbc.NavLink("Create New", href="/page-1", id="page-1-link"),
                dbc.NavLink("Read New", href="/page-2", id="page-2-link"),
                dbc.NavLink("Update Existing",
                            href="/page-3", id="page-3-link"),
                dbc.NavLink("Delete Existing",
                            href="/page-4", id="page-4-link")

            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


# this callback uses the current pathname to set the active state of the
# corresponding nav link to true, allowing users to tell see page they are on
@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]


# ------ VIEW: PAGE ------- #
page_view = html.Div(
    [
        html.H1('Explore Existing Data'),
        html.P("Oh cool, this is page 4!"),
        dbc.Row(dbc.Col(html.Div("A single column"))),

        dbc.Row(
            [
                dbc.Col(dcc.Slider()),
                dbc.Col(

                    dcc.Dropdown(
                        options=[
                            {'label': 'New York City', 'value': 'NYC'},
                            {'label': 'Montreal', 'value': 'MTL'},
                            {'label': 'San Francisco', 'value': 'SF'}
                        ],
                        value=['MTL', 'NYC'],
                        multi=False
                    )

                ),
                dbc.Col(dcc.Dropdown(
                    options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': 'Montreal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'}
                    ],
                    value=['MTL', 'NYC'],
                    multi=True
                )),
            ]
        ),

    ]
)


# ------ View: Create ------ #
page_create = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-data-upload'),
])


# ------ VIEW: OTHER ------- #
page_delete = html.P("Oh cool, this is page 4!")
page_update = html.P("Oh cool, this is page 3!")



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
