# Universidad Simon Bolivar 
#
# Laboratorio de Algoritmos y Estructuras II
#
# Ricardo Churion. Carnet: 11-10200
# Douglas Torres. Carnet: 11-11027
# Grupo: 06
#
# Archivo donde se encuentran las operaciones del TAD Matriz

import sys


# Clase del ajedrez

class Matriz:

# Aqui se inicializan las instancias a usar

	def __init__(self):
		self.tablero = [ [ "#" for i in range (9) ] for j in range (8) ]
		self.columnas = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
		self.diccionario = {}

# Aqui se declara la funcion que permite cargar cada tablero

	def LOAD (self,tablero,nombre):

		self.tablero= [ [ "#" for i in range (9) ] for j in range (8) ]

		with open(tablero) as Archivo:
		
			for i in range(8):
	
				for j in range(9):

					self.tablero[i][j] = Archivo.read(1).rstrip()
		
		self.diccionario[str(nombre)] = self.tablero

		Archivo.closed

# Aqui se declara la funcion que imprime en el archivo especificado cada
# tablero con su formato.

	def PRINT (self,nombre):
		with open(sys.argv[2], 'a') as salida:
			if nombre in self.diccionario:
				salida.write ("Tablero: " + nombre + "\n")
				for i in self.diccionario[nombre]:
					salida.write ("".join(i) + "\n")
				salida.write("--------" + "\n")
			else:
				salida.write("No esta en el diccionario" + "\n")
		salida.closed

# Aqui se declara la funcion que verifica la validez de los movimientos 
# a realizar, se verifican todas las posibilidades pedidas en el enunciado.

	def CHECK(self,origen,destino,nombre):
		with open(sys.argv[2], 'a') as salida:
		
			filorigen = 7 - int(origen[1]) + 1
			colorigen = self.columnas[origen[0]]
			fildestino = 7 - int(destino[1]) + 1
			coldestino = self.columnas[destino[0]]
			cuadricula = self.diccionario[nombre]

			if (cuadricula[filorigen][colorigen] == "#"):
				
				salida.write("INVALID" + "\n")

				resultado = False
			
			elif (cuadricula[filorigen][colorigen] == "P"):
			
				if (fildestino > filorigen):
				
					salida.write("INVALID" + "\n")

					resultado = False					

				elif (filorigen == 6):
			
					if (fildestino < 4):
			
						salida.write("INVALID" + "\n")
						
						resultado = False

					elif (fildestino == 4 and colorigen == coldestino and\
						cuadricula[fildestino][coldestino] == "#"):
						
						if (cuadricula[3][colorigen] == "#"):

							salida.write("VALID"+ "\n")

							resultado = True

						else:

							salida.write("INVALID" + "\n")

							resultado = False
			
					elif (fildestino == 5 and colorigen == coldestino and\
						cuadricula[fildestino][coldestino] == "#"):
			
						salida.write("VALID"+ "\n")

						resultado = True
			
					elif (colorigen == 0):
					
						if (cuadricula[5][1] == "p" and fildestino == 5 and\
							(coldestino == 1)):
					
							salida.write("VALID" + "\n")

							resultado = True							
					
						else:
					
							salida.write("INVALID" + "\n")
							
							resultado = False

					elif (colorigen == 7):

						if (cuadricula[5][6] == "p" and fildestino ==5 and\
							(coldestino == 6)):
													
							salida.write("VALID" + "\n")

							resultado = True
						
						else:

							salida.write("INVALID" + "\n")

							resultado = False

					elif (colorigen != 0 and colorigen != 7):

						if (cuadricula[fildestino][coldestino] == "p" and\
							fildestino == filorigen - 1 and\
							(colorigen == coldestino +1 or\
							colorigen == coldestino - 1)):
							
							salida.write("VALID" + "\n")

							resultado = True

						else:
							salida.write("INVALID" + "\n")

							resultado = False

					elif (colorigen == coldestino and\
						(fildestino == filorigen - 1 or\
						fildestino == filorigen - 2) and\
						cuadricula[fildestino][coldestino] != "#"):
						
						salida.write("INVALID" + "\n")

						resultado = False

				elif (filorigen < 6):

					if (fildestino == filorigen - 1 and\
						cuadricula[fildestino][coldestino] == "#" and\
						colorigen == coldestino):

						salida.write("VALID" + "\n")

						resultado = True

					elif (colorigen == 0):
					
						if (cuadricula[fildestino][coldestino] == "p" and\
							fildestino == filorigen - 1 and\
							(coldestino == 1 or colorigen == coldestino)):
					
							salida.write("VALID" + "\n")
					
							resultado = True

						else:

							salida.write("INVALID" + "\n")

							resultado = False

					elif (colorigen == 7):

						if (cuadricula[fildestino][coldestino] == "p" and\
							fildestino == filorigen - 1 and\
							(coldestino == 6 or colorigen == coldestino)):
						
							salida.write("VALID" + "\n")

							resultado = True
				
						else:

							salida.write("INVALID" + "\n")

							resultado = False

					elif (colorigen != 0 and colorigen != 7):
		
						if (cuadricula[fildestino][coldestino] == "p" and\
							fildestino == filorigen - 1 and\
							(colorigen == coldestino + 1 or\
							colorigen == coldestino - 1)):
							
							salida.write("VALID" + "\n")

							resultado = True

						else:
				
							salida.write("INVALID" + "\n")

							resultado = False

				else:
		
					salida.write("INVALID" + "\n")

					resultado = False

			elif(cuadricula[filorigen][colorigen] == "p"):

				if (fildestino < filorigen):
				
					salida.write("INVALID" + "\n")

					resultado = False
		
				elif (filorigen == 1):
			
					if (fildestino > 3):
			
						salida.write("INVALID" + "\n")
						
						resultado = False

					elif (fildestino == 3 and colorigen == coldestino and\
						cuadricula[fildestino][coldestino] == "#"):

						if (cuadricula[2][colorigen] == "#"):

							salida.write("VALID" + "\n")

							resultado = True

						else:

							salida.write("INVALID" + "\n")

							resultado = False
			
					elif (fildestino == 2 and colorigen == coldestino and\
						cuadricula[fildestino][coldestino] == "#"):
			
						salida.write("VALID" + "\n")

						resultado = True

					elif (colorigen == 0):
					
						if (cuadricula[2][1] == "P" and fildestino == 2 and\
							(coldestino == 1)):
					
							salida.write("VALID" + "\n")

							resultado = True
	
						else:
					
							salida.write("INVALID" + "\n")

							resultado = False

					elif (colorigen == 7):

						if (cuadricula[2][6] == "P" and fildestino == 2 and\
							(coldestino == 6)):
													
							salida.write("VALID" + "\n")

							resultado = True
						
						else:

							salida.write("INVALID" + "\n")

							resultado = False

					elif (colorigen != 0 and colorigen != 7):

						if (cuadricula[fildestino][coldestino] == "P" and\
							fildestino == filorigen + 1 and\
							(colorigen == coldestino + 1 or\
							colorigen == coldestino - 1)):
							
							salida.write("VALID" + "\n")

							resultado = True
						
						else:
							salida.write("INVALID" + "\n")

							resultado = False

					elif (colorigen == coldestino and\
						(fildestino == filorigen + 1 or\
						fildestino == filorigen + 2) and\
						cuadricula[fildestino][coldestino] != "#"):
						
						salida.write("INVALID" + "\n")

						resultado = False

				elif (filorigen > 1):

					if (fildestino == filorigen + 1 and\
						cuadricula[fildestino][coldestino] == "#" and\
						colorigen == coldestino):

						salida.write("VALID" + "\n")

						resultado = True

					elif (colorigen == 0):
					
						if (cuadricula[fildestino][coldestino] == "P" and\
							fildestino == filorigen + 1 and (coldestino == 1)):
					
							salida.write("VALID" + "\n")
					
							resultado = True

						else:

							salida.write("INVALID" + "\n")

							resultado = False

					elif (colorigen == 7):

						if (cuadricula[fildestino][coldestino] == "P" and\
							fildestino == filorigen + 1 and\
							(coldestino == 6)):
						
							salida.write("VALID" + "\n")

							resultado = True														
						
						else:

							salida.write("INVALID" + "\n")

							resultado = False

					elif (colorigen != 0 and colorigen != 7):
		
						if (cuadricula[fildestino][coldestino] == "P" and\
							fildestino == filorigen + 1 and\
							(colorigen == coldestino + 1 or\
							colorigen == coldestino - 1)):
							
							salida.write("VALID" + "\n")

							resultado = True
						
						else:
							salida.write("INVALID" + "\n")

							resultado = False
	
				else:
		
					salida.write("INVALID" + "\n")

					resultado = False

			else:
				salida.write("INVALID" + "\n")

				resultado = False

		salida.closed

		return resultado

