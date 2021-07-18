frase = "Hola mundo como has estado"
vocales = []
if car in {'a','e','i','o','u'}:
    vocales.append(car)
print(vocales)



print([car for car in "Hola Mundo como has estado" if car in ('a','e','i','o','u')])
