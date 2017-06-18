class Pila:
    def __init__(self):
        self.items = []
    def esta_vacia(self):
        return len(self.items) == 0
    def apilar(self,dato):
        self.items.append(dato)
    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.items.pop()
    def ver_tope(self):
        if self.esta_vacia():
            raise IndexError("La pila esta vacia")
        return self.items[-1]
