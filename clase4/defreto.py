'''¿Que realiza el siguiente bloque de código?
Escribir python y explicar

definir suma ( parametro1 , parametro2 ) :
    retornar parametro1 + parametro2 ;

definir potencia ( parametro1 , parametro2 ) :
    retornar parametro1 ∗∗ parametro2 ;

definir sumaPotencia ( parametro1 , parametro2 ) :
    retornar parametro1 + parametro2 , parametro1 ∗∗ parametro2 ;

resultado1 = suma ( 2 , 3 ) ;
imprimir resultado1 ;
resultado2 = potencia ( 2 , 3 ) ;
imprimir resultado2 ;
resultado3 = sumaPotencia ( 2 , 3 ) ;
imprimir resultado3
'''

def suma(var1,var2):
    return var1+var2

def potencia(var1,var2):
    return var1*var2

def sumaPotencia(var1,var2):
    return var1+var2, var1*var2

result1=suma(2,3)
print(result1)

result2=potencia(2,3)
print(result2)

result3=sumaPotencia(2,3)
print(result3)