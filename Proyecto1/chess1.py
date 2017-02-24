# Universidad Simon Bolivar 
#
# Laboratorio de Algoritmos y Estructuras II
#
# Ricardo Churion. Carnet: 11-10200
# Douglas Torres. Carnet: 11-11027
# Grupo: 06
#
#
# Archivo que contiene el llamado de las funciones

import sys
from matriz import Matriz

Lista = []

juego = Chess()

with open(sys.argv[1]) as Instrucciones:
	for line in Instrucciones.readlines():
		unalinea = line.split()
		Lista.append(unalinea)
Instrucciones.closed

for i in Lista:

	if i[0] == "LOAD":

		juego.LOAD(i[1],i[2])

	elif i[0] == "PRINT":

		juego.PRINT(i[1])

	elif (i[0]+i[1]) == "CHECKTHREAT":

		juego.CHECKTHREAT(i[2],i[3])

	elif i[0] == "CHECK":

		juego.CHECK(i[1],i[2],i[3])

	elif i[0] == "MOVE":

		juego.MOVE(i[1],i[2],i[3])