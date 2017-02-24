# Descripción: Módulo con la implementación de algoritmos de ordenamientos
#              que son aplicados sobre listas de elementos que son comparables
#              entre sí. Al aplicar algún algoritmo de ordenamiento, la lista a ordenar
#              es copiada y se retorna una nueva lista con los elementos ordenados.
# Autor: Guillermo Palma
# email: gvpalma@usb.ve
# version 0.1


# Todos los algoritmos de ordenamiento tienen los siguentes parámetros
# Parámetros: seq: objeto lista de python que contiene elementos comparables
#
#             cmpf: Función que compara dos elementos de la lista.
#             Esta función es llamada repetidamente por los algoritmos de ordenamiento
#             para comparar dos elementos. La función cmpf toma como argumento
#             dos elementos de la lista, y retorna un número entero. Su prototipo es:
#             cmpf(x, y) --> int
#             El  número entero  define el orden
#             de los elementos de la siguiente manera:
#                 cmpf(x, y) < 0 : significa que el elemento x va antes del elemento y
#                 cmpf(x, y) > 0 : significa que el elemento x va después del elemento y
#                 cmpf(x, y) = 0 : significa que los elementos x, y son equivalentes

#Roberto Romero 10-10642
#Verónica Machado 10-10407

#Funcion cmpf
def cmpf(x1,x2):
	resultado = x1-x2
	return resultado

# Ordenamiento por Inserción
def insertion(seq, cmpf):
    n = len(seq)
    for i in range(1, n) :
        value = seq[i]
        pos = i
        while pos > 0 and cmpf(value, seq[pos - 1]) < 0 :
            seq[pos] = seq[pos - 1]
            pos -= 1
        seq[pos] = value

# Ordenamiento por Quicksort
def quicksort(seq,cmpf,izq=0,der=1):
	if der-izq >= 2:
		#particionar
		i=izq+1
		j=izq+1
		while j!= der:
			if cmpf(seq[j],seq[izq])<=0:
				aux=seq[i]
				seq[i]=seq[j]
				seq[j]=aux
				i+=1
			j+=1
		aux2=seq[izq]
		seq[izq]=seq[i-1]
		seq[i-1]=aux2	
		pivote=i-1
		#fin particionar
		quicksort(seq,cmpf,izq,pivote)
		quicksort(seq,cmpf,pivote+1,der)

#funcion mezclar
def mezclar(seq, izq, med, der, cmpf):
	i = izq
	j = med
	k = 0
	b = []
	while i!=med and j!=der:
		if cmpf(seq[i],seq[j]) <=0:
			b += [seq[i]]
			i += 1
		if seq[i] > seq[j]:
			b += [seq[j]]
			j += 1
	while i!=med:
		b += [seq[i]]
		i += 1
	while j!= der:
		b += [seq[j]]
		j += 1
	while k<(der-izq):
		seq[izq+k] = b[k]
		k += 1
	return seq

# Ordenamiento por Mergeort
def mergesort(seq, cmpf,izq, der ):
	if (der - izq) >= 2:
		med = ((izq + der + 1) // 2)
		mergesort(seq,cmpf, izq, med)
		mergesort(seq,cmpf,med, der)
		mezclar(seq, izq, med, der, cmpf)
	return seq
    
#Proc acomodarHeap
def acomodarHeap(tam, seq, l, m, cmpf):
	k = l
	listo = False
	while listo == False:
		mayor = k
		if (2*k + 1 < m) and cmpf(seq[2*k+1], seq[mayor]) > 0:
			mayor = 2*k+1
		if (2*k + 2 < m) and cmpf(seq[2*k+2], seq[mayor]) > 0:
			mayor = 2*k+2
		if mayor == k:
			listo = True
		if mayor !=k:
			a = seq[mayor]
			b = seq[k]
			seq[mayor] = b
			seq[k] = a
			k = mayor
	return seq
#proc construirHeap
def construirHeap(seq, cmpf):
	k = len(seq)//2
	while k!=0:
		k -= 1
		acomodarHeap(len(seq), seq, k, len(seq), cmpf)
	return seq

# Ordenamiento por Heapsort
def heapsort(seq, cmpf):
	construirHeap(seq, cmpf)
	j = len(seq)
	while j>0:
		j -= 1
		a= seq[0]
		b= seq[j]
		seq[0] = b
		seq[j] = a
		acomodarHeap(len(seq), seq, 0, j, cmpf)
	return seq

# Ordenamiento por Bubblesort0
def bubblesort0(seq, cmpf):
	n = 0
	while n != len(seq):
		k = len(seq)-1
		while k != n :
			if cmpf(seq[k-1],seq [k]) > 0:
				c = seq[k-1]
				d = seq[k]
				seq[k-1] = d
				seq[k] = c
			k = k-1
		n = n+1
	return seq

# Ordenamiento por Bubblesort1
def bubblesort1(seq, cmpf):
	n = 0
	b = False
	while n != len(seq) and b == False:
		k = len(seq)-1
		b=True
		while k != n :
			if cmpf(seq[k-1],seq [k]) > 0:
				b = False
				c = seq[k-1]
				d = seq[k]
				seq[k-1] = d
				seq[k] = c
			k = k-1
		n = n+1
	return seq

