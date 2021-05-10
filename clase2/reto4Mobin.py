'''
Reto 4
Escribe un algoritmo que solicite números y que sea capaz de:
●	Sumar dos números complejos
●	Dividir números en base 10
'''

print('Numero complejo 1:')
numero1 = complex(input())
print('Numero complejo 2:')
numero2 = complex(input())
suma=numero1+numero2

print('Numero 1 base 10:')
num_e1=float(input())
print('Numero 2 base 10:')
num_e2=float(input())
division=num_e1/num_e2

print('La suma es: ', suma)
print('la division de numeros complejos es', division)

