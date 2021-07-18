class Puesto:
    secuencia=0
    def __init__(self,des="Sin Puesto"):
        Puesto.secuencia=Puesto.secuencia+1
        self.codigo=Puesto.secuencia
        self.descripcion=des

if __name__ == "__main(__":
    Puesto1 = Puesto()
    print(Puesto1.codigo,Puesto1.descripcion)
    Puesto2 = Puesto()
    Puesto2.descripcion="Gerente"
    print(Puesto2.codigo,Puesto2.descripcion)
    cargo3 = Puesto("Contador")
    print(Puesto3.codigo,Puesto3.descripcion)
    # print(Puesto.secuencia)
    # print(Puesto1.secuencia)
    # print(Puesto2.secuencia)
    # print(Puesto3.secuencia)
