class PilaOrdenada:
	def __init__(self,valor=None,siguiente=None):
		self.valor = valor
		self.siguiente = siguiente
	
	def longitud(self):
		if self.siguiente:
			return self.siguiente.longitud() + 1

		elif self.valor:
			return 1
		else:
			return 0

	def empilar (self,valor):
		
		temp = PilaOrdenada()
		temp.valor = self.valor
		temp.siguiente = self.siguiente
		self.valor = valor
		self.siguiente = temp
		return True

	def imprimir(self):
		if self.valor:
			print(self.valor)
		if self.siguiente:
			self.siguiente.imprimir()
		
	def obtener(self,indice):
		if indice == 0:
			return self.valor
		elif self.siguiente:
			return self.siguiente.obtener(indice-1)
		else:
			return None

	def desempilar(self):
		
		self.valor = self.siguiente
		self.siguiente = self.siguiente.valor
		return True