def suma_digitos (x):
    if isinstance (x, int) and (x > 0):
        return suma_digitos2 (abs (x))
    else:
        return "ERROR"
    
def suma_digitos2 (x):
    if (x == 0) :
        return 0
    else:
        return x % 10 + suma_digitos2 (x // 10)
