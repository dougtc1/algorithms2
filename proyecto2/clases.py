# Universidad Simon Bolivar 
#
# Laboratorio de Algoritmos y Estructuras II
#
# Ricardo Churion. Carnet: 11-10200
# Douglas Torres. Carnet: 11-11027
# Grupo: 06
#
# * VA SIN ACENTOS *
#
# Archivo que contiene las clases usadas en el archivo simulador.py

# Definicion de la clase paquete

class Paquete:
	
	def __init__(self,destinatario=None,prioridad=None,capacidad=None,\
				duracion=None,subpaquetes=None):
	
		self.destinatario = destinatario
		self.prioridad = prioridad
		self.capacidad = capacidad
		self.duracion = duracion
		self.subpaquetes = subpaquetes


# Definicion de la clase Cola de Prioridades

class ColaP:
	
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

	def obtener(self,indice):
		if indice == 0:
			return self.valor
		elif self.siguiente:
			return self.siguiente.obtener(indice-1)
		else:
			return None


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

# Definicion de la clase Pila que sera usada en cada mensajero

class Pila:
	def __init__(self,valor=None,siguiente=None):
		self.valor = valor
		self.siguiente = siguiente

	def remover(self,indice):
		if indice == 0:
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
	
	def longitud(self):
		if self.siguiente:
			return self.siguiente.longitud() + 1

		elif self.valor:
			return 1
		else:
			return 0

	def obtener(self,indice):
		if indice == 0:
			return self.valor
		elif self.siguiente:
			return self.siguiente.obtener(indice-1)
		else:
			return None

	def empilar (self,valor):
		
		if self.valor == None:
			self.valor = valor
         
		elif self.siguiente:
			self.siguiente.empilar(valor)

		else:
			self.siguiente = Pila(valor)

	def desempilar(self):

		salida = self.obtener(self.longitud() - 1)
		
		self.remover(self.longitud() - 1)
		
		return(salida)

	def mostrarUlt(self):
		
		elemento = self.desempilar()
		self.empilar(elemento)
		return (elemento)

	def esVacia(self):
		
		if self.valor:
			return False
		else:
			return True

# Definicion de la clase Mensajero

class Mensajero:
	def __init__(self,identificador=None,paquetesEmpilados=None,\
				tiempoEmpilado=None,ini=False):
	
		self.identificador = identificador
		self.paquetesEmpilados = Pila()
		
		# Momento en el que inicia 
		self.tiempoEmpilado = tiempoEmpilado
		
		# Inicializacion, dice si el mensajero ya inicio la entrega del paquete
		
		self.ini = ini