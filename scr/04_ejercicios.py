#%%
import pandas as pd
altura = [166, 159, 168, 173, 162, 178]
altura

# %% Ejercicio 2 - obtener la altura max
serie_altura = pd.Series(altura)
serie_altura.max()


# %% Ejercicio 3 - obtener las alturas superiores a 165 cm
serie_altura[serie_altura > 165]

# %% Ejercicio 4 - calcular la altura en metros
serie_altura / 100



# %% Ejercicio 5 - crear un dataframe
# y utilizar la columna flor como índice
datos={
    "flor":["Rosa", "Tulipan", "Hortensia", "Anturio", "Alstroemeria", "Girasol", "Gerbera"],
    "precio":[12, 15, 9, 18, 21, 13, 18],
    "stock":[2900, 2300, 1800, 1900, 1700, 2500, 2200]
}
floreria = pd.DataFrame(
  datos,
  index = datos["flor"], #columna flor como índice
  columns = ["precio", "stock"] #escoger las columnas que deben aparecer 
)
floreria



# %% Ejericio 6 - obterner el precio de rosas y hortensias
# utilizando el df anterior
floreria.loc[["Rosa", "Hortensia"], ["precio"]]



# %% Ejercicio 7 - obtener información sobre flores en la posición 2 y 3.
floreria.iloc[[1,2]]

# %% Ejercicio 8 - Obtener datos de la columna 'precio'
floreria[["precio"]]

# %% Ejercicio 9 - obtener el precio promedio de las flores
#floreria.precio.mean()
floreria['precio'].mean()

# %% Ejercicio 10 - obtener el stock de las flores superiores a 2000
floreria[floreria.stock > 2000]

# %% Calcular el precio de las flores por docena
def docena(x):
  return x*12
floreria["precio docena"] = floreria.precio.apply(docena)
floreria
# %% Ejercicio 12 - Guardar el DataFrame anterior 
# en un archivo llamado "flores.xlxs"
floreria.to_excel("./flores.xlxs", sheet_name="Flores", index_label="Flor")

# %%
