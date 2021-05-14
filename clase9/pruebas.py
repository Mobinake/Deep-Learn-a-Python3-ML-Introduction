import numpy as np

"""matriz=np.array([22, 14,15,16,8,14])
print(matriz[:4])
matriz2=np.array([1, 2, 3, 4, 5, 4, 4])
print(matriz2)
matriz3=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(matriz3)

#pasar de vector a matriz
preparar_m=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
matriz_var=preparar_m.reshape(4,3)
print(matriz_var)"""
"""
#filtro
mat_filtro=np.array([56,87,21,32,45,85])
filtro2=[True,True,False,False,True,False]
filtro=mat_filtro%2==0
n_vector=mat_filtro[filtro]
n_vector_f2=mat_filtro[filtro2]
print('true o false',n_vector_f2)
print('filtro normal',n_vector)
"""
"""
#busqueda
v_original=np.array([2,1,6,4,8,9])
where=np.where(v_original==4)
print(where)"""
"""
#union e interseccion
vector1=np.array([7,14,21,77])
vector2=np.array([2,14,77,5])
v_union=np.union(vector1,vector2)
print(v_union)
v_inter=np.intersect(vector1,vector2)
print(v_inter)
"""
#metodo lineal solved(parametros)------np.linalg.solved(vec1,vec2)
#Ax=B x con indice n-1












