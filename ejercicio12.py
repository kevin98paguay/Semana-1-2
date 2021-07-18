class Operaciones:
    def __init__(self,num1,num2):
        self.numero1=num1
        self.numero2=num2

    def suma(self):
        suma=self.numero1 + self.numero2
        return suma

    def resta(self):
        return self.numero1 - self.numero2


    def multiplicacion(self):
        return self.numero1 * self.numero2


    def division(self):
        if self.numero2 != 0: return self.numero1 / self.numero2
        return 0

    def divisionEntera(self):
        if self.numero2 != 0: return self.numero1 // self.numero2
        return 0

    def residuo(self):
        return self.numero1 % self.numero2

    def exponente(self):
        return self.numero1 ** self.numero2

    def mostrar(self):
        print("operando1={}, operando2={}".format(self.numero1, self.numero2))

print("**Lista De Operaciones Matematicas**")
print((" 1) Suma\n 2) Resta\n 3) Multiplicacin\n 4) Division\n 5) Division entera\n 6) Residuo\n 7)Exponente\n 8)salir"))
opc= "0"
while opc != "8":
    opc= input("Escoja una opcion[1...8]: ")
    num1= int(input("Esbriba numero 1: "))
    num2= int(input("Escriba numero 2: "))
    ope= Operaciones(num1,num2)
    if opc == "1":
        print("{}+{}={}".format(ope.numero1,ope.numero2,ope.suma()))

    elif opc == "2":
        print("{}-{}={}".format(ope.numero1,ope.numero2,ope.resta()))

    elif opc == "3":
        print("{}*{}={}".format(ope.numero1,ope.numero2,ope.multiplicacion()))

    elif opc == "4":
        print("{}/{}={}".format(ope.numero1,ope.numero2,ope.division()))

    elif opc == "5":
        print("{}/{}={}".format(ope.numero1,ope.numero2,ope.divisionEntera()))

    elif opc == "6":
        print("{}%{}={}".format(ope.numero1,ope.numero2,ope.residuo()))

    elif opc == "7":
        print("{}**{}={}".format(ope.numero1,ope.numero2,ope.exponente()))

print("Muchas Gracias!!")

# operacion=Operaciones(10,20)
# x=operacion.suma()
# #print(operacion.suma())
# #print(operacion.division())
# y=operacion.resta()
# z=x ** y
# print(z)
# operacion.mostrar()