# Se define la funcion move que mueve a una pieza en el tablero siempre y
# cuando cumpla con la validez del movimiento de la funcion check


	def MOVE(self,origen,destino,nombre):

		with open(sys.argv[2], 'a') as salida:
			
			filorigen = 8 - int(origen[1])
			colorigen = self.columnas[origen[0]]
			fildestino = 8 - int(destino[1])
			coldestino = self.columnas[destino[0]]
			cuadricula = self.diccionario[str(nombre)]
			validez = self.CHECK(origen,destino,str(nombre))

		salida.closed

		salida = open(sys.argv[2]).readlines()
		open(sys.argv[2], 'w').writelines(salida[:-1])


		with open(sys.argv[2], 'a') as salida:

			if (validez):

				cuadricula[fildestino][coldestino] =\
				cuadricula[filorigen][colorigen]

				cuadricula[filorigen][colorigen] = "#"

			else:

				salida.write("INVALID" + '\n')

		salida.closed

# Aqui se define la funcion check threat que dado un jugador verifica a todas
# las piezas de dicho jugador y dice si esta en riesgo de ser comida alguna


	def CHECKTHREAT(self,jugador,nombre):
		cuadricula = self.diccionario[nombre]

		with open(sys.argv[2], 'a') as salida:
			
			if (jugador != "P" and jugador != "p"):
			
				print("El jugador introducido no es valido")
			
			elif (jugador == "P" and any(cuadricula[i][j] == "P"\
				for i in range (8) for j in range (8)\
				if (cuadricula[i-1][j-1] == "p" or\
				cuadricula[i-1][j+1] == "p"))):
				
					salida.write('YES' + '\n')

			elif (jugador == "p" and any(cuadricula[i][j] == "p"\
				for i in range (8) for j in range (8)\
				if (cuadricula[i+1][j-1] == "P" or\
				cuadricula[i+1][j+1] == "P"))):
				
					salida.write('YES' + '\n')
			
			else:
			
				salida.write('NO' + '\n')

		salida.closed