from sympy import Symbol, diff, integrate, limit, oo, simplify


x = Symbol('x')
f = 2**x*5**x
a = 0
b = 3
integral1 = integrate(f,(x,a,b))
print(f'Ejer1: {integral1}')


f2 = 8**(3*x+1)
a2 = 2
b2 = 5
integral2 = integrate(f2,(x,a2,b2))
print(f'Ejer2: {integral2}')


f3 = 5 / (x**2-4*x+8)
a3 = 1
b3 = 6
integral3 = integrate(f3,(x,a3,b3))
print(f'Ejer3: {integral3}')


#integrales dobles

y = Symbol('y')
f = x*y
a = 0
b = 0.5
c = 0
d = 1-2*y
I1 = integrate(f,(y,c,d))
I2 = simplify(integrate(I1,(x,a,b)))
print(f'Doble integral: {I2}')


#integrales con Scipy
#
#f = lambda x: 5*x
#a = 1
#b = 3
#I = quad(f,a,b)
#print(f'Resultado: {I}')
