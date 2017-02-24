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

	def __init__(self,capacidadTotal,Cola=None,Cola2=None,tiempo=1):
		
		self.capacidadTotal = 0
		self.Cola = ColaP()
		self.Cola2 = ColaP()
		self.ListaMensajeros = [Mensajero(1),Mensajero(2),Mensajero(3),\
								Mensajero(4)]
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

		return True

	def asignar(self):
		
		i = 0

		while ((i < 4) and not(self.Cola.esVacia())):

			elemento = Paquete()

			elemento = self.Cola.desencolar()

			if (self.capacidadTotal + int(elemento.capacidad) <= 1024 and\
				self.ListaMensajeros[i].paquetesEmpilados.esVacia()):
				
				self.ListaMensajeros[i].tiempoEmpilado = self.tiempo

				if (int(elemento.subpaquetes) > 0):

					N = int(elemento.subpaquetes)

					with open(sys.argv[2], 'a') as salida:
						salida.write(str(self.ListaMensajeros[i].tiempoEmpilado) + " Empilando " +\
									 str(N) + " subpaquetes del paquete " +\
									 str(elemento.destinatario) +\
									 " en el mensajero " + str(i+1) + "\n")
					salida.closed

					for j in range (0,N):

						hijo = Paquete()

						hijo.prioridad = elemento.prioridad

						hijo.capacidad = elemento.capacidad

						hijo.duracion = elemento.duracion

						hijo.destinatario = (elemento.destinatario + \
											"-" + str(int(N)-j-1)) 

						self.ListaMensajeros[i].paquetesEmpilados.empilar(hijo)

					self.ListaMensajeros[i].paquetesEmpilados.empilar(elemento)

					self.capacidadTotal = self.capacidadTotal +\
											int(elemento.capacidad)

					i = i + 1

				else:
					
					self.ListaMensajeros[i].paquetesEmpilados.empilar(elemento)

					self.capacidadTotal = int(self.capacidadTotal) +\
												int(elemento.capacidad)
					seguir = False

					i = i + 1

			elif (self.capacidadTotal + int(elemento.capacidad) <= 1024 and\
				not(self.ListaMensajeros[i].paquetesEmpilados.esVacia())):

				i = i + 1

			else:

				self.Cola2.encolar(elemento)
		
		vacia = self.Cola2.esVacia()


		while (not vacia):

			pivote = Paquete()

			pivote = self.Cola2.desencolar()
			
			self.Cola.encolar(pivote)
			
			vacia = self.Cola2.esVacia()

		return True


	def entregar(self):

		tiempo1 = 0
		tiempo2 = 0
		tiempo3 = 0
		tiempo4 = 0

		for i in range (0,4):

			if (not(self.ListaMensajeros[i].ini) and\
					not(self.ListaMensajeros[i].paquetesEmpilados.esVacia())):
				
				ultimo = Paquete()
				ultimo = self.ListaMensajeros[i].paquetesEmpilados.mostrarUlt()

				with open(sys.argv[2], 'a') as salida:
					salida.write(str(self.tiempo) + " Iniciando " +\
								" paquete " + str(ultimo.destinatario) +\
								" por el mensajero " +	str(i+1) + "." + "\n")
				salida.closed

				self.ListaMensajeros[i].ini = True


			else:
				pass

		# Ciclo donde se lleva el control del tiempo

		if not (self.ListaMensajeros[0].paquetesEmpilados.esVacia()):

			tiempo1 = int((self.ListaMensajeros[0].tiempoEmpilado +\
						int(self.ListaMensajeros[0].paquetesEmpilados.valor.duracion))-1)
		
		if not (self.ListaMensajeros[1].paquetesEmpilados.esVacia()):		
		
			tiempo2 = int((self.ListaMensajeros[1].tiempoEmpilado +\
						int(self.ListaMensajeros[1].paquetesEmpilados.valor.duracion))-1)
		
		if not (self.ListaMensajeros[2].paquetesEmpilados.esVacia()):

			tiempo3 = int((self.ListaMensajeros[2].tiempoEmpilado +\
						int(self.ListaMensajeros[2].paquetesEmpilados.valor.duracion))-1)
		
		if not (self.ListaMensajeros[3].paquetesEmpilados.esVacia()):

			tiempo4 = int((self.ListaMensajeros[3].tiempoEmpilado +\
						int(self.ListaMensajeros[3].paquetesEmpilados.valor.duracion))-1)


		while (not((self.tiempo == tiempo1) or (self.tiempo == tiempo2) or\
				(self.tiempo == tiempo3) or (self.tiempo ==tiempo4))):

			self.tiempo = self.tiempo + 1

			if ((repartidor.tiempo % 100) == 0):
				repartidor.listar()

		with open(sys.argv[2], 'a') as salida:

			if self.tiempo == tiempo1:
			
				paquete1 = Paquete()
				paquete1 = self.ListaMensajeros[0].paquetesEmpilados.desempilar()

				if (self.ListaMensajeros[0].paquetesEmpilados.esVacia()):

					self.capacidadTotal = self.capacidadTotal - int(paquete1.capacidad)
			
				salida.write(str(self.tiempo) + " Finalizando " + " paquete " +\
							str(paquete1.destinatario) +\
							" por el mensajero " + str(1) + "." + "\n")
			
			elif self.tiempo == tiempo2:

				paquete2 = Paquete()
				paquete2 = self.ListaMensajeros[1].paquetesEmpilados.desempilar()

				if (self.ListaMensajeros[1].paquetesEmpilados.esVacia()):

					self.capacidadTotal = self.capacidadTotal - int(paquete2.capacidad)

				salida.write(str(self.tiempo) + " Finalizando " + " paquete " +\
								str(paquete2.destinatario) +\
								" por el mensajero " + str(2) + "." + "\n")
			
			elif self.tiempo == tiempo3:
			
				paquete3 = Paquete()
				paquete3 = self.ListaMensajeros[2].paquetesEmpilados.desempilar()

				if (self.ListaMensajeros[2].paquetesEmpilados.esVacia()):

					self.capacidadTotal = self.capacidadTotal - int(paquete3.capacidad)

				salida.write(str(self.tiempo) + " Finalizando " + " paquete " +\
							str(paquete3.destinatario) +\
							" por el mensajero " + str(3) + "." + "\n")
			
			elif self.tiempo == tiempo4:
			
				paquete4 = Paquete()
				paquete4 = self.ListaMensajeros[3].paquetesEmpilados.desempilar()

				if (self.ListaMensajeros[3].paquetesEmpilados.esVacia()):

					self.capacidadTotal = self.capacidadTotal - int(paquete4.capacidad)

				salida.write(str(self.tiempo) + " Finalizando " + " paquete " +\
							str(paquete4.destinatario) +\
							" por el mensajero " + str(4) + "." + "\n")
		salida.closed

		self.tiempo = self.tiempo + 1

		return True

	def listar (self):

		with open(sys.argv[2], 'a') as salida:

			salida.write (str(self.tiempo) + " Listado" + "\n")

			for i in range(0,4):
				
				if (self.ListaMensajeros[i].paquetesEmpilados.valor):
					
					resultado = Pila()
					
					resultado.valor = self.ListaMensajeros[i].paquetesEmpilados.valor
					
					resultado.siguiente = self.ListaMensajeros[i].paquetesEmpilados.siguiente
					
					vacia = resultado.esVacia()

					while not(vacia):

						a = Paquete()

						a = resultado.desempilar()

						print (a.destinatario)

						salida.write(a.destinatario +" " + a.prioridad +\
									" "+ a.capacidad + " " + a.duracion + \
									" mensajero" + " " +\
									str(self.ListaMensajeros[i].identificador) +"\n")
						vacia = resultado.esVacia()
				
				else:

					pass
			
			if self.Cola.valor:
				
				self.Cola2.valor = self.Cola.valor
				
				self.Cola2.siguiente = self.Cola.siguiente
				
				vacia2 = self.Cola2.esVacia()

				while not(vacia2):
				
					b = Paquete()
				
					b = self.Cola2.desencolar()
				
					salida.write(b.destinatario + " " + b.prioridad + " " +\
							b.capacidad +" " + b.duracion +\
							" Cola de prioridades" + "\n")
				
					vacia2 = self.Cola2.esVacia()

			salida.write("Fin listado." + "\n")
			
		salida.closed

		return True

repartidor = Simulador(1024)

repartidor.leer()

while not (repartidor.Cola.esVacia() and\
			repartidor.ListaMensajeros[0].paquetesEmpilados.esVacia() and\
			repartidor.ListaMensajeros[1].paquetesEmpilados.esVacia() and\
			repartidor.ListaMensajeros[2].paquetesEmpilados.esVacia() and\
			repartidor.ListaMensajeros[3].paquetesEmpilados.esVacia()):
	
	repartidor.asignar()

	repartidor.entregar()

with open(sys.argv[2], 'a') as salida:

	salida.write(str(repartidor.tiempo) + " Fin.")

salida.closed