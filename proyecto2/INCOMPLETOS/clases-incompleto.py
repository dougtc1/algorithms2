class Paquete:
	
	def __init__(self,destinatario=None,prioridad=None,capacidad=None,\
				duracion=None,subpaquetes=None):
	
		self.destinatario = destinatario
		self.prioridad = prioridad
		self.capacidad = capacidad
		self.duracion = duracion
		self.subpaquetes = subpaquetes

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
		if self.valor:
			return(self.valor)
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
			self.siguiente = Pila()
			self.siguiente.valor = valor
		
	def imprimir(self):	
		
		if self.valor:
			temporal = self.valor
			if self.siguiente:
				self.siguiente.imprimir()
				return temporal
		
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

	def esVacia(self):
		
		if self.valor:
			return False
		else:
			return True

class Mensajero:
	
	def __init__(self,identificador : int,paquetesEmpilados=None):
	
		self.identificador = identificador
		self.paquetesEmpilados = Pila()


a = Pila()
a.empilar(1)
a.empilar(2)
a.empilar(3)

respuesta = a.imprimir()

print(respuesta)