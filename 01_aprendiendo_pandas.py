import pandas as pd

# ejercicio 1: crear una serie de pandas con el siguiente arreglo

edades = [22, 13, 8, 33, 25, 44, 38, 22]
# print(edades)

serie_edades = pd.Series(edades)
# print(serie_edades)

""" 
print(serie_edades.head()) # obterner los primeros 5 registros utilizando head
print(serie_edades.tail(3)) # obtener los últimos 3 registros utilizando tail
print(serie_edades.max()) # máximo
print(serie_edades.min()) # mínimo
print(serie_edades.mean()) # promedio

print(serie_edades[1]) # posición 2
print(serie_edades.get(2)) # posición 3 con código de pandas
print(serie_edades[serie_edades == 22]) #obtener registro que tengan un valor igual a 22
"""


edades_2 = [23, 15, 12, 25, 20, 50, 31, 2]
serie_edad_2 = pd.Series(edades_2)
# print(serie_edad_2)

print(edades + edades_2) # sumar listas: juntar en una sola lista
print(serie_edades + serie_edad_2) # sumar seriers: se suman los valoressegún el índice

edades_3 = [2]
serie_edad_3 = pd.Series(edades_3)
print(serie_edad_3 + serie_edades) # "no se puede"





