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

	def __init__(self,capacidadTotal : int,Cola=None,Cola2=None,tiempo=1):
		
		self.capacidadTotal = 0
		self.Cola = ColaP()
		self.Cola2 = ColaP()
		self.ListaMensajeros = [Mensajero(1),Mensajero(2),Mensajero(3),Mensajero(4)]
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
		
		vacia = self.Cola2.esVacia()

		for i in range(0,4):

			elemento = Paquete()

			elemento = self.Cola.desencolar()

			if (self.capacidadTotal + int(elemento.capacidad) <= 1024 and\
				self.ListaMensajeros[i].paquetesEmpilados.esVacia()):
			
				if (int(elemento.subpaquetes) > 0):

					with open(sys.argv[2], 'a') as salida:
						salida.write(self.tiempo + " Empilando " + str(N) + \
									" subpaquetes del paquete " + \
									str(elemento.destinatario) + \
									" en el mensajero " + str(i))
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

				else:
				
					self.ListaMensajeros[i].paquetesEmpilados.empilar(elemento)

					self.capacidadTotal = int(self.capacidadTotal) +\
											int(elemento.capacidad)

			
			elif (self.capacidadTotal + int(elemento.capacidad) <= 1024 and\
				not(self.ListaMensajeros[i].paquetesEmpilados.esVacia())):

				pass

			else:
					
				self.Cola2.encolar(self.Cola.desencolar())


		while (not vacia):
			
			self.Cola.encolar(self.Cola2.desencolar())
			
			vacia = self.Cola2.esVacia()


	def entregar(self):

		pass

	def listar (self):

		recorrido = True

		with open(sys.argv[2], 'a') as salida:

			salida.write(str(self.tiempo) + "Listado" + "\n")

			for i in range(0,4):
				
				if self.ListaMensajeros[i].paquetesEmpilados.valor:
					
					while recorrido:
						resultado = Pila()
						resultado.valor = self.ListaMensajeros[i].paquetesEmpilados.valor
						resultado.siguiente = self.ListaMensajeros[i].paquetesEmpilados.siguiente 
						salida.write (resultado.valor.destinatario + "mensajero" +\
									str(self.ListaMensajeros[i].identificador) + "\n")
				
				else:

					pass

			while :
				pass

				if self.Cola:
				
				resultado2 = ColaP()
				resultado2.valor = self.Cola
				salida.write (resultado2 + "Cola de prioridades")

			salida.write("Fin listado")
			
		salida.closed



#tiempo = 1

"""while seguirtiempo:
	pass
"""

ejemplo = Simulador(1024)

ejemplo.leer()

ejemplo.asignar()

ejemplo.listar()


"""with open(sys.argv[2], 'a') as salida:

	salida.write(self.tiempo,"Fin")

salida.closed"""


"""seguir =
	mensjareo2.empilar(Cola.desencolar())
	mensjareo3.empilar(Cola.desencolar())
	mensjareo4.empilar(Cola.desencolar())
"""