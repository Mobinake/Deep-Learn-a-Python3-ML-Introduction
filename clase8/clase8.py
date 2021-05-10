import clase8 as np
estacion=np.array((['Hoja','Verde','Verano']))
print(estacion)
#creacion de matrices de 2 y 3 dimensiones
print(np.array([[1,2,3,4,5],[2,3,4,5,7]]))
vector=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
print(vector)

#cargar el vector 4x4 con 0s
m_zeros=np.zeros((4,4))
print(m_zeros)

#crear una matriz identidad
m_identidad=np.identity(6)
print(m_identidad)

#un rango, desde donde 0, hasta donde 20 y cada cuanto los saltos 1
m_rango=np.arange(0,20,1)
print(m_rango[3])
print(m_rango)

#acceder a un valor de una matriz
m_acceder=np.array([[10,13,15],[13,15,12]])
print((m_acceder[1][0]))
print(np.ones((2,3)))

#diferentes operaciones que se pueden hacer
suma1=np.array([1,2,3,4])
suma2=np.array([3,4,5,6])
print(suma1+suma2)  #np.add(m1,m2)
print(suma1*2)  #np.multiply(m1,m2)
print(suma2/2)  #np.divide(m1,m2)
print(suma2-suma1)  #subtract(m1,m2)
print(suma2**2)     #np.
print(suma1//2)     #np.mod(m1,m2)

negativo=np.negative(suma2)
print(negativo)
#elevar
expt=np.exp(suma2)
print(expt)
#multiplicar matrices
m1=np.array([[1,2,3,4],[4,5,6,7],[5,6,7,8]])
m2=np.array([[2,3,4],[2,3,5],[1,2,3],[5,6,7]])
print(m1)
print(m2)
print(m1.dot(m2))

#transpuesta de una matriz
print(m1.T)

#random desde donde, hasta donde, tamanio de matriz, tipo de dato dtype=np.int8
mrandom=np.random.randint(1,100, (3,3), dtype=np.int8)
print("Random")
print(mrandom)

#ordenar matricez
print(mrandom)
print(np.sort(mrandom,None))

#ordenar palabras
palabras=np.array(['unanime','vector','almeja','zanahoria','perrito','gato','astronauta'])
print(np.sort(palabras,None))
