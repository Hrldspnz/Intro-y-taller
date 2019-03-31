#1
def combinaciones (hp,dell):
       if isinstance(hp, list) and (dell,list) and len(hp) >0 and len(dell)>0:
              return combinaciones_aux(hp,dell,[])
       else:
              return "Error, hay un problema con las listas"

def combinaciones_aux(hp,dell,resultado):
       if hp == []:
              return resultado
       else:
              return  combinaciones_aux(hp[1:],dell,resultado + comb_aux(hp[0],dell,[]))
       
def comb_aux(hp,dell,Preresult):
       if dell == []:
              return Preresult
       else:
              return comb_aux(hp,dell[1:],Preresult + [hp + dell[0]])

#2
import math
def std (lista,avg):
       if isinstance(lista,list) and isinstance(avg,float):
              return math.sqrt(std_aux(lista,avg,0)/(len(lista)-1))
       else:
              return "Error, hay un problema con los parammetros"

def std_aux(lista,avg,result):
       if lista == []:
              return result
       else:
              return std_aux(lista[1:],avg,result + (lista[0]-avg)**2)

#3
def zScore(listaX,S,avg):
       if isinstance (listaX,list) and (S,float) and (avg,float):
              return zScore_aux(listaX,S,avg,[])
       else:
              return "Error"

def zScore_aux(listaX,S,avg,resultado):
       if listaX == []:
              return resultado
       else:
              return zScore_aux(listaX[1:],S,avg,resultado + [(listaX[0]-avg)/S])

#4
def rScore(Zx,Zy):
       if isinstance(Zx,list) and (Zy,list) and len(Zx==Zy):
              return rScore_aux(Zx,Zy,0)
       else:
              return "Error, problema con las listas"

def rScore_aux(Zx,Zy,result):
       if Zx == [] and Zy == []:
              return result
       else:
              return rScore_aux(Zx[1:],Zy[1:],result + (Zx[0]*Zy[0]))
