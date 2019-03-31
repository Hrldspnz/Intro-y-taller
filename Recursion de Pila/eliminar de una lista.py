def deletelist(lista, x):
    if (isinstance (lista, list) and isinstance(x, int)):
        return eliminar (lista, x)
    else:
        return "Error: el valor no es una lista"


def eliminar (lista, x):
    if lista == [ ]:
        return [ ]
    elif (lista [0] == x):
       return eliminar (lista[1:], x)
    else:
        return [lista[0]] + (lista [1:], x)
       
