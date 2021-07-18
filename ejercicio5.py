class ciclos:
    def _init_(self,num1=5):
        self.numero=num1

    def usowhile(self):
        car = input("Ingresar la vocal: ")
        car = car.lower()
        while car not in('a','e','i','o','u'):
            car = input("Ingrese la vocal: ").lower()
            print("felicitacion caracter:{} es vocal".format(car))

ciclo1 = ciclos()
ciclo1.usowhile()
