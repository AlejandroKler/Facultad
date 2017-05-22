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
estsetsfsklfalkdfgnñzgb 
