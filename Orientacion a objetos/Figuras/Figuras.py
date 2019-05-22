class fig:
	def __init__(self,x,y):
		self.__x = x #con "__" se encapsula, osea se oculta
		self.__y = y

	def getX(self):
		return self.__x

	def setX(self, x):
		if x >= 0 and x <=1023:
			self.__x = x
		else:
			print("El valor debe estar entre 0 y 1023")

	def getY(self):
		return self.__y

	def setY(self,y):
		if y >= 0 and y <= 767:
			self.__y = y
		else:
			print("El valor debe estar entre 0 y 763")


