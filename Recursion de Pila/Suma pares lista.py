def sumarpar (lista):
    if isinstance (lista, list):
        return sumarparlist (lista)
    else:
        return "Error: el valor no es una lista"


def sumarparlist (lista):
    if lista == [ ]:
        return 0
    elif (lista [0] % 2 == 0):
       return (lista [0] + sumarparlist (lista [1:]))
    else:
        return sumarparlist (lista [1:])
       
