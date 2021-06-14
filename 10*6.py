#num=21
#if type(num) == int:
#   print("respuesta: ",num*2)
#else:
#    print("el dato no es numerico")

#  def mensaje(men):
#print(men)

# mensaje("Mi primer programa")
# mensaje("mi segundo programa")
class Sintaxis: 
    isinstancia=0 #variable de clase(opcional)
    #_int_Metodo constructor que se ejecuta cuando la instancia de la clase cuyo objetivo es crear
    #e inicializar los atribitos de la clase. self es un objeto que representa la clase 
def _init_(self,dato="Inicializacion"):
    self.frase=dato #variables de instancia
    #Sintaxis.instancia = Sintaxis.instancia+1

def usoDeVariables(self):
    edad, _peso = 21, 56,5
    nombres= "Kevin Paguay"

    Sexo='M'
    ConddicionCivil= True

#tuplas =() son coleccioones de datos de cualquier tipo inmutable
  # tuplas =() son coleccioones de datos de cualquier tipo inmutable
    usuario = ()
    usuario = ('Kevin', 1234123, 'kevin@unemi.edu.ec', True)
    #usuario[3]="Guayaquil"
    # listas = [] colecciones mutables 
    materias= []
    materias= ['Programacion Web', 'PHP', 'POO']

    materias[1]= "Python"
    materias.append("Go")
    # diccionario = {} colecciones de objetos clave: valor tipo json
    docente = {}
    docente = {'nombre': 'Kevin', 'Edad': '21', 'fac' : 'faci'}
    docente['carera']= "CS"
    # presentacion con format
    #print (""Mi nombre es {}, tengo{} 
    # anos"".format(nombres,edad))
    #print(usuarios,materias,docentes)
    #print(usuarui,usuario[0],usuario[0:2],usuario[-1])
    #print(materias,materias[2:],materias[:3],materias[:],materias[-2:])
    print(docente,docente,['nombre'])


x=5
ejercicio1= Sintaxis() #se crea un onjeto que es una instancia de la clase y se ejecuta el constructor
ejercicio1=usoDeVariables
#----------------------------------------------------------------------------------------------------------
#Clase Condiciones
class Condicion:
    # _init_ Metodo Constructorque se ejecutan cuando se instancia a clase cuyo objetivo es crear e
    # inicializar los atributos de la clase. self es un objeto que representa la clase crear
    def _init_(self,num1=0,num2=0):
        self.numero1=num1 #variable de instancia
        self.numero2=num2 #variable de instancia
        numero = num1+num2
        self.numero3 = numero
        #variables de instancia

    def usoIf(self):
        #if elif else:permiten condicionar la ejecucion e uno o varios bloques 
        # de sentencias al cumplimiento de una o varias conciones
        if self.numero1 == self.numero2:
            print("num1:{}, num2{}:son iguales".format(self.num1,self.num2))
        elif self.numero1 == self.numero2:
            print("numero1:{}, numero3:{}son iguales".format(self.numero1, self.numero2))
        else:
            print("No Son Iguales")
 #usar clase
#cond1 = Condicion()
#print(cond1.numero1)
#print(cond1.numero2)

cond2 = Condicion(10,10)
cond2.usoIf() #llamada a un metodo de la clase
print(cond2.numero1) #llamada a un atributo de la clase

#---------------------------------------------------------------------------------------------------------------------
#Ciclos
class ciclos:
    def _init_(self,num1=5):
        self.numero=num1

    def usoWhile(self):
        #ciclo repetitivo que se ejecutan por verdadero y sale por falso

        vc = input("Ingrese una Vocal: ")
        vc = vc.lower()
        while car not in('a','e','i','o','u'):
            vc = input("Ingrese la vocal: ").lower()
        print("Felicitaciones el caracter:{} es una vocal".format(vc))

ciclo1=ciclos()
ciclo1.usoWhile()
