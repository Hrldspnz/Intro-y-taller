def sumar(lista):
       if isinstance (lista,list):
              return sumar_aux(lista)
       else:
              return "Error"

def sumar_aux(lista):

       if lista == []:
              return 0
       elif isinstance (lista[0],list):
              return sumar_aux(lista[0] + lista[1:])
       else:
              return lista[0] + sumar_aux(lista[1:])
