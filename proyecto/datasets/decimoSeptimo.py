#Librerias para trabajar con visualizaciones interactivas
import plotly
import plotly.express as px
#Librerias para crear un tablero con plotly
from jupyter_dash import JupyterDash
from dash import dcc
from dash import html
import dash
#Libreria para cambiar el diseño de un tablero en dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
#Libreria para manipulacion de datos con dataframes
import pandas as pd
import numpy as np
#Para manipulacion de fechas en controles de dash
from datetime import date

#Se añade un tema especifico CSS para el tablero de dash
external_stylesheets=[dbc.themes.CERULEAN]
#Se crea una aplicacion de dash
app = JupyterDash(__name__, external_stylesheets=external_stylesheets)
#Nombre del tablero dentro del navegador
app.title = "Decimoséptimo tablero interactivo"
#Contenedor principal del tablero
app.layout = html.Div([
    #Barra de titulo del tablero
    html.Div(children=[dbc.Col(html.H1(children="Mi decimoséptimo tablero en dash",className="ext-warning"))],
                className="navbar navbar-expand-lg navbar-dark bg-dark"),
    #Se añade en la primera fila con cuatro tipos de controles y un grafico
    
    dbc.Row([dbc.Col(children=[
        #Primer control (menu desplegable)
        html.Div(children=[
            html.Div(children=html.B(children=html.H4("Seleccionar color de grafico")),
                        className="alert alert-dismissible alert-success"),
            #Tipo de control
            dcc.Dropdown(id="dropDown",
                        clearable=False,
                        value="plasma",
                        style = {'font-size': '18px'},
                        options=[{"label": c, "value": c}for c in px.colors.named_colorscales()])],
            #Estilo
            style={"border":"2px black solid"},
            #Clase de control
            className="accordion-item"),
        
        #Segundo control (barra desplegable)
        html.Div(children=[
            html.Div(children=html.B(children=html.H4("Seleccionar periodo de tiempo")),
                        className="alert alert-dismissible alert-success"),
            #Tipo de control
            dcc.RangeSlider(id="rangeSlider",min=1957,max=2007,count=1,
                            value=[2007, 2007],allowCross=False,
                            marks={i: f'{i}' for i in ["1952", "1957",
                                                    "1962", "1967",
                                                    "1972", "1977",
                                                    "1982", "1987",
                                                    "1992", "1997",
                                                    "2002", "2007"]})],
            #Estilo
            style={"border":"2px black solid"},
            #Clase de control
            className="accordion-item"),

        #Tercer control (boton de opcion)
        html.Div(children=[
            html.Div(children=html.B(children=html.H4("Escoger tipo de busqueda")),
                        className="alert alert-dismissible alert-success"),
                #Tipo de control
                dcc.RadioItems(id="radioItem",
                                options=[{"label": "Continente", "value":"Continent"},{"label": "Pais", "value": "Country"},{"label": "Todo", "value": "All"}],
                                inputStyle={"margin-right": "10px"},
                                labelStyle={'width':'70%'},
                                style = {'width': '40%','font-size': '18px'},
                                value="All")],
                #Estilo
                style={"border":"2px black solid"},
                #Clase de control
                className="accordion-item"),

        #Cuarto control (casilla de verificacion)
        html.Div(children=[
            html.Div(children=html.B(children=html.H4("Escoger pais")),
                        className="alert alert-dismissible alert-success"),
            #Tipo de control
            dcc.Input(id="inputBox",
                        type="text",
                        disabled = True,
                        style = {'font-size': '18px'},
                        className="form-control"),
            html.Button("Enviar",
                        id="button",
                        disabled = True,
                        className="btn btn-info")],
            #Estilo
            style={"border":"2px black solid"},
            #Clase de control
            className="accordion-item")
    ],
    style={"height": "103vh",
        "border":"2px black solid",
        "padding-top": "5px",
        "padding-left": "20px"},
    #Clase de control sobre todos los botones
    className="toast show"),
    #Se añade en primera fila, segunda columna con areas de texto y grafico
    dbc.Col(html.Div(children=[
        dbc.Row([
            #Area de texto 1
            dbc.Col(html.Div(children=html.B(children= html.H4("Esperanza de vida")),
                    id="area1",
                    style={"border":"2px black solid",
                            "height": "25vh",
                            "width": "100%",
                            "display": "flex",
                            "align-items":"center",
                            "justify-content":"center"},
                    className="card text-white bg-primary mb-3")),
            #Area de texto 2
            dbc.Col(html.Div(children=html.B(children= html.H4("Cantidad de población")),
                    id="area2",
                    style={"border":"2px black solid",
                        "height": "25vh",
                        "width": "100%",
                        "display": "flex",
                        "align-items":"center",
                        "justify-content":"center"},
                    className="card text-white bg-success mb-3"))]),
        dbc.Row([
            #Area de texto 3
            dbc.Col(html.Div(children=html.B(children= html.H4("PIB")),
                    id="area3",
                    style={"border":"2px black solid",
                            "height": "25vh",
                            "width": "100%",
                            "display": "flex",
                            "align-items":"center",
                            "justify-content":"center"},
                    className="card text-white bg-danger mb-3")),
            #Area de texto 4
            dbc.Col(html.Div(children=html.B(children= html.H4("Años")),
                    id="area4",
                    style={"border":"2px black solid",
                        "height": "25vh",
                        "width": "100%",
                        "display": "flex",
                        "align-items":"center",
                        "justify-content":"center"},
                    className="card text-white bg-warning mb-3"))]),
            #Se añade un grafico debajo de las areas interactivas de texto
        dbc.Row([
            dbc.Col(html.Div(dcc.Graph(id="pieChart",
                                        style={"height": "47vh",
                                                "width": "100%"},
                                        config={"displayModeBar": False}),
                                        style={"border":"2px black solid"},
                                        #Tipo de elemento sobre el tablero
                                        className="modal-content",))])
        #Tipo de elemento sobre el tablero
        ],className="modal-content")),
    #Fin de la primera fila
    ]),
   #Se añade una segunda fila con un solo grafico
   dbc.Row([
          dbc.Col(html.Div(dcc.Graph(id="scatterPlot",
                                      config={"displayModeBar": False}),
                                      style={"border":"2px black solid"},
                                      #Tipo de elemento sobre el tablero
                                      className="modal-content",)),
    ]),
#Se cierra el contenedor de todo el tablero
])

