# Libreria para manejo de archivos json
import json

# Librerias para trabajar con visualizaciones interactivas
import plotly
import plotly.express as px

# Librerias para crear un tablero con plotly
from jupyter_dash import JupyterDash
from dash import dcc
from dash import html
import dash

# Libreria para cambiar el diseño de un tablero en dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

# Libreria para manipulacion de datos con dataframes
import pandas as pd
import numpy as np

# Para manipulacion de fechas en controles de dash
from datetime import date

"""
Montamos el path
"""

# Obtenemos el path del archivo

path = (
    r"/Users/blckwlf/Documents/GitHub/ProgramacionAvanzada/proyecto/datasets/cinepolis/"
)

# Creacion de un tablero para la visualizacion inicial
def page0():
    return html.Div(
        [
            html.Div(
                children=[
                    html.Div(
                        children=html.B(children=html.H4("Descripción del reto")),
                        className="alert alert-dismissible alert-success",
                    ),
                    html.P(
                        "El objetivo del reto Cinépolis es el de detectar a personal,de la compañía que\n realiza transacciones fraudulentas a través del programa de lealtad de tarjetas\n al adjudicarse ventas de los clientes que no redimen sus puntos."
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
                    ),
                    html.P(
                        "En primera instancia, se hace uso de visualizaciones/gráficos sobre los datos de Cinépolis\n para detectar elementos anómalos en la información a través de la creación de varias\n hipótesis sustentadas por una narrativa de datos y elementos básicos de estadística."
                    ),
                ],  # Clase de control
                className="accordion-item",
            ),
            html.Div(
                children=[
                    html.Div(
                        children=html.B(children=html.H4("Aprendizaje de maquina")),
                        className="alert alert-dismissible alert-success",
                    ),
                    html.P(
                        "Después de un análisis inicial, se utilizan técnicas de descubrimiento de patrones mas\n sofisticadas basadas en el aprendizaje supervisado, no supervisado y semi-supervisado\n con el propósito de encontrar transacciones fraudulentas a mayor granularidad en los\n millones de registros provistos por Cinépolis."
                    ),
                ],
                # Clase de control
                className="accordion-item",
            ),
            # Se cierra el contenedor de todo el tablero
        ]
    )


# Creacion de un tablero para una visualizacion de tipo mapa
def page1():
    return html.Div(
        [
            # Barra de titulo del tablero
            html.Div(
                children=[
                    html.H1(
                        children="Mapa interactivo de Mexico",
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
                                                "Seleccionar color de grafico"
                                            )
                                        ),
                                        className="alert alert-dismissible alert-success",
                                    ),
                                    # Primer control (menu desplegable)
                                    dcc.Dropdown(
                                        id="dropDown1",
                                        clearable=False,
                                        style={"font-size": "18px"},
                                        options=[
                                            {"label": c, "value": c}
                                            for c in px.colors.named_colorscales()
                                        ],
                                    ),
                                ],
                                # Clase de control
                                className="accordion-item",
                            ),
                            html.Div(
                                children=[
                                    html.Div(
                                        children=html.B(
                                            children=html.H4("Escoger estado")
                                        ),
                                        className="alert alert-dismissible alert-success",
                                    ),
                                    # Segundo control (caja de texto)
                                    dcc.Input(
                                        id="inputBox1",
                                        type="text",
                                        disabled=False,
                                        value="",
                                        placeholder="Nombre de estado de México",
                                        style={"font-size": "18px"},
                                        className="form-control",
                                    ),
                                    # Tercer control (boton clasico)
                                    html.Button(
                                        "Enviar",
                                        id="button1",
                                        disabled=False,
                                        className="btn btn-info",
                                    ),
                                    # Cuarto control (mensaje de alerta)
                                    dcc.ConfirmDialog(
                                        id="warning",
                                        message="Seleccione un estado valido, se mostrarán todos los estados",
                                    ),
                                ],
                                # Clase de control
                                className="accordion-item",
                            ),
                        ],
                        style={"height": "57v", "margin-left": "11px", "margin": "4px"},
                    ),
                    # Se añade en primera fila una segunda columna con informacion
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
                                                            "Numero de",
                                                            html.Br(),
                                                            "Transacciones",
                                                        ]
                                                    )
                                                ),
                                                id="area1",
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
                                                            "Promedio de",
                                                            html.Br(),
                                                            "transacciones",
                                                        ]
                                                    )
                                                ),
                                                id="area2",
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
                                                        ["Mas", "transacciones"]
                                                    )
                                                ),
                                                id="area3",
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
                                                            "Menos",
                                                            html.Br(),
                                                            "transacciones",
                                                        ]
                                                    )
                                                ),
                                                id="area4",
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
                            dcc.Graph(id="mapPlot", config={"displayModeBar": False}),
                            style={"border": "2px black solid"},
                            # Tipo de elemento sobre el tablero
                            className="modal-content",
                        )
                    ),
                ]
            ),
            # Se cierra el contenedor de todo el tablero
        ]
    )


