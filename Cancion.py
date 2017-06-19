from ListaEnlazada import ListaEnlazada
from ListaEnlazada import _IteradorListaEnlazada
from MarcaDeTiempo import MarcaDeTiempo
import soundPlayer as pysounds

class Cancion():
    """Representa un conjunto de marcas de tiempo y sonidos (tracks)"""
    def __init__(self):
        """Crea una instancia de la clase."""
        self.tiempos = ListaEnlazada() # Marcas de tiempo
        self.tracks = [] # Lista de tracks
        self.cursor = _IteradorListaEnlazada(self.tiempos.prim)
        self.funciones_disponibles = ["sine","triangular","square"] # Constante con los tipos de tracks

    def store(self,name):
        """Guarda la cancion
        Parametros:
            name (string) Nombre del archivo sin extension"""
        self.cursor = _IteradorListaEnlazada(self.tiempos.prim) # Volvemos el iterador al comienzo
        with open(name + ".plp","w") as f:
            f.write("C,"+str(self.cant_tracks())+"\n")
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
                    for x in range(0,self.cant_tracks()):
                        if x in MarcaDeTiempo.tracks_habilitados:
                            cadena += "#"
                        else:
                            cadena += "·"
                    f.write("N,"+cadena+"\n")
                except StopIteration:
                    break

    def step(self):
        """Avanza a la siguiente marca de tiempo si la hay. Si no, no hace nada."""
        try:
            self.cursor.next()
        except StopIteration:
            return
            
    def stepm(self,n):
        """Avanza N marcas de tiempo hacia adelante o las que pueda."""
        try:
            for x in range(0,n):
                self.cursor.next()
        except StopIteration:
            return
            
    def back(self):
        """Retrocede a la anterior marca de tiempo si puede."""
        try:
            self.cursor.prev()
        except StopIteration:
            return

    def backm(self,n):
        """Retrocede N marcas de tiempo hacia atras o las que pueda."""
        try:
            for x in range(n):
                self.cursor.prev()
        except StopIteration:
            return 

    def track_add(self,funcion,frecuencia,volumen):
        """Agrega un track con el sonido indicado."""
        if funcion.lower() not in self.funciones_disponibles:
            print('El sonido introducido no existe')
            return
        if volumen > 1 or volumen < 0:
            print('El volumen no puede tomar un valor mayor a uno ni ser menor que 0')
            return
        self.tracks.append([funcion,frecuencia,volumen])

    def track_del(self,posicion):
        """Elimina un track por numero."""
        try:
            self.tracks.pop(posicion)
        except IndexError:
            print('Este track no se encuentra en la canción')

    def mark_add(self,duracion):
        """Agrega una marca de tiempo de la duracion establecida. Originalmente
        todos los tracks arrancan como deshabilitados"""
        mark = MarcaDeTiempo(duracion)
        self.tiempos.insert(self.cursor.posicion,mark)
        self._mover_cursor()

    def mark_add_next(self,duracion):
        """Igual que MARKADD pero la inserta luego de la marca en la cual esta
        actualmente el cursor"""
        mark = MarcaDeTiempo(duracion)
        self.tiempos.insert(self.cursor.posicion + 1,mark)
        self._mover_cursor()

    def mark_add_prev(self,duracion):
        """Igual que MARKADD pero la inserta antes de la marca en la cual esta
        actualmente el cursor"""
        mark = MarcaDeTiempo(duracion)
        if self.cursor.posicion == 0:
            print('No hay posición anterior para insertar una marca')
            return
        if not self.tiempos.prim:
            print('Debe insertar al menos una marca para utilizar esta función')
            return
        self.tiempos.insert(self.cursor.posicion - 1, mark)
        self._mover_cursor(1)

    def track_on(self,numero):
        """Habilita al track durante la marca de tiempo en la cual esta parada el
        cursor."""
        try:
            track = self.tracks[numero]
            if not track in self.cursor.actual.dato.tracks_habilitados: 
                self.cursor.actual.dato.tracks_habilitados.append(track)
        except IndexError:
            print('No existe tal track en la canción')
        
    def track_off(self,numero):
        """Deshabilita al track durante la marca de tiempo en la cual esta parada el
        cursor."""
        try:
            track = self.tracks[numero]
            self.cursor.actual.dato.tracks_habilitados.remove(track)
        except IndexError:
            print('No existe tal track en la canción')
        except ValueError:
            print('Este track no se encuentra habilitado')
            
    def play(self):
        """Reproduce la marca en la que se encuentra el cursor actualmente."""
        self.reproducir(self.cursor.actual.dato)

    def play_all(self):
        """Reproduce la cancion completa desde el inicio."""
        self.cursor = _IteradorListaEnlazada(self.tiempos.prim)
        for i in range (0, self.cant_tracks()):
            self.reproducir(self.cursor.actual.dato)
            if i != (self.cant_tracks() -1):
                self.cursor.next()

    def play_marks(self,n):
        """Reproduce las proximas n marcas desde la posicion actual del cursor."""
        try:
            for i in range (0, n):
                self.reproducir(self.cursor.actual.dato)
                self.cursor.next()
        except StopIteration:
            return 

    def play_seconds(self,segundos):
        """Reproduce los proximos segundos la posicion actual del cursor."""
        suma_duracion = 0
        while True:
            try:
                self.reproducir(self.cursor.actual.dato)
                suma_duracion += self.cursor.actual.dato.duracion
                if suma_duracion >= segundos:
                    break
                self.cursor.next()
            except StopIteration:
                break
        
    def cant_tracks(self):
        """Obtiene la cantidad de tracks cargados"""
        return len(self.tracks)

    def _mover_cursor(self,desplazamiento=0):
        """ Reinicia el iterador y mueve el cursor a la posicion actual (por defecto) o a la posicion indicada por parametro.
        Recibe un parametro desplazamiento que indica el desplazamiento con repecto a la posicion original"""
        posicion_cursor = self.cursor.posicion
        self.cursor = _IteradorListaEnlazada(self.tiempos.prim)
        for i in range(0 , posicion_cursor + desplazamiento):
            if i != (posicion_cursor + desplazamiento - 1):
                self.cursor.next()
        
    def reproducir(self,mark):              
        sp = pysounds.SoundPlayer(len(self.tracks))
        duracion = mark.duracion
        sonidos_a_reproducir = []
        for track in mark.tracks_habilitados:
            tipo = track[0]
            freq = track[1]
            vol = track[2]
            if tipo == "sine":
                sonidos_a_reproducir.append(pysounds.SoundFactory.get_sine_sound(freq,vol))
            if tipo == "triangular":
                sonidos_a_reproducir.append(pysounds.SoundFactory.get_triangular_sound(freq,vol))
            if tipo == "square":
                sonidos_a_reproducir.append(pysounds.SoundFactory.get_square_sound(freq,vol))
        sp.play_sounds(sonidos_a_reproducir, duracion)
