class MarcaDeTiempo():
	"""Descripcion"""
	def __init__(self,duracion):
        """Crea una instancia de la clase.
        Parametros:
        	duracion (float) Duracion de la marca de tiempo"""
        self.duracion = duracion
        self.habilitados = []

    def habilitar_track(self,posicion):
    	if not posicion in self.habilitados:
    		self.habilitados.append(posicion)

    def deshabilitar_track(self,posicion):
    	try:
    		self.habilitados.remove(posicion)
        except ValueError:
            pass
