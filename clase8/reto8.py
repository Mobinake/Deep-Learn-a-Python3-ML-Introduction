import numpy as np

#ejer1 Realice transposición de matriz[n][n][n] y especifique las nuevas posiciones
m= np.array([[1,2,3],[4,5,6],[7,8,9]])
print('La matriz es: \n', m)
print('La matriz transpuesta es \n',m.T)

#ejer2 Realice la multiplicación de dos matrices[n][n] Identidad
m_id1=np.identity(4)
m_id2=np.identity(4)
print(m_id1)
print(m_id2)
print('La multiplicación de esas matrices es: \n', m_id2.dot(m_id1))

#ejer3 Realice la potencia de 2 una matrices[n][n]
m_pot=np.array([[1,2,3,4,5]])
print('La matriz es:\n',m_pot)
print('La potencia 2 es: \n', m_pot**2)

#ejer4 Ordene una matriz con palabras aleatorias de a-z
palabras=np.array(['unanime','vector','almeja','zanahoria','perrito','gato','astronauta'])
print('Las palabras desordenadas son: \n', palabras)
print('Las palabras ordenadas son: \n', np.sort(palabras, None))

#ejer5 Ordene una matriz con numeros aleatorios del 1 al 100
mrandom=np.random.randint(1,100, (6,6), dtype=np.int8)
print('La matriz desordenada es: \n', mrandom)
print('La matriz ordenada es: \n', np.sort(mrandom, None))
