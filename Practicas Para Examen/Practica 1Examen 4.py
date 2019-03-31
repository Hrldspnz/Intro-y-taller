def multid(digi,num):
       if isinstance (num,int) and (digi,int):
              return multid_aux(digi,num,0)
       else:
              return "Error"

def multid_aux(digi,num,potencia):
       if num == 0:
              return 0
       elif digi * (num%10) <= 9:
              return digi * (num%10) * 10 ** potencia + multid_aux(digi,num // 10,potencia+1)
       else:
              return multid_aux(digi,num//10,potencia)

