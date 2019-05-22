#-------------------------------Problema 1------------------------------------------
class generar(object):
	def __init__(self):
		pass

	def matriz(self,numero):
		if isinstance (numero,int):
			return self.matrizaux(numero,0,0,0,[ ],[ ])
		else:
			return "Error"

	def matrizaux(self,num,fila,col,asteriscos,rfila,rmatriz):
		if fila == num:
			return rmatriz #Profe sin querer me comí la "r" por la presion del examen pero me referia a la matriz reultante
		elif col == num:
			return self.matrizaux(num,fila+1,0,asteriscos+1,[],rmatriz+[rfila])
		elif col < asteriscos:
			return self.matrizaux(num,fila,col+1,asteriscos,rfila+["*"],rmatriz)
		else:
			return self.matrizaux(num,fila,col+1,asteriscos,rfila+[asteriscos+1],rmatriz)

#----------------------------Problema 2-------------------------------------------------
class orden(object):
	def __init__(self):
		pass

	def permutaciones(self,nobjetos,xobjetos):
		if isinstance(nobjetos,int) and isinstance(xobjetos,int) and nobjetos > xobjetos:
			return self.permutacionesaux(nobjetos,1,1)//self.permutacionesaux(nobjetos-xobjetos,1,1)
		else:
			return "Error"

	def permutacionesaux(self,num,factorial,total):
		if factorial > num:
			return total
		else:
			return self.permutacionesaux(num,factorial+1,total*factorial)

#-----------------------------Problema 3--------------------------------------------------
class cubo(object):
	def __init__(self):
		pass

	def es_magico(self,matriz):
		if isinstance(matriz,list) and len(matriz)==len(matriz[0]):
			return self.comparar(self.sumfila(matriz,0,0,0,[])+self.sumcol(matriz,0,0,0,[])+
								[self.sumdiag(matriz,0,0)]+[self.sumantid(matriz,0,0)],0)
		else:
			return "Error"

	def comparar(self,lista,indice):
		if indice == (len(lista)-1):
			return True
		elif lista[indice]==lista[indice+1]:
			return self.comparar(lista,indice+1)
		else:
			return False

	def sumfila(self,matriz,fila,col,suma,result):
		if fila == len(matriz):
			return result
		elif col == len(matriz[0]):
			return self.sumfila(matriz,fila+1,0,0,result+[suma])
		else:
			return self.sumfila(matriz,fila,col+1,suma+matriz[fila][col],result)

	def sumcol(self,matriz,fila,col,suma,result):
		if col == len(matriz[0]):
			return result
		elif fila == len(matriz):
			return self.sumcol(matriz,0,col+1,0,result+[suma])
		else:
			return self.sumcol(matriz,fila+1,col,suma+matriz[fila][col],result)

	def sumdiag(self,matriz,indice,suma):
		if indice == len(matriz):
			return suma 
		else:
			return self.sumdiag(matriz,indice+1,suma+matriz[indice][indice])

	def sumantid(self,matriz,indice,suma):
		if indice == len(matriz):
			return suma 
		else:
			return self.sumantid(matriz,indice+1,suma+matriz[indice][-(indice+1)])

#---------------------------Problema 4-------------------------------------------------------------------
class graficar(object):
	def __init__(self):
		pass

	def grafico(self,datos):
		if isinstance(datos,list) and datos != []:
			return self.graficoaux(datos,len(datos),0,0,self.mayor(datos,0,0),[],[])
		else:
			return "Error"

	def mayor(self,lista,indice,mayor):
		if indice == len(lista): #Se me fueron estos dos puntos
			return mayor
		elif lista[indice] > mayor:
			return self.mayor(lista,indice+1,lista[indice])
		else:
			return self.mayor(lista,indice+1,mayor)

	def graficoaux(self,datos,filas,indicef,asteriscos,colums,rfila,rmatriz): #estos dos puntos tambien se me fueron 
		if indicef == filas:
			return rmatriz
		elif asteriscos == colums:
			return self.graficoaux(datos,filas,indicef+1,0,colums,[],rmatriz+[rfila])
		elif asteriscos < datos[indicef]:
			return self.graficoaux(datos,filas,indicef,asteriscos+1,colums,rfila+["*"],rmatriz)
		else:
			return self.graficoaux(datos,filas,indicef,asteriscos+1,colums,rfila+[" "],rmatriz)













