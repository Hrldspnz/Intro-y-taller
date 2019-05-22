#--------------------------Problema 1--------------------------------------#
class SumaMatriz(object):
	def __init__(self):
		pass

	def sumas(self,matriz):
		if isinstance (matriz,list) and len(matriz)==len(matriz[0]):
			return (self.sumafila(matriz,0,0),self.sumacol(matriz,0,0),self.sumantid(matriz,0,0),
					self.sumafila(matriz,0,0)+self.sumacol(matriz,0,0)+self.sumantid(matriz,0,0))
		else:
			return "Error en la matriz"

	def sumafila(self,matriz,result,indice):

		if indice == len(matriz[0]):
			return result

		else:
			return self.sumafila(matriz,result+matriz[0][indice]+matriz[-1][indice],indice+1)

	def sumacol(self,matriz,result,indice):

		if indice == len(matriz):
			return result

		else:
			return self.sumacol(matriz,result+matriz[indice][0]+matriz[indice][-1],indice+1)

	def sumantid(self,matriz,result,indice):

		if indice==len(matriz):
			return result
		else:
			return self.sumantid(matriz,result+matriz[indice][-(indice+1)],indice+1)

matriz = [[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]]
s = SumaMatriz()
print(s.sumas(matriz))


#------------------------------Problema 2--------------------------#

class EstadisticaMatriz(object):
	def __init__(self):
		pass

	def estadisticas(self,matriz):
		if isinstance(matriz,list) and len(matriz) == len(matriz[0]):
			return (self.promdiag(matriz,0,0)//len(matriz),self.mediana(matriz))
		else:
			return "Error"

	def promdiag(self,matriz,indice,result):
		if indice == len(matriz):
			return result
		else:
			return self.promdiag(matriz,indice+1,result+matriz[indice][indice])

	def mediana(self,matriz):
		if len(matriz)%2 == 0:
			return (matriz[len(matriz)//2-1][len(matriz)//2-1]+matriz[len(matriz)//2][len(matriz)//2])/2
		else:
			return (matriz[len(matriz)//2][len(matriz)//2])/2
		
matriz =  ([[8, 12, 16], [20, 24, 28], [32, 36, 40]])
m=EstadisticaMatriz()
print(m.estadisticas(matriz))

#--------------------------------Problema 3-------------------------------------------------------#

class factor(object):
	def __init__(self):
		pass
	def polinomio(self,bx,c):
		if isinstance (bx,int) and isinstance (c, int):
			return self.factorizar(bx,c,1)
		else:
			return "Error"

	def factorizar(self,bx,c,factor):
		if factor == c:
			return "El polinomio no tiene factores"
		elif c%factor == 0:
			if c//factor+factor == bx:
				return (c//factor,factor)
			else:
				return self.factorizar(bx,c,factor+1)
		else:
			return self.factorizar(bx,c,factor+1)
		
bx = (9)
c = (18)
f = factor()
print(f.polinomio(bx,c))

#--------------------------------Problema 4-------------------------------------------------------#
class Notcientifica(object):
	def __init__(self):
		pass

	def notacion(self,numero):
		if numero != 0:
			return self.conversion(numero,0)
		else:
			return "Error el numero no puede ser 0"

	def conversion(self,numero,exponente):
		if 1 <= numero < 10:
	 		return str(numero) +" x 10 ** "+str(exponente)
		elif numero < 1:
			return self.conversion(numero*10,exponente-1)
		else:
			return self.conversion(numero//10,exponente+1)

n = Notcientifica()
numero = (0.0000000000000166)
print(n.notacion(numero))
		