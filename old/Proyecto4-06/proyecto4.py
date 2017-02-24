#Roberto Romero 10-10642
#veronica Machado 10-10407




class arbin(object):

	#CONSTRUCTOR
	def __init__(self):
		self.izq=None
		self.der=None
		self.cant_veces = 0

		
	#OPERACION LECTURA
	def lectura(self,secuencia):
		aux = self 
		no_esta=False
		secu= ''
		for h in range(len(secuencia)):
			secu = secu + str(secuencia[h])
		for i in range(len(secuencia)):
			if secuencia[i] == 'A':
				aux = aux.izq
				if aux == None:
					no_esta = True
					break	
			if secuencia[i] == 'T':
				aux= aux.der
				if aux == None:
					no_esta = True
					break	
		if no_esta == False:
			archi.write(secu)
			archi.write(' ')
			archi.write(str(aux.cant_veces))
			archi.write('\n')
		elif no_esta == True:
			archi.write(secu)
			archi.write(' 0')	
			archi.write('\n')
			
	#OPERACION ADICION
	def adicion(self,secuencia):
		aux = self
		for i in range(len(secuencia)):
			if secuencia[i] == 'A' :
				if aux.izq == None:
					aux.izq = arbin()
					aux = aux.izq
				elif aux.izq != None:
					aux = aux.izq
			if secuencia[i] == 'T':
				if aux.der == None:
					aux.der = arbin()
					aux = aux.der
				elif aux.der != None:
					aux = aux.der
			if i == len(secuencia)-1:
				aux.cant_veces += 1
			
	#PROCEDIMIENTO AUXILIAR DE LONGITUD MAXIMA
	def longitudmaximaaux(self):
		if self != None:
			if self.izq != None:
				a = self.izq.longitudmaximaaux()
			if self.izq == None:
				a = 0	
			if self.der != None:
				b = self.der.longitudmaximaaux()
			if self.der == None:
				b = 0		
			if a > b:
				longmax = a + 1
			if a <= b:
				longmax = b + 1	
		if self == None:
			longmax = 0
		return longmax  
	# PROCEDIMIENTO LONGITUD MAXIMA
	def longitudmaxima(self):
		archi.write('longitud maxima = ')
		archi.write(str(self.longitudmaximaaux() - 1))
		archi.write('\n')
	
	#PROCEDIMIENTO ELIMINAR 
	def eliminar(self,secuencia):
		aux = self 
		no_esta = False
		for i in range(len(secuencia)):
			if secuencia[i] == 'A':
				aux = aux.izq	
				if aux == None:
					no_esta = True
					break
			if secuencia[i] == 'T':
				aux= aux.der	
				if aux == None :
					no_esta = True
					break
		if no_esta == False:
			aux.cant_veces= aux.cant_veces - 1
		elif no_esta == True:
			archi.write('ERROR: Cannot DELETE')	
			archi.write('\n')
	
	#PROCEDIMIENTO AUXILIAR PODAR ARBOL
	def podarArbol(self):
		if self != None:
			if self.cant_veces == 0:
				if self.izq == None and self.der == None:
					self = None
				if self.izq != None or self.der != None:
					if self.izq != None:
						self.izq.podarArbol()
					if self.der != None:	
						self.der.podarArbol()
			if arbol.cant_veces > 0:
				self.izq.podarArbol()
				self.der.podarArbol()
		if self == None:
			pass
		
	#PROCEDIMIENTO REEMPLAZO
	def reemplazo(self,secuencia,n):
		aux = self 
		no_esta=False
		for i in range(len(secuencia)):
			if secuencia[i] == 'A':
				aux = aux.izq
				if aux == None:
					no_esta = True
					break	
			if secuencia[i] == 'T':
				aux= aux.der
				if aux == None:
					no_esta = True
					break	
		if no_esta == False:
			aux.cant_veces = n
		elif no_esta == True:
			for i in range(n):
				self.adicion(secuencia)
		if n == 0:
			self.podarArbol()
		
	#PROCEDIMIENTO FUSION
	def fusion(self,seqor,seqdes):
		#se busca el nodo a cambiar y se guarda en aux1
		aux1 = self
		no_esta2 = False
		for h in range(len(seqor)):
			if seqor[h] == 'A':
				aux1 = aux1.izq
				if aux1 == None:
					no_esta2 = True
					break	
			if seqor[h] == 'T':
				aux1 = aux1.der
				if aux1 == None:
					no_esta2 = True
					break
		if no_esta2 == True:
			archi.write('No existe ninguna secuencia con ese comienzo')
			archi.write('\n')
		elif no_esta2 == False:	
			#se busca o crea el nodo por el cual cambiar y se guarda en aux2
			aux2 = self
			for j in range(len(seqdes)):
				if seqdes[j] == 'A':
					if aux2.izq == None:
						aux2.izq = arbin()
						aux2 = aux2.izq
					elif aux2.izq != None:
						aux2 = aux2.izq	
				if seqdes[j] == 'T':
					if aux2.der == None:
						aux2.der = arbin()
						aux2 = aux2.der
					elif aux2.der != None:
						aux2 = aux2.der		
			aux2.izq = aux1.izq
			aux2.der = aux1.der
			aux1.izq= None
			aux1.der= None
			
	#PROCEDIMIENTO MIGRACION
	def migracion(self,seqor,seqdes):
	#se verifica que no exista alguna seccuencia 
		#que comience igual a la que se va a cambiar
		aux = self 
		no_esta=False
		for i in range(len(seqdes)):
			if seqdes[i] == 'A':
				aux = aux.izq
				if aux == None:
					no_esta = True
					break	
			if seqdes[i] == 'T':
				aux= aux.der
				if aux == None:
					no_esta = True
					break	
		if no_esta == False:
			archi.write('ERROR: Cannot CHANGE. Use CHANGEMERGE instead')
			archi.write('\n')
		elif no_esta == True:
			#se busca el nodo a cambiar y se guarda en aux1
			aux1 = self
			no_esta2 = False
			for h in range(len(seqor)):
				if seqor[h] == 'A':
					aux1 = aux1.izq
					if aux1 == None:
						no_esta2 = True
						break	
				if seqor[h] == 'T':
					aux1 = aux1.der
					if aux1 == None:
						no_esta2 = True
						break
			if no_esta2 == True:
				archi.write('No existe ninguna secuencia con ese comienzo')
				archi.write('\n')
			elif no_esta2 == False:	
				#se busca o crea el nodo por el cual cambiar y se guarda en aux2
				aux2 = self
				for j in range(len(seqdes)):
					if seqdes[j] == 'A':
						if aux2.izq == None:
							aux2.izq = arbin()
							aux2 = aux2.izq
						elif aux2.izq != None:
							aux2 = aux2.izq	
					if seqdes[j] == 'T':
						if aux2.der == None:
							aux2.der = arbin()
							aux2 = aux2.der
						elif aux2.der != None:
							aux2 = aux2.der		
				aux2.izq = aux1.izq
				aux2.der = aux1.der
				aux1.izq= None
				aux1.der= None

	#PROCEDIMIENTO LISTADO	
	def listado(self,st=''):
		aux = self
		string = st
		string2 = ''
		
		if aux.izq != None:
			if aux.izq.cant_veces != 0:
				string2=string
				string = string + 'A'
				archi.write(string)
				archi.write(' ')
				archi.write(str(aux.izq.cant_veces))
				archi.write('\n')
			if aux.izq.cant_veces == 0:
				string2=string
				string = string + 'A'
			aux.izq.listado(string)
			
			
			string=string2
				
		if aux.der != None:
			if aux.der.cant_veces != 0:
				string2 = string
				string = string + 'T'
				archi.write(string)
				archi.write(' ')
				archi.write(str(aux.der.cant_veces))
				archi.write('\n')
			if aux.der.cant_veces == 0:
				string2 = string
				string = string + 'T'
			aux.der.listado(string)
				
			if aux.der.izq == None and aux.der.der == None:
				string=string2

