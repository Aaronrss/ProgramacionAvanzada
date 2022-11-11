import numpy as np
import pandas as pd

# Read csv file
data = pd.read_csv("dow_jones_index/dow_jones_index.data", encoding='unicode_escape')
print(data.head())

# create dataframe from csv file and use column names
df = pd.DataFrame(data)
# print dataframe
print(df)
print(type(df))

# print column names
print(df.columns)

# print column names and types
print(df.dtypes)

# print first 5 rows complete printed
print(df.head())


#usar display en lugar de print para ver todo el dataframe

# hacer dos tableros de datos con el de medicamentos y stocks. 