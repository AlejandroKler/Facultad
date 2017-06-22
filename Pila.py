class Pila:
    """Modela el funcionamiento de una pila. En esta se puede apilar elementos, desapilar elementos, ver el tope de la pila o
    chequear si está vacía"""
    def __init__(self):
        """Crea una nueva instancia de la clase Pila"""
        self.items = []
    def esta_vacia(self):
        """Revisa si la pila está vacía y devuelve un booleano"""
        return len(self.items) == 0
    def apilar(self,dato):
        """Apila un elemento en la pila"""
        self.items.append(dato)
    def desapilar(self):
        """Desapila el último elemento que se apiló"""
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.items.pop()
    def ver_tope(self):
        """Devuelve el tope de la pila, es decir, el último elemento que se apiló"""
        if self.esta_vacia():
            raise IndexError("La pila esta vacia")
        return self.items[-1]
