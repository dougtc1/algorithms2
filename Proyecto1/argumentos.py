'''
Lectura de argumentos en Python.

Los argumentos del programa están almacenados en la secuencia sys.argv
Se pueden obtener los argumentos usando la notación [X]
Puede probar esto usando la llamada a este programa:
python3 argumentos.py primer_argumento segundo_argumento
'''
import sys

print('Número de argumentos:', len(sys.argv))
print('Argumentos:', sys.argv)
print('Primer argumento:', sys.argv[0])
if len(sys.argv) > 1:
	print('Segundo argumento:', sys.argv[1])
if len(sys.argv) > 2:
	print('Tercer argumento:', sys.argv[2])