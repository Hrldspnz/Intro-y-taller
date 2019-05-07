class Transp (object):
       def __init__(self):
              pass

       def transpmatriz(self,matriz):
        if isinstance (matriz,list):
          return self.transpuestamataux(matriz,0,0,[],[])
        else:
          return "Error en la matriz"
       def transpuestamataux(self,matriz,pfila,pcol,result,rfila):
        if pcol == len(matriz[0]):
          return result
        elif pfila == len(matriz):
          return self.transpuestamataux(matriz,0,pcol+1,result+[rfila],[])
        else:
          return self.transpuestamataux(matriz,pfila+1,pcol,result,rfila+[matriz[pfila][pcol]])
         

m = Transp()
matriz = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]
print(m.transpmatriz(matriz))