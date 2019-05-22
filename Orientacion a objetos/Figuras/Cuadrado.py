import math
from Figuras import fig

class cuadrado(fig):
	def __init__(self, x, y, lado):
		super().__init__(x,y)
		self.__lado = lado

	def getLado(self):
		return self.__lado

	def setLado(self,lado):
		self.__lado = lado

	def calcularArea(self):
		return self.__lado * self.__lado
		