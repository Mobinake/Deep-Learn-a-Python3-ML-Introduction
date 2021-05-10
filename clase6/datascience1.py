import pandas as pd


"""
RETO 6
Descarga de https://nasa.github.io/data-nasa-gov-frontpage/ o https://www.datos.gov.py/  un archivo de tipo(txt, excel o csv), utiliza los siguientes comandos y explica el resultado.
(Es importante explicar de qué trata el archivo)

.index-
.head() -
.info() 
.loc[filas, columnas] 
.iloc[i] :-
.describe()
groupby().get_group()
"""
datos=pd.read_csv('promedio.csv')

print(datos.index)  #lo que hace es decir la cantidad de datos que hay en el documento
print(datos.head(1)) #trae los x primeros elementos
#print(datos.info()) #
print(datos.loc[:1, ('Total','Mujeres')])   #trae un elemento de determinada fila y columna
print(datos.iloc[1])    #trae los elementos de determianda
print(datos.describe()) #depende del tipo de dato, si es string saca las palabras mas usadas o menos. si es entero encuentra el mean, min, max, promedio y mas ejercicios estadisticos
print(datos.groupby('Total').get_group('Totalpais'))  #sirve para agrupas los elementos del archivo eligiendo como agruparlos
print(datos['Total']>2.195)