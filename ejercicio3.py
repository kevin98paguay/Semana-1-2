class clase:
    instancia=0
    def _init_(self,dato = "Inicializacion"):
        self.frase = dato

    def usarVariable(self):
        edad, _peso = 30, 90.7
        nombres = 'Juanito Lopez'
        Tipo_Sexo =  'M'
        civil = True
        ususario=()
        ususario = ('dchiki', 1234, 'hiki@gmail.com',True)
        asignatura = []
        asignatura = ['Programa Web', 'PHP', 'POO']
        asignatura[1]="Python"
        asignatura.append("Go")
        docente = {}
        docente = {'nombre': 'Juanito', 'edad': 30, 'fac': 'faci'}
        docente['profesion']="CS"
        # print("""Mi nombre es {}, tengo {}
        #       años""".format(nombres, edad)
        # print(ususario,asignatura,docente)
        # print(ususario,ususario[0],ususario[0:2],ususario[-1])
        # print(asignatura,asignatura[2:],asignatura[:3],asignatura[::],asignatura[-2:])
        print(docente,docente['nombre'])

ejer1 = clase()
ejer1.usarVariable()
