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
# Archivo que contiene la clase simulador y codigo principal del programa.

# Se importa sys para poder obtener los argumentos pasados al ejecutar el
# programa como se especifica en el enunciado

import sys

# Aqui se importan todas las clases a usar en el simulador

from clases import Paquete

from clases import ColaP

from clases import Pila

from clases import Mensajero

# Definicion de la clase Simulador

class Simulador:

	def __init__(self,capacidadTotal,Cola=None,Cola2=None,tiempo=1):
		
		# Capacidad del simulador
		self.capacidadTotal = 0
		self.Cola = ColaP()
		self.Cola2 = ColaP()
		self.ListaMensajeros = [Mensajero(1),Mensajero(2),Mensajero(3),\
								Mensajero(4)]
		self.tiempo = tiempo

	def leer(self):

	# Se crea una funcion que lee el archivo de entrada y guarda en una matriz
	# los paquetes validos leidos de dicho archivo
		
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

	# Se declara una funcion que, dependiendo de la cantidad disponible en el
	# simulador y disponibilidad de cada mensajero, le asigna a cada uno
	# un paquete distinto.
		
		i = 0

		while ((i < 4) and not(self.Cola.esVacia())):

			elemento = Paquete()

			elemento = self.Cola.desencolar()

			if (self.capacidadTotal + int(elemento.capacidad) <= 1024 and\
				self.ListaMensajeros[i].paquetesEmpilados.esVacia()):
				
				self.ListaMensajeros[i].tiempoEmpilado = self.tiempo

				# Aqui se verifica si se le entrega al mensajero un paquete que
				# tenga subpaquetes

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
							
					self.capacidadTotal = self.capacidadTotal +\
											int(elemento.capacidad)

					self.ListaMensajeros[i].paquetesEmpilados.empilar(elemento)
					
					i = i + 1

				else:
					
					self.capacidadTotal = int(self.capacidadTotal) +\
											int(elemento.capacidad)

					self.ListaMensajeros[i].paquetesEmpilados.empilar(elemento)

					seguir = False

					i = i + 1

			elif (self.capacidadTotal + int(elemento.capacidad) <= 1024 and\
				not(self.ListaMensajeros[i].paquetesEmpilados.esVacia())):

				i = i + 1

			# Para el caso en que un paquete no pueda entrar a un mensajero
			# debido a que su capacidad haria sobrepasar la capacidad del 
			# simulador, este se pasa a una cola auxiliar, Cola2, donde se van
			# a guardar mientras se le entregan a los mensajeros los paquetes
			# que pueden salir a entregar. Cabe destacar que al encolarse en
			# Cola2, automaticamente se ordenan los paquetes por prioridad.

			else:

				self.Cola2.encolar(elemento)
		
		vacia = self.Cola2.esVacia()

		# Cuando todos los mensajeros esten ocupados y la cola de prioridades
		# original, Cola, se encuentre vacia, se pasan todos los paquetes de
		# Cola2 a Cola. Como esto se hace desencolando de Cola2 y encolando en
		# Cola, se vuelven a ordenar por prioridad, quedando la Cola ordenada 
		# como le corresponde

		while (not vacia):

			pivote = Paquete()

			pivote = self.Cola2.desencolar()
			
			self.Cola.encolar(pivote)
			
			vacia = self.Cola2.esVacia()

		return True


	def entregar(self):

	# Se inicializan los tiempos de cada mensajero

		tiempo1 = 0
		tiempo2 = 0
		tiempo3 = 0
		tiempo4 = 0

		# Se verifica si hay paquetes en cada mensajero y se imprime en el
		# archivo de salida.

		for i in range (0,4):

			if (not(self.ListaMensajeros[i].ini) and\
					not(self.ListaMensajeros[i].paquetesEmpilados.esVacia())):
				
				ultimo = Paquete()
				ultimo = self.ListaMensajeros[i].paquetesEmpilados.mostrarUlt()

				with open(sys.argv[2], 'a') as salida:
					salida.write(str(self.tiempo) + " Iniciando" +\
								" paquete " + str(ultimo.destinatario) +\
								" por el mensajero " +	str(i+1) + "." + "\n")
				salida.closed

				self.ListaMensajeros[i].ini = True

			else:
				pass

		# Se calculan los tiempos que deberian tomar en entregarse cada paquete,
		# usando tomando el tiempo en el que se empilo cada paquete en dicho 
		# mensajero mas el tiempo que  deberia durar el tiempo de entrega
		# de tal paquete. Se le resta el 1 que es el tiempo de origen del tiempo

		if not (self.ListaMensajeros[0].paquetesEmpilados.esVacia()):

			tiempo1 = (int(self.ListaMensajeros[0].tiempoEmpilado) +\
						int(self.ListaMensajeros[0].paquetesEmpilados.valor.duracion))-1
		
		if not (self.ListaMensajeros[1].paquetesEmpilados.esVacia()):		
		
			tiempo2 = (int(self.ListaMensajeros[1].tiempoEmpilado) +\
						int(self.ListaMensajeros[1].paquetesEmpilados.valor.duracion))-1
		
		if not (self.ListaMensajeros[2].paquetesEmpilados.esVacia()):

			tiempo3 = (int(self.ListaMensajeros[2].tiempoEmpilado) +\
						int(self.ListaMensajeros[2].paquetesEmpilados.valor.duracion))-1
		
		if not (self.ListaMensajeros[3].paquetesEmpilados.esVacia()):

			tiempo4 = (int(self.ListaMensajeros[3].tiempoEmpilado) +\
						int(self.ListaMensajeros[3].paquetesEmpilados.valor.duracion))-1

		# Ciclo donde se lleva el control del tiempo del simulador.
		# Cuando haya un tiempo de entrega de un paquete, en un mensajero, 
		# igual al tiempo del simulador, se deja de aumentar el tiempo y se 
		# pasa al desempilado de dicho paquete del mensajero.
		# Mientras el tiempo aumenta, si el tiempo llega a ser multiplo de 100
		# se llama a la funcion Listar.

		while (not((self.tiempo == tiempo1) or (self.tiempo == tiempo2) or\
				(self.tiempo == tiempo3) or (self.tiempo == tiempo4))):

			self.tiempo = self.tiempo + 1

			if ((self.tiempo % 100) == 0):
				self.listar()

		with open(sys.argv[2], 'a') as salida:

			if self.tiempo == tiempo1:

				self.ListaMensajeros[0].ini = False
				paquete1 = Paquete()
				paquete1 = self.ListaMensajeros[0].paquetesEmpilados.desempilar()

				if (self.ListaMensajeros[0].paquetesEmpilados.esVacia()):

					self.capacidadTotal = self.capacidadTotal - int(paquete1.capacidad)

					self.ListaMensajeros[0].ini = False

				else :
					self.ListaMensajeros[0].tiempoEmpilado = self.tiempo + 1

					self.ListaMensajeros[0].ini = False

				salida.write(str(self.tiempo) + " Finalizando" + " paquete " +\
							str(paquete1.destinatario) +\
							" por el mensajero " + str(1) + "." + "\n")
			
			if self.tiempo == tiempo2:

				self.ListaMensajeros[1].ini = False
				paquete2 = Paquete()
				paquete2 = self.ListaMensajeros[1].paquetesEmpilados.desempilar()

				if (self.ListaMensajeros[1].paquetesEmpilados.esVacia()):

					self.capacidadTotal = self.capacidadTotal - int(paquete2.capacidad)

					self.ListaMensajeros[1].ini = False


				else :
					self.ListaMensajeros[1].tiempoEmpilado = self.tiempo +1

					self.ListaMensajeros[1].ini = False

				salida.write(str(self.tiempo) + " Finalizando " + " paquete " +\
								str(paquete2.destinatario) +\
								" por el mensajero " + str(2) + "." + "\n")
			
			if self.tiempo == tiempo3:
				
				self.ListaMensajeros[2].ini = False
				paquete3 = Paquete()
				paquete3 = self.ListaMensajeros[2].paquetesEmpilados.desempilar()

				if (self.ListaMensajeros[2].paquetesEmpilados.esVacia()):

					self.capacidadTotal = self.capacidadTotal - int(paquete3.capacidad)

					self.ListaMensajeros[2].ini = False


				else :
					self.ListaMensajeros[2].tiempoEmpilado = self.tiempo +1

					self.ListaMensajeros[2].ini = False

				salida.write(str(self.tiempo) + " Finalizando " + " paquete " +\
							str(paquete3.destinatario) +\
							" por el mensajero " + str(3) + "." + "\n")
			
			if self.tiempo == tiempo4:
				
				self.ListaMensajeros[3].ini = False
				paquete4 = Paquete()
				paquete4 = self.ListaMensajeros[3].paquetesEmpilados.desempilar()

				if (self.ListaMensajeros[3].paquetesEmpilados.esVacia()):

					self.capacidadTotal = self.capacidadTotal - int(paquete4.capacidad)

					self.ListaMensajeros[3].ini = False

				else :
					self.ListaMensajeros[3].tiempoEmpilado = self.tiempo +1

					self.ListaMensajeros[3].ini = False


				salida.write(str(self.tiempo) + " Finalizando " + " paquete " +\
							str(paquete4.destinatario) +\
							" por el mensajero " + str(4) + "." + "\n")
		salida.closed

		# Se le aumenta una unidad al tiempo despues de que se desempilen todos
		# los paquetes que tocaban desempilar

		self.tiempo = self.tiempo + 1
		
		return True

	def listar (self):

		# Definicion de la funcion listar que imprime en el archivo el estado 
		# de los mensajeros, es decir, si se encuentran en un mensajero se 
		# especifica en cual y si se encuentran en la cola de prioridades.

		with open(sys.argv[2], 'a') as salida:

			salida.write (str(self.tiempo) + " Listado" + "\n")

			for i in range(0,4):
				
				if (self.ListaMensajeros[i].paquetesEmpilados.valor):
					
					longitud = int(self.ListaMensajeros[i].paquetesEmpilados.longitud()) 
					while longitud != 0 :
						longitud = longitud - 1
						a =self.ListaMensajeros[i].paquetesEmpilados.obtener(longitud)
						salida.write(a.destinatario +" " + a.prioridad +\
									" "+ a.capacidad + " " + a.duracion + \
									" mensajero" + " " +\
									str(self.ListaMensajeros[i].identificador) +"\n")
				
				else:

					pass
			
			if self.Cola.valor:
				 
				largo = int(self.Cola.longitud())

				while largo != 0:
					largo = largo -1
					b = self.Cola.obtener(largo)
					salida.write(b.destinatario + " " + b.prioridad + " " +\
							b.capacidad +" " + b.duracion +\
							" Cola de prioridades" + "\n")
					vacia2 = self.Cola2.esVacia()

			else:

				pass

			salida.write("Fin listado." + "\n")
			
		salida.closed

		return True

# Programa principal

# Se declara una variable de la clase Simulador

repartidor = Simulador(1024)

# Leo el archivo de entrada

repartidor.leer()

# Ciclo principal del programa.

# Aqui se realiza la verificacion del estado de todo el simulador, asi, si hay 
# un paquete en la cola de prioridades o en algun mensajero, se seguira 
# iterando hasta que todos sean enviados y los 4 mensajeros queden vacios, al
# igual que la cola de prioridades.  

while not (repartidor.Cola.esVacia() and\
			repartidor.ListaMensajeros[0].paquetesEmpilados.esVacia() and\
			repartidor.ListaMensajeros[1].paquetesEmpilados.esVacia() and\
			repartidor.ListaMensajeros[2].paquetesEmpilados.esVacia() and\
			repartidor.ListaMensajeros[3].paquetesEmpilados.esVacia()):
	
	repartidor.asignar()

	repartidor.entregar()

# Se escribe en el archivo lo que seria el final del programa.

with open(sys.argv[2], 'a') as salida:

	salida.write(str(repartidor.tiempo) + " Fin.")

salida.closed