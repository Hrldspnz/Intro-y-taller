class mult (object):
       def __init__(self):
              pass

       def producto(self,mat1,mat2):
              if isinstance (mat1, list) and isinstance(mat2,list):
                     return self.producto_aux(mat1,mat2,0,0,0,0,[],[])
              else:
                     return "Error"

       def producto_aux(self,mat1,mat2,fila,centro,col,result,refila,matriz):
              if fila == len(mat1):
                     return matriz
              elif col == len(mat2[0]):
                     return self.producto_aux(mat1,mat2,fila+1,0,0,0,[],matriz+[refila])
              elif centro == len(mat1[0]):
                     return self.producto_aux(mat1,mat2,fila,0,col+1,0,refila+[result],matriz)
              else:
                     return self.producto_aux(mat1,mat2,fila,centro+1,col,result+mat1[fila][centro]*mat2[centro][col],refila,matriz)




o= mult()
mat1 = [[1,2,3,4],
        [1,2,3,4]]

mat2 = [[2,3,4],
        [2,3,4],
        [2,3,4],
        [2,3,4]]

print(o.producto(mat1, mat2))
