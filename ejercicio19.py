class Empresa:
    def __init__(self, nom="Extermix", ruc="0943598011", telf="0989852099",
                 dir="nice to me too"):  # parametros crear para que sea mas generico.
        self.nombre = nom
        self.ruc = ruc
        self.telefono = telf
        self.direccion = dir

    def mostrarEmpresa(self):
        print('Empresa:{:15} Ruc:{} Telefono:{} Direccion:{}'.format(self.nombre, self.ruc, self.telefono,
                                                                     self.direccion))


class Cliente:
    def __init__(self, nom, ced, telf, dir):
        self.nombre = nom
        self.cedula = ced
        self.telefono = telf
        self.direccion = dir

    def mostrarCliente(self):
        print('Nombre:{:15} Cedula:{} Telefono:{} Direccion:{}'.format(self.nombre, self.cedula, self.telefono,
                                                                       self.direccion))


class ClienteCorporativo(Cliente):
    def __init__(self, nom, ced, telf, dir, contrato):
        super().__init__(nom, ced, telf, dir)
        self.__contrato = contrato

    @property  # getter sirve para obetener valor privado
    def contrato(self):
        return self.__contrato

    @contrato.setter  # setter asigna valor atrivuto privado
    def contrato(self, value):
        if value:
            self.__contrato = value
        else:
            self.__contrato = 'Sin contrato'

    def mostrarCliente(self):
        print('Nombre:{:15} Contrato:{}'.format(self.nombre, self.__contrato))


class ClientePersonal(Cliente):
    def __init__(self, nom, ced, telf, dir, descuento=True):
        super().__init__(nom, ced, telf, dir)
        self.__descuento = descuento

    @property  # getter nos sirve para obetener el valor privado
    def descuento(self):
        if self.__descuento == True:
            return "Usted obtiene 15% de Descuento"
        else:
            return "No tiene  Descuento"

    @descuento.setter  # setter asigna valor atrivuto privado
    def descuento(self, value):
        self.__descuento = value

    def mostrarCliente(self):
        print('Nombre:{:15}'.format(self.nombre), self.descuento)


class Articulo:
    secuencia = 0
    iva = 0.12

    def __init__(self, des, pre, sto):
        Articulo.secuencia += 1
        self.codigo = Articulo.secuencia
        self.descripcion = des
        self.precio = pre
        self.stock = sto

    def mostrarArticulo(self):
        print(self.codigo, self.descripcion)


class Detalle_de_Venta:
    linea = 0

    def __init__(self, articulo, cantidad):
        Detalle_de_Venta.linea += 1
        self.articulo = articulo
        self.cantidad = cantidad
        self.precio = articulo.precio
        self.cantidad = cantidad


class CabVenta:
    def __init__(self, empresa, factura, fecha, cliente, tot=0):
        self.empresa = empresa
        self.factura = factura
        self.fecha = fecha
        self.cliente = cliente
        self.total = tot
        self.detalleVent = []

    def agregarDetalle(self, articulo, cantidad):
        detalle = Detalle_de_Venta(articulo, cantidad)
        self.total += detalle.preceio * detalle.cantidad
        self.detalleVent.append(detalle)

    def mostrarVenta(self, empNombre, empRuc):
        print("Empresa: {:15} Ruc: {}".format(empNombre, empRuc))
        print("Factura.N#: {:13} Fecha: {}".format(self.factura, self.fecha))
        self.cliente.mostrarCliente()
        print("Linea Articulo       Precio Cantidad Subtotal")
        for det in self.detalleVent:
            print("{:5} {:10} {} {:6} {:7}".format(det.linea, det.articulo, det.descripcion, det.precio, det.cantidad))
            print("Total Venta:{:26}".format(self.total))


Emp = Empresa()

# cli1= Cliente("Juan Perez","120554545","064684165","villaPark")
# cli1.mostrarCliente()

# cli2 = ClienteCorporativo("Juan Perez","120554545","064684165","villaPark",'01')
# cli2.mostrarCliente()

cli3 = ClientePersonal("Juan Perez", "120554545", "064684165", "villaPark", True)

art1 = Articulo("aceitte", 5, 100)
art2 = Articulo("cola", 4, 50)
art3 = Articulo("cervezA", 14, 600)

today = date.today()
fecha = date(2021, 8, 25)

venta = CabVenta('F00001', date.today(), cli3)
venta.agregarDetalle(art1, 5)
venta.agregarDetalle(art2, 4)
venta.agregarDetalle(art2, 3)
venta.mostrarVenta(Empresa.nombre, Empresa.ruc)
