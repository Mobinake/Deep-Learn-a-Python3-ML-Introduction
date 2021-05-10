'''
Realizar el ejercicio anterior aplicando funciones
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
    prueba(prueba, perdiste)
    perdiste(prueba, cantLetras)
print("Ahorcado terminado")

def prueba(prueba, perdiste):
    if letra in vector:
        print("Estas cerca de lograrlo")
        prueba+=1
    else:
        perdiste-=1
def perdiste(prueba, cantLetras):
    if prueba == cantLetras:
        print("Ganaste!")
    elif perdiste == 0:
        print("Perdiste")