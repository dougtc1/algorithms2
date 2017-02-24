class ColaP:
	def __init__(self,valor=None,siguiente=None):
		self.valor = valor
		self.siguiente = siguiente
	
	def encolar(self,valor):
		if self.valor == None:
			self.valor = valor

		else:
			if self.valor.prioridad > valor.prioridad:
				temp = ColaP()
				temp.valor = self.valor
				temp.siguiente = self.siguiente
				self.valor = valor
				self.siguiente = temp
			elif self.siguiente:
				self.siguiente.encolar(valor)
			else:
				self.siguiente = ColaP()
				self.siguiente.valor = valor

	def imprimir(self):
		if self.valor.destinatario:
			return(self.valor.destinatario,self.valor.prioridad)
		if self.siguiente:
			self.siguiente.imprimir()
		
	def obtener(self,indice):
		if indice == 0:
			return self.valor.destinatario
		elif self.siguiente:
			return self.siguiente.obtener(indice-1)
		else:
			return None

	def desencolar(self):

		salida = self.valor

		if (self.siguiente == None):

			self.valor = None

		else:

			temp = ColaP()
			temp.valor = self.siguiente.valor
			temp.siguiente = self.siguiente.siguiente
			self.valor = temp.valor
			self.siguiente = temp.siguiente

		return (salida)

	def esVacia(self):
		if self.valor:
			return False
		else:
			return True