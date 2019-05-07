class invert (object):
      def __init__(self):
              pass
      def invertir(self,lista):
        if isinstance(lista,list) and len(lista)%2 == 0:
          return self.invertir_aux(lista,0,-1)
        else:
          return "Error"

      def invertir_aux(self,lista,indice,indice2):
        if indice == len(lista)/2:
          return lista
        else:
            lista[indice],lista[indice2] = lista[indice2],lista[indice]
            return self.invertir_aux(lista,indice+1,indice2-1)

l = invert()
lista = [1,2,3,4]

print(l.invertir(lista))
