archivo, f= 'datos.txt',""
profesor =[{'nombre':'David','edad':40,'fac':'Ingenieria'},
    {'nombre':'Anibal','edad':30,'fac':'Salud',},
    {'nombre':'Byron','edad':20,'fac':'Administrativa',}]

#escribir archivo: w - a: write - writeline
with open (archivo, 'w') as writer:
    for i in range(len(profesor)):
        linea=''
        for clave, valor in profesor [i].items():
            if clave == 'fac':
                linea = linea + (str(valor)if type (valor)== int else valor)
            else:
                linea = linea + (str(valor)if type (valor)== int else valor)
            writer.writelines(linea)

#Leer archivo: r: read - readline - readlines - in
try:
    f= open(archivo, "r")
    for line in f:
        print(linea[:-1])
except Exception as e:
        print('Problema de documento: '+ str(e))
finally:
    f.close()
