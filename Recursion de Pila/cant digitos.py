def num_par (x):
    if (isinstance(x, int) and (x>0)):
        
        return numpar (x)
    else:   return "Error"
    
def numpar (x):
    if (x <= 0) :
        return 0
    
    elif (x % 10 % 2 == 0):
        return 1 + numpar(x//10)
    else: return numpar (x // 10)
