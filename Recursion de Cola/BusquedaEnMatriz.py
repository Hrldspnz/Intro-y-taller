class Busqueda (object):
       def __init__(self):
              pass

       def buscarmatriz(self,elemento,matriz):
              if isinstance (matriz, list) and isinstance (elemento,int):
                     return self.buscarmatriz_aux(elemento,matriz,0,0)
              else:
                     return "Error"

       def buscarmatriz_aux(self,elemento,matriz,fila,col):
              if fila == len(matriz):
                return False
              elif col == len(matriz[0]):
                return self.buscarmatriz_aux(elemento,matriz,fila+1,0)
              elif elemento == matriz[fila][col]:
                return True
              else:
                     return self.buscarmatriz_aux(elemento,matriz,fila,col+1)




o= Busqueda()
matriz =  [[1,2,3,4],
           [5,6,7,8]]
elemento = 4

print(o.buscarmatriz(elemento,matriz))
