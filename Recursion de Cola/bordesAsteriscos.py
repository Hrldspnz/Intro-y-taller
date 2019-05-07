class Change (object):
       def __init__(self):
              pass

       def asteriscos(self,matriz):
              if isinstance (matriz, list):
                     return self.asteriscos_aux(matriz,0,0,[],[])
              else:
                     return "Error"

       def asteriscos_aux(self,matriz,fila,col,result,refila):
              if fila == len(matriz):
                     return result
              elif col == len(matriz[0]):
                     return self.asteriscos_aux(matriz,fila+1,0,result+[refila],[])
              elif fila == 0 or fila == len(matriz)-1 or col == 0 or col == len(matriz[0])-1:
                     return self.asteriscos_aux(matriz,fila,col+1,result,refila+['*'])
              else:
                     return self.asteriscos_aux(matriz,fila,col+1,result,refila+[matriz[fila][col]])




o= Change()
matriz =  [[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]

print(o.asteriscos(matriz))
