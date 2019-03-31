#Problema 1)
def formarLista(num):
    if isinstance (num, int) and num != 0:
        return formar_lista(num)
    else:
        return "Error"

def formar_lista(num):
    if num == 0:
        return [ ]
    elif num % 10 % 2 == 0:
        return formar_lista(num // 10) + [num%10]
    else:
        return formar_lista(num // 10)


#Problema 2)
def palindromo(num):
    if isinstance (num,int) and num != 0:
        return comparar(num,invertir(num,cantidad(num)))
    else:
        return "Error"
def cantidad (num):
    if num == 0:
        return 0
    else:
        return 1 + cantidad(num//10)

def invertir(num,largo):
    if num == 0:
        return 0
    else:
        return (num % 10)*10**(largo-1) + invertir(num//10,largo-1)


def comparar(num,invertido):
    if num == invertido:
        return True
    else:
        return False




#Problema 3)
def contarConsonantes(palabra):
    if isinstance (palabra, str):
        return contarconsonantes_aux(palabra)
    else:
        return "Error"

def contarconsonantes_aux(palabra):
    if palabra == "":
        return 0
    elif (palabra [0] == "a" or palabra [0] == "e" or palabra [0] == "i"
            or palabra [0] == "o" or palabra [0] == "u"):
        return contarconsonantes_aux(palabra[1:])
    else:
        return 1 + contarconsonantes_aux(palabra[1:])

#Problema 4)
def intercambiar(lista):
    if isinstance (lista,list):
        return intercambiar_aux(lista)
    else:
        return "Error"

def intercambiar_aux(lista):
    if lista == [ ]:
        return []
    else:
        return [lista[1]]+[lista[0]] + intercambiar_aux(lista[2:])
