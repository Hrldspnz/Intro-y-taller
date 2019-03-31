def verifcero(lista):
    if isinstance (lista, list):
        return verificar (lista)
    else:
        return "Error: el valor no es una lista"


def verificar (lista):
    if lista == [ ]:
        return False
    elif (lista [0] == 0):
       return True
    else:
        return verificar(lista [1:])
       
