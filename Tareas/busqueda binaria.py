class buscar(object):
       def __init__(self):
              pass

       def busqueda(self,num,lista):
              if isinstance (num,int) and isinstance(lista,list):
                     return self.busqueda_aux(num,lista,0,len(lista)-1,(len(lista)-1)//2)
              else:
                     return "Error"

       def busqueda_aux(self,num,lista,inicio,final,indice):
              if final<inicio:
                     return -1
              elif lista[indice] == num:
                     return indice
              elif lista [indice]<num:
                     return self.busqueda_aux(num,lista,indice+1,final,(inicio+final)//2)
              else:
                     return self.busqueda_aux(num,lista,inicio,indice-1,(inicio+final)//2)
