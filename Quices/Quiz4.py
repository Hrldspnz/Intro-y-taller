class buscar(object):
       def __init__(self):
              pass

       def busqueda(self,num,lista):
              if isinstance (num,int) and isinstance(lista,list):
                     return self.busqueda_aux(num,lista,[],0)
              else:
                     return "Error"

       def busqueda_aux(self,num,lista,posicion,indice):
              if indice == len(lista):
                     return posicion
              elif lista[indice] == num:
                     return self.busqueda_aux(num,lista,posicion+[indice],indice+1)
              else:
                     return self.busqueda_aux(num,lista,posicion,indice+1)
