def sumatoriaL(lista,i):
    if len(lista)==i:
        return 0
    else: return lista[i]*i*5**3 + sumatoriaL(lista,i+1)
