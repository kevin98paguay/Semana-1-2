from ejercicio11 import Puesto

class Funcionario:
    secuencia=0
    def __init__(self,nom,ced,sue,ejercicio11):
        self.codigo=self.generarCodigo
        self.nombre=nom
        self.cedula=ced
        self.sueldo=sue
        self.cargo=ejercicio11
    def mostrar(self):
        print("codigo:{} nombre:{} cargo:{}-{}".format(self.codigo,self.nombre,self.puesto.codigo,self.puesto.description))

    def generarCodigo(self):
        Funcionario.secuencia=Funcionario.secuencia+1
        return Funcionario.secuencia

cargo1= Puesto("Gerente")
func1= Funcionario("Byron","0943598011",500,puesto1)
func1.mostrar()
puesto2= Puesto("Contador")
func2= Funcionario("Anibal","0989852099",400,puesto2)
func2.mostrar()
