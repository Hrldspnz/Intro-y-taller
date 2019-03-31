class paridad(object):
       def __init__(self):
              pass
       def pares(self,lista):
              if isinstance(lista,list):
                     par = lambda digito : digito%2 == 0
                     return self.pares_aux(lista,par,[])
              else:
                     return "Error"

       def pares_aux(self,lista,cond,resultado):
              if lista == []:
                     return resultado
              elif isinstance (lista[0], list):
                     return self.pares_aux(lista[0]+lista[1:],cond,resultado)
              elif cond(lista[0]):
                     return self.pares_aux(lista[1:],cond,resultado + [lista[0]])
              else:
                     return self.pares_aux(lista[1:],cond,resultado)
       
