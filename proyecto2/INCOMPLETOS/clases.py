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
	
	def empilar (self,valor):
		if self.valor == None:
			self.valor = valor
         
		elif self.siguiente:
			self.siguiente.empilar(valor)

		else:
			self.siguiente = Pila(valor)

	def desempilar(self):

		if self.siguiente == None:
			salida = self.valor
			self.valor = None

		else:

			salida = self.siguiente.desempilar()

		return (salida)

	def mostrarUlt(self):
		
		elemento = self.desempilar()
		self.empilar(elemento)
		return (elemento)

	def esVacia(self):
		
		if self.valor:
			return False
		else:
			return True

class Mensajero:
	def __init__(self,identificador=None,paquetesEmpilados=None,\
				tiempoEmpilado=None,ini=False):
	
		self.identificador = identificador
		self.paquetesEmpilados = Pila()
		
		# Momento en el que inicia 
		self.tiempoEmpilado = tiempoEmpilado
		
		# inicializacion, dice si el mensajero ya inicio la entrega del paquete
		
		self.ini = ini

c = Paquete()
c.destinatario = "Nombre"
d = Paquete()
d.destinatario = "Nombre2"

a = Pila()

a.empilar(1)
a.empilar(2)
a.empilar(d)
a.empilar(c)
b = a.desempilar()

print(b.destinatario)

d = a.desempilar()

print(d.destinatario)
