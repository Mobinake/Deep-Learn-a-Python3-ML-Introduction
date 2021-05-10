'''
Reto 5
Solicite al usuario Nombre, apellido, edad, CI, año de nacimiento, fecha de cumpleaños e ingrese el la lista.
Imprima por un lado Nombre, apellido, CI, por otro lado imprima edad, año, fecha.

	lista[nombre,apellido,edad,CI, año, fecha]
'''


print('Nombre:')
nombre=input()
print('Apellido:')
apellido=input()
print('Edad:')
edad=int(input())
print('CI:')
ci=str(input())
print('Año de nacimiento:')
anio_nacimiento=input()
print('Cumple:')
cumple=str(input())

lista=[nombre,apellido,edad,ci,anio_nacimiento,cumple]

print(lista[0],lista[1],lista[3])
print(lista[2],lista[4],lista[5])