# Creacion de un tablero para una visualizacion de tipo linea
def page2():
    return html.Div(
        [
            # Barra de titulo del tablero
            html.Div(
                children=[
                    html.H1(
                        children="Cantidad de boletos vendidos en México",
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
                                                "Seleccionar rango de años"
                                            )
                                        ),
                                        className="alert alert-dismissible alert-success",
                                    ),
                                    # Primer control (menu desplegable)
                                    dcc.RangeSlider(
                                        id="rangeSlider1",
                                        min=2020,
                                        max=2022,
                                        count=1,
                                        value=[2020, 2022],
                                        allowCross=False,
                                        marks={i: f"{i}" for i in [2020, 2021, 2022]},
                                    ),
                                ],
                                # Clase de control
                                className="accordion-item",
                            ),
                            html.Div(
                                children=[
                                    html.Div(
                                        children=html.B(
                                            children=html.H4("Escoger estado")
                                        ),
                                        className="alert alert-dismissible alert-success",
                                    ),
                                    # Segundo control (caja de texto)
                                    dcc.Input(
                                        id="inputBox2",
                                        type="text",
                                        disabled=False,
                                        value="",
                                        placeholder="Nombre de estado de México",
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
                                        message="Seleccione un estado ,→valido, se mostrarán todos los estados",
                                    ),
                                ],
                                # Clase de control
                                className="accordion-item",
                            ),
                        ],
                        style={"height": "57v", "margin-left": "11px", "margin": "4px"},
                    ),
                    # Se añade en la primera fila una segunda columna con areas de texto y un ,→grafico
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
                                                            "Numero de",
                                                            html.Br(),
                                                            "boletos",
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
                            dcc.Graph(id="linePlot", config={"displayModeBar": False}),
                            style={"border": "2px black solid"},
                            # Tipo de elemento sobre el tablero
                            className="modal-content",
                        )
                    ),
                ]
            ),
            # Se cierra el contenedor de todo el tablero
        ]
    )


