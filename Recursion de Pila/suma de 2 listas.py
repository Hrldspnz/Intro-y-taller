def sumadelistas (lista,lista2):
    if ((isinstance (lista,list))and (isinstance(lista2, list) and (len(lista)==len(lista2)))):
        return sumalists(lista, lista2)
    else:
        return "Error: hay un problema con la lista"

def sumalists(lista, lista2):
    if lista == [ ] :
        return 0

    else:
        return lista [0] + lista2 [0] + sumalists(lista[1:],lista2[1:])
