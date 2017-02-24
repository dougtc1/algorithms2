class Pila:
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
		if self.valor == None:
			self.valor = valor
         
		elif self.siguiente:
			self.siguiente.empilar(valor)
		else:
			self.siguiente = Pila(valor)

	def imprimir(self):	
		if self.valor != None and self.siguiente == None:
			return (self.valor)
		if self.siguiente and self.valor:
			self.siguiente.imprimir()

		
	def obtener(self,indice):
		if indice == 0:
			return self.valor

		elif self.siguiente:
			return self.siguiente.obtener(indice-1)

		else:
			return None

	def desempilar(self):
		if self.siguiente == None:
			self.valor = None
			print('La pila ha quedado vacia')

		else:

			if self.siguiente.siguiente:
				self.siguiente.desempilar()
			else:
				self.siguiente = None

a = Pila()
a.valor = "1"
a.siguiente = Pila()
a.siguiente.valor = "2"
a.siguiente.siguiente = None

resultado = a.imprimir()

print (resultado)