class Menu:
    def __init__(self, titulo, opciones=[]):
        self.titulacion = titulacion
        self.opciones = opciones

    def menuPrincipal(self):
        print(self.titulacion)
        for opcion in self.opciones:
            print(opcion)
        opcion = input("eliga la opcion[1...{}]".format(len(Self.opciones)))
        return opcion


objetivo = Menu("menu principal", ["1) CALCULADORAS", "2) NUMEROS", "3) LISTAS", "4) CADENAS", "5) SALIR"])
opcion = objetivo.menuPrincipal()

if opcion == "1":
    objetivo = Menu("menu de calculadora", ["1) suma", "2) resta", "3) salir")
    opcion1 = opcion1.menuprincipal()
    if opcion == "1":
        print("suma 2 numeros")
    n1 = int(input("escriba n1: "))
    n2 = int(input("escriba n2: "))
    suma = n1 + n2
    print("{}+{}={}".format(n1, n2, suma))

    elif opcion == "2":
    objetivo = Menu("menu numer", ["1) perfecto", "2) primo", "3) salir"])
    opcion2 = opcion2.menuprincipal()

    elif opcion == "3":
    print("menu lista")
    elif opcion == "4":
    print("menu cadenas")
    elif opcion == "5":
    print("Muchas gracias por su presencia")

    else:
    print("opcion no corecta")
