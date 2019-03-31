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
class Restas(object):
    def __init__(self):
        pass

    def RestasBaseN(self,lista1,lista2,base):
        if isinstance(lista1,list)and(lista2,list)and(base,int):
            return self.RestasBN(lista1,lista2,base,0)
        else:
            return "Error problema con los parametros"

    def RestasBN(self,lista1,lista2,base,prestado):
        if lista1 == []:
            return ["-"]+lista2
        if lista2 == []:
            return lista1
        elif (lista1[-1]-prestado)>lista2[-1]:
            return self.RestasBN(lista1[:-1],lista2[:-1],base,prestado=0) + [hexa[(lista1[-1]-prestado)-lista2[-1]]]
        elif(lista1[-1]-prestado)== lista2[-1]:
            return self.RestasBN(lista1[:-1],lista2[:-1],base,prestado=0) + [hexa[(lista1[-1]-prestado)-lista2[-1]]]
        else:
            return self.RestasBN(lista1[:-1],lista2[:-1],base,prestado=1) + [hexa[((lista1[-1]-prestado)+base)-lista2[-1]]]


                                                                            
