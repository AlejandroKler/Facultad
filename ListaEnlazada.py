from Pila import Pila

class _IteradorListaEnlazada():
    """Itera una instancia de la clase ListaEnlazada"""
    def __init__(self, prim):
        self.actual = prim
        self.pila_auxiliar = Pila()
        self.posicion = 0
    def next(self):
        """Avanza una posicion y devuelve el dato. Si no hay posicion siguiente lanza una excepcion StopIteration. Si no hay elemento lanza una excepcion AttributeError."""
        if not self.actual.prox:
            raise StopIteration('No hay más elementos en la lista')
        dato = self.actual
        self.pila_auxiliar.apilar(dato)
        self.actual = self.actual.prox
        self.posicion += 1
        return self.actual.dato
    def prev(self):
        """Retrocede una posicion y devuelve el dato. Si no hay posicion anterior lanza una excepcion StopIteration. Si no hay elemento lanza una excepcion AttributeError."""
        if self.pila_auxiliar.esta_vacia():
            raise StopIteration('No hay elemento previo')
        dato = self.pila_auxiliar.desapilar()
        self.actual = dato
        self.posicion -= 1
        return self.actual.dato
            
class ListaEnlazada():
    def __init__(self):
        """Crea una lista enlazada vacía."""
        self.prim = None
        self.len = 0
        self.iterador = self.obtener_iterador()
    
    def pop(self, posicion = None):
        """ Elimina el nodo y devuelve el dato contenido.
        Si está fuera de rango, se lanza una excepcion IndexError.
        Si no se recibe la posición, devuelve el último elemento."""
        if not posicion:
            posicion = self.len - 1
        if posicion < 0 or posicion >= self.len:
            raise IndexError('Indice fuera de rango')
        if posicion == 0:
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            n_ant = self.prim
            n_act = n_ant.prox
            for pos in range (1, posicion):
                n_ant = n_act
                n_act = n_ant.prox
            dato = n_act.dato
            n_ant.prox = n_act.prox
        self.len -= 1
        return dato
        
    def append(self,dato):
        """Agrega un elemento al final de la lista enlazada"""
        nuevo = _Nodo(dato)
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
        
    def insert(self, posicion, dato):
        """Inserta el dato en la posición indicada.
        Si la posición es inválida, lanza una excepcion IndexError"""
        if posicion < 0 or posicion > self.len:
            raise IndexError("Posición inválida")
        nuevo = _Nodo(dato)
        if posicion == 0:
            nuevo.prox = self.prim
            self.prim = nuevo
        else:
            n_ant = self.prim
            for pos in range(1, posicion):
                n_ant = n_ant.prox
            nuevo.prox = n_ant.prox
            n_ant.prox = nuevo
        self.len += 1

    def esta_vacia(self):
        """Devuelve true si la lista no tiene ningun elemento"""
        return (self.len == 0)

    def obtener_iterador(self):
        """ Devuelve el iterador de la lista. """
        return _IteradorListaEnlazada(self.prim)

    def siguiente(self):
        """Avanza al siguiente elemento y lo devuelve. Si no hay marca o es la ultima, lanza una excepcion StopIteration"""
        try:
            return self.iterador.next()
        except AttributeError:
            raise StopIteration 
    
    def anterior(self):
        """Retrocede al anterior elemento y lo devuelve.  Si no hay marca o es la primera, lanza una excepcion StopIteration"""
        try:
            return self.iterador.prev()
        except AttributeError:
            raise StopIteration 

    def actual(self):
        """Devuelve el dato en la posicion actual del iterador. Si hay elemento, lanza una excepcion AttributeError."""
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
            if i < (self.len - 1):
                self.iterador.next()

    def posicion_actual(self):
        """Devuelve la posicion actual del iterador"""
        return self.iterador.posicion

class _Nodo():
    def __init__(self, dato, prox = None):
        self.dato = dato
        self.prox = prox
