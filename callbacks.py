
from dash.dependencies import Input, Output
from app import app
from tools import uploaded_files, file_download_link, save_file
import dash_html_components as html


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
    print(df)
    new_drop = [
        [{'label': x, 'value': x} for x in i['regions']]
        for i in df if i['name'] == value
    ][0]
    return new_drop, new_drop


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
        #print([{'label':i,'value':i} for i in files])
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
