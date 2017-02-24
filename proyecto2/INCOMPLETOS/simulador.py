#
#
#
#
#
#
#

import sys

from clases import Paquete

from clases import ColaP

from clases import Pila

from clases import Mensajero

class Simulador:

	def __init__(self,capacidadTotal : int,Cola=None,Cola2=None,\
				ListaMensajeros=[],tiempo=1):
		
		self.capacidadTotal = 0
		self.Cola = ColaP()
		self.Cola2 = ColaP()
		self.ListaMensajeros = []
		self.tiempo = tiempo

	def leer(self):
		
		Lista = []

		with open(sys.argv[1]) as Entrada:
			for line in Entrada.readlines():
				unalinea = line.split()
				Lista.append(unalinea)
		Entrada.closed

		for i in Lista:

			if (i[0] != "paquete"):
	
				pass
	
			else:

				P = Paquete(i[1],i[2],i[3],i[4],i[5])
			
				self.Cola.encolar(P)

	def asignar(self):
		
		vacia = self.Cola.esVacia()

		for i in range(0,4):
				
			while (not vacia):

				elemento = Paquete()

				elemento = self.Cola.desencolar()

				if (self.capacidadTotal + int(elemento.capacidad) <= 1024 and\
					self.ListaMensajeros[i].paquetesEmpilados.esVacia()):
			
					if (int(elemento.subpaquetes) > 0):

						with open(sys.argv[2], 'a') as salida:
							salida.write(self.tiempo,"Empilando",N,\
								"subpaquetes del paquete",\
								elemento.destinatario,"en el mensajero",i)
						salida.closed

						N = int(elemento.subpaquetes)
						
						for j in range (N):

							hijo = Paquete()

							hijo.prioridad = elemento.prioridad

							hijo.capacidad = elemento.capacidad

							hijo.duracion = elemento.duracion

							hijo.destinatario = (elemento.destinatario + \
												"-" + str(int(N)-j-1)) 

							self.ListaMensajeros[i].paquetesEmpilados.empilar(hijo)
						
						self.ListaMensajeros[i].paquetesEmpilados.empilar(elemento)

						self.capacidadTotal = self.capacidadTotal + elemento.capacidad

						break

					else:
					
						self.ListaMensajeros[i].paquetesEmpilados.empilar(elemento)

						self.capacidadTotal = self.capacidadTotal + elemento.capacidad

						break

				else:
					
					self.Cola2.encolar(Cola.desencolar())


				vacia = self.Cola.esVacia()

		if vacia and self.Cola2.valor != None:
				
			self.Cola.valor = self.Cola2.valor
				
			self.Cola.siguiente = self.Cola2.siguiente

		elif (not vacia) and self.Cola2.valor != None:
				
			pass

		elif (not vacia) and self.Cola2.valor == None:
				
			pass

		"""else:
			while :
				pass"""

def entregar(self):

	pass

def listar (self):

	recorrido = True

	with open(sys.argv[2], 'a') as salida:

		salida.write(self.tiempo,"Listado" + "\n")

		for i in range(0,4):
			
			if self.ListaMensajeros[i].paquetesEmpilados:
				
				resultado = self.ListaMensajeros[i].paquetesEmpilados.imprimir()
				salida.write (resultado,"mensajero",\
							self.ListaMensajeros[i].identificador,"\n")
			
			else:

				pass

		if self.Cola:
			resultado2 = self.Cola.imprimir()
			salida.write (resultado2,"Cola de prioridades")

		salida.write("Fin listado")
		
	salida.closed

"""ListaMensajeros.append(Mensajero(1))
ListaMensajeros.append(Mensajero(2))
ListaMensajeros.append(Mensajero(3))
ListaMensajeros.append(Mensajero(4))
"""

#tiempo = 1

"""while seguirtiempo:
	pass
"""

ejemplo = Simulador(1024)

ejemplo.leer()

ejemplo.asignar()

ejemplo.listar()



with open(sys.argv[2], 'a') as salida:

	salida.write(self.tiempo,"Fin")

salida.closed


"""seguir =
	mensjareo2.empilar(Cola.desencolar())
	mensjareo3.empilar(Cola.desencolar())
	mensjareo4.empilar(Cola.desencolar())
"""