hexa = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}
class Sumar(object):

    def __init__(self):
        pass
    def sumalist(self,lista,lista2,b,a):
        if ((isinstance (lista,list))and (isinstance(lista2, list)
            and (isinstance(b,int)) and (isinstance(a,int)))):
                return self.suma_list(lista,lista2,b,a)
        else:
                return "Error: hay un problema, revise los parametros"


    def suma_list(self,lista,lista2,b,a):
        if lista == [ ]:
            return lista2[:-1]+[hexa[lista2[-1]+a]]
        if lista2 == [ ]:
            return lista[:-1]+[hexa[lista[-1]+a]]

        elif (lista[-1] + lista2[-1] + a >= b):
            return self.suma_list(lista[:-1],lista2[:-1],b,a=1) + [hexa[((a+lista[-1]+lista2[-1])-b)]]
        else:
            return self.suma_list(lista[:-1],lista2[:-1],b,a=0) + [hexa[((lista[-1]+lista2[-1])+a)]]
        
