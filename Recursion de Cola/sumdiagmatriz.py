class Suma (object):
       def __init__(self):
              pass

       def sumdiagmatriz(self,matriz):
        if isinstance (matriz,list):
          return self.sumdiagmaux(matriz,0,0)
        else:
          return "Error en la matriz"

       def sumdiagmaux(self,matriz,pfila,result):
        if pfila == len(matriz):
          return result
        else:
          return self.sumdiagmaux(matriz,pfila+1,result+matriz[pfila][pfila])

m = Suma()
matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(m.sumdiagmatriz(matriz))