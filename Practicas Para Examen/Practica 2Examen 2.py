class cons (object):
      def __init__(self):
              pass
      def consecutivos(self,matriz):
              if isinstance (matriz, list) :
                     return self.consecutivos_aux(1,matriz,0,0)
              else:
                     return "Error"

      def consecutivos_aux(self,elemento,matriz,fila,col):
              if elemento > len(matriz)**2:
                return True
              elif fila == len(matriz):
                return False
              elif col == len(matriz[0]):
                return self.consecutivos_aux(elemento,matriz,fila+1,0)
              elif elemento == matriz[fila][col]:
                return self.consecutivos_aux(elemento+1,matriz,0,0)
              else:
                return self.consecutivos_aux(elemento,matriz,fila,col+1)

l = cons()
matriz = [[3,1,5],
          [4,7,2],
          [9,8,6]]

print(l.consecutivos(matriz))