# Creacion de un tablero para una visualizacion de dispersion
def page3():
    df = pd.read_csv(path + "usuarios.csv", sep=",", encoding="utf-8")
    df["year"] = df["year"].astype(str)
    df.query("ticketsAmount > 2000 and numberTickets > 10")
    fig1 = px.scatter(
        df,
        x="member_id",
        y="ticketsAmount",
        hover_name="state",
        size="numberTickets",
        size_max=30,
        color="year",
        labels={
            "year": "Año",
            "member_id": "Clientes",
            "numberTickets": "Cantidad de boletos vendidos",
            "ticketsAmount": "Costo de la transacción",
        },
        title="Distribución de clientes con respecto a costo y cantidad de boletos",
    )
    fig1.update_xaxes(showticklabels=False)
    return html.Div(
        [
            # Barra de titulo del tablero
            html.Div(
                children=[
                    html.H1(
                        children="Usuarios sospechosos en los estados más relevantes de México",
                        style={"color": "black", "height": "57v"},
                    )
                ]
            ),
            # Visualizacion de dispersion
            html.Div(
                dcc.Graph(id="linePlot", figure=fig1, config={"displayModeBar": False}),
                style={"border": "2px black solid"},
                # Tipo de elemento sobre el tablero
                className="modal-content",
            ),
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
        html.Img(
            src="cinePolis.png",
            style={
                "height": "20%",
                "width": "68%",
                "padding-left": "53px",
            },
        ),
        html.H2("Cinépolis", className="display-4"),
        html.Hr(),
        html.P("Tablero interactivo", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Reto Cinépolis", href="/", active="exact"),
                dbc.NavLink("Gráfico de mapa", href="/page-1", active="exact"),
                dbc.NavLink("Gráfico de línea", href="/page-2", active="exact"),
                dbc.NavLink("Gráfico de dispersión", href="/page-3", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)
# Creacion del tablero principal que se actualizara con cada opcion escogida
content = html.Div(id="page-content", style=CONTENT_STYLE)
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


# Funcion activadora para unir cada subtablero con la pagina principal
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return page0()
    elif pathname == "/page-1":
        return page1()
    elif pathname == "/page-2":
        return page2()
    elif pathname == "/page-3":
        return page3()
    # Si el usuario usa una página diferente, se enviara un mensaje 404
    return html.Div(
        [
            html.H1("404: Pagina no encontrada", className="text-danger"),
            html.Hr(),
            html.P(f"La URL {pathname} no es reconocida..."),
        ],
        className="p-3 bg-light rounded-3",
    )


# Creacion de un decorador para la interaccion con el tablero
# Funcion que realizara la parte dinamica del mapa
@app.callback(
    [
        Output("area1", "children"),
        Output("area2", "children"),
        Output("area3", "children"),
        Output("area4", "children"),
        Output("mapPlot", "figure"),
        Output("warning", "displayed"),
    ],
    [Input("dropDown1", "value"), Input("button1", "n_clicks")],
    State("inputBox1", "value"),
)
def updatePage2(colorscale, n_clicks, search):
    # Obtenemos el contexto de los controles
    ctx = dash.callback_context
    message = False
    status = False
    # Cargamos el dataframe de estados/transacciones completo
    df = pd.read_csv(path + "estados.csv", sep=",", encoding="utf-8")
    # Lat/lon estados de mexico
    geoFile = open(path + "mexico.json")
    dataMexico = json.load(geoFile)
    # Revisamos el nombre del control que activo el evento
    buttonId = ctx.triggered[0]["prop_id"].split(".")[0]
    # Se escogio el boton de carga del mapa
    if buttonId == "button1":
        # Cargamos el dataframe de un estado especifico
        df = df.query("state=='" + search + "'")
        if not (df.empty) and search != "":
            message = False
            status = True
        else:
            df = pd.read_csv(path + "estados.csv", sep=",", encoding="utf-8")
            message = True
            status = False
        # Se escogio otro control
    else:
        if search != "":
            df = df.query("state=='" + search + "'")
            if not (df.empty):
                message = False
                status = True
            else:
                df = pd.read_csv(path + "estados.csv", sep=",", encoding="utf-8")
                message = True
                status = False
        else:
            status = False
    if status == False:
        # Obtenemos estadisticas de los estados
        numero = df["numerTransactions"].sum()
        promedio = round(df["numerTransactions"].mean(), 2)
        alto = df["numerTransactions"].iloc[0]
        bajo = df["numerTransactions"].iloc[-1]
        numero = str(numero) if numero != np.nan else "0"
        promedio = str(promedio) if promedio != np.nan else "0"
        alto = str(alto) if alto != np.nan else "0"
        bajo = str(bajo) if bajo != np.nan else "0"
        # Creamos las casillas dinamicas
        text1 = html.H5(["Numero de", html.Br(), "Transacciones", html.Br(), numero])
        text2 = html.H5(
            ["Promedio de", html.Br(), "transacciones", html.Br(), promedio]
        )
        text3 = html.H5(["Mas", html.Br(), "transacciones", html.Br(), alto])
        text4 = html.H5(["Menos", html.Br(), "transacciones", html.Br(), bajo])
    else:
        numero = df["numerTransactions"].sum()
        numero = str(numero) if numero != np.nan else "0"
        # Creamos las casillas dinamicas
        text1 = html.H5(["Numero de", html.Br(), "Transacciones", html.Br(), numero])
        text2 = html.H5(["Promedio de", html.Br(), "transacciones", html.Br()])
        text3 = html.H5(["Mas", html.Br(), "transacciones", html.Br()])
        text4 = html.H5(["Menos", html.Br(), "transacciones", html.Br()])

    # Creamos el grafico de mapa
    fig = px.choropleth_mapbox(
        data_frame=df,
        # Tipo de mapa
        mapbox_style="carto-positron",
        # Nivel maximo de ampliacion/reduccion sobre el grafico
        zoom=3,
        # Dataframe con informacion de los estados y porcentajes
        geojson=dataMexico,
        # Opacidad del mapa
        opacity=0.7,
        # Titulo que aparecera cuando el cursor este sobre el estado
        hover_name=df["numerTransactions"],
        # Latitud y longitud donde se centrara el mapa al visualizar
        center={"lat": 19.408351, "lon": -99.155119},
        # Nombre de los estados de la republica a mapear
        locations=df["state"],
        # Ruta al campo del archivo json antes con latitudes y longitudes
        featureidkey="properties.name",
        # El color depende de los porcentajes creados de manera aleatoria
        color=df["numerTransactions"],
        # Se agrega el color del menu desplegable
        color_continuous_scale=colorscale,
        labels={
            "numerTransactions": "Número de transacciones",
            "state": "Nombre de estado",
        },
        title="Número de transacciones en los distintos estados de la republica Mexicana (2020-2022)",
    )
    fig.update_geos(
        showcountries=True, showcoastlines=True, showland=True, fitbounds="locations"
    )

    return text1, text2, text3, text4, fig, message


# Creacion de un decorador para la interaccion con el tablero
# Funcion que realizara la parte dinamica del grafico de linea
@app.callback(
    [
        Output("area5", "children"),
        Output("area6", "children"),
        Output("area7", "children"),
        Output("area8", "children"),
        Output("linePlot", "figure"),
        Output("warning2", "displayed"),
    ],
    [Input("rangeSlider1", "value"), Input("button2", "n_clicks")],
    State("inputBox2", "value"),
)
def updatePage2(year, n_clicks, search):
    # Obtenemos el contexto de los controles
    ctx = dash.callback_context
    message = False
    status = False
    # Cargamos el dataframe de boletos vendidos
    df = pd.read_csv(path + "boletos.csv", sep=",", encoding="utf-8")
    df = df.query("year >= " + str(year[0]) + " and year <= " + str(year[1]))
    # Revisamos el nombre del control que activo el evento
    buttonId = ctx.triggered[0]["prop_id"].split(".")[0]
    # Se escogio el boton de carga del mapa
    if buttonId == "button2":
        # Cargamos el dataframe de un estado especifico
        df = df.query(
            "year >= "
            + str(year[0])
            + " and year <= "
            + str(year[1])
            + "and state=='"
            + search
            + "'"
        )
        if not (df.empty) and search != "":
            message = False
            status = True
        else:
            df = pd.read_csv(path + "boletos.csv", sep=",", encoding="utf-8")
            df = df.query("year >= " + str(year[0]) + " and year <= " + str(year[1]))
            message = True
            status = False
    # Se escogio otro control
    else:
        if search != "":
            df = df.query(
                "year >= "
                + str(year[0])
                + " and year <= "
                + str(year[1])
                + "and state=='"
                + search
                + "'"
            )
            if not (df.empty):
                message = False
                status = True
            else:
                df = pd.read_csv(path + "boletos.csv", sep=",", encoding="utf-8")
                df = df.query(
                    "year >= " + str(year[0]) + " and year <= " + str(year[1])
                )
                message = True
                status = False
        else:
            status = False
    if status == False:
        # Obtenemos estadisticas de los estados
        tickets = df["numberTickets"].sum()
        money = df["ticketsAmount"].sum()
        ticketAvg = round(df["numberTickets"].mean(), 2)
        moneyAvg = round(df["ticketsAmount"].mean(), 2)
        tickets = str(tickets) if tickets != np.nan else "0"
        money = str(money) if money != np.nan else "0"
        ticketAvg = str(ticketAvg) if ticketAvg != np.nan else "0"
        moneyAvg = str(moneyAvg) if moneyAvg != np.nan else "0"
        # Creamos las casillas dinamicas
        text1 = html.H5(["Numero de", html.Br(), "boletos", html.Br(), tickets])
        text2 = html.H5(["Cantidad de", html.Br(), "dinero", html.Br(), money])
        text3 = html.H5(["Promedio de", html.Br(), "boletos", html.Br(), ticketAvg])
        text4 = html.H5(["Promedio de", html.Br(), "dinero", html.Br(), moneyAvg])
    else:
        # Obtenemos estadisticas de un estado
        tickets = df["numberTickets"].sum()
        money = df["ticketsAmount"].sum()
        tickets = str(tickets) if tickets != np.nan else "0"
        money = str(money) if money != np.nan else "0"
        text1 = html.H5(["Numero de", html.Br(), "boletos", html.Br(), tickets])
        text2 = html.H5(["Cantidad de", html.Br(), "dinero", html.Br(), money])
        text3 = html.H5(["Promedio de", html.Br(), "boletos", html.Br()])
        text4 = html.H5(["Promedio de", html.Br(), "dinero", html.Br()])
    fig = px.line(
        df,
        x="month",
        y="numberTickets",
        color="state",
        facet_col="year",
        hover_name="state",
        labels={
            "year": "Año",
            "numberTickets": "Cantidad de boletos vendidos",
            "month": "Mes",
            "state": "Estado",
        },
        title="Numero de boletos sobre estados de la república mexicana de ,→"
        + str(year[0])
        + " a "
        + str(year[1]),
    )
    return text1, text2, text3, text4, fig, message


# Se inicializa la aplicacion de dash
app.run_server(host="127.0.0.1", port="8055", debug=True)
