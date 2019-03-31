def sumatoria(n):
        if ((isinstance(n, int) and (n>0))):
            return sumatoria2 (n)
        else:   return "Error"


def sumatoria2(n):
    if (n<0):
        return 0
    else:
        return (n + 3) + sumatoria2(n-1)
