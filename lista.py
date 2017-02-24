class ListaOrdenada:
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

	def agregar(self,valor):
		if self.valor == None:
			self.valor = valor
         
		elif self.siguiente:
			self.siguiente.agregar(valor)
		else:
			self.siguiente = ListaOrdenada(valor)

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

	def insertar(self,valor,indice):
		if indice == 0:
			if self.siguiente:
				temp = ListaOrdenada()
				temp.valor = self.valor
				temp.siguiente = self.siguiente
				self.valor = valor
				self.siguiente = temp
				return True
			
		elif self.siguiente:
			return self.siguiente.insertar(valor, indice-1)
		
		else:
			return False

	"""def insertar(self,valor,indice):
		if indice == 0:
			if not self.valor:
				self.valor = valor
			else:
				temp = self.siguiente
				self.siguiente = ListaOrdenada(valor)
				self.siguiente.siguiente = temp
		
		elif self.siguiente:
			self.siguiente.insertar(valor, indice-1)
		
		else:
			return None 
	"""
	def remover(self,indice,anterior = None):
		if indice == 0:
			if anterior:
				anterior.siguiente = self.siguiente
			else:
				if self.siguiente:
					self.valor = self.siguiente.valor
					self.siguiente = self.siguiente.siguiente
				else:
					self.valor = None
			return True
		elif self.siguiente:
			self.siguiente.remover(indice-1)
		
		else:
			return False
		
		
