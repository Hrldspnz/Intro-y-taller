def par_impar (x):
    if (isinstance(x, int) and (x>0)):
        return numpar (x), numimpar(x)
    else:   return "Error"
    
def numpar (x):
    if (x == 0) :
        return 0    
    elif (x % 10 % 2 == 0):
        return 1 + numpar(x//10)
    else: return numpar (x // 10)
    
def numimpar (x):
    if (x == 0) :
        return 0    
    elif (x % 10 % 2 == 1):
        return 1 + numimpar(x//10)
    else: return numimpar (x // 10)
