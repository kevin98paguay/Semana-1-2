class ordenar:
    def __init__(self, lista):
        self.lista = lista

    def burbuja(self):
        for i in range(len(self.lista)):
            for j in range(i + 1, len(self.lista)):
                if self.lista[i] > self.lista[j]:
                    aux = self.listä[i]
                    self.lista[i] = self.lista[j]
                    self.lista[j] = aux

    def insertar(self, valor):
        self.burbuja()
        auxilista = []
        enc = False
        for pos, ele in enumerate(self.lista):
            if ele > valor:
                auxilista.append(valor)
                enc = True
                break
        if enc == True:
            #    for i in range(pos):
            #        auxilista.append(self.lista[i])
            #    for j in range(pos,len(self.lista))
            #   auxilista.append(self.lista[j])
            #   self.lista = auxilista
            auxilista = self.lista[0:pos] + auxilista + self.lista[pos:]
        else:
            self.lista.append(valor)
        return self.lista


ord1 = ordenar([18, 15, 20, 70, 80])
#               0   1  2  3  4
#                        pos
print(ord1.insertar(50))
ord1.burbuja()
print(ord1.lista)
