from Pila import Pila

class _IteradorListaEnlazada():
    """Itera una instancia de la clase ListaEnlazada"""
    def __init__(self, prim):
        self.actual = prim
        self.pila_auxiliar = Pila()
        self.posicion = 0
    def next(self):
        if self.actual.prox is None:
            raise StopIteration('No hay más elementos en la lista')
        dato = self.actual
        self.pila_auxiliar.apilar(dato)
        self.actual = self.actual.prox
        self.posicion += 1
        return self.actual.dato
    def prev(self):
        if not self.pila_auxiliar.esta_vacia():
            dato = self.pila_auxiliar.desapilar()
            self.actual = dato
        else:
            raise StopIteration('No hay elemento previo')
        self.posicion -= 1
        return self.actual.dato
            
class ListaEnlazada():
    def __init__(self):
        self.prim = None
        self.len = 0
        self.iterador = self.obtener_iterador()
    
    def pop(self, i = None):
        if not i:
            i = self.len - 1
        if i < 0 or i >= self.len:
            raise IndexError('Indice fuera de rango')
        if i == 0:
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            n_ant = self.prim
            n_act = n_ant.prox
            for pos in range (1, i):
                n_ant = n_act
                n_act = n_ant.prox
            dato = n_act.dato
            n_ant.prox = n_act.prox
        self.len -= 1
        return dato
        
    def append(self,x):
        nuevo = _Nodo(x)
        if self.len == 0:
            self.prim = nuevo
        if self.len == 1:
            self.prim.prox = nuevo
        if self.len != 0 and self.len != 1:
            n_act = self.prim
            for pos in range(1,self.len):
                n_act = n_act.prox
            n_act.prox = nuevo
        self.len += 1
        
    def insert(self, i, x):
        """Inserta el elemento x en la posición i.
        Si la posición es inválida, levanta IndexError"""
        if i < 0 or i > self.len:
            raise IndexError("Posición inválida")
        nuevo = _Nodo(x)
        if i == 0:
            nuevo.prox = self.prim
            self.prim = nuevo
        else:
            n_ant = self.prim
            for pos in range(1, i):
                n_ant = n_ant.prox
                nuevo.prox = n_ant.prox
                n_ant.prox = nuevo
        self.len += 1
        
    def obtener_iterador(self):
        """ Devuelve el iterador de la lista. """
        return _IteradorListaEnlazada(self.prim)

    def siguiente(self):
    	"""Avanza al siguiente elemento y lo devuelve"""
    	return self.iterador.next()
    
    def anterior(self):
    	"""Retrocede al anterior elemento y lo devuelve"""
    	return self.iterador.prev()

    def actual(self):
    	""" Devuelve el dato en la posicion actual del iterador"""
    	return self.iterador.actual.dato

    def volver_al_inicio(self):
    	"""Vuelve el iterador a la posicion inicial"""
    	self.iterador = self.obtener_iterador()

    def actualizar(self,desplazamiento=0):
    	""" Reinicia el iterador y mueve el cursor a la posicion anterior (por defecto) o a la posicion indicada por parametro.
        Recibe un parametro desplazamiento que indica el desplazamiento con repecto a la posicion anterior"""
    	posicion = self.iterador.posicion
    	self.iterador = self.obtener_iterador()
    	for i in range(posicion + desplazamiento):
            if i != (posicion + desplazamiento - 1):
                self.siguiente()

    def posicion_actual(self):
    	"""Devuelve la posicion actual del iterador"""
    	return self.iterador.posicion

class _Nodo():
    def __init__(self, dato, prox = None):
        self.dato = dato
        self.prox = prox
    def __str__(self):
        return str(self.dato)
