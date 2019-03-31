#20 pts
def convertir (num):
       if isinstance (num,float): #5 pts
              return (convertir_int(num// )),convertir_float(num - num // 1)) #7.5 pts
       else:
              return "Error"#7.5 pts

#40 pts
def convertir_int(num):
       if num == 0: #10 pts
              return [ ] # 10 pts
       else:
              return convertir_int(num // 2) + [num % 2] #20 pts

#40 pts
def convertir_float(num):
       if num == 1.0:#10 pts
              return [ 1 ]
       elif num * 2 <= 1:
              return [int(num * 2 )] + convertir_float(num * 2)#20 pts
       else:
              return [int(num * 2 )] + convertir_float(num * 2 - 1)#20 pts
