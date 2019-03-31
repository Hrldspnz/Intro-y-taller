def separarnum (num):
    if isinstance (num, list):
        negativo = lambda digito : digito < 0
        positivo = lambda digito : digito >= 0
        return (separar(num,negativo),separar(num,positivo))
    else:
        return "Error"

def separar (num,condicion):
    if num == []:
        return []
    elif condicion (num[0]):
        return [num[0]] + separar(num[1:],condicion)
    else:
        return separar (num[1:],condicion)
