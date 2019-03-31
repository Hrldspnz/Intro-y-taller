#Problama 1)
def multiplicaciones(lista):
    if isinstance (lista, list):
        return multip(lista,0)
    else:
        return "Error"

def multip(lista,indice):
    if lista == []:
        return []
    else:
        return [lista[0] * indice] + multip(lista[1:],indice+1)

#Problema 2)
def suma(lista):
    if isinstance (lista,list):
        return suma_aux(lista,0)
    else:
        return "Error"

def suma_aux(lista,i):
    if lista == []:
        return 0
    elif isinstance(lista[0],list):
        return suma_aux(lista[0]+lista[1:],i)
    else:
        return lista[0]**(i+1) + suma_aux(lista[1:],i+1)

#Problema 3)
def summ(n):
    if isinstance (n,int):
        return summ_aux(n,1)
    else:
        return "Error"

def summ_aux(n,j):
    if n < j:
        return 0
    else:
        return mult(j,1)+ summ_aux(n,j+1)

def mult(j,z):
    if j < z:
        return 1
    else:
        return (3*(z**2) - z) * mult(j,z+1)

#Problema 4)
def intercambiar(num):
    if isinstance (num,int):
        return intercambiar_aux(num,0)
    else:
        return "Error"

def intercambiar_aux(num,potencia):
    if num == 0:
        return 0
    else:
        return ((num%10)*10**(potencia+1)) + ((num%100//10) *10** potencia) + intercambiar_aux(num//100,potencia+2)
    
