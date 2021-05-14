import numpy as np
"""1. Cortar elementos desde el principio hasta el índice 4 (no incluido):"""
matriz=np.array([22, 14,15,16,8,14])
print('ejer 1',matriz[:4])

"""2. Encuentre los índices donde los valores son pares: [1, 2, 3, 4, 5, 4, 4]"""
matriz2=np.array([1, 2, 3, 4, 5, 4, 4])
filtro=matriz2%2==0
n_vector=matriz2[filtro]
print('ejer 2: pares',n_vector)

"""3. Cree una matriz de filtros que devolverá solo valores superiores a 7:"""
matriz3=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
filtro=matriz3>7
n_vector2=matriz3[filtro]
print('ejer 3: mayor a 7',n_vector2)

"""4. Encuentre la intersección y la unión de los siguientes dos conjuntos de
matrices:[1, 20, 63, 4, 5], [5, 72, 63, 9, 11]"""
vector1=np.array([1,3,5,7,9])
vector2=np.array([2,4,6,8,10])
v_union=np.union1d(vector1,vector2)
v_inter=np.intersect1d(vector1,vector2)
print('ejer 4: interseccion:',v_inter,'union:',v_union)


"""5. Un pizzeria vendió 20 bolsitas de papas fritas y 10 pizzas en un día por un
total de $ 350. Al día siguiente vendió 17 bolsitas de papas fritas y 22 pizzas
por $ 500. Si los precios se mantuvieron sin cambios en ambos días, ¿cuál
fue el precio de una bolsita de papas fritas y una pizza?"""
#metodo lineal solved(parametros)------np.linalg.solved(vec1,vec2)
#Ax=B x con indice n-1
#dia 1= 20x+10y=350
#dia 2= 17x+22y=500
a=np.array([[20,10],[17,22]])
b=np.array([350,500])
x=np.linalg.solve(a,b)
print('ejer 5: el valor de x e y es: ',x,'respectivamente')




