#
#
#
#
#
#
#

import sys

from cola import ColaP

from pila import Pila

class Mensajero:
	
	def __init__(self,identificador : int,paquetesEmpilados=None,capacidadTotal=0):
	
		self.identificador = identificador
		self.paquetesEmpilados = Pila()

class Paquete:
	
	def __init__(self,destinatario=None,prioridad=None,capacidad=None,duracion=None,subpaquetes=None):
	
		self.destinatario = destinatario
		self.prioridad = prioridad
		self.capacidad = capacidad
		self.duracion = duracion
		self.subpaquetes = subpaquetes

def ControlTiempo (tiempo:int):
	
	if ((tiempo % 100) == 0):

		print("imprimo en archivo")

	else:
		pass

	return True

Lista = []

Cola = ColaP()

Cola2 = ColaP()

ListaMensajeros = []

ListaMensajeros.append(Mensajero(1))
ListaMensajeros.append(Mensajero(2))
ListaMensajeros.append(Mensajero(3))
ListaMensajeros.append(Mensajero(4))

vacia = True

vuelta = True

capacidadTotal = 0

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
	
		Cola.encolar(P)

while vuelta and :
	
	for i in range(0,4):
		
		while (not vacia) and (capacidadTotal < 1024):

			elemento = Paquete()

			elemento = Cola.desencolar()

			if (capacidadTotal+elemento.capacidad <= 1024):
	
				if (int(elemento.subpaquetes) > 0):

					N = int(elemento.subpaquetes)
				
					for j in range (N):

						hijo = Paquete()

						hijo.prioridad = elemento.prioridad

						hijo.capacidad = elemento.capacidad

						hijo.duracion = elemento.duracion

						hijo.destinatario = (elemento.destinatario + "-" + str(int(N)-j-1)) 

						ListaMensajeros[i].paquetesEmpilados.empilar(hijo)
				
					ListaMensajeros[i].paquetesEmpilados.empilar(elemento)

					capacidadTotal = capacidadTotal + elemento.capacidad

					break

				else:
			
					ListaMensajeros[i].paquetesEmpilados.empilar(elemento)

					capacidadTotal = capacidadTotal + elemento.capacidad

					break

			else:
			
				Cola2.encolar(Cola.desencolar())


			vacia = Cola.esVacia()

	
	vuelta = vacia

	if vacia and Cola2.valor != None:
		
		Cola.valor = Cola2.valor
		Cola.siguiente = Cola2.siguiente

	elif (not vacia) and Cola2.valor != None:
		pass

	elif (not vacia) and Cola2.valor == None:
		pass

	else:
		while :
			pass

tiempo = 1

while seguirtiempo:

	

"""seguir =
	mensjareo2.empilar(Cola.desencolar())
	mensjareo3.empilar(Cola.desencolar())
	mensjareo4.empilar(Cola.desencolar())
"""