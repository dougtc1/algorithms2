# Universidad Simon Bolívar.
#
# Laboratorio de Algoritmos y Estructuras II
# Ricardo Churion Carné: 11-10200.
# Douglas Torres Carné: 11-11027.
# Grupo 06.
# Archivo que contiene el TAD Matriz

class Matriz:
	nombre = ""
	juego = [ [ "#" for i in range (8)] for j in range (8)]

tablero = Matriz()

for i in range (tablero.juego):
	print (" ".join(i))