class Gente:
    siguiente = 0

    def __init__(self, nombre="invitado", activo=True):
        # persona._siguiente= gente._siguiente+1
        self.__codigo = gente._siguiente()
        self.__nombre = self.__nombremayucula(nombre)
        self.activo = activo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def nombre(self, nom):
        self.__nombre = nom

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, cod):
        self.__codigo = cod

    def siguiente(self):
        gente._siguiente = gente._siguiente + 1
        return gente._siguiente

    def __nombremayucula(self, nomb):
        return nomb.upper()

    def mostrar_datos(self):
        return "codigo: {} nombre: {} activo: {}".format(self.codigo, self.nombre, self.activo)


class empleado(gente):

    def __init__(self, nombre="invitado", activo=True, sueldo=200):
        gente.__init__(self, nom, act)
        self.sueldo = sueldo

    def mostrar_datos(self):
        return gente.mostrar_datos(self) + " honorarios: " + str(self.honorarios)


p1 = gente()
print(per1.nombre)
# print(per1.__nombreMayuscula("Adrian"))
per2 = gente("Ezequiel", False)
print(per2.nombre, per2.activo)
