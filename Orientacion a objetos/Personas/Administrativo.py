from Persona import Persona

class Administrativo(Persona):
	def __init__(self, nombre, cedula, edad, departamento, puesto):
		super().__init__(nombre, cedula, edad)
		self.__departamento = departamento
		self.__puesto = puesto

	@Property
	def departamento(self):
		return self.__departamento
	@departamento.setter
	def departamento(self, departamento):
		self.__departamento = departamento

	@Property
	def puesto(self):
		return self.__puesto
	@puesto.setter
	def puesto(self, puesto):
		self.__puesto = puesto