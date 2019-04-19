class mayor(object):
       def __init__(self):
              pass
       
       def mayorlist(self,lista):
              if isinstance(lista,list):
                     return self.mayorlist_aux(lista,0,0)
              else:
                     return "Error"

       def mayorlist_aux(self,lista,result,i):
              if i == len(lista):
                     return result
              elif result <= lista[i]:
                     return self.mayorlist_aux(lista,lista[i],i+1)
              else:
                     return self.mayorlist_aux(lista,result,i+1)


m = mayor()
lista=[5,6,7,81,23,120,9,10,11]
print(m.mayorlist(lista))
