# Tarea5
import numpy as np
import pandas as pd

# 1. Crear un objeto Series a partir de una lista, numpy array y diccionario
# 1.1 Lista
print("1.1 Inicizalizando un objeto Series a partir de una lista")
lista = [1, 2, 3, 4, 5]
print(lista)
print(type(lista))
obj = pd.Series(lista)
print(obj)
print("-----------------------")

print("1.2 Inicializar un objeto Series con un numpy array")
# 1.2 Numpy array
array = np.array([1, 2, 3, 4, 5])
print(array)
print(type(array))
obj = pd.Series(array)
print(obj)
print("-----------------------")

print("1.3 Inicizando con valores e indices especificos")
# 1.3 Valores e índices
valores = [1, 2, 3, 4, 5]
indices = ['a', 'b', 'c', 'd', 'e']
indices.reverse()
print(valores)
print(type(valores))
print(indices)
print(type(indices))
obj = pd.Series(valores, indices)
print(obj)
print("-----------------------")

print("1.4 Inicializando con diccionario")
# 1.4 Diccionario
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(diccionario)
print(type(diccionario))
obj = pd.Series(diccionario)
print(obj)
print("-----------------------")

print("1.5 Declarando serie vacia y agregando datos con at")
# 1.5 Serie vacía
obj = pd.Series()
print(obj)
obj.at[0] = "Hola"
obj.at[1] = "Mundo"
obj.at[2] = "!"
print(obj)
print("-----------------------")

print("1.6 Imprimir valores por indice clasicos, especificos, rangos y listas")
# 1.6 Serie con índices de fecha
fechas = pd.date_range('20130101', periods=6)
print(fechas)
print(type(fechas))
obj = pd.Series(np.random.randn(6), index=fechas)
print(obj)
print("Elemento 1: ", obj[0])
print("Elemento 2: ", obj["20130102"])
print("Ultimo elemento: ", obj[-1])
print("Cortar principio:\n", obj[0:3])
print("Cortar final:\n", obj[-3:])
print("Lista de indices:\n", obj[["20130102", "20130104"]])
print("-----------------------")

print("1.7 Añadir datos a una serie")
# 1.7 Añadir datos a una serie
obj = pd.Series([1, 2, 3, 4, 5])
print(obj)
obj[5] = 'seis'
obj[6] = 'siete'
obj[7] = 'ocho'
print(obj)

# añadir datos con append
obj = obj.append(pd.Series([9, 10], index=["ocho","nueve"]))
print(obj)
print("-----------------------")

print("1.8 Eliminar datos de una serie")
# 1.8 Eliminar datos de una serie
obj = pd.Series([0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610])
print(obj)
obj = obj.drop(labels=[0, 2, 4, 6, 8, 10, 12, 14])
print(obj)

print("1.9 Cambiar datos de una serie")
# 1.9 Cambiar datos de una serie
obj = pd.Series([1, 2, 3, 4, 5, 6])
print(obj)
print("1.9.1 Cambiar datos por indice")
obj[0] = 0
obj[2] = 1
obj[4] = 0
print(obj)
print("1.9.2 Cambiar datos de una serie con update")
obj.update(pd.Series([10, 11, 100], index=[1, 3, 5]))
print(obj)
print("-----------------------")

print("1.10 Obtener estadisticas de una serie EXTRA")
# 1.9 Obtener estadísticas de una serie
obj = pd.Series([0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610])
print(obj)
print("Media: ", obj.mean())
print("Mediana: ", obj.median())
print("Moda: ", obj.mode())
print("Desviación estándar: ", obj.std())
print("Varianza: ", obj.var())
print("Mínimo: ", obj.min())
print("Máximo: ", obj.max())
print("Suma: ", obj.sum())
print("Cuenta: ", obj.count())
print("Cuantil 0.25: ", obj.quantile(0.25))
print("Cuantil 0.5: ", obj.quantile(0.5))
print("Cuantil 0.75: ", obj.quantile(0.75))
print("-----------------------")

print("2.0 Crear DataFrame")
# 2.0 Crear DataFrame
datos = {'Nombre': ['Juan', 'Pedro', 'Maria', 'Jose', 'Luis'],'Edad': [24, 13, 53, 33, 43],'Pais': ['Mexico', 'Colombia', 'Argentina', 'Chile', 'Peru']}
df = pd.DataFrame(datos)
print(df)
print("-----------------------")

