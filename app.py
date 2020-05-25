# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output


# ui
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

colors = {
    'background': '#FFFFFFF',
    'text': '#000000'
}


# -------- data --------- #
data_in = pd.read_csv('./data.csv')
graph_1_data = data_in.groupby(
    'group')[['value1', 'value2']].sum().reset_index()

viz1_x = graph_1_data['group'].tolist()
viz1_y1 = graph_1_data['value1'].tolist()
viz1_y2 = graph_1_data['value2'].tolist()

data = [
    {'x': viz1_x, 'y': viz1_y1, 'type': 'bar', 'name': 'SF'},
    {'x': viz1_x, 'y': viz1_y2, 'type': 'bar', 'name': 'm'}
]


markdown_text = '''
# Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''


# -------- functions --------- #


def generate_table(dataframe, max_rows=10):
    """
    take dataframe make data table
    """
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


#
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[
        html.H1(
            children='Hello Dash',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        html.Div(children='Dash: A web application framework for Python.',
                 style={
                     'textAlign': 'center',
                     'color': colors['text']
                 }),


        html.Div(
            children=[
                generate_table(data_in.reset_index()),
                dcc.Markdown(children=markdown_text)],
            style={'align': 'center'}
        ),
        html.Div([

            # column 1
            html.Div([
                dcc.Graph(
                    id='example-graph-2',
                    figure={
                        'data': data,
                        'layout': {
                            'plot_bgcolor': colors['background'],
                            'paper_bgcolor': colors['background'],
                            'font': {
                                'color': colors['text']
                            }
                        }
                    },
                    style={
                        'textAlign': 'center',
                        'color': colors['text']
                    }
                )

            ]),

            # column 2
            html.Div([
                html.Label('Multi-Select Dropdown'),
                dcc.Dropdown(
                    id='group-selector',
                    options=[
                        {'label': 'a', 'value': 'a'},
                        {'label': 'b', 'value': 'b'},
                        {'label': 'C', 'value': 'c'}
                    ],
                    value=['b'],
                    multi=True
                ),
                dcc.Graph(id='graph-with-slider')
            ])

            



        ], style={'columnCount': 2})



    ])


@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('group-selector', 'value')])
def update_figure(selected_group):

    print(selected_group)

    if len(selected_group) == 0:
        filtered_df = data_in
    else:
        filtered_df = data_in[data_in.group.isin(selected_group)]

    traces = []

    # color
    for i in filtered_df.group.unique():
        df_by_group = filtered_df[filtered_df['group'] == i]
        traces.append(dict(
            x=df_by_group['value2'],
            y=df_by_group['value1'],
            text=df_by_group['group'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
        ))

    return {
        'data': traces,
        'layout': dict(
            xaxis={'title': 'Value 2',
                   'range': [1, 100]},
            yaxis={'title': 'Value 1', 'range': [1, 100]},
            legend={'x': 0, 'y': 1},
            hovermode='closest',
            transition={'duration': 500},
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)
