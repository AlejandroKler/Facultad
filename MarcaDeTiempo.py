class MarcaDeTiempo():
    """Una marca de tiempo consiste en un conjunto de tracks que deben sonar (habilitados) y la duracion de la misma."""
    def __init__(self,duracion):
        """
        Crea una instancia de la clase.
        Parametros:
            duracion (float) Duracion de la marca de tiempo
        """
        self.duracion = duracion
        self.tracks_habilitados = []
