def sumabin(lista,lista2,a):
    if ((isinstance (lista,list))and (isinstance(lista2, list) and (len(lista)==len(lista2)) and (isinstance(a,int)))):
            return suma_bin(lista,lista2,a)
    else:
            return "Error: hay un problema, revise los parametros"


def suma_bin(lista,lista2,a):
    if lista == [ ]:
        return [a]
    elif (lista[-1] + lista2[-1] + a == 2):
        return suma_bin(lista[:-1],lista2[:-1],a=1) + [0]
    elif (lista[-1] + lista2[-1] + a == 3):
        return suma_bin(lista[:-1],lista2[:-1],a=1) + [1]
    else:
        return suma_bin(lista[:-1],lista2[:-1],a=0) + [lista[-1]+lista2[-1]+a]

    