#Funcion activadora que realizara la parte dinamica del tablero
@app.callback(
    [Output("area1", "children"),
     Output("area2", "children"),
     Output("area3", "children"),
     Output("area4", "children"),
     Output("inputBox", "disabled"),
     Output("button", "disabled"),
     Output("inputBox", "placeholder"),
     Output("pieChart", "figure"),
     Output("scatterPlot", "figure")],
    [Input("radioItem", "value"),
     Input("rangeSlider", "value"),
     Input("dropDown", "value"),
     Input("button", "n_clicks")],
    State("inputBox", "value"))

def updateArea(type,years,colorscale,n_clicks,search):
    ctx = dash.callback_context
    #Valores por default en caso de error
    text1=html.H4("Esperanza de vida")
    text2=html.H4("Cantidad de población")
    disable=True
    disable2=True
    value="Inserte su busqueda"
    #Revisamos si la pagina se crea por primera vez
    if not(ctx.triggered):
        title1="Distribución de población del mundo durante ,→"+str(years[0])+"-"+str(years[1])
        title2="Pob vs esperanza de vida en países del mundo durante ,→"+str(years[0])+"-"+str(years[1])
        df = px.data.gapminder().query("year == 2007")
        disable=True
        disable2=True
    #En caso de que pagina ya exista
    else:
        #Revisamos el nombre del boton que activo el evento
        buttonId = ctx.triggered[0]['prop_id'].split('.')[0]
        #Se utilizo la casilla de verificacion
        if buttonId == "radioItem":
            if (type=="All"):
                df = px.data.gapminder().query("year >= "+str(years[0])+" and year <= "+str(years[1]))
                title1="Distribución de población del mundo durante"+str(years[0])+"-"+str(years[1])
                title2="Pob vs esperanza de vida en países del mundo durante"+str(years[0])+"-"+str(years[1])
                disable=True
                disable2=True
            elif(type=="Continent"):
                df = px.data.gapminder().query("year >= "+str(years[0])+" and year <= "+str(years[1]))
                title1="Distribución de población del mundo durante ,→"+str(years[0])+"-"+str(years[1])
                title2="Pob vs esperanza de vida en países del mundo durante ,→"+str(years[0])+"-"+str(years[1])
                disable=False
                disable2=False
                value="Nombre del continente"
            else:
                df = px.data.gapminder().query("year >= "+str(years[0])+" and year <= "+str(years[1]))
                title1="Distribución de población del mundo durante"+str(years[0])+"-"+str(years[1])
                title2="Pob vs esperanza de vida en países del mundo durante"+str(years[0])+"-"+str(years[1])
                disable=False
                disable2=False
                value="Nombre del pais"
    #Se oprimio el boton de busqueda sobre continente o pais
        elif buttonId == "button":
            if(type=="Continent"):
                title1="Distribución de población de "+search+" durante"+str(years[0])+"-"+str(years[1])
                title2="Pob vs esperanza de vida de "+search+" durante"+str(years[0])+"-"+str(years[1])
                df = px.data.gapminder().query("continent =='"+search+"' and year >="+str(years[0])+" and year <= "+str(years[1]))
                disable=False
                disable2=False
            else:
                title1="Distribución de población en "+search+" durante ,→"+str(years[0])+"-"+str(years[1])
                title2="Pob vs esperanza de vida en "+search+" durante ,→"+str(years[0])+"-"+str(years[1])
                df = px.data.gapminder().query("country =='"+search+"' and year >= ,→"+str(years[0])+" and year <= "+str(years[1]))
                disable=False
                disable2=False
        #Se oprimio la barra de desplazamiento de años
        elif buttonId == "rangeSlider":
            if (type=="All"):
                title1="Distribución de población del mundo durante"+str(years[0])+"-"+str(years[1])
                title2="Pob vs esperanza de vida en países del mundo durante"+str(years[0])+"-"+str(years[1])
                df = px.data.gapminder().query("year >= "+str(years[0])+" and year<= "+str(years[1]))
                disable=True
                disable2=True
            elif(type=="Continent"):
                title1="Distribución de población de "+search+" durante ,→"+str(years[0])+"-"+str(years[1])
                title2="Pob vs esperanza de vida de "+search+" durante ,→"+str(years[0])+"-"+str(years[1])
                df = px.data.gapminder().query("continent =='"+search+"' and year >= ,→"+str(years[0])+" and year <= "+str(years[1]))
                disable=False
                disable2=False
            else:
                title1="Distribución de población en "+search+" durante ,→"+str(years[0])+"-"+str(years[1])
                title2="Pob vs esperanza de vida en "+search+" durante ,→"+str(years[0])+"-"+str(years[1])
                df = px.data.gapminder().query("country =='"+search+"' and year >= ,→"+str(years[0])+" and year <= "+str(years[1]))
                disable=False
                disable2=False
        #Se oprimio el menu desplegable de color
        elif buttonId == "dropDown":
            if (type=="All"):
                title1="Distribución de población del mundo durante"+str(years[0])+"-"+str(years[1])
                title2="Pob vs esperanza de vida en países del mundo durante"+str(years[0])+"-"+str(years[1])
                df = px.data.gapminder().query("year >= "+str(years[0])+" and year <= "+str(years[1]))
                disable=True
                disable2=True
            elif(type=="Continent"):
                title1="Distribución de población de "+search+" durante ,→"+str(years[0])+"-"+str(years[1])
                title2="Pob vs esperanza de vida de "+search+" durante ,→"+str(years[0])+"-"+str(years[1])
                df = px.data.gapminder().query("continent =='"+search+"' and year >= ,→"+str(years[0])+" and year <= "+str(years[1]))
                disable=False
                disable2=False
            else:
                title1="Distribución de población en "+search+" durante ,→"+str(years[0])+"-"+str(years[1])
                title2="Pob vs esperanza de vida en "+search+" durante ,→"+str(years[0])+"-"+str(years[1])
                df = px.data.gapminder().query("country =='"+search+"' and year >= ,→"+str(years[0])+" and year <= "+str(years[1]))
                disable=False
                disable2=False
    #Se crean las areas dinamicas y graficos con las opciones escogidas
    #Se ajustan valores en caso de busquedas erroneas
    lifeExp=round(df["lifeExp"].mean(),2)
    lifeExp="0" if pd.isnull(lifeExp) else str(lifeExp)
    pop=df["pop"].sum()
    pop=str(pop) if pop!=np.nan else "0"
    pib=round(df["gdpPercap"].sum(),2)
    pib="0" if pd.isnull(pib) else str(pib)
    #Se agregan los valores de las areas dinamicas
    text1=html.H4(["Esperanza de vida",
                    html.Br(),
                    lifeExp+"%"],
                style={'textAlign': 'center'})
    text2=html.H4(["Cantidad de población",
                    html.Br(),
                    pop],
                style={'textAlign': 'center'})
    text3=html.H4(["PIB",
                    html.Br(),
                    pib+"%"],
                    style={'textAlign': 'center'})
    text4=html.H4(["Años",
                    html.Br(),
                    str(years[0])+"-"+str(years[1])],
                    style={'textAlign': 'center'})
    #Se crean las visualizaciones
    fig1= px.pie(df,
                    values="pop",
                    hole=0.35,
                    names="country",
                    labels={"pop": "Cantidad de habitantes",
                            "country": "Pais"})
    fig1.update_traces(textinfo='none')
    fig1.update_layout(title=title1)
    fig2= px.scatter(df,
                        x="lifeExp",
                        y="pop",
                        color="gdpPercap",
                        color_continuous_scale=colorscale,
                        hover_name="country",
                        labels={"pop": "Cantidad de habitantes",
                                "lifeExp": "Esperanza de vida",
                                "gdpPercap": "Producto Interno Bruto",
                                "country": "Pais"})
    fig2.update_layout(title=title2)
    #Regresamos los cambios para que dash los impelemente en el tablero
    return text1,text2,text3,text4,disable,disable2,value,fig1,fig2
#Se ejecuta la aplicacion de dash en 'local host'
app.run_server(host="127.0.0.1", port="8050", debug=True)