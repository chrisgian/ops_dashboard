
from dash.dependencies import Input, Output, State
from dash_table import DataTable
from dash import callback_context
from app import app, UPLOAD_DIRECTORY
from tools import uploaded_files, file_download_link, save_file
import dash_html_components as html
import pandas as pd
import os
import datetime

# drop down update from delete or load


@app.callback(
    Output("dropdown_filelist_load", "options"),
    [Input("hidden-div-2", "children"),
     Input("hidden-div", "children"),
     Input("hidden-div-save", "children")])
def refresh_dropdowns(file_upload, file_delete, file_save):
    """Refresh drop downs with new file list"""

    context = [prop['prop_id'] for prop in callback_context.triggered][0]

    if context == 'hidden-div.children':
        print('Refresh after delete')
    elif context == 'hidden-div-2.children':
        print('Refresh after upload')
    elif context == 'hidden-div-save.children':
        print('Refresh after save')
    else:
        print('Refresh due to error')

    # call a helper function to retrieve file list
    files = [{'label': file, 'value': file} for file in uploaded_files()]

    return files


# data management: delete


@app.callback(
    Output('hidden-div', 'children'),
    [Input('button_file_delete', 'n_clicks')],
    [State('dropdown_filelist_load', 'value')])
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
    if (
        (uploaded_filenames is not None) and
        (uploaded_file_contents is not None) and
            ('.csv' in uploaded_filenames[0])):
        for name, data in zip(uploaded_filenames, uploaded_file_contents):
            save_file(name, data)


@app.callback(
    Output("confirm", "displayed"),
    [Input("upload-data", "filename")])
def notify(uploaded_filenames):
    """Save uploaded files"""
    if (uploaded_filenames is not None) and ('.csv' not in uploaded_filenames[0]):
        return True
    else:
        return False


# update ui with new file list after new upload


@app.callback(
    Output('file-list', 'children'),
    [Input('hidden-div-2', 'children'),
     Input("hidden-div", "children"),
     Input("hidden-div-save", "children")])
def update_filelist_for_uploaded(file_upload, file_delete, file_save):
    """x"""
    files = uploaded_files()
    if len(files) == 0:
        return [html.Li("No files yet!")]
    else:
        return [html.Li(file_download_link(filename)) for filename in files]


@app.callback(
    Output('hidden-div-save', 'children'),
    [Input('button_file_save', 'n_clicks'),
     Input('button_file_overwrite', 'n_clicks')],
    [State('editable_table', 'data'),
     State('dropdown_filelist_load', 'value')])
def save_edited_table(n_clicks_save, n_clicks_overwrite, data, file_name):
    """
    x
    """

    context = [prop['prop_id'] for prop in callback_context.triggered][0]
    if context == 'button_file_save.n_clicks':
        datetag = datetime.datetime.strftime(
            datetime.datetime.now(), '%Y%m%d_%H%M%S')
    else:
        datetag = ''

    if file_name is not None and '.csv' in file_name:

        new_file_name = (
            file_name.replace('.csv', '')
            + datetag
            + '.csv')

        (pd.DataFrame(data)
         .to_csv(os.path.join(UPLOAD_DIRECTORY, new_file_name), index=None))


@app.callback(
    [Output('editable_table', 'data'),
     Output('editable_table', 'columns')],
    [Input('button_file_load', 'n_clicks'),
     Input('button_file_reset', 'n_clicks'),
     Input('button_file_delete', 'n_clicks')

     ],
    [State('dropdown_filelist_load', 'value')])
def load_selected_table(
        n_clicks_load,
        n_clicks_reset,
        n_clicks_delete,
        input_value):
    """
    x
    """
    context = [prop['prop_id'] for prop in callback_context.triggered][0]

    if input_value is not None and context == 'button_file_load.n_clicks':
        try:
            df_loaded = pd.read_csv(
                os.path.join(UPLOAD_DIRECTORY, input_value))
            return (df_loaded.to_dict('records')), ([{"name": i, "id": i} for i in df_loaded.columns])
        except FileNotFoundError:
            return (), ()
    elif context == 'button_file_load.n_clicks':
        return (), ()
    else:
        return (), ()


@app.callback(
    Output('table-editing-simple-output', 'figure'),
    [Input('table-editing-simple', 'data'),
     Input('table-editing-simple', 'columns')])
def display_output(rows, columns):
    """
    x
    """
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
