'''
Cree un vector con n elementos y  llénelo
con números consecutivos enteros positivos.
'''

vector=[]

n=int(input("Ingrese un numero n"))
for i in range(0,n):
    vector.append(i)

print(vector)