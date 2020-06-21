
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
# Normally, Dash creates its own Flask server internally. By creating our own,
# we can create a route for downloading files directly:
app = dash.Dash()
app.layout = html.Div(children=[

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
     
    dcc.Graph(id='plot')

])


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
    Output('dropdown2', 'options'),
    [Input('dropdown', 'value')])
def create_graph_figure(value):
    # you should define a function here that returns your plot
    df = [
        {'regions': ['Tenderloin', 'Knob Hill', 'SOMA'], 'name': 'SF'},
        {'regions': ['Downtown', 'Laurelhurst', 'Foster-Powell'],'name': 'PDX'},
        {'regions': ['Little Tokyo', 'Chinatown', 'Silverlake'], 'name': 'LAX'},
        {'regions': ['CHAZ', 'Capitol Hill', 'Dingus'], 'name': 'SEA'},
        {'regions': ['Italian Market', 'Old town', 'Fishtown'],  'name': 'PHL'},
    ]
    print(df)
    new_drop = [
        [{'label': x, 'value': x} for x in i['regions']] 
        for i in df if i['name'] == value
        ][0]
    return new_drop

if __name__ == "__main__":
    app.run_server(port=8888, debug=True)
