class For:
    def __init__(self):
        pass

    def uso_del_For(self):
        informe=["Pedro",43,True]
        cifras=(2,5,6,4,1)
        profesor = {'nombre': 'Alex', 'edad': 43, 'faci': 'faci'}
        lista_de_Nota = [(30,40),[20,40,30],(50,40,20,10)]
        lista_de_Alumnos = [{"nombre":"Joel","final":40},{"nombre":"Ana","final":60},{"nombre":"Adrian","final":50}]
        for i in range(5):
            print("i={}".format(i))
        for i in range(2,10):
            print("i={}".format(i))
        for i in range(4,10,2):
            print("i={}".format(i),end=" ")


        longitud = len(informe)
        for i in range(longitud):
            print(informe[i],end=' ')

        j=0
        while j < longitud:
            print("while",informe[j])
            j=j+1

        for i in range(longitud-1,1,-1):
            print(informe[i])

        for i,dato in enumerate(cifras):
            print("for",i,informe)

        for dato in cifras:
            print(informe)

        for dato in['h','e','l','l','o']:
            print(informe)

        print("\nDiccionario de notas")
        for clave,valor in profesor.items():
            print(clave,":",valor,end=" ")

Obj1= For()
Obj1.uso_del_For()
