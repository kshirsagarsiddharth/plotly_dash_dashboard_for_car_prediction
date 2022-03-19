import pandas as pd
import dash_bootstrap_components as dbc
import dash_daq as daq


df = pd.read_csv('car_price_data.csv').drop('Unnamed: 0', axis=1)

card_content = []

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
