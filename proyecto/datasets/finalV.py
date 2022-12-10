# Libreria para manejo de archivos json
import json

# Librerias para trabajar con visualizaciones interactivas
import plotly
import plotly.express as px
import plotly.graph_objects as go

# Librerias para crear un tablero con plotly
from jupyter_dash import JupyterDash
import dash
from dash import dcc
from dash import html
from dash import dash_table

# Libreria para cambiar el diseño de un tablero en dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

# Libreria para manipulacion de datos con dataframes
import pandas as pd
import numpy as np

# Para manipulacion de fechas en controles de dash
from datetime import date

# Libreria para hilos
import threading

# Libreria para el tiempo de la maquina
import time
from datetime import datetime


path = r"/Users/blckwlf/Documents/GitHub/ProgramacionAvanzada/proyecto/datasets/dow_jones_index/dow_jones_index.csv"

# Creacion de un tablero para la visualizacion inicial
def page0():
    return html.Div(
        [
            html.Div(
                children=[
                    html.Div(
                        children=html.B(
                            children=html.H4("Descripción del Proyecto Final")
                        ),
                        className="alert alert-dismissible alert-success",
                        style={"text-align": "center"},
                    ),
                    html.Div(
                        html.P(
                            "El objetivo del Proyecto Final es crear un tablero interactivo en dash tomando como base un conjunto de datos del Indice Dow Jones. Haciendo uso de controles interactivos y la visualización de al menos 4 gráficos (dispersión, línea, histograma, barras, etc.)."
                        ),
                        style={"margin": "5%"},
                    ),
                ],
                # Clase de control
                className="accordion-item",
            ),
            html.Div(
                children=[
                    html.Div(
                        children=html.B(children=html.H4("Uso de Visualizaciones")),
                        className="alert alert-dismissible alert-success",
                        style={"text-align": "center"},
                    ),
                    html.P(
                        "En primera instancia, se hace uso de visualizaciones/gráficos, regularmente tenemos que proveer el stock es decir alguno de los siguientes. (AA, AXP, BA, BAC, CAT, CSCO, CVX, DD, DIS, GE, HD, HPQ, IBM, INTC, JNJ, JPM, KRFT, KO, MCD, MMM, MRK, MSFT, PFE, PG, T, TRV, UTX, UNH, VZ, WMT, XOM)",
                        style={"margin": "5%"},
                    ),
                ],  # Clase de control
                className="accordion-item",
            ),
            # Se cierra el contenedor de todo el tablero
        ]
    )


