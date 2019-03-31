import math
def sumatoriaL(lista,i):
    if len(lista)==i:
        return 0
    else: return math.sqrt(lista[i])+ sumatoriaL(lista,i+1)
    #else: return (lista[i]**(1/2))+ sumatoriaL(lista,i+1)
     
