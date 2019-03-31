def pareslist(lista):
       if isinstance (lista,list):
              par = lambda digito : digito % 2 == 0
              return pares_list(lista,par,[])
       else:
              return "Error"

def pares_list(lista,par, result):
       if lista == []:
              return result
       elif par(lista[0]):
              return pares_list(lista[1:],par,result + [lista[0]])
       else:
              return pares_list(lista[1:],par,result)
              
