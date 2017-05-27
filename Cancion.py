class Cancion():
	"""Descripcion"""

	def __init__(self):
        """Crea una instancia de la clase."""
        self.tiempos = ListaEnlazada() # Marcas de tiempo
        self.tracks = [] # Lista de tracks
	self.cursor = _IteradorListaEnlazada(self.tiempos.prim)
    
    def load(self,file):
    	"""Carga la cancion desde el archivo. Reemplaza la cancion en edicion
		actual si es que la hay."""
		pass

	def store(self):
    	"""Guarda la cancion"""
		pass

	def step(self,file):
    	"""Avanza a la siguiente marca de tiempo."""
		self.cursor.next()

	def stepm(self,n):
    	"""Avanza N marcas de tiempo hacia adelante."""
		for x in range(0,n):
			self.cursor.next()

	def back(self):
    	"""Retrocede a la anterior marca de tiempo"""
		self.cursor.prev()

	def backm(self,n):
    	"""Retrocede N marcas de tiempo hacia atras."""
		for x in range(0,n):
			self.cursor.prev()

	def track_add(self,funcion,frecuencia,volumen):
    	"""Agrega un track con el sonido indicado."""
		self.tracks.append([funcion,frecuencia,volumen])

	def track_del(self,posicion = None):
    	"""Elimina un track por numero."""
		self.tracks.pop(posicion)

	def mark_add(self,duracion):
    	"""Agrega una marca de tiempo de la duracion establecida. Originalmente
		todos los tracks arrancan como deshabilitados"""
		mark = MarcaDeTiempo(duracion)
		self.tiempos.append(mark)

	def mark_add_next(self,duracion):
    	"""Igual que MARKADD pero la inserta luego de la marca en la cual esta
		actualmente el cursor"""

	def mark_add_prev(self,duracion):
    	"""Igual que MARKADD pero la inserta antes de la marca en la cual esta
		actualmente el cursor"""
		pass

	def track_on(self,numero):
    	"""Habilita al track durante la marca de tiempo en la cual esta parada el
		cursor."""

	def track_off(self,numero):
    	"""Deshabilita al track durante la marca de tiempo en la cual esta parada el
		cursor."""
		pass

	def play(self):
    	"""Reproduce la marca en la que se encuentra el cursor actualmente."""
		pass

	def play_all(self):
    	"""Reproduce la cancion completa desde el inicio."""
		pass

	def play_marks(self,n):
    	"""Reproduce las proximas n marcas desde la posicion actual del cursor."""
		pass

	def play_seconds(self,n):
    	"""Reproduce los proximos N segundos la posicion actual del cursor. Si
		alguna marca dura mas del tiempo restante, la reproduccion se corta
		antes."""
		



	def track_len(self):
		""" Obtiene la cantidad de tracks cargados"""
		return len(self.tracks)
