from sympy import Symbol, diff, limit, oo, integrate

def menu():
    """Funcion que Muestra el Menu"""
    print("""Menu 1) Suma 2) Resta 3) Multiplicacion 4) Division 5) Limites 6) Derivadas 7) Intelgrales 8) Salir""")


def calculadora():
    menu()
    opc = int(input("Selecione Opcion\n"))
    while opc > 0 and opc < 5:
        if opc == 1:
            print("Suma seleccionada")
            try:
                suma()
            except ValueError:
                print("Ingrese un valor valido: un entero.")
                suma()
            opc = int(input("Selecione Opcion\n"))
        elif opc == 2:
            print("Resta seleccionada")
            try:
                resta()
            except ValueError:
                print("Ingrese un valor valido: un entero.")
                resta()
            opc = int(input("Selecione Opcion\n"))
        elif opc == 3:
            print("Multiplicacion seleccionada")
            try:
                multiplicacion()
            except ValueError:
                print("Ingrese un valor valido: un entero.")
                multiplicacion()
            opc = int(input("Selecione Opcion\n"))
        elif opc == 4:
            print("Division seleccionada")
            try:
                division()
            except ValueError:
                print("Ingrese un valor valido: un entero.")
                division()
            opc = int(input("Selecione Opcion\n"))
        elif opc == 4:
            limites()
            opc = int(input("Selecione Opcion\n"))
        elif opc == 4:
            derivadas()
            opc = int(input("Selecione Opcion\n"))
        elif opc == 4:
            integrales()
            opc = int(input("Selecione Opcion\n"))

def suma():
    x = int(input("Ingrese Numero\n"))
    y = int(input("Ingrese Otro Numero\n"))
    print("La Suma es:", x + y)
    menu()

def resta():
    x = int(input("Ingrese Numero\n"))
    y = int(input("Ingrese Otro Numero\n"))
    print("La Resta es:", x - y)
    menu()

def multiplicacion():
    x = int(input("Ingrese Numero\n"))
    y = int(input("Ingrese Otro Numero\n"))
    print("La Multiplicacion es:", x * y)
    menu()

def division():
    try:
        x = int(input("Ingrese Numero\n"))
        y = int(input("Ingrese Otro Numero\n"))
        print("(La Division es:", x / y)
        menu()
    except ZeroDivisionError:
        print("No se Permite la Division Entre 0.")
        menu()

def limites():
    print("Limites seleccionado")
    x = Symbol("x")
    f = input("A continuacion ingrese la funcion: \n")
    limite = limit(f, x, oo)
    print(f'El limite es: {limite}')
    menu()

def derivadas():
    print("Derivadas seleccionado")
    x = Symbol('x')
    f = input("A continuacion ingrese la funcion: \n")
    derivada1 = diff(f, x)
    print(f'La primera derivada es: {derivada1}')
    menu()

def integrales():
    print("Integrales")
    x = Symbol('x')
    f = input("A continuacion ingrese la funcion: \n")
    a = int(input("Desde donde: \n"))
    b = int(input("Hasta donde: \n"))
    integral1 = integrate(f, (x, a, b))
    print(f'La primera integral de la funcion es: {integral1}')
    menu()

calculadora()