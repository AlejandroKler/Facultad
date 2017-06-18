from ListaEnlazada import ListaEnlazada
from ListaEnlazada import _IteradorListaEnlazada
from MarcaDeTiempo import MarcaDeTiempo
import soundPlayer as pysounds

class Cancion():
    """Descripcion"""
    def __init__(self):
        """Crea una instancia de la clase."""
        self.tiempos = ListaEnlazada() # Marcas de tiempo
        self.tracks = [] # Lista de tracks
        self.cursor = _IteradorListaEnlazada(self.tiempos.prim)

    def store(self,name):
        """Guarda la cancion
        Parametros:
            name (string) Nombre del archivo sin extencion"""
        self.cursor = _IteradorListaEnlazada(self.tiempos.prim) # Volvemos el iterador al comienzo
        with open(name + ".plp","w") as f:
            f.write("C,"+self.track_len()+"\n")
            for track in self.tracks:
                f.write("S,{}|{}|{}\n".format(track[0],track[1],track[2]))
            anterior = None
            while True:
                try:
                    MarcaDeTiempo = self.cursor.next()
                    if not MarcaDeTiempo.duracion == anterior:
                        f.write("T,"+MarcaDeTiempo.duracion+"\n")
                    anterior = MarcaDeTiempo.duracion
                    cadena = ""
                    for x in range(0,self.track_len()):
                        if x in MarcaDeTiempo.habilitados:
                            cadena += "#"
                        else:
                            cadena += "·"
                    f.write("N,"+cadena+"\n")
                except StopIteration:
                    break

    def step(self):
        """Avanza a la siguiente marca de tiempo."""
        try:
            self.cursor.next()
        except StopIteration:
            return
            
    def stepm(self,n):
        """Avanza N marcas de tiempo hacia adelante."""
        try:
            for x in range(0,n):
                self.cursor.next()
        except StopIteration:
            return
            
    def back(self):
        """Retrocede a la anterior marca de tiempo"""
        try:
            self.cursor.prev()
        except StopIteration:
            return

    def backm(self,n):
        """Retrocede N marcas de tiempo hacia atras."""
        try:
            for x in range(0,n):
                self.cursor.prev()
        except StopIteration:
            return 

    def track_add(self,funcion,frecuencia,volumen):
        """Agrega un track con el sonido indicado."""
        funcion_minuscula = funcion.lower()
        if funcion_minuscula not in ['sine', 'triangular', 'square']:
            return 'El sonido introducido no existe'
        if volumen > 1 or volumen < 0:
            return 'El volumen no puede tomar un valor mayor a uno ni ser menor que 0'
        self.tracks.append([funcion,frecuencia,volumen])

    def track_del(self,posicion = None):
        """Elimina un track por numero."""
        try:
            self.tracks.pop(posicion)
        except IndexError:
            return 'Este track no se encuentra en la canción'

    def mark_add(self,duracion):
        """Agrega una marca de tiempo de la duracion establecida. Originalmente
        todos los tracks arrancan como deshabilitados"""
        mark = MarcaDeTiempo(duracion)
        if self.tiempos.prim == None:
            self.tiempos.append(mark)
            return
        self.tiempos.insert(self.cursor.posicion,mark)
        self.mover_cursor()

    def mark_add_next(self,duracion):
        """Igual que MARKADD pero la inserta luego de la marca en la cual esta
        actualmente el cursor"""
        mark = MarcaDeTiempo(duracion)
        self.tiempos.insert(self.cursor.posicion + 1,mark)
        self.mover_cursor()

    def mark_add_prev(self,duracion):
        """Igual que MARKADD pero la inserta antes de la marca en la cual esta
        actualmente el cursor"""
        mark = MarcaDeTiempo(duracion)
        if self.cursor.posicion == 0:
            return 'No hay posición anterior para insertar una marca'
        if self.tiempos.prim == None:
            return 'Debe insertar al menos una marca para utilizar esta función'
        self.tiempos.insert(self.cursor.posicion - 1, mark)
        self.mover_cursor(1)

    def track_on(self,numero):
        """Habilita al track durante la marca de tiempo en la cual esta parada el
        cursor."""
        try:
            track = self.tracks[numero]
            if not track in self.cursor.actual.dato.habilitados: 
                self.cursor.actual.dato.habilitados.append(track)
        except IndexError:
            return 'No existe tal track en la canción'
        
    def track_off(self,numero):
        """Deshabilita al track durante la marca de tiempo en la cual esta parada el
        cursor."""
        try:
            track = self.tracks[numero]
        except IndexError:
            return 'No existe tal track en la canción'
        try:
            self.cursor.actual.dato.habilitados.remove(track)
        except ValueError:
            return 'Este track no se encuentra habilitado'
            
    def play(self):
        """Reproduce la marca en la que se encuentra el cursor actualmente."""
        self.reproducir(self.cursor.actual.dato)

    def play_all(self):
        """Reproduce la cancion completa desde el inicio."""
        self.cursor = _IteradorListaEnlazada(self.tiempos.prim)
        for i in range (0, self.track_len()):
            self.reproducir(self.cursor.actual.dato)
            if i != (self.track_len() -1):
                self.cursor.next()

    def play_marks(self,n):
        """Reproduce las proximas n marcas desde la posicion actual del cursor."""
        try:
            for i in range (0, n):
                self.reproducir(self.cursor.actual.dato)
                self.cursor.next()
        except StopIteration:
            return 

    def play_seconds(self,n):
        """Reproduce los proximos N segundos la posicion actual del cursor. Si
        alguna marca dura mas del tiempo restante, la reproduccion se corta
        antes."""
        suma_duracion = 0
        while True:
            try:
                self.reproducir(self.cursor.actual.dato)
                suma_duracion += self.cursor.actual.dato.duracion
                if suma_duracion >= n:
                    break
                self.cursor.next()
            except StopIteration:
                break
        
    def track_len(self):
        """Obtiene la cantidad de tracks cargados"""
        return len(self.tracks)

    def mover_cursor(self,n=0):
        """ Genera una nueva instancia del iterador y mueve el cursor.
        Recibe un parametro n que indica el desplazamiento con repecto a la posicion original"""
        posicion_cursor = self.cursor.posicion
        self.cursor = _IteradorListaEnlazada(self.tiempos.prim)
        for i in range(0 , posicion_cursor + n):
            if i != (posicion_cursor + n - 1):
                self.cursor.next()
        
    def reproducir(self,mark):              
        sp = pysounds.SoundPlayer(len(self.tracks))
        duracion = mark.duracion
        sonidos_a_reproducir = []
        for x in mark.habilitados:
            freq = x[1]
            vol = x[2]
            if x[0] == "sine":
                sonidos_a_reproducir.append(pysounds.SoundFactory.get_sine_sound(freq,vol))
            if x[0] == "triangular":
                sonidos_a_reproducir.append(pysounds.SoundFactory.get_triangular_sound(freq,vol))
            if x[0] == "square":
                sonidos_a_reproducir.append(pysounds.SoundFactory.get_square_sound(freq,vol))
        sp.play_sounds(sonidos_a_reproducir, duracion)
