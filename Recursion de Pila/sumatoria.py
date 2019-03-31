def sumatoria(i,n):
        if ((isinstance(n, int) and (n>0)) and (isinstance(i, int) and(i==0))):
            return sumatoria2 (n,i)
        else:   return "Error"


def sumatoria2(i,n):
    if (i>n):
        return 0
    else:
        return (i + 3) + sumatoria2(i+1,n)
