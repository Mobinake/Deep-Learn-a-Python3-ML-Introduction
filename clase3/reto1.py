'''
Interpretar el programa, asignarle valores a x para que se
cumplan cada sentencia y anticipar los valores que tendrían
x en if, elif, else
'''

x = int(input())
print(" Antes del bloque if , el valor en x = ")
print(x)
if (x == 0):
    y = -1
    x = x + y
elif (x < 0.5):
    y = 2
    x = x + y
else:
    y = 3
    x = x + y
print(" Después del bloque if , el valor en x = ")
print(x)
