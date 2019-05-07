class Prom (object):
       def __init__(self):
              pass

       def prommatriz(self,matriz):
              if isinstance (matriz, list):
                     return self.prommatriz_aux(matriz,0,0,0)/(len(matriz)*len(matriz[0]))
              else:
                     return "Error"

       def prommatriz_aux(self,matriz,fila,col,result):
              if fila == len(matriz):
                     return result
              elif col == len(matriz[0]):
                     return self.prommatriz_aux(matriz,fila+1,0,result)
              else:
                     return self.prommatriz_aux(matriz,fila,col+1,result + matriz[fila][col])




o= Prom()
matriz =  [[1,2,3,4],
           [5,6,7,8]]

print(o.prommatriz(matriz))
