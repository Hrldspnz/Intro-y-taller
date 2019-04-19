class suma(object):
       def __init__(self):
              pass
       
       def sumarlist(self,lista):
              if isinstance(lista,list):
                     return self.sumarlist_aux(lista,0,0)
              else:
                     return "Error"

       def sumarlist_aux(self,lista,indice,result):
              if indice == len(lista):
                     return result
              elif isinstance(lista[indice],list):
                     return self.sumarlist_aux(lista[indice],0,0) + self.sumarlist_aux(lista,indice+1,result)
              else:
                     return self.sumarlist_aux(lista,indice+1,result + lista[indice])


s = suma()
lista=[5,[6,[7,8],9,10],11]
print(s.sumarlist(lista))
