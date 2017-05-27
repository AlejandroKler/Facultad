class _IteradorListaEnlazada:
    """Itera una instancia de la clase ListaEnlazada"""
    def __init__(self, prim):
        self.actual = prim
    def __next__(self):
        if self.actual is None:
            raise StopIteration()
        dato = self.actual.dato
        self.actual = self.actual.prox
        return dato

class _Nodo:
    def __init__(self, dato = None, prox = None):
        self.dato = dato
        self.prox = prox
    def __str__(self):
        return str(self.dato)

class ListaEnlazada:
    """Modela una lista enlazada."""
    
    def __init__(self):
        """Crea una lista enlazada vacía."""
        # referencia al primer nodo (None si la lista está vacía)
        self.prim = None
        # cantidad de elementos de la lista
        self.len = 0
        return self
    
    def pop(self, i=None):
        """Elimina el nodo de la posición i, y devuelve el dato contenido.
        3 Si i está fuera de rango, se levanta la excepción IndexError.
        4 Si no se recibe la posición, devuelve el último elemento."""
        if i is None:
            i = self.len - 1
        if i < 0 or i >= self.len:
            raise IndexError("Índice fuera de rango")
        if i == 0:
            # Caso particular: saltear la cabecera de la lista
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            # Buscar los nodos en las posiciones (i-1) e (i)
            n_ant = self.prim
            n_act = n_ant.prox
            for pos in range(1, i):
                n_ant = n_act
                n_act = n_ant.prox
            # Guardar el dato y descartar el nodo
            dato = n_act.dato
            n_ant.prox = n_act.prox
        self.len -= 1
        return dato

    def remove(self, x):
        """Borra la primera aparición del valor x en la lista.
         Si x no está en la lista, levanta ValueError"""
        if self.len == 0:
            raise ValueError("Lista vacía")
        if self.prim.dato == x:
            self.prim = self.prim.prox
        else:
            n_ant = self.prim
            n_act = n_ant.prox
        while n_act is not None and n_act.dato != x:
            n_ant = n_act
            n_act = n_ant.prox
        if n_act == None:
            raise ValueError("El valor no está en la lista.")
            n_ant.prox = n_act.prox
        self.len -= 1
        
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
    def __iter__(self):
        """Devuelve un iterador de la lista."""
        return _IteradorListaEnlazada(self.prim)
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
