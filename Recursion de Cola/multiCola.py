def multi(num):
       if isinstance (num,list):
              return multiplicacion(num,1)
       else:
              return "Error"


def multiplicacion(num,result):
       if num == [ ]:
              return result
       else:
              return multiplicacion(num[1:],result * num[0])