# Creacion de un tablero para una visualizacion de tipo linea
def page1():
    return html.Div(
        [
            # Barra de titulo del tablero
            html.Div(
                children=[
                    html.H1(
                        children="Volumen de acciones vendidas en el 2011",
                        style={"color": "black", "height": "57v"},
                    )
                ]
            ),
            # Se añade en la primera fila con cuatro tipos de controles y un grafico
            dbc.Row(
                [
                    dbc.Col(
                        children=[
                            html.Div(
                                children=[
                                    html.Div(
                                        children=html.B(
                                            children=html.H4(
                                                "Seleccionar rango de cuartos"
                                            )
                                        ),
                                        className="alert alert-dismissible alert-success",
                                    ),
                                    # Primer control (menu desplegable)
                                    dcc.RangeSlider(
                                        id="rangeSlider1",
                                        min=1,
                                        max=2,
                                        count=1,
                                        value=[0, 2],
                                        allowCross=False,
                                        marks={i: f"{i}" for i in [1, 2]},
                                    ),
                                ],
                                # Clase de control
                                className="accordion-item",
                            ),
                            html.Div(
                                children=[
                                    html.Div(
                                        children=html.B(
                                            children=html.H4("Escoge una Accion")
                                        ),
                                        className="alert alert-dismissible alert-success",
                                    ),
                                    # Segundo control (caja de texto)
                                    dcc.Input(
                                        id="inputBox2",
                                        type="text",
                                        disabled=False,
                                        value="",
                                        placeholder="Nombre de la accion",
                                        style={"font-size": "18px"},
                                        className="form-control",
                                    ),
                                    # Tercer control (boton clasico)
                                    html.Button(
                                        "Enviar",
                                        id="button2",
                                        disabled=False,
                                        className="btn btn-info",
                                    ),
                                    # Cuarto control (mensaje de alerta)
                                    dcc.ConfirmDialog(
                                        id="warning2",
                                        message="Seleccione una accion valida, se mostrarán todos los estados",
                                    ),
                                ],
                                # Clase de control
                                className="accordion-item",
                            ),
                        ],
                        style={"height": "57v", "margin-left": "11px", "margin": "4px"},
                    ),
                    # Se añade en la primera fila una segunda columna con areas de texto y un grafico
                    dbc.Col(
                        html.Div(
                            children=[
                                dbc.Row(
                                    [
                                        # Area de texto 1
                                        dbc.Col(
                                            html.Div(
                                                children=html.B(
                                                    children=html.H5(
                                                        [
                                                            "Volumen total de",
                                                            html.Br(),
                                                            "acciones",
                                                        ]
                                                    )
                                                ),
                                                id="area5",
                                                style={
                                                    "border": "2px black solid",
                                                    "height": "25vh",
                                                    "width": "100%",
                                                    "display": "flex",
                                                    "align-items": "center",
                                                    "justify-content": "center",
                                                    "background-color": "#BEBEBE",
                                                },
                                            )
                                        ),
                                        # Area de texto 2
                                        dbc.Col(
                                            html.Div(
                                                children=html.B(
                                                    children=html.H5(
                                                        [
                                                            "Cantidad de",
                                                            html.Br(),
                                                            "dinero",
                                                        ]
                                                    )
                                                ),
                                                id="area6",
                                                style={
                                                    "border": "2px black solid",
                                                    "height": "25vh",
                                                    "width": "100%",
                                                    "display": "flex",
                                                    "align-items": "center",
                                                    "justify-content": "center",
                                                    "background-color": "#BEBEBE",
                                                },
                                            )
                                        ),
                                    ],
                                    style={"margin": "10px"},
                                ),
                                dbc.Row(
                                    [
                                        # Area de texto 3
                                        dbc.Col(
                                            html.Div(
                                                children=html.B(
                                                    children=html.H5(
                                                        [
                                                            "Promedio de",
                                                            html.Br(),
                                                            "boletos",
                                                        ]
                                                    )
                                                ),
                                                id="area7",
                                                style={
                                                    "border": "2px black solid",
                                                    "height": "25vh",
                                                    "width": "100%",
                                                    "display": "flex",
                                                    "align-items": "center",
                                                    "justify-content": "center",
                                                    "background-color": "#BEBEBE",
                                                },
                                            )
                                        ),
                                        # Area de texto 4
                                        dbc.Col(
                                            html.Div(
                                                children=html.B(
                                                    children=html.H5(
                                                        [
                                                            "Promedio de",
                                                            html.Br(),
                                                            "dinero",
                                                        ]
                                                    )
                                                ),
                                                id="area8",
                                                style={
                                                    "border": "2px black solid",
                                                    "height": "25vh",
                                                    "width": "100%",
                                                    "display": "flex",
                                                    "align-items": "center",
                                                    "justify-content": "center",
                                                    "background-color": "#BEBEBE",
                                                },
                                            )
                                        ),
                                    ],
                                    style={"margin": "10px"},
                                ),
                                # Tipo de elemento sobre el tablero
                            ]
                        )
                    ),
                    # Fin de la primera fila
                ]
            ),
            # Se añade una segunda fila con un solo grafico
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            dcc.Graph(id="piePlot"),
                        )
                    ),
                ]
            ),
            # Se cierra el contenedor de todo el tablero
        ]
    )


