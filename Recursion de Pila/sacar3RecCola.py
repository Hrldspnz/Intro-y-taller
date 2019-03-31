class divisor(object):
       
       def __init__(self):
              pass

       def dividir (self,num):
              if isinstance(num,int):
                     return self.div(num,0,0)
              else:
                     return "Error, el numero no es un entero"

       def div (self, num, potencia,resultado):
              if num == 0:
                     return resultado
              elif num%10%3==0:
                     return self.div(num//10,potencia,resultado)
              else:
                     return self.div(num//10,potencia+1,(resultado + num%10*10**potencia)) 
              
              
       
