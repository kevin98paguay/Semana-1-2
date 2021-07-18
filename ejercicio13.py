"""
mercaderia
cpmprador
venta
venta det
"""
class Mercaderia:
    def __init__(self,cod,des,pre,stoc):
        self.codigo=cod
        self.descripcion=des
        self.precio=pre
        self.stock=stoc

class Comprador:
    def __init__(self,ced,nom,dir,tel):
        self.cedula=ced
        self.nombre=nom
        self.direccion=dir
        self.telefono=tel

class Venta:
    def __init__(self,fac,fec,cliente,tot,detalle):
        self.factura=fac
        self.fecha=fec
        self.cliente=cliente
        self.total=tot
        self.detalle=detalle

class ventaDet:
    def __init__(self,venta,mercaderia,precio,cantida):
        self.mercaderia=mercaderia
        self.precio=precio
        self.cantida=cantida
