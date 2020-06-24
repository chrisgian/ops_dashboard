
from dash.dependencies import Input, Output, State
from dash import callback_context
from app import app, UPLOAD_DIRECTORY
from tools import uploaded_files, file_download_link, save_file
import dash_html_components as html
import pandas as pd
import os


# drop down update from delete or load

@app.callback(
    [Output("dynamic_dropdown1", "options"),
     Output("dropdown_filelist_delete", "options")],
    [Input("hidden-div-2", "children"),
     Input("hidden-div", "children")])
def refresh_dropdowns(file_upload, file_delete):
    """Refresh drop downs with new file list"""

    context = [prop['prop_id'] for prop in callback_context.triggered][0]

    if context == 'hidden-div.children':
        print('Refresh after delete')
    elif context == 'hidden-div-2.children':
        print('Refresh after upload')
    else:
        print('Refresh due to error')

    # call a helper function to retrieve file list
    files = [{'label': file, 'value': file} for file in uploaded_files()]

    return files, files


# data management: delete


@app.callback(
    Output('hidden-div', 'children'),
    [Input('button_filelist_delete', 'n_clicks')],
    [State('dropdown_filelist_delete', 'value')])
def delete_file(n_clicks, input_value):
    """
    delete a selected file upon selection and click
    """
    if input_value is not None:
        try:
            os.remove(
                "./{}/{}".format(UPLOAD_DIRECTORY, input_value))
        except FileNotFoundError:
            print("file name not found")

# save uploaded contents


@app.callback(
    Output("hidden-div-2", "children"),
    [Input("upload-data", "filename"),
     Input("upload-data", "contents")])
def save_data_for_uploaded(uploaded_filenames, uploaded_file_contents):
    """Save uploaded files"""

    if uploaded_filenames is not None and uploaded_file_contents is not None:
        for name, data in zip(uploaded_filenames, uploaded_file_contents):
            save_file(name, data)


# update ui with new file list after new upload


@app.callback(
    Output('file-list', 'children'),
    [Input('hidden-div-2', 'children'), Input("hidden-div", "children")])
def update_filelist_for_uploaded(a, b):
    files = uploaded_files()
    if len(files) == 0:
        return [html.Li("No files yet!")]
    else:
        return [html.Li(file_download_link(filename)) for filename in files]


# update plot after dropdown selected


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


# Conditional Drop Down

@app.callback(
    [Output('dropdown2', 'options'),
     Output('dropdown3', 'options')],
    [Input('dropdown', 'value')])
def query_conditional_dropdown(value):
    """
    based on what dropdown is will select dropdown contents for  
    """
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


# editable table


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
