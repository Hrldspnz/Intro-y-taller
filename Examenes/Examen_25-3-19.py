#1
def combinaciones(hp,dell):
    if isinstance(hp,list)and (dell,list):
        return combinaciones_aux(hp,dell)+combinaciones_2(hp,dell)
    else:
        return "Error"

def combinaciones_aux(hp,dell):
    if hp == []:
        return []
    else:
        return [hp[0]+dell[0]]+ combinaciones_aux(hp[1:],dell)

def combinaciones_2(hp,dell):
    if hp == []:
        return []
    else:
        return [hp[0]+dell[1]] + combinaciones_2(hp[1:],dell)


#2
import math
def std(lista,avg):
    if isinstance (lista,list):
        return (math.sqrt(std_aux(lista,avg)/(len(lista)-1)))
    else:
        return "Error"

def std_aux(lista,avg):
    if lista == []:
        return 0
    else:
        return (lista[0]-avg)**2 + std_aux(lista[1:],avg)


#3
def zScore(listaX,S,avg):
    if isinstance(listaX,list):
        return zScore_aux(listaX,S,avg)
    else:
        return "Error"

def zScore_aux(listaX,S,avg):
    if listaX == []:
        return []
    else:
        return [(listaX[0]-avg)/S]+ zScore_aux(listaX[1:],S,avg)


#4
def rScore(Zx,Zy):
    if (isinstance (Zx,list) and (Zy,list) and (isinstance
                        (len(Zx)==len(Zy)))):
        return (rScore_aux(Zx,Zy)/(len(Zx)-1))
    else:
        return "Error"

def rScore_aux(Zx,Zy):
    if Zx == [] and Zy == []:
        return 0
    else:
        return(Zx[0]*Zy[0]) + rScore_aux(Zx[1:],Zy[1:])
