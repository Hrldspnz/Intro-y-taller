def verificar (n):
    if (isinstance (n, int)):
      return verif(n)
    else:
      return "Error"

def verif(n):    
    if (n == 0) :
           return True   
    elif (4 >= n % 10 >= 0):
            return verif(n//10,)

    else: return False
