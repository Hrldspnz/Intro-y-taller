def verifpos(lista):
    if isinstance (lista, list):
        return verificar (lista)
    else:
        return "Error: el valor no es una lista"


def verificar (lista):
    if lista == [ ]:
        return True
    elif (lista [0] < 0):
       return False
    else:
        return verificar(lista [1:])
       
