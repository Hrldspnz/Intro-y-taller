def sumar (lista):
    if isinstance (lista, list):
        return sumalist (lista)
    else:
        return "Error: el valor no es una lista"


def sumalist (lista):
    if lista == [ ]:
        return 0
    else:
        return lista [0] + sumalist(lista[1:])
