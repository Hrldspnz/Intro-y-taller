#1
def combinaciones (hp,dell):
       if isinstance(hp, list) and (dell,list) and len(hp) >0 and len(dell)>0:
              return combinaciones_aux(hp,dell)
       else:
              return "Error, hay un problema con las listas"

def combinaciones_aux(hp,dell):
       if hp == []:
              return []
       else:
              return comb_aux(hp[0],dell) + combinaciones_aux(hp[1:],dell)

def comb_aux(hp,dell):
       if dell == []:
              return []
       else:
              return [hp + dell[0]] +comb_aux(hp,dell[1:])

#2
import math
def std (lista,avg):
       if isinstance(lista,list) and isinstance(avg,float):
              return math.sqrt(std_aux(lista,avg)/(len(lista)-1))
       else:
              return "Error, hay un problema con los parammetros"

def std_aux(lista,avg):
       if lista == []:
              return 0
       else:
              return (lista[0]-avg)**2 + std_aux(lista[1:],avg)


#3
def zScore(listaX,S,avg):
       if isinstance (listaX,list) and (S,float) and (avg,float):
              return zScore_aux(listaX,S,avg)
       else:
              return "Error"

def zScore_aux(listaX,S,avg):
       if listaX== []:
              return []
       else:
              return [(listaX[0]-avg)/S] + zScore_aux(listaX[1:],S,avg)
       

#4
def rScore(Zx,Zy):
       if isinstance(Zx,list) and (Zy,list) and len(Zx==Zy):
              return rScore_aux(Zx,Zy)
       else:
              return "Error, problema con las listas"

def rScore_aux(Zx,Zy):
       if Zx == [] and Zy == []:
              return 0
       else:
              return (Zx[0]*Zy[0]) + rScore_aux(Zx[1:],Zy[1:])
































       
