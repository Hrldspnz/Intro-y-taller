def medgeo(lista):
    if isinstance (lista, list):
        return medgeometrica(lista)-1,medgeometrica(lista)**(1/len(lista))-1
    else:
        return "Error hay un problema con la lista"

def medgeometrica(lista):
    if lista == []:
        return 1
    else:
        return lista[-1]*medgeometrica(lista[:-1])


