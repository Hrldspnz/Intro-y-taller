class funcion (object):
      def __init__(self):
              pass
      def magico(self,matriz):
        if isinstance (matriz, list) :
            return self.magico_aux(matriz,0,0)
        else:
            return "Error"
      def magico_aux(self,matriz,fila,col)


l = funcion()
matriz = [[3,1,5],
          [4,7,2],
          [9,8,6]]

print(l.magico(matriz))
