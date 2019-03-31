def palindromo(Palabra):
    if isinstance(Palabra,list):
        return palindromo_aux(Palabra)
    else:
        return "Error"

def palindromo_aux(palabra):
    if len(palabra)<=1:
        return True
    elif palabra[0]==palabra[-1]:
        return palindromo_aux(palabra[1:-1])
    else:
        return False


def promedio(numero,longitud):
    if isinstance(numero,int):
        return promedio_aux(numero,longitud)
    else:
        return "Error"

def promedio_aux(numero,longitud):
    if numero==0:
        return 0
    else:
        return (((numero%10)/longitud)+promedio_aux(numero//10,
                                                    longitud))
