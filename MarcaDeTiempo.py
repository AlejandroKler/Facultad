class MarcaDeTiempo():
    """Una marca de tiempo consiste en un conjunto de tracks que deben sonar (habilitados) y la duracion de la misma."""
    def __init__(self,duracion):
        """
        Crea una instancia de la clase.
        Parametros:
            duracion (float) Duracion de la marca de tiempo
        """
        self.duracion = duracion
        self.tracks_habilitados = [] # Almacena los numeros de los tracks habilitados

    def obtener_habilitados(self):
        """ Devuelve la lista de tracks habilitados"""
        return self.tracks_habilitados

    def obtener_duracion(self):
        """ Devuelve la duracion de la marca"""
        return self.duracion

    def habilitar_track(self,numero_de_track):
        """Habilita un track"""
        self.tracks_habilitados.append(numero_de_track)

    def deshabilitar_track(self,numero_de_track):
        """Deshabilita un track"""
        self.tracks_habilitados.remove(numero_de_track)
