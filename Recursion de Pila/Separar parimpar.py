def separarnum (num):
    if isinstance (num, list):
        par = lambda digito : digito % 2 == 0
        impar = lambda digito : digito % 2 == 1
        return (separar(num,par),separar(num,impar))
    else:
        return "Error"

def separar (num,condicion):
    if num == []:
        return []
    elif condicion (num[0]):
        return [num[0]] + separar(num[1:],condicion)
    else:
        return separar (num[1:],condicion)
