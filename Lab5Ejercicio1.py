import random

class Busqueda:

    def __init__ (self):
        self.N = int(input ("Introduzca el tamaño del arreglo: "))
        self.arreglo = [random.randint(0,self.N) for i in range(self.N)]
        self.ordenado = False
        self.indice = -2
        self.entero = -3


    def InsertionSort(self):
        k = 0

        while k != self.N:
            temp,l = self.arreglo[k],k
            while l != 0 and temp < self.arreglo[l-1]:
                self.arreglo[l] = self.arreglo[l-1]
                l = l-1

            self.arreglo[l] = temp
            k = k+1
        print (self.arreglo)
        self.ordenado = True
        print (self.ordenado)
        return self.ordenado
    
    def SelectionSort(self):
        
        k = 0
        
        while (k != self.N):
            l = k+1
            mini = k
            while ( l != self.N):
                if (self.arreglo[l] <= self.arreglo[mini]):
                    mini = l
                elif (self.arreglo[mini] < self.arreglo[l]):
                    pass
                l = l+1
            self.arreglo[k],self.arreglo[mini] = self.arreglo[mini],self.arreglo[k]
            k = k+1
        print (self.arreglo)
        self.ordenado = True
        return self.ordenado
        
    def BubbleSort (self):
        k = 0

        while (k != self.N):
            l = self.N - 1
            cambios = False

            while l != k:
                if self.arreglo[l-1]>self.arreglo[l]:
                    self.arreglo[l],self.arreglo[l-1] = self.arreglo[l-1],self.arreglo[l]
                    cambios = True
                elif self.arreglo[l-1] <= self.arreglo[l]:
                    pass
                l = l -1

            k = k+1

        print (self.arreglo)
        self.ordenado = True

        return self.ordenado
                

    def LinearSearch(self):
        entero = input("Introduzca un entero a buscar: ")
        indice = -1
        if (self.ordenado):
            for i in range (0,self.N):
                if (int(entero) == int(self.arreglo[i])):
                    indice = i
                    break
                else:
                    pass
        return indice

    def BinarySearch(self, inicio, final):
        if self.indice == -1 and self.ordenado:
            if (self.N >= 2 and self.arreglo[final // 2] == entero):
                self.indice = self.N // 2
            elif (self.N >= 2 and entero < (self.arreglo[final // 2]) ):
                self.indice = self.BinarySearch(0,final // 2)
            else:
                self.indice = self.BinarySearch((final // 2) + 1,final)
        elif self.ordenado:
            self.indice = -1
            self.entero = int(input("Introduzca un entero a buscar: "))
            if (self.N >= 2 and self.arreglo[final // 2] == entero):
                self.indice = self.N // 2
            elif (self.N >= 2 and entero < (self.arreglo[final // 2]) ):
                self.indice = self.BinarySearch(0,final // 2)
            else:
                self.indice = self.BinarySearch((final // 2) + 1,final)
        

        return self.indice



prueba = Busqueda()

print(prueba.arreglo)

print("----------")

prueba.InsertionSort()


print(prueba.ordenado)

print("----------")

lineal = prueba.BinarySearch(0,prueba.N)

print (lineal)

print('Hola Mundo')
