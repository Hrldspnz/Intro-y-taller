class orden (object):
       def __init__(self):
              pass

       def ordenarlist(self,lista):
              if isinstance (lista, list):
                     return self.ordenarlist_aux(lista,0,len (lista)-1)
              else:
                     return "Error"

       def ordenarlist_aux(self,lista,indice,burbuja):
              if burbuja == 0:
                     return lista
              elif indice == burbuja:
                     return self.ordenarlist_aux(lista,0,burbuja-1)
              elif lista[indice]>lista[indice+1]:
                     lista[indice],lista[indice+1] = lista[indice+1],lista[indice]
                     return self.ordenarlist_aux(lista,indice+1,burbuja)
              else:
                     return self.ordenarlist_aux(lista,indice+1,burbuja)

o= orden()
lista = [8,3,1,2,5]
print(o.ordenarlist(lista))
