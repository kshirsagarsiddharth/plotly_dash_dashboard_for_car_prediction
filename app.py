import plotly.graph_objects as go
import joblib
from utils import row1, row2, row3, row4, row5
import pandas as pd
from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import dash_daq as daq


df = pd.read_csv('car_price_data.csv').drop('Unnamed: 0', axis=1)

loaded_model = joblib.load('final_car_prediction_model.pkl')
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.Div([row1,
              row2,
              row3,
              row4,
              dbc.Button("Submit", className="me-1",
                         id='submit-button-state', color="dark",),
              ], className='container'),

    #html.Button(id='submit-button-state', n_clicks=0, children='Submit'),


    html.Div([
         row5,
        html.Div(id='year-picker-output'),
        html.Div(id='engine-size-slider-output'),

        html.Div(id='km-per-liters-slider-output'),
        html.Div(id='model-dropdown-output'),
        html.Div(id='transmission-dropdown-output'),
        html.Div(id='fuel-type-dropdown-output'),
        html.Div(id='prediction', style={'font-size': '60px'})
    ])

])


@app.callback(
    Output('year-picker-output', 'children'),
    Output('engine-size-slider-output', 'children'),
    Output('km-per-liters-slider-output', 'children'),
    Output('model-dropdown-output', 'children'),
    Output('transmission-dropdown-output', 'children'),
    Output('fuel-type-dropdown-output', 'children'),
    Output('prediction', 'children'),

    Input('submit-button-state', 'n_clicks'),
    State('km-travelled-slider', 'value'),
    State('year-picker', 'value'),
    State('engine-size-slider', 'value'),
    State('tax-slider', 'value'),
    State('km-per-liters-slider', 'value'),
    State('model-dropdown', 'value'),
    State('transmission-dropdown', 'value'),
    State('fuel-type-dropdown', 'value')
)
def update_output(n_clicks, km_travelled, date_value, engine_size, tax_value, km_per_liters, model_name, transmission, fuel_type):
    prediction = loaded_model.predict(pd.DataFrame(
        data=[[str(date_value), km_travelled, tax_value, engine_size,
               km_per_liters, model_name, transmission, fuel_type]],
        columns=joblib.load('column_names.pkl')))

   

    return (f"date_value: {date_value}",
            f"engine_size: {engine_size}",
            f"Km Per Liters: {km_per_liters}",
            f"model name: {model_name}",
            f"transmission: {transmission}",
            f"fuel_type: {fuel_type}",
            f"prediction: {prediction}"
            )

@app.callback(Output('km-travelled-gauge', 'value'), Input('km-travelled-slider', 'value'))
def km_travelled_update(km_travelled):
    return km_travelled

@app.callback( Output('tax-slider-output', 'figure'), Input('tax-slider', 'value'),)
def tax_update(tax_value):
   return go.Figure(go.Indicator(
    mode = "number+delta",
    value = tax_value,
    delta = {"reference": df['tax'].mean()},
    title = {"text": "Tax Entered(relative to average)"},
    domain = {'x': [0, 1], 'y': [0, 1]}
    ))
   




if __name__ == "__main__":
    app.run_server(debug=True)