print("2.1 Crear DataFrame con indices predefinidos")
# 2.1 Crear DataFrame con índices predefinidos
datos = {'Nombre': ['Juan', 'Pedro', 'Maria', 'Jose', 'Luis'],'Edad': [24, 13, 53, 33, 43],'Pais': ['Mexico', 'Colombia', 'Argentina', 'Chile', 'Peru']}
df = pd.DataFrame(datos, columns=['Pais', 'Nombre', 'Edad'])
print(df)
print("-----------------------")

print("2.2 Crear DataFrame con indices predefinidos y con datos faltantes")
# 2.2 Crear DataFrame con índices predefinidos y con datos faltantes
datos = {'Nombre': ['Juan', 'Pedro', 'Maria', 'Jose', 'Luis'],'Edad': [24, 13, 53, 33, 43],'Pais': ['Mexico', 'Colombia', 'Argentina', 'Chile', 'Peru']}
df = pd.DataFrame(datos, columns=['Pais', 'Nombre', 'Edad', 'Sexo'])
print(df)
print("-----------------------")

print("2.3 Crear DataFrame vacio y añadir datos")
# 2.3 Crear DataFrame vacío y añadir datos
df = pd.DataFrame()
print(df)
print("2.3.1 Crear DataFrame vacio y con etiquetas")
df = pd.DataFrame(columns=['Pais', 'Nombre', 'Edad', 'Sexo'])
print(df)

print("2.3.2 Crear DataFrame vacio con etiquetas e indices")
df = pd.DataFrame(columns=['Pais', 'Nombre', 'Edad', 'Sexo'], index=['a', 'b', 'c', 'd', 'e'])
print(df)
print("-----------------------")

print("2.4 Acceder a datos de un DataFrame")
# 2.4 Acceder a datos de un DataFrame
datos = {'Nombre': ['Juan', 'Pedro', 'Maria', 'Jose', 'Luis'],'Edad': [24, 13, 53, 33, 43],'Pais': ['Mexico', 'Colombia', 'Argentina', 'Chile', 'Peru']}
print(datos)
df = pd.DataFrame(datos, columns=['Pais', 'Nombre', 'Edad', 'Sexo'])
print(df)
print(df['Nombre'])
print(type(df['Nombre']))
print(df.Edad)
print(type(df.Edad))
print(df[['Nombre', 'Edad']])
print(type(df[['Nombre', 'Edad']]))
print("-----------------------")

print("2.5 Recuperar como lista/diccionario por loc e iloc")
# 2.5 Recuperar como lista/diccionario por loc e iloc
datos = {'Nombre': ['Juan', 'Pedro', 'Maria', 'Jose', 'Luis'],'Edad': [24, 13, 53, 33, 43],'Pais': ['Mexico', 'Colombia', 'Argentina', 'Chile', 'Peru']}
df = pd.DataFrame(datos, columns=['Pais', 'Nombre', 'Edad', 'Sexo'], index=['a', 'b', 'c', 'd', 'e'])
print(df)
print("2.5.1 Elementos de la fila 1")
print(df[['Nombre', 'Edad']]['a':'a'])
print(type(df[['Nombre', 'Edad']]['a':'a']))

print("2.5.2 Elementos de la fila 1 columna Pais")
print(df['Pais']['a':'a'])
print(type(df['Pais']['a':'a']))

print("2.5.3 Elementos de la fila 3")
print(df[['Nombre', 'Edad']][:'c'])
print(type(df[['Nombre', 'Edad']][:'c']))

#funcion loc
print("2.5.4 Elementos de la fila 3 con loc")
print(df.loc[['c']])
print(type(df.loc[['c']]))
print("2.5.5 Elementos de la fila 3 columna Nombre con loc")
print(df.loc[['c'], ['Nombre']])
print(type(df.loc[['c'], ['Nombre']]))
print("2.5.6 Elementos de la fila 1 a 3 con loc")
print(df.loc['a':'c'])
print(type(df.loc['a':'c']))

#funcion iloc




