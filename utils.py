import pandas as pd
from dash import dcc, html
import dash_bootstrap_components as dbc
import numpy as np
import dash_daq as daq
import plotly.graph_objects as go

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


card_content = [
    # dbc.CardHeader("Card header"),
    # dbc.CardBody(
    #     [
    #         html.H5("Card title", className="card-title"),
    #         html.P(
    #             "This is some card content that we'll reuse",
    #             className="card-text",
    #         ),
    #     ]
    # ),
]

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
        class_name="col-sm-2"),

    dbc.Col(
        daq.Gauge(
            id='km-per-liters-slider-output',
            label="KM/L Entered",
            value=df['km_per_liters'].min(),
            min=df['km_per_liters'].min(),
            max=df['km_per_liters'].max(),
            showCurrentValue=True,
            units="KM/L",

        ),
        class_name="col-sm-2"),

    dbc.Col(
        daq.Tank(
            id='engine-size-slider-output',
            label="Engine Size",
            value=df['engineSize'].min(),
            min=df['engineSize'].min(),
            max=df['engineSize'].max(),
            showCurrentValue=True,
            units="CC",

        ),
        class_name="col-sm-2"),

    dbc.Col([
        dbc.Row(
            [
                dbc.Col(dbc.Card(card_content,
                        id='tax-slider-output', className='card-class')),
                dbc.Col(dbc.Card(card_content,
                        id='year-picker-output')),

            ],

        ),

        dbc.Row(
            [
                dbc.Col(dbc.Card(card_content,
                        id='fuel-type-dropdown-output')),
                dbc.Col(dbc.Card(card_content,
                        id='transmission-dropdown-output')),

            ],

        ),
    ])
], style={'border-style': 'solid'})


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
            
        ),
    ],
    brand="Car Price Prediction dashboard",
    brand_href="#",
   
    
)
