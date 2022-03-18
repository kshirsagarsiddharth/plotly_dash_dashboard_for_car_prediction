import pandas as pd
from dash import dcc, html
import dash_bootstrap_components as dbc
import numpy as np
import dash_daq as daq
import plotly.graph_objects as go

df = pd.read_csv('car_price_data.csv').drop('Unnamed: 0', axis=1)


row1 = dbc.Row([
    dbc.Col(html.H5('KM Travelled')),
    dbc.Col(dcc.Slider(
        min=df['km_traveled'].min(),
        max=df['km_traveled'].max(),
        value=df['km_traveled'].min(),
        id='km-travelled-slider',
        tooltip={"placement": "bottom"}
    )),
    dbc.Col(html.H5('Pick Car Year')),
    dbc.Col(dcc.Dropdown(
        id='year-picker',
        options=np.sort(df['year'].unique()),
        value=2017
    ))
])

row2 = dbc.Row([
    dbc.Col(html.H5('tax-picker'),),
    dbc.Col(dcc.Slider(
        min=df['tax'].min(),
        max=df['tax'].max(),
        value=df['tax'].min(),
        id='tax-slider',
        tooltip={"placement": "bottom"}
    ),),
    dbc.Col(html.H5('engine-size'),),
    dbc.Col(dcc.Slider(
        min=df['engineSize'].min(),
        max=df['engineSize'].max(),
        value=df['engineSize'].min(),
        id='engine-size-slider',
        marks={i: str(i) for i in np.sort(df['engineSize'].unique())},
        tooltip={"placement": "bottom"}
    ),)
])


row3 = dbc.Row([
    dbc.Col(html.H5('km-per-liter'),),
             dbc.Col(dcc.Slider(
                 min=df['km_per_liters'].min(),
                 max=df['km_per_liters'].max(),
                 value=df['km_per_liters'].min(),
                 id='km-per-liters-slider',
                 tooltip={"placement": "bottom"}
             ),), 

   dbc.Col(html.H5('model-dropdown'),),
    dbc.Col(dcc.Dropdown(
        id='model-dropdown',
        options=np.sort(df['model'].unique()),
        value=df['model'][0]
    ),)
])

row4 = dbc.Row([
    dbc.Col(html.H5('transmission-dropdown'),),
    dbc.Col(dcc.Dropdown(
        id='transmission-dropdown',
        options=np.sort(df['transmission'].unique()),
        value=df['transmission'][0]
    ),),
    dbc.Col(html.H5('fuel-type-dropdown'),),
    dbc.Col(dcc.Dropdown(
        id='fuel-type-dropdown',
        options=np.sort(df['fuel_type'].unique()),
        value=df['fuel_type'][0]
    ),)
])


row5 = dbc.Row([
    dbc.Col(
         daq.Gauge(
            id='km-travelled-gauge',
            label="KM Travelled Entered",
            value=df['km_traveled'].min(),
            min=df['km_traveled'].min(),
            max=df['km_traveled'].max(),
            showCurrentValue=True,
            units="KM",
    ),
    ),
    dbc.Col(
        dcc.Graph(id='tax-slider-output')
    )
])
