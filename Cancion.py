from ListaEnlazada import ListaEnlazada
from ListaEnlazada import _IteradorListaEnlazada
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
        self.tiempos.insert(self.cursor.posicion,mark)
        self.mover_cursor(1)

    def mark_add_next(self,duracion):
        """Igual que MARKADD pero la inserta luego de la marca en la cual esta
        actualmente el cursor"""
        mark = MarcaDeTiempo(duracion)
        self.tiempos.insert(self.cursor.posicion + 1,mark)
        self.mover_cursor(1)

    def mark_add_prev(self,duracion):
        """Igual que MARKADD pero la inserta antes de la marca en la cual esta
        actualmente el cursor"""
        mark = MarcaDeTiempo(duracion)
        self.tiempos.insert(self.cursor.posicion - 1, mark)
        self.mover_cursor(1)

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

    def mover_cursor(self,n=0):
        """ Genera una nueva instancia del iterador y mueve el cursor.
        Recibe un parametro n que indica el desplazamiento con repecto a la posicion original"""
        posicion_cursor = self.cursor.posicion
        self.cursor = _IteradorListaEnlazada(self.tiempos.prim)
        for i in range(0 , posicion_cursor + n):
            self.cursor.next()
