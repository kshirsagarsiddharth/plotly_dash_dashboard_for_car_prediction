import pandas as pd
from dash import dcc, html
import dash_bootstrap_components as dbc
import numpy as np


df = pd.read_csv('car_price_data.csv').drop('Unnamed: 0', axis=1)


row1 = dbc.Row([

    dbc.Col([html.H6("KM Travelled"),
             dcc.Slider(
        min=df['km_traveled'].min(),
        max=df['km_traveled'].max(),
        value=df['km_traveled'].min(),
        id='km-travelled-slider',
        tooltip={"placement": "bottom"}
    )], className="col-sm"),


    dbc.Col([html.H6('Year'),
             dcc.Dropdown(
        id='year-picker',
        options=np.sort(df['year'].unique()),
        value=2017,
         className='dropdown-class'
    )])
], class_name="row sm-2")

row2 = dbc.Row([

    dbc.Col([
        html.H6('Tax'),
        dcc.Slider(
            min=df['tax'].min(),
            max=df['tax'].max(),
            value=df['tax'].min(),
            id='tax-slider',
            tooltip={"placement": "bottom"}
        ),
    ]),

    dbc.Col([
        html.H6('Engine Size'),
        dcc.Slider(
            min=df['engineSize'].min(),
            max=df['engineSize'].max(),
            value=df['engineSize'].min(),
            id='engine-size-slider',
            tooltip={"placement": "bottom"}
        ),
    ])
], className="mb-2",)


row3 = dbc.Row([

    dbc.Col([
        html.H6('KM/L'),
        dcc.Slider(
            min=df['km_per_liters'].min(),
            max=df['km_per_liters'].max(),
            value=df['km_per_liters'].min(),
            id='km-per-liters-slider',
            tooltip={"placement": "bottom"}
        ),
    ]),


    dbc.Col([
        html.H6('Model'),
        dcc.Dropdown(
            id='model-dropdown',
            options=np.sort(df['model'].unique()),
            value=df['model'][0],
            className='dropdown-class'
        ),
    ])
])

row4 = dbc.Row([
    dbc.Col([
        html.H6('Transmission'),
        dcc.Dropdown(
            id='transmission-dropdown',
            options=np.sort(df['transmission'].unique()),
            value=df['transmission'][0],
            className='dropdown-class'
        ),
    ]),

    dbc.Col([
        html.H6('Fuel Type'),
        dcc.Dropdown(
            id='fuel-type-dropdown',
            options=np.sort(df['fuel_type'].unique()),
            value=df['fuel_type'][0],
            className='dropdown-class',
            
        ),
    ])
])


