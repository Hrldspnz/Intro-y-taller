class Suma (object):
       def __init__(self):
              pass

       def sumarmatriz(self,matriz):
              if isinstance (matriz, list):
                     return self.sumarmatriz_aux(matriz,len(matriz),len(matriz[0]),0,0,0)
              else:
                     return "Error"

       def sumarmatriz_aux(self,matriz,num_fil,num_col,fila,col,result):
              if fila == num_fil:
                     return result
              elif col == num_col:
                     return self.sumarmatriz_aux(matriz,num_fil,num_col,fila+1,0,result)
              else:
                     return self.sumarmatriz_aux(matriz,num_fil,num_col,fila,col+1,result + matriz[fila][col])




o= Suma()
lista = [[1,2,3,4],
            [5,6,7,8]]
print(o.sumarmatriz(lista))
