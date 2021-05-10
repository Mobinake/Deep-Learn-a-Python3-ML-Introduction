'''
Cree el juego del ahorcado utilizando lo aprendido.
-Ingrese 5 letras por input en un vector
-Busque las letras de manera desordenada, cada vez
que el usuario no ingrese ninguna de las letras pierde
un punto e imprime que está equivocado.
-Solo tiene 5 oportunidades para equivocarse
-En caso de encontrar las letras en el vector, imprimir
“Estas cerca de lograrlo”
-Si encuentra todas las letras gana, en caso contrario
pierde imprimir al final el vector

'''

vector=[]
prueba=0
perdiste=5

cantLetras=int(input("Cantidad de letras del ahorcado: "))

for i in range(0,cantLetras):
    valor = str(input("Ingrese letras, tienes 5 vidas: "))
    vector.append(valor)

while prueba <= cantLetras:
    letra = str(input("Ingrese las letras a buscar: "))
    if letra in vector:
        print("Estas cerca de lograrlo")
        prueba+=1
    else:
        perdiste-=1
    if prueba == cantLetras:
        print("Ganaste!")
        break
    elif perdiste == 0:
        print("Perdiste")
        break

print("Ahorcado terminado")

















