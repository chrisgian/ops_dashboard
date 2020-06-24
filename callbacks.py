
from dash.dependencies import Input, Output, State
from dash import callback_context
from app import app
from tools import uploaded_files, file_download_link, save_file
import dash_html_components as html
import pandas as pd
from app import UPLOAD_DIRECTORY
import os


@app.callback(
    [Output('dropdown2', 'options'),
     Output('dropdown3', 'options')],
    [Input('dropdown', 'value')])
def create_graph_figure(value):
    # you should define a function here that returns your plot
    df = [
        {'regions': ['Tenderloin', 'Knob Hill', 'SOMA'], 'name': 'SF'},
        {'regions': ['Downtown', 'Laurelhurst',
                     'Foster-Powell'], 'name': 'PDX'},
        {'regions': ['Little Tokyo', 'Chinatown',
                     'Silverlake'], 'name': 'LAX'},
        {'regions': ['CHAZ', 'Capitol Hill', 'Dingus'], 'name': 'SEA'},
        {'regions': ['Italian Market', 'Old town',
                     'Fishtown'],  'name': 'PHL'},
    ]

    new_drop = [
        [{'label': x, 'value': x} for x in i['regions']]
        for i in df if i['name'] == value
    ][0]
    return new_drop, new_drop


@app.callback(
    Output('hidden-div', 'children'),
    [Input('button_filelist_delete', 'n_clicks')],
    [State('dropdown_filelist_delete', 'value')]
)
def delete_file(n_clicks, input_value):
    print(
        """
        x{}
        y   {}
        """.format(n_clicks, input_value)
    )
    if input_value is not None:
        try:
            os.remove(
                "/Users/chris/projects/dash_app/uploaded/{}".format(input_value))
        except FileNotFoundError:
            print("Oops! No such file")


@app.callback(
    [Output("dynamic_dropdown1", "options"),
     Output("dropdown_filelist_delete", "options")],
    [Input("upload-data", "filename"),
     Input("upload-data", "contents"),
     Input("hidden-div", "children")
     ]
)
def test_dropdown(uploaded_filenames, uploaded_file_contents, click_delete):
    """Save uploaded files and regenerate the file list."""

    context = [p['prop_id'] for p in callback_context.triggered][0]

    if context == 'hidden-div.children':
        print('Refresh after delete')

    files = uploaded_files()
    files = [{'label': file, 'value': file} for file in files]
    return files, files


@app.callback(
    Output("hidden-div-2", "children"),
    [Input("upload-data", "filename"),
     Input("upload-data", "contents")
     ],
)
def save_data(uploaded_filenames, uploaded_file_contents):
    """Save uploaded files and regenerate the file list."""

    context = [p['prop_id'] for p in callback_context.triggered][0]

    if context == 'hidden-div.children':
        print('Refresh after delete')

    if uploaded_filenames is not None and uploaded_file_contents is not None:
        for name, data in zip(uploaded_filenames, uploaded_file_contents):
            save_file(name, data)


@app.callback(
    Output('file-list', 'children'),
    [
        Input('hidden-div-2', 'children'),
        Input("hidden-div", "children")]
)
def refresh_filelist(a, b):
    files = uploaded_files()
    if len(files) == 0:
        return [html.Li("No files yet!")]
    else:
        return [html.Li(file_download_link(filename)) for filename in files]


@app.callback(
    Output('plot', 'figure'),
    [Input('dropdown', 'value')])
def create_graph_figure(value):
    # you should define a function here that returns your plot
    df = [
        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'PDX'},
        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'LAX'},
        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'SEA'},
        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'PHL'},
    ]
    df_filtered = [i for i in df if value not in i['name']]
    return {
        'data': df_filtered,
        'layout': {
            'title': 'Dash Data Visualization'
        }
    }


@app.callback(
    Output('table-editing-simple-output', 'figure'),
    [Input('table-editing-simple', 'data'),
     Input('table-editing-simple', 'columns')])
def display_output(rows, columns):
    df = pd.DataFrame(rows, columns=[c['name'] for c in columns])
    return {
        'data': [{
            'type': 'parcoords',
            'dimensions': [{
                'label': col['name'],
                'values': df[col['id']]
            } for col in columns]
        }]
    }
