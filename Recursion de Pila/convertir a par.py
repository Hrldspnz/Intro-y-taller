def div_par_impar(n,p):
    if ((isinstance(n, int) and (n>0)) and (isinstance(p, int) and(p==0))):
        return conjunto_par (n,p),conjunto_impar (n,p)
    else:   return "Error"

def conjunto_par (n,p):
    
    if (n == 0) :
           return 0    
    elif (n % 10 % 2 == 0):
            return ((n%10) * (10 ** p) + conjunto_par(n//10,p+1))
         
    else:
            return  conjunto_par (n // 10,p)

def conjunto_impar (n,p):
    
    if (n == 0) :
           return 0    
    elif (n % 10 % 2 == 1):
            return ((n%10) * (10 ** p) + conjunto_impar(n//10,p+1))
         
    else:
            return  conjunto_impar (n // 10,p)
                    
