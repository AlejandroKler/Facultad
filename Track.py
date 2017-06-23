class Track():
    """Representa un track de una cancion"""
    def __init__(self,tipo,frecuencia,volumen):
        """Constructor de la clase"""
        self.tipo = str(tipo).lower()
        self.frecuencia = int(frecuencia)
        self.volumen = float(volumen)

    def obtener_tipo(self):
        """Devuelve el tipo"""
        return self.tipo

    def obtener_frecuencia(self):
        """Devuelve la frecuencia"""
        return self.frecuencia

    def obtener_volumen(self):
        """Devuelve el volumen"""
        return self.volumen
