import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from styles import CONTENT_STYLE, UPLOADER_STYLE
from app import app


# ------ VIEW: Explore ------- #
page_view = html.Div(
    [
        html.H1('Explore Existing Data'),
        html.P("Oh cool, this is page 5!"),
        dbc.Row(dbc.Col(html.Div("A single column"))),
        dbc.Row([
            dbc.Col(dcc.Slider()),
            dbc.Col(dcc.Dropdown(options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montreal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}])),
            dbc.Col(dcc.Dropdown(id='dynamic_dropdown1'))])])
# ------ VIEW: READ ------- #

params = ['Weight', 'Torque', 'Width', 'Height',
          'Efficiency', 'Power', 'Displacement']

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
        html.Br(),
        html.Br(),
        dcc.Markdown(
            '''
              ### Data Management: Delete

              On this page, you can delete a file that you uploaded. Simply select the file of interest and click 'Delete'.
            '''),
        html.Hr(),
        dcc.Dropdown(id='dropdown_filelist_delete'),
        html.Br(),
        dbc.Button("Delete", color="danger", id="button_filelist_delete")
    ]
)

# ------ VIEW: EDIT ------- #

page_update = html.Div(children=[
    html.Br(),
    html.Br(),
    dcc.Markdown(
        '''
        ### Data Management: Edit
        On this page, you can Edit a file that you uploaded. Simply select the file of interest and click 'Delete'.
        '''),
    html.Hr(),
    html.Br(),
    dbc.Row(
        [dbc.Col(
            dcc.Dropdown(
                id='dropdown',
                options=[{'label': i, 'value': i}
                         for i in ['SEA', 'LAX', 'SF', 'PHL', 'PDX']],
                value='LAX',
            )),
         dbc.Col(dcc.Dropdown(id='dropdown2')),
         dbc.Col(dcc.Dropdown(id='dropdown3'))]
    ),
    html.Br(),
    dcc.Graph(id='plot')

])

# ------ VIEW: Create ------ #
page_welcome = html.Div([
    html.Br(),
    html.Br(),
     dcc.Markdown(
         '''
         ### Overview
         
         At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.

         At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.

         At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.
         '''),

])
page_create = html.Div(
    [
        html.Br(),
        html.Br(),
        dcc.Markdown(
            '''
            ### Data Management: Upload
            On this page, you can Edit a file that you uploaded. Simply select the file of interest and click 'Delete'.
            '''),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Upload"),
                        html.Br(),
                        dcc.Upload(
                            id="upload-data",
                            children=html.Div([
                                "Drag and drop or click to select a file to upload."
                            ]),
                            style=UPLOADER_STYLE,
                            multiple=True
                        )]
                ),
                dbc.Col(
                    [html.H2("File List"),
                     html.Br(),
                     html.Ul(id="file-list")]
                )
            ]
        )
    ]

)


# tab controller


app.layout = html.Div([
    dcc.Markdown(
        '''
        # Python Dash: Scenario Tool
        [Learn More](https://www.google.com)
        '''),
    html.Div(id='hidden-div'),
    html.Div(id='hidden-div-2'),
    html.Hr(),
    dcc.Tabs(id='tabs-example', value='welcome',
             children=[
                 dcc.Tab(label='Overview', children=page_welcome,
                  value= 'welcome'),
                 dcc.Tab(label='Upload Scenario', children=page_create),
                 dcc.Tab(label='Create Scenario ', children=page_read),
                 dcc.Tab(label='Edit Scenario', children=page_update),
                 dcc.Tab(label='Delete Scenario', children=page_delete),
                 dcc.Tab(label='View Dependencies', children=page_view),
             ]),
    html.Div(id='tabs-example-content')
], style=CONTENT_STYLE)
