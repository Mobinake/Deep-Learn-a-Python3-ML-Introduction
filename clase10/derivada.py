from sympy import Symbol, diff, limit, oo

''' Respecto a que se deriva '''
x = Symbol('x')

''' f es la funcion, diff es el metodo que deriva la funcion respecto a x '''
f = 2*x**2-6*x+5
derivada1 = diff(f,x)
print(f'Ejer1: {derivada1}')

f2 = 3*x**2
derivada2 = diff(f2,x)
print(f'Ejer2: {derivada2}')

f3 = x**2+4*x-5
derivada3 = diff(f3,x)
print(f'Ejer3: {derivada3}')

f4 = x**2-x+1
derivada4 = diff(f4,x)
print(f'Ejer4: {derivada4}')

f5 = x / (x-1)
derivada5 = diff(f5,x)
print(f'Ejer5: {derivada5}')