#PROCEDIMIENTO PARA LEER ARCHIVO DE TEXTO
def leer(nombre_archivo):
	comando=[]
	global arbol
	with open(nombre_archivo) as f:
		lineas = f.readlines()
	for linea in lineas:
		linea = linea.strip('\t');
		if linea == "":break
		comando = linea.split()
		if comando != '':
			if comando[0] == 'GET':
				seq = list(comando[1])
				arbol.lectura(seq)
			if comando[0] == 'ADD':
				seq = list(comando[1])
				arbol.adicion(seq)
			if comando[0] == 'GETALL':
				arbol.listado()
			if comando[0] == 'MAXLENGTH':
				arbol.longitudmaxima()
			if comando[0] == 'DELETE':
				seq = list(comando[1])
				arbol.eliminar(seq)	
			if comando[0] == 'SET':
				seq = list(comando[1])
				n = int(comando[2])
				arbol.reemplazo(seq,n)
			if comando[0] == 'CHANGE':
				seqor = list(comando[1])
				seqdes = list(comando[2])
				arbol.migracion(seqor,seqdes)
			if comando[0] == 'CHANGEMERGE':
				seqor = list(comando[1])
				seqdes = list(comando[2])
				arbol.fusion(seqor,seqdes)				
			if comando [0] == 'PRINT':
				archi.write(comando[1])
				archi.write('\n')

#-------------------------------------------------------------------------------------------------------------										
#----------------------------------------------->MAIN<--------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------


archi=open('result_salida.txt','w')
archi.close()

archi=open('result_salida.txt','a')
arbol=arbin()

leer('entrada.txt')

	
archi.close()
