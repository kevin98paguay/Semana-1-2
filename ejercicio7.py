class For:
    def __init__(self):
        pass

    def uso_del_For(self):
        lista_de_Nota = [(50,60),[40,60,50],(50,60,40,30)]
        acumulador = 0
        longi = 0
        for nota in lista_de_Nota:
            acuparcial = 0
            print(datos,end=" ")
            for datos in datos:
                print(nota)
                longi = longi+1
                acum = acumulador + datos
                acuparcial += datos
                promParcial = acuparcial/len(datos)
            print("Nota parcial= {} Promedio Parcial= {}".format(acuparcial,promParcial))
        prom = acum/longi
        print("Total de datos= {} - #dotas= {}: promedio= {} ".format(acumulador,longi,prom))


Obj1= For()
Obj1.uso_del_For()
