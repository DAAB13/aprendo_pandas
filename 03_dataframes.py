#%%
import pandas as pd


#%%
datos_diccionario = {
    'nombre': ['Argentina', 'Brasil', 'Chile', 'Colombia', 'Ecuador', 'Paraguay', 'Peru'],
    'capital': ['Buenos Aires', 'Brasilia', 'Santiago de Chile', 'Bogotá', 'Quito', 'Asunción', 'Lima'],
    'poblacion': [45380000, 212600000, 19120000, 50880000, 17640000, 7133000, 32970000],
    'superficie_km2': [2780000, 8516000, 756950, 1143000, 283560, 406752, 1285216]
}
datos_diccionario

#%%
paises = pd.DataFrame(datos_diccionario)
# paises
# paises.head()
# paises.tail(3)
paises[0 : 4]

#%%
# crear una tabla con las columnas "nombre" y "poblacion"
tabla_1 = pd.DataFrame(datos_diccionario, columns = ["nombre", "poblacion"]) 
tabla_1

#%%

# nombre como índice
tabla_2 = pd.DataFrame(
  datos_diccionario,
  index = datos_diccionario['nombre'], 
  columns = ['capital', 'poblacion', 'superficie_km2']
)
tabla_2

#%%
tabla_2.loc[["Argentina", "Brasil"], ["capital", "poblacion"]]


#%%
# obtener la indormación de los paises con una superdicie 
# mayor a 1,000,000 km2 utlizando loc

tabla_2["superficie_km2"] > 1000000
tabla_2.loc[tabla_2["superficie_km2"] > 1000000]


#%%
#cambiar capital de brasil a "Río de Janeiro"
tabla_2.loc["Brasil", "capital"] = "Río de Janeiro"
tabla_2

#%% obterner los datos de la fila de la tercera posición - iloc
tabla_2.iloc[2]

#%% Obterner todos los datos de la columna de la 2da posición - iloc
tabla_2.iloc[:, 1]
# %% obterner datos de las filas (tercera y cuarta posición - iloc)
tabla_2.iloc[[2, 3]]



# %% obterner la columna población
tabla_2.poblacion
# %% obtener los valores de la columna 'poblacion'
tabla_2.poblacion.values
# %% obtener el nombre la columna 'poblacion'
tabla_2.poblacion.name


# %% obtener el valor mínimo de la columna poblacion
tabla_2.poblacion.min()
# %% obtener la desviación estandar de 'poblacion'
tabla_2.poblacion.std()


# %% obtener dataframe con columnas 'poblacion' y 'capital'
tabla_2[["poblacion", "capital"]]


# %% paises con una población mayor a 50,000,000
tabla_2[tabla_2.poblacion > 50000000]

#%% Agregar una columna al DataFrame 
# que contenga la poblacion en millones
tabla_2["pob. en mill."] = tabla_2.poblacion / 1000000
tabla_2





###------------apply----------------------------------------------
# %% agregar columna usando apply
#definimos una función
def millones(x):
  return x / 1000000
tabla_2["mill apply"] = tabla_2.poblacion.apply(millones)
tabla_2

# %% Agregar columna 'densidad' (ratio de población por cada km2)
def densidad(df):
  return df["poblacion"] / df["superficie_km2"]
tabla_2["densidad"] = tabla_2.apply(densidad, axis=1)
tabla_2






###--------------del DataFrame a archivos csv y xlsx-------------
# %% Guardar en csv
tabla_2.to_csv(".\csv")

# %% Gruardar en xlsx
tabla_2.to_excel(
  ".\excel.xlsx",
  sheet_name = "paises",
  index_label = "pais"
)
# %% leer archivo csv
paises_csv = pd.read_csv("./csv")
paises_csv
# %% leer archivo de excel xlsx
paises_excel = pd.read_excel("./excel.xlsx", index_col = "pais")
paises_excel

