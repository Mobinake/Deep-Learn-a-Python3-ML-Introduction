'''Escribe este algoritmo en python y explique que hace
Inicio  del Algoritmo
    Escribir "Dime un número"
    Leer x
    suma = 0
    Mientras x mayor o igual a 0 Hacer
        suma = suma + x
        Escribir "Hasta ahora, la suma es ", suma
        x=x-1
    FinMientras
    	Escribir "Terminado"
FinAlgoritmo
'''

i = int(input("Pasame un numero: "))    #primero le pasamos el numero a usar
suma = 0

while i >= 0:   #mientras que el numero sea mayor o igual a 0
    suma=suma+i #crea una variable que va sumando en cada vuelta la variable original anterior con la actual
    print("La suma actual es: ", suma)
    i = i - 1   #resta la variable original en 1, hasta alcanzar 0
print("Terminado")