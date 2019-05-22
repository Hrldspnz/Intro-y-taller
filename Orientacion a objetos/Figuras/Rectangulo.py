import math
from Cuadrado import cuadrado

class rectangulo(cuadrado):
	def __init__(self, x, y, lado, ancho):
		super().__init__(x,y,lado)
		self.__ancho = ancho

	def getAncho(self):
		return self.__ancho

	def setAncho(self,ancho):
		self.__ancho = ancho	

	def calcularArea(self):
		return super().getLado() * self.__ancho
		