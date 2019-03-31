def pareslista(num):
       if isinstance (num,int):
              par = lambda digito : digito % 10 % 2 == 0
              return pareslista2(num,par)
       else: return "Error el numero no es un entero"


def pareslista2(num,condicion):
       if num == 0:
              return []
       elif condicion(num%10):
              return [num%10] + pareslista2(num//10,condicion)
       else:
              return pareslista2(num//10,condicion)
