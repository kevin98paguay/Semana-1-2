class For:
    def __init__(self):
        pass

    def uso_del_For(self):
        lista_de_Estudiantes = [{"nombre":"Joel","final":40},{"nombre":"Ana","final":60},{"nombre":"Adrian","final":50}]
        acum=0
        cont=0
        for estudiantes in lista_de_Estudiantes:
            print(estudiantes)
            for clave,valor in estudiantes.items():
                print(clave,":",valor,end=" ")
                if clave=="final": acum=acum+valor
            cont+=1
        print(acum/cont)

Obj1= For()
Obj1.uso_del_For()
