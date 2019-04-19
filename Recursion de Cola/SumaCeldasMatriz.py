class Suma (object):
       def __init__(self):
              pass

       def sumarmatriz(self,matriz1,matriz2):
              if (isinstance (matriz1, list) and isinstance(matriz2, list) and len(matriz1) == len(matriz2)
                  and len(matriz1[0]) == len(matriz2[0])):
                     return self.sumarmatriz_aux(matriz1,matriz2, len(matriz1),len(matriz2[0]),0,0,[],[])
              else:
                     return "Error"

       def sumarmatriz_aux(self,matriz1,matriz2,num_fil,num_col,fila,col,result,rfila):
              if fila == num_fil:
                     return result
              elif col == num_col:
                     return self.sumarmatriz_aux(matriz1,matriz2,num_fil,num_col,fila+1,0,result+[rfila],[])
              else:
                     return self.sumarmatriz_aux(matriz1,matriz2, num_fil,num_col,fila,col+1,result, rfila + [matriz1[fila][col]+matriz2[fila][col]])




o= Suma()
matriz1 = [[1,2,3,4],
           [5,6,7,8]]

matriz2 = [[4,3,2,1],
           [8,7,6,5]]
print(o.sumarmatriz(matriz1, matriz2))