# Funcion que se encarga de crear el tablero de la pagina dos
def page2():
    return html.Div(
        [
            # Barra de titulo del tablero
            html.Div(
                children=[
                    html.H1(
                        children="Volumen de acciones vendidas en el 2011",
                        style={"color": "black", "height": "57v"},
                    )
                ]
            ),
            # Se añade en la primera fila con cuatro tipos de controles y un grafico
            dbc.Row(
                [
                    dbc.Col(
                        children=[
                            html.Div(
                                children=[
                                    html.Div(
                                        children=html.B(
                                            children=html.H4("Escoge una Accion")
                                        ),
                                        className="alert alert-dismissible alert-success",
                                    ),
                                    # Segundo control (caja de texto)
                                    dcc.Input(
                                        id="inputBox2",
                                        type="text",
                                        disabled=False,
                                        value="",
                                        placeholder="Nombre de la accion",
                                        style={"font-size": "18px"},
                                        className="form-control",
                                    ),
                                    # Tercer control (boton clasico)
                                    html.Button(
                                        "Enviar",
                                        id="ButtonHisto",
                                        disabled=False,
                                        className="btn btn-info",
                                    ),
                                    # Cuarto control (mensaje de alerta)
                                    dcc.ConfirmDialog(
                                        id="warning3",
                                        message="Seleccione una accion valida, se mostrarán todos los estados",
                                    ),
                                ],
                                # Clase de control
                                className="accordion-item",
                            ),
                            html.Div(
                                children=[
                                    html.Div(
                                        children=html.B(
                                            children=html.H4("Slider de promedio")
                                        ),
                                        className="alert alert-dismissible alert-success",
                                    ),
                                    # Primer control (menu desplegable)
                                    dcc.Slider(
                                        id="mean",
                                        min=-3,
                                        max=3,
                                        value=0,
                                        marks={-3: "-3", 3: "3"},
                                    ),
                                ],
                                # Clase de control
                                className="accordion-item",
                            ),
                            html.Div(
                                children=[
                                    html.Div(
                                        children=html.B(
                                            children=html.H4("Standard Deviation")
                                        ),
                                        className="alert alert-dismissible alert-success",
                                    ),
                                    # Primer control (menu desplegable)
                                    dcc.Slider(
                                        id="std",
                                        min=1,
                                        max=3,
                                        value=1,
                                        marks={1: "1", 3: "3"},
                                    ),
                                ],
                                # Clase de control
                                className="accordion-item",
                            ),
                        ],
                        style={"height": "57v", "margin-left": "11px", "margin": "4px"},
                    ),
                    # Fin de la primera fila
                ]
            ),
            # Se añade una segunda fila con un solo grafico
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            dcc.Graph(id="histogramPlot"),
                        )
                    ),
                ]
            ),
            # Se cierra el contenedor de todo el tablero
        ]
    )


def page3():
    return html.Div(
        [
            # Barra de titulo del tablero
            html.Div(
                children=[
                    html.H1(
                        children="Volumen de acciones vendidas en el 2011",
                        style={"color": "black", "height": "57v"},
                    )
                ]
            ),
            # Se añade en la primera fila con cuatro tipos de controles y un grafico
            dbc.Row(
                [
                    dbc.Col(
                        children=[
                            html.Div(
                                children=[
                                    html.Div(
                                        children=html.B(
                                            children=html.H4("Escoge una Accion")
                                        ),
                                        className="alert alert-dismissible alert-success",
                                    ),
                                    # Tercer control (boton clasico)
                                    dcc.Dropdown(
                                        id="ticker",
                                        options=[
                                            "AA",
                                            "AXP",
                                            "BA",
                                            "BAC",
                                            "CAT",
                                            "CSCO",
                                            "CVX",
                                            "DD",
                                            "DIS",
                                            "GE",
                                            "HD",
                                            "HPQ",
                                            "IBM",
                                            "INTC",
                                            "JNJ",
                                            "JPM",
                                            "KRFT",
                                            "KO",
                                            "MCD",
                                            "MMM",
                                            "MRK",
                                            "MSFT",
                                            "PFE",
                                            "PG",
                                            "T",
                                            "TRV",
                                            "UTX",
                                            "VZ",
                                            "WMT",
                                            "XOM",
                                        ],
                                        value="AA",
                                    ),
                                ],
                                # Clase de control
                                className="accordion-item",
                            ),
                        ],
                        style={"height": "57v", "margin-left": "11px", "margin": "4px"},
                    ),
                    # Fin de la primera fila
                ]
            ),
            # Se añade una segunda fila con un solo grafico
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            dcc.Graph(id="timeSeriesChart"),
                        )
                    ),
                ]
            ),
            # Se cierra el contenedor de todo el tablero
        ]
    )


