def menordelista(lista):
    if isinstance (lista, list) :
        return menor (lista)
    else:
        return "Error: el valor no es una lista"


def menor (lista):
    if lista[1:] == [ ]:
        return lista [0]
    elif (lista [0] >= lista [1] ):
       return menor ([lista [0]] + lista [2:])
    else:
        return menor (lista [1:])
