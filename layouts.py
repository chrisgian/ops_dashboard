import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from styles import CONTENT_STYLE
from app import app


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
                    dcc.Dropdown(id='dynamic_dropdown1')
                )
            ]
        )
    ]
)
# ------ VIEW: READ ------- #

params = [
    'Weight', 'Torque', 'Width', 'Height',
    'Efficiency', 'Power', 'Displacement'
]
page_read = html.Div(
    [
        html.H1('Read Data'),
        html.P("Oh cool, this is page 5!"),
        dbc.Row(dbc.Col(html.Div("A single column"))),
        dash_table.DataTable(
            id='table-editing-simple',
            columns=(
                [{'id': 'Model', 'name': 'Model'}] +
                [{'id': p, 'name': p} for p in params]
            ),
            data=[dict(Model=i, **{param: 0 for param in params})
                  for i in range(1, 5)],
            editable=True
        ),
        dcc.Graph(id='table-editing-simple-output')
    ]
)

# ------ VIEW: Delete ------- #
page_delete = html.Div(
    [
        dcc.Markdown(
            '''
              ## Delete something
            '''),
        html.Hr(),
        dcc.Dropdown(id='dropdown_filelist_delete'),
        dbc.Button("Primary", color="danger", id="button_filelist_delete")
    ]
)

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
    dcc.Dropdown(id='dropdown2'),
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


app.layout = html.Div([
    dcc.Markdown(
        '''
        # Python Dash: Scenario Tool
        [Learn More](https://www.google.com)
        '''),
    html.Div(id='hidden-div'),
    html.Div(id='hidden-div-2'),
    html.Hr(),
    dcc.Tabs(id='tabs-example', value='create',
             children=[
                 dcc.Tab(label='Upload Scenario', children=page_create),
                 dcc.Tab(label='Create Scenario ', children=page_read),
                 dcc.Tab(label='Edit Scenario', children=page_update),
                 dcc.Tab(label='Delete Scenario', children=page_delete),
                 dcc.Tab(label='View Dependencies', children=page_view),
             ]),
    html.Div(id='tabs-example-content')
], style=CONTENT_STYLE)
