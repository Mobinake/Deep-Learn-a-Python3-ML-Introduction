import sympy as sp
from sympy import Symbol, diff, limit, oo

#1
print('Example number 1:')
x = Symbol("x")
f = (5*x**3+2*x**2-1) / 2*x+3
limite = limit(f,x,oo)
print(f'limite: {limite}')

#2
print('\nExample number 2:')
x = Symbol("x")
f = ((x**2+x-2) / (x**2-3*x+2))
limite = limit(f,x,1)
print(f'limite: {limite}')

#3
print('\nExample number 3:')
x = Symbol("x")
f = (-5*x**3+8*x-3*x**6)
limite = limit(f,x,-oo)
print(f'limite: {limite}')

#4
print('\nExample number 4:')
x = Symbol("x")
f = (x+3)/2
limite = limit(f,x,1)
verificador = limite == 2
print(f'limite: {limite}\n'
      f'verificador: {verificador}'
    )

