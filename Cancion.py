from ListaEnlazada import ListaEnlazada
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
        if self.tiempos.esta_vacia():
            return
        self.tiempos.volver_al_inicio()
        with open(name + ".plp","w") as f:
            f.write("C,"+str(self.cant_tracks())+"\n")
            for track in self.tracks:
                f.write("S,{}|{}|{}\n".format(track.obtener_tipo(),track.obtener_frecuencia(),track.obtener_volumen()))
            anterior = None
            MarcaDeTiempo = self.tiempos.actual()
            while True:
                try:
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
            
    def stepm(self,numero):
        """Avanza N marcas de tiempo hacia adelante o las que pueda.
        Parametros:
            numero (int) Numero de marcas a avanzar"""
        try:
            for x in range(numero):
                self.tiempos.siguiente()
        except StopIteration:
            return
            
    def back(self):
        """Retrocede a la anterior marca de tiempo si puede."""
        try:
            self.tiempos.anterior()
        except StopIteration:
            return

    def backm(self,numero):
        """Retrocede N marcas de tiempo hacia atras o las que pueda.
        Parametros:
            numero (int) Numero de marcas a retroceder"""
        try:
            for x in range(numero):
                self.tiempos.anterior()
        except StopIteration:
            return 

    def track_add(self,funcion,frecuencia,volumen):
        """Agrega un track con el sonido indicado.
        Parametros:
            funcion (string) nombre de la funcion
            frecuencia (int) frecuencia de onda
            volumen (float) volumen del sonido comprendido entre 0 y 1"""
        if funcion.lower() not in self.FUNCIONES_DISPONIBLES:
            raise ValueError('El sonido introducido no existe')
        self.tracks.append(Track(funcion,int(frecuencia),float(volumen)))

    def track_del(self,posicion):
        """Elimina un track por numero. Levanta un IndexError si no esta habilitado.
        Parametros:
            posicion (int) Posicion a quitar"""
        self.tracks.pop(posicion)

    def mark_add(self,duracion):
        """Agrega una marca de tiempo de la duracion indicada. Originalmente
        todos los tracks estan deshabilitados
        Parametros:
            duracion (float) duracion de la marca de tiempo"""
        mark = MarcaDeTiempo(duracion)
        self.tiempos.insert(self.tiempos.posicion_actual(),mark)
        self.tiempos.actualizar()

    def mark_add_next(self,duracion):
        """Igual que MARKADD pero la inserta luego de la marca en la cual esta
        actualmente el cursor
        Parametros:
            duracion (float) duracion de la marca de tiempo"""
        mark = MarcaDeTiempo(duracion)
        self.tiempos.insert(self.tiempos.posicion_actual()+1,mark)
        self.tiempos.actualizar()

    def mark_add_prev(self,duracion):
        """Igual que MARKADD pero la inserta antes de la marca en la cual esta
        actualmente el cursor
        Parametros:
            duracion (float) duracion de la marca de tiempo"""
        if not self.tiempos.posicion_actual():
            self.mark_add(duracion) # Si se encuentra en la posicion inicial no hay marca previa
            return
        mark = MarcaDeTiempo(duracion)
        self.tiempos.insert(self.tiempos.posicion_actual()-1, mark)
        self.tiempos.actualizar()

    def track_on(self,numero):
        """Habilita al track durante la marca de tiempo en la cual esta parada el
        cursor. Si el track no existe lanza IndexError. Si no hay marca levanta AttributeError.
        Parametros:
            numero (int) Numero de track (o posicion)"""
        track = self.tracks[numero] #Para levantar una excepcion si no existe el track
        if not numero in self.tiempos.actual().obtener_habilitados():
            self.tiempos.actual().habilitar_track(numero)
        
    def track_off(self,numero):
        """Deshabilita al track durante la marca de tiempo en la cual esta parada el
        cursor. Si el track no estaba habilitado, no hace nada. Si no hay marca levanta AttributeError.
        Parametros:
            numero (int) Numero de track (o posicion)"""
        if numero in self.tiempos.actual().obtener_habilitados():
            self.tiempos.actual().deshabilitar_track(numero)
    
    def play(self):
        """Reproduce la marca en la que se encuentra el cursor actualmente."""
        if not self.tiempos.esta_vacia():
            self._reproducir(self.tiempos.actual())

    def play_all(self):
        """Reproduce la cancion completa desde el inicio. Y vuelve a la posicion actual."""
        posicion_actual = self.tiempos.posicion_actual()
        self.tiempos.volver_al_inicio()
        while True:
            try:
                if not self.tiempos.esta_vacia():
                    self._reproducir(self.tiempos.actual())
                self.tiempos.siguiente()
            except StopIteration:
                self.tiempos.volver_al_inicio()
                self.tiempos.actualizar(posicion_actual)

    def play_marks(self,numero):
        """Reproduce las proximas n marcas desde la posicion actual del cursor. Y vuelve a la posicion actual.
        Parametros:
            numero (int) Numero de marcas a reproducir"""
        posicion_actual = self.tiempos.posicion_actual()
        try:
            for i in range(numero):
                if not self.tiempos.esta_vacia():
                    self._reproducir(self.tiempos.actual())
                self.tiempos.siguiente()
        except StopIteration:
            self.tiempos.volver_al_inicio()
            self.tiempos.actualizar(posicion_actual) 

    def play_seconds(self,segundos):
        """Reproduce los proximos segundos la posicion actual del cursor. Y vuelve a la posicion actual.
        Parametros:
            segundos (int) Segundos de marcas a reproducir"""
        suma_duracion = 0
        posicion_actual = self.tiempos.posicion_actual()
        while True:
            try:
                if not self.tiempos.esta_vacia():
                    self._reproducir(self.tiempos.actual())
                suma_duracion += self.tiempos.actual().obtener_duracion()
                if suma_duracion >= segundos:
                    break
                self.tiempos.siguiente()
            except StopIteration:
                self.tiempos.volver_al_inicio()
                self.tiempos.actualizar(posicion_actual)
        
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
