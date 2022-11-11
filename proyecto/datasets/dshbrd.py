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
import pandas as pd
from IPython.display import display

#Se carga un dataframe con informacion de paises para dash
df = px.data.gapminder()
print("Dataframe del conjunto de datos de paises para dash:")
#Se muestra la informacion a modo de ejemplo
display(df)

#Se carga un dataframe con informacion de paises de America para dash
df = px.data.gapminder().query("continent == 'Americas'")
#Se crea una aplicacion de dash
app = JupyterDash(__name__)
#Se crea el primer grafico en plotly express
fig1 = px.pie(df,
              values='pop',
              names='country',
              labels={"pop": "Cantidad de habitantes",
                    "country": "Pais"},
              title="Porcentaje de población en los países de América")
#Se crea el segundo grafico en plotly express
fig2 = px.scatter(df,
              x='lifeExp',
              y='pop',
              color="country",
              labels={"pop": "Cantidad de habitantes",
                      "lifeExp": "Esperanza de vida",
                      "country": "Pais"},
              title="Distribución de población vs esperanza de vida en algunos,→países de América")
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
        dcc.Graph(figure=fig2),
] )
#Se ejecuta la aplicacion de dash en 'local host'
app.run_server(host="127.0.0.1", port="8050", debug=True)