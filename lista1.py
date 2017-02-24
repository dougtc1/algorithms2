class ListaOrdenada:
    def __init__(self,valor=None,siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

    def longitud(self):
        if self.siguiente:
            return self.siguiente.longitud()+1
        if self.valor:
            return 1
        else:
            return 0
        pass

    def agregar(self,valor):
        if self.valor == None:
            self.valor = valor
        elif self.siguiente:
            self.siguiente.agregar(valor)
        else:
            self.siguiente = ListaOrdenada(valor)
            
    def obtener(self,indice):
        if indice == 0:
            return self.valor
        if self.siguiente:
            return self.siguiente.obtener(indice - 1)
        else:
            return None

# Inserta en elemento en el indice + 1
# Insertar en la posición siguiente a la dada
    '''
    def insertar(self,valor,indice):
        if indice ==0:
            if not self.valor:
                self.valor = valor
            else:
                temp = self.siguiente
                self.siguiente = ListaOrdenada(valor)
                self.siguiente = temp
        elif self.siguiente:
            self.siguiente.insertar(valor, indice -1)
        else:
            return None
    '''
# El insertar que tal 
    def insertar(self,valor,indice):
        if indice == 0:
            temp = ListaOrdenada()
            temp.valor = self.valor
            temp.siguiente = self.siguiente
            self.valor = valor
            self.siguiente = temp
            return True
        elif self.siguiente:
            return self.siguiente.insertar(valor, indice - 1)
        else:
            return False
        

    def remover(self,indice, anterior = None):
        if indice == 0:
            if anterior:
                anterior.siguiente = self.siguiente
            else:
                if self.siguiente:
                    self.valor = self.siguiente.valor
                    self.siguiente = self.valor = self.siguiente.siguiente
                else:
                    self.valor = None
            return True
        elif self.siguiente:
            self.siguiente.remover(indice - 1, self)
        else
            return False

    def imprimir(self):
        if self.valor:
            print(self.valor)
        if self.siguiente:
            self.siguiente.imprimir()
