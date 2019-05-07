class Prom (object):
       def __init__(self):
              pass

       def prommatriz(self,matriz):
              if isinstance (matriz, list):
                     return self.prommatriz_aux(matriz,0)/(len(matriz)*len(matriz[0]))
              else:
                     return "Error"

       def prommatriz_aux(self,matriz,result):
              if matriz == []:
                     return result
              elif isinstance (matriz[0],list):
                     return self.prommatriz_aux(matriz[0]+matriz[1:],result)
              else:
                     return self.prommatriz_aux(matriz[1:],result + matriz[0])




o= Prom()
matriz =  [[1,2,3,4],
           [5,6,7,8]]

print(o.prommatriz(matriz))
