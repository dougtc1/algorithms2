from lista import ListaOrdenada

miLista = ListaOrdenada()
miLista.agregar(1)
miLista.agregar(2)
miLista.agregar(3)
miLista.imprimir()
miLista.remover(2)
miLista.imprimir()





p = Paquete ()
p.destinatario = ('Luis')
p.prioridad = 2
w = Paquete ()
w.destinatario = ('Jose')
w.prioridad = 1
r = Paquete ()
r.destinatario = ('Gabriel')
r.prioridad = 1
f = Paquete ()
f.destinatario = ('Leo')
f.prioridad = 4
a = Paquete ()
a.destinatario = ('Marcos')
a.prioridad = 3

c = ColaP()
c.encolar(p)
c.encolar(w)
c.encolar(r)
c.encolar(f)
c.encolar(a)
c.desencolar()
c.imprimir()