def page4():
    return html.Div(
        [
            # Barra de titulo del tablero
            html.Div(
                children=[
                    html.H1(
                        children="Volumen de acciones vendidas en el 2011",
                        style={"color": "black", "height": "57v"},
                    )
                ]
            ),
            # Se añade en la primera fila con cuatro tipos de controles y un grafico
            dbc.Row(
                [
                    dbc.Col(
                        children=[
                            html.Div(
                                children=[
                                    html.Div(
                                        children=html.B(
                                            children=html.H4("Escoge una Accion")
                                        ),
                                        className="alert alert-dismissible alert-success",
                                    ),
                                    # Segundo control (caja de texto)
                                    dcc.Input(
                                        id="inputBoxCandle",
                                        type="text",
                                        disabled=False,
                                        value="",
                                        placeholder="Nombre de la accion",
                                        style={"font-size": "18px"},
                                        className="form-control",
                                    ),
                                    # Tercer control (boton clasico)
                                    html.Button(
                                        "Enviar",
                                        id="buttonCandle",
                                        disabled=False,
                                        className="btn btn-info",
                                    ),
                                    # Cuarto control (mensaje de alerta)
                                    dcc.ConfirmDialog(
                                        id="warning5",
                                        message="Seleccione una accion valida, se mostrarán todos los estados",
                                    ),
                                ],
                                # Clase de control
                                className="accordion-item",
                            ),
                        ],
                        style={"height": "57v", "margin-left": "11px", "margin": "4px"},
                    ),
                    # Fin de la primera fila
                ]
            ),
            # Se añade una segunda fila con un solo grafico
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            dcc.Graph(id="candleGraph"),
                        )
                    ),
                ]
            ),
            # Se cierra el contenedor de todo el tablero
        ]
    )


# Creacion de la aplicacion principal de dash
app = JupyterDash(
    __name__,
    prevent_initial_callbacks=True,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)
