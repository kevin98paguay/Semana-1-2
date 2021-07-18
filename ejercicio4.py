class condicion:
    contador=0
    def _init_(self,num1=0,num2=1):
        self.numero1=num1
        self.numero2=num2
        # numero = num1+num2
        self.numero3 = num1

    def usoIf(self):
        if self.numero1 == self.numero2:
            print("numero1:{}, numero2:{}: son identicos".format(self.numero1, self.numero2))
        elif self.numero1 == self.numero3:
            print("numero1:{}, numero3:{}: son identicos".format(self.numero1, self.numero3))
        else:
            print("no son identicos ")
# # cond1 = condicion()
# # print=(cond1.numero1)
# # print=(cond1.numero2)

cond2 =condicion(10,20)
cond2.usoIf()
print(cond2.numero1)
