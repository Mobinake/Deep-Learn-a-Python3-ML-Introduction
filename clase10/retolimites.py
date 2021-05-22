from sympy import limit,Symbol,oo,diff
import sympy as sp
#1
x= Symbol("x")
f=(5*x**3+2*x**2-1)/2*x+3
limite= limit(f,x,oo)

#2
from sympy import limit,Symbol,oo
x= Symbol("x")
f=((x**2+x-2)/(x**2-3*x+2))
limite= limit(f,x,1)
print(limite)

#3
from sympy import limit,Symbol,oo
x= Symbol("x")
f=(-5*x**3+8*x-3*x**6)
limite= limit(f,x,-oo)
print(limite)

4
from sympy import limit,Symbol,oo
x= Symbol("x")
f=(x+3)/2
limite= limit(f,x,1)
verificador= limite==2
print(limite, verificador)
print (limite)