# Elementos de estilo para la barra lateral izquierda (CSS)
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#BEBEBE",
}
# Elementos de estilo para la pagina principal/central de la pagina
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
# Creacion de la barra latarel izquierda
sidebar = html.Div(
    [
        html.Div(
            html.B(
                children=html.H5(
                    [
                        "clockText",
                    ]
                )
            ),
            id="areaClock",
            style={"text-align": "center"},
        ),
        html.Img(
            src="https://upload.wikimedia.org/wikipedia/commons/4/47/Logo_del_ITESM.svg",
            style={
                "height": "10%",
                "width": "70%",
                "padding-left": "53px",
            },
        ),
        html.H2("Dow Jones", className="display-5"),
        html.Hr(),
        html.P("Tablero interactivo", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Proyecto Final", href="/", active="exact"),
                dbc.NavLink("Gráfico de pastel", href="/page-1", active="exact"),
                dbc.NavLink("Histograma", href="/page-2", active="exact"),
                dbc.NavLink("Time Series", href="/page-3", active="exact"),
                dbc.NavLink("Candlestick", href="/page-4", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

# Funcion para actualizar el reloj


# Creacion del tablero principal que se actualizara con cada opcion escogida
content = html.Div(id="page-content", style=CONTENT_STYLE)
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

# Funcion activadora para unir cada subtablero con la pagina principal
@app.callback(
    Output("areaClock", "children"),
    Output("page-content", "children"),
    [Input("url", "pathname")],
)
def render_page_content(pathname):
    # instanciar hilo
    hilo = threading.Thread(target=update_clock())
    hilo.start()
    clockText = tiempo
    if pathname == "/":
        return clockText, page0()
    elif pathname == "/page-1":
        return clockText, page1()
    elif pathname == "/page-2":
        return clockText, page2()
    elif pathname == "/page-3":
        return clockText, page3()
    elif pathname == "/page-4":
        return clockText, page4()
    # Si el usuario usa una página diferente, se enviara un mensaje 404
    return html.Div(
        [
            html.H1("404: Pagina no encontrada", className="text-danger"),
            html.Hr(),
            html.P(f"La URL {pathname} no es reconocida..."),
        ],
        className="p-3 bg-light rounded-3",
    )


def update_clock():
    global tiempo
    currentTime = datetime.now().strftime("%H:%M:%S")
    time.sleep(1)
    tiempo = currentTime


# Creacion de un decorador para la interaccion con el tablero
# Funcion que realizara la parte dinamica del grafico de linea
@app.callback(
    [
        Output("area5", "children"),
        Output("area6", "children"),
        Output("area7", "children"),
        Output("area8", "children"),
        Output("piePlot", "figure"),
        Output("warning2", "displayed"),
    ],
    [Input("rangeSlider1", "value"), Input("button2", "n_clicks")],
    State("inputBox2", "value"),
)
def updatePage1(quarter, n_clicks, search):
    # Obtenemos el contexto de los controles
    ctx = dash.callback_context
    message = False
    status = False
    # Cargamos el dataframe de boletos vendidos
    df = pd.read_csv(path, sep=",", encoding="utf-8")
    df = df.query(
        "quarter >= " + str(quarter[0]) + " and quarter <= " + str(quarter[1])
    )
    # Revisamos el nombre del control que activo el evento
    buttonId = ctx.triggered[0]["prop_id"].split(".")[0]
    # Se escogio el boton de carga del mapa
    if buttonId == "button2":
        # Cargamos el dataframe de un estado especifico
        df = df.query(
            "quarter >= "
            + str(quarter[0])
            + " and quarter <= "
            + str(quarter[1])
            + "and stock=='"
            + search
            + "'"
        )
        if not (df.empty) and search != "":
            message = False
            status = True
        else:
            df = pd.read_csv(path, sep=",", encoding="utf-8")
            df = df.query(
                "quarter >= " + str(quarter[0]) + " and quarter <= " + str(quarter[1])
            )
            message = True
            status = False
    # Se escogio otro control
    else:
        if search != "":
            df = df.query(
                "quarter >= "
                + str(quarter[0])
                + " and quarter <= "
                + str(quarter[1])
                + "and stock=='"
                + search
                + "'"
            )
            if not (df.empty):
                message = False
                status = True
            else:
                df = pd.read_csv(path, sep=",", encoding="utf-8")
                df = df.query(
                    "quarter >= "
                    + str(quarter[0])
                    + " and quarter <= "
                    + str(quarter[1])
                )
                message = True
                status = False
        else:
            status = False
    if status == False:
        # Obtenemos estadisticas de los estados
        tickets = df["volume"].sum()
        money = df["close"].sum()
        ticketAvg = round(df["volume"].mean(), 2)
        moneyAvg = round(df["close"].mean(), 2)
        tickets = str(tickets) if tickets != np.nan else "0"
        money = str(money) if money != np.nan else "0"
        ticketAvg = str(ticketAvg) if ticketAvg != np.nan else "0"
        moneyAvg = str(moneyAvg) if moneyAvg != np.nan else "0"
        # Creamos las casillas dinamicas
        text1 = html.H5(["Volumen", html.Br(), "total de aciones", html.Br(), tickets])
        text2 = html.H5(["Cantidad de", html.Br(), "dinero", html.Br(), money])
        text3 = html.H5(["Promedio de", html.Br(), "acciones", html.Br(), ticketAvg])
        text4 = html.H5(
            ["Promedio de", html.Br(), "valor de accion", html.Br(), moneyAvg]
        )
    else:
        # Obtenemos estadisticas de un estado
        tickets = df["volume"].sum()
        money = df["close"].sum()
        tickets = str(tickets) if tickets != np.nan else "0"
        money = str(money) if money != np.nan else "0"
        text1 = html.H5(["Numero de", html.Br(), "boletos", html.Br(), tickets])
        text2 = html.H5(["Cantidad de", html.Br(), "dinero", html.Br(), money])
        text3 = html.H5(["Promedio de", html.Br(), "boletos", html.Br()])
        text4 = html.H5(["Promedio de", html.Br(), "dinero", html.Br()])
    fig = px.pie(
        df,
        values="volume",
        names="stock",
        color_discrete_sequence=px.colors.sequential.RdBu,
        title="Volumen de acciones vendidas del cuarto"
        + str(quarter[0])
        + " al "
        + str(quarter[1]),
    )
    return text1, text2, text3, text4, fig, message


# Funcion que realizara la parte dinamica del grafico de linea
@app.callback(
    [
        Output("histogramPlot", "figure"),
        Output("warning3", "displayed"),
    ],
    [Input("mean", "value"), Input("std", "value"), Input("ButtonHisto", "n_clicks")],
    State("inputBox2", "value"),
)
def updatePage2(n_clicks, mean, std, search):
    # Obtenemos el contexto de los controles
    ctx = dash.callback_context
    message = False
    status = False
    # Cargamos el dataframe de boletos vendidos
    df = pd.read_csv(path, sep=",", encoding="utf-8")
    df = df.query("quarter >= 1 and quarter <= 2")
    buttnoId = ctx.triggered[0]["prop_id"].split(".")[0]
    if buttnoId == "ButtonHisto":
        df = df.query("quarter >= 1 and quarter <= 2 and stock=='" + search + "'")
        if not (df.empty) and search != "":
            message = False
            status = True
        else:
            df = pd.read_csv(path, sep=",", encoding="utf-8")
            df = df.query("quarter >= 1 and quarter <= 2")
            message = True
            status = False
    # Se escogio otro control mean std
    else:
        if search != "":
            df = df.query("quarter >= 1 and quarter <= 2 and stock=='" + search + "'")
            df = df["close"].round()

            if not (df.empty):
                message = False
                status = True
            else:
                df = pd.read_csv(path, sep=",", encoding="utf-8")
                df = df["close"].round()
                message = True
                status = False
        else:
            status = False
    if status == False:
        # Obtenemos estadisticas de los stocks
        mean = df["close"].mean()
        std = df["close"].std()
        mean = str(mean) if mean != np.nan else "0"
        std = str(std) if std != np.nan else "0"
        # Creamos las casillas dinamicas
        text1 = html.H5(["Media", html.Br(), mean])
        text2 = html.H5(["Desviacion", html.Br(), "Estandar", html.Br(), std])
    fig = px.histogram(
        df,
        x="date",
        y="volume",
        color="stock",
        color_discrete_sequence=px.colors.sequential.RdBu,
    )
    return fig, message


@app.callback(

    Output("timeSeriesChart", "figure"),
    Input("ticker", "value"),
)
def updatePage3(ticker):
    # Cargamos el dataframe de boletos vendidos
    df = pd.read_csv(path, sep=",", encoding="utf-8")
    df = df.query("quarter >= 1 and quarter <= 2 and stock=='" + ticker + "'")
    # Creamos el data frame solo con las acciones de ticker
    fig = go.Figure(
        go.Ohlc(
            x=df["date"],
            open=df["open"],
            high=df["high"],
            low=df["low"],
            close=df["close"],
        )
    )

    return fig


# Funcion que realizara la parte dinamica del grafico de linea
@app.callback(
    [
        Output("candleGraph", "figure"),
        Output("warning5", "displayed"),
    ],
    [Input("buttonCandle", "n_clicks")],
    State("inputBoxCandle", "value"),
)
def updatePage4(n_clicks, search):
    # Obtenemos el contexto de los controles
    ctx = dash.callback_context
    message = False
    status = False
    # Cargamos el dataframe de boletos vendidos
    df = pd.read_csv(path, sep=",", encoding="utf-8")
    df = df.query("quarter >= 1 and quarter <= 2")
    buttnoId = ctx.triggered[0]["prop_id"].split(".")[0]
    if buttnoId == "ButtonHisto":
        df = df.query("quarter >= 1 and quarter <= 2 and stock=='" + search + "'")
        if not (df.empty) and search != "":
            message = False
            status = True
        else:
            df = pd.read_csv(path, sep=",", encoding="utf-8")
            df = df.query("quarter >= 1 and quarter <= 2")
            message = True
            status = False
    # Se escogio otro control mean std
    else:
        if search != "":
            df = df.query("quarter >= 1 and quarter <= 2 and stock=='" + search + "'")
            if not (df.empty):
                message = False
                status = True
            else:
                df = pd.read_csv(path, sep=",", encoding="utf-8")
                message = True
                status = False
        else:
            status = False
    if status == False:
        pass
    fig = go.Figure(
        go.Candlestick(
            x=df["date"],
            open=df["open"],
            high=df["high"],
            low=df["low"],
            close=df["close"],
        )
    )

    fig.update_layout(
        yaxis_title=search + " Stock Price",
    )
    return fig, message


# Se inicializa la aplicacion de dash
app.run_server(host="127.0.0.1", port="8053", debug=True)


# histograma
# https://plotly.com/python/histograms/


# son complementarios
# mapa de calor, muestra densidad

# grafica de pastel

# hilo que acutalice algo dentro del grafico...

# precio del dolar

# api de yahoo finance
