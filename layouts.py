import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from styles import SIDEBAR_STYLE

# ------ VIEW: Explore ------- #
page_view = html.Div(
    [
        html.H1('Explore Existing Data'),
        html.P("Oh cool, this is page 5!"),
        dbc.Row(dbc.Col(html.Div("A single column"))),

        dbc.Row(
            [
                dbc.Col(dcc.Slider()),
                dbc.Col(
                    dcc.Dropdown(
                        options=[
                            {'label': 'New York City', 'value': 'NYC'},
                            {'label': 'Montreal', 'value': 'MTL'},
                            {'label': 'San Francisco', 'value': 'SF'}]
                    )
                ),
                dbc.Col(

                )
            ]
        )
    ]
)
# ------ VIEW: SIDEBAR ------- #

page_sidebar = html.Div(
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


# ------ VIEW: OTHER ------- #
page_delete = html.P("Oh cool, this is page 4!")

# ------ VIEW: EDIT ------- #
page_update = html.Div(children=[

    html.H1(children='Hello Dash'),

    html.Div(children='''Dash: A web application framework for Python.'''),

    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': i, 'value': i} for i in ['SEA', 'LAX', 'SF', 'PHL', 'PDX']],
        value='LAX'
    ),

    dcc.Dropdown(
        id='dropdown2'
    ),

    dcc.Dropdown(id='dropdown3'),


    dcc.Graph(id='plot')

])

# ------ VIEW: Create ------ #
page_create = html.Div(
    [
        html.H1("File Browser"),
        html.H2("Upload"),
        dcc.Upload(
            id="upload-data",
            children=html.Div(
                ["Drag and drop or click to select a file to upload."]
            ),
            style={
                "width": "100%",
                "height": "60px",
                "lineHeight": "60px",
                "borderWidth": "1px",
                "borderStyle": "dashed",
                "borderRadius": "5px",
                "textAlign": "center",
                "margin": "10px",
            },
            multiple=True,
        ),
        html.H2("File List"),
        html.Ul(id="file-list"),
    ],
    style={"max-width": "500px"},
)
