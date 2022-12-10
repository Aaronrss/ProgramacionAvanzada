# Librerias basicas.
from IPython.display import display
#Librerias para trabajar con visualizaciones interactivas
import plotly
import plotly.express as px
#Librerias para crear un tablero con plotly
from jupyter_dash import JupyterDash
from dash import dcc
from dash import html
#Libreria para cambiar el diseño de un tablero en dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
#Libreria para manipulacion de datos con dataframes
import numpy as np
import pandas as pd


# Read data file

df = pd.read_csv("./proyecto/datasets/dow_jones_index/dow_jones_index.data", encoding='unicode_escape')

""" 
#usar display en lugar de print para ver todo el dataframe
display(df.head())
# Imprimir una linea de separacion del tamaño de la pantalla
print("-"*120)
display(df)
print("-"*120)
print(type(df))
print("-"*120)
# print column names
print(df.columns)
print("-"*120)
# print column names and types
print(df.dtypes)
print("-"*120) """


external_stylesheets=[dbc.themes.CERULEAN]
#Se crea una aplicacion de dash
app = JupyterDash(__name__, external_stylesheets=external_stylesheets)

#Nombre del tablero dentro del navegador
app.title = "Quinto tablero interactivo"

#Se crea el primer grafico en plotly express
fig1 = px.bar(df, x="stock", y="high", color="stock", barmode="group", title="Precios de las acciones de la bolsa de valores")

#Se define el estilo del tablero
app.layout = html.Div(
    children=[
        #Se crea un encabezado en el tablero
        html.H1(children="Mi primer tablero en dash",),
        #Se agrega un parrafo despues del encabezado
        html.P(
           children="Creación de dos visualizaciones dentro "
            "de un tablero de dash pero sin "
            "ninguna interactividad superior al de las figuras",
),
        #Se añaden los graficos dentro del tablero/pagina de dash
        dcc.Graph(figure=fig1),
] )
#Se ejecuta la aplicacion de dash en 'local host'
app.run_server(host="127.0.0.1", port="8050", debug=True)