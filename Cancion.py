from ListaEnlazada import ListaEnlazada
from ListaEnlazada import _IteradorListaEnlazada
from MarcaDeTiempo import MarcaDeTiempo
from Track import Track
import soundPlayer as pysounds

class Cancion():
    """Representa un conjunto de marcas de tiempo y sonidos (tracks)"""
    FUNCIONES_DISPONIBLES = ["sine","triangular","square"] # Constante con los tipos de tracks
    def __init__(self):
        """Crea una instancia de la clase."""
        self.tiempos = ListaEnlazada() # Marcas de tiempo
        self.tracks = [] # Lista de tracks

    def store(self,name):
        """Guarda la cancion, si no recibe una cadena valida levanta ValueError
        Parametros:
            name (string) Nombre del archivo sin extension"""
        if not name:
            raise ValueError("Debe indicar el nombre")
        self.tiempos.volver_al_inicio()
        with open(name + ".plp","w") as f:
            f.write("C,"+str(self.cant_tracks())+"\n")
            for track in self.tracks:
                f.write("S,{}|{}|{}\n".format(track.obtener_tipo(),track.obtener_frecuencia(),track.obtener_volumen()))
            anterior = None
            MarcaDeTiempo = self.tiempos.actual()
            while True:
                try:
                    print(MarcaDeTiempo.obtener_duracion())
                    if not MarcaDeTiempo.obtener_duracion() == anterior:
                        f.write("T,"+str(MarcaDeTiempo.obtener_duracion())+"\n")
                    anterior = MarcaDeTiempo.obtener_duracion()
                    cadena = ""
                    for posicion in range(self.cant_tracks()):
                        if posicion in MarcaDeTiempo.obtener_habilitados():
                            cadena += "#"
                        else:
                            cadena += "·"
                    f.write("N,"+cadena+"\n")
                    MarcaDeTiempo = self.tiempos.siguiente()
                except StopIteration:
                    break

    def step(self):
        """Avanza a la siguiente marca de tiempo si la hay. Si no, no hace nada."""
        try:
            self.tiempos.siguiente()
        except StopIteration:
            return
            
    def stepm(self,n):
        """Avanza N marcas de tiempo hacia adelante o las que pueda."""
        try:
            for x in range(n):
                self.tiempos.siguiente()
        except StopIteration:
            return
            
    def back(self):
        """Retrocede a la anterior marca de tiempo si puede."""
        try:
            self.tiempos.anterior()
        except StopIteration:
            return

    def backm(self,n):
        """Retrocede N marcas de tiempo hacia atras o las que pueda."""
        try:
            for x in range(n):
                self.tiempos.anterior()
        except StopIteration:
            return 

    def track_add(self,funcion,frecuencia,volumen):
        """Agrega un track con el sonido indicado."""
        if funcion.lower() not in self.FUNCIONES_DISPONIBLES:
            print('El sonido introducido no existe')
            return
        if volumen > 1 or volumen < 0:
            print('El volumen no puede tomar un valor mayor a uno ni ser menor que 0')
            return
        self.tracks.append(Track(funcion,frecuencia,volumen))

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
        self.tiempos.insert(self.tiempos.posicion_actual(),mark)
        print("posicion ",self.tiempos.posicion_actual())
        self.tiempos.actualizar(1)

    def mark_add_next(self,duracion):
        """Igual que MARKADD pero la inserta luego de la marca en la cual esta
        actualmente el cursor"""
        mark = MarcaDeTiempo(duracion)
        self.tiempos.insert(self.tiempos.posicion_actual() + 1,mark)
        self.tiempos.actualizar()

    def mark_add_prev(self,duracion):
        """Igual que MARKADD pero la inserta antes de la marca en la cual esta
        actualmente el cursor"""
        mark = MarcaDeTiempo(duracion)
        if self.tiempos.posicion_actual() == 0:
            print('No hay posición anterior para insertar una marca')
            return
        if not self.tiempos.prim:
            print('Debe insertar al menos una marca para utilizar esta funcion')
            return
        self.tiempos.insert(self.tiempos.posicion_actual() - 1, mark)
        self.tiempos.actualizar(1)

    def track_on(self,numero):
        """Habilita al track durante la marca de tiempo en la cual esta parada el
        cursor. Si el track no existe lanza IndexError"""
        track = self.tracks[numero] #Para levantar una excepcion si no existe el track
        print("va a trackon  ")
        print(self.tiempos.actual().obtener_habilitados())
        if not numero in self.tiempos.actual().obtener_habilitados():
            print("TRAOK  ",numero) 
            self.tiempos.actual().habilitar_track(numero)
        
    def track_off(self,numero):
        """Deshabilita al track durante la marca de tiempo en la cual esta parada el
        cursor. Si el track no estaba habilitado, no hace nada."""
        if numero in self.tiempos.actual().obtener_habilitados():
            self.tiempos.actual().deshabilitar_track(numero)
    
    def play(self):
        """Reproduce la marca en la que se encuentra el cursor actualmente."""
        self._reproducir(self.tiempos.actual())

    def play_all(self):
        """Reproduce la cancion completa desde el inicio."""
        self.tiempos.volver_al_inicio()
        for i in range (self.cant_tracks()):
            self._reproducir(self.tiempos.actual())
            if i != (self.cant_tracks() -1):
                self.tiempos.siguiente()

    def play_marks(self,n):
        """Reproduce las proximas n marcas desde la posicion actual del cursor."""
        try:
            for i in range(n):
                self._reproducir(self.tiempos.actual())
                self.tiempos.siguiente()
        except StopIteration:
            return 

    def play_seconds(self,segundos):
        """Reproduce los proximos segundos la posicion actual del cursor."""
        suma_duracion = 0
        while True:
            try:
                self._reproducir(self.tiempos.actual())
                suma_duracion += self.tiempos.actual().obtener_duracion()
                if suma_duracion >= segundos:
                    break
                self.tiempos.siguiente()
            except StopIteration:
                break
        
    def cant_tracks(self):
        """Obtiene la cantidad de tracks cargados"""
        return len(self.tracks)
        
    def _reproducir(self,mark):
        """Reproduce una marca de tiempo"""
        sp = pysounds.SoundPlayer(self.cant_tracks())
        duracion = mark.obtener_duracion()
        sonidos_a_reproducir = []
        for track_numero in mark.obtener_habilitados():
            track = self.tracks[track_numero]
            tipo = track.obtener_tipo()
            freq = track.obtener_frecuencia()
            vol = track.obtener_volumen()
            if tipo == "sine":
                sonidos_a_reproducir.append(pysounds.SoundFactory.get_sine_sound(freq,vol))
            if tipo == "triangular":
                sonidos_a_reproducir.append(pysounds.SoundFactory.get_triangular_sound(freq,vol))
            if tipo == "square":
                sonidos_a_reproducir.append(pysounds.SoundFactory.get_square_sound(freq,vol))
        sp.play_sounds(sonidos_a_reproducir, duracion)
