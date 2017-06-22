from Cancion import Cancion
from ListaEnlazada import ListaEnlazada,_IteradorListaEnlazada
import cmd

class Shell(cmd.Cmd):
    intro = "Bienvenido a Sounds of Cyber City.\n Ingrese help o ? para listar los comandos.\n"
    prompt = "Sounds of Cyber City: "
    cancion = Cancion()
    def do_LOAD(self,file):
        """Carga la cancion desde el archivo. Reemplaza la cancion en edicion
        actual si es que la hay."""
        print(load_cancion(file,self))
    def do_STORE(self,name):
        """Guarda la cancion"""
        if not name:
            print("Debe indicar el nombre")
            return
        self.cancion.store(name)
    def do_STEP(self,params=None):
        """Avanza a la siguiente marca de tiempo si la hay. Si no, no hace nada."""
        self.cancion.step()
    def do_STEPM(self,n):
        """Avanza N marcas de tiempo hacia adelante o las que pueda."""
        if not is_numeric(n):
            return
        self.cancion.stepm(int(n))
    def do_BACK(self,params=None):
        """Retrocede a la anterior marca de tiempo si puede."""
        self.cancion.back()
    def do_BACKM(self,n):
        """Retrocede N marcas de tiempo hacia atras o las que pueda."""
        if not is_numeric(n):
            return
        self.cancion.backm(int(n))
    def do_TRACKADD(self,params):
        """Agrega un track indicandole la funcion, la frecuencia y el volumen (separados por espacios)."""
        lista_parametros = params.split()
        if not len(lista_parametros) == 3:
            print("No ingreso los 3 parametros correctamente")
            return
        funcion,frecuencia,volumen = lista_parametros
        if not is_numeric(frecuencia) or not is_numeric(volumen):
            return
        if float(volumen) < 0 or 1 < float(volumen):
            print("El volumen debe estar comprendido entre 0 y 1")
            return
        try:
            self.cancion.track_add(funcion,int(frecuencia),float(volumen))
        except ValueError as e:
            print(e)
    def do_TRACKDEL(self,n):
        """Elimina un track por numero"""
        if not is_numeric(n):
            return
        try:
            self.cancion.track_del(int(n))
        except IndexError:
            print('Este track no se encuentra en la canción')
    def do_MARKADD(self,duracion):
        """Agrega una marca de tiempo de la duracion indicada."""
        if not is_numeric(duracion):
            return
        self.cancion.mark_add(float(duracion))
    def do_MARKADDNEXT(self,duracion):
        """Agrega una marca de tiempo de la duracion indicada en la posicion siguente"""
        if not is_numeric(duracion):
            return
        self.cancion.mark_add_next(float(duracion))
    def do_MARKADDPREV(self,duracion):
        """Agrega una marca de tiempo de la duracion indicada en la posicion anterior"""
        if not is_numeric(duracion):
            return
        self.cancion.mark_add_prev(float(duracion))
    def do_TRACKON(self,n):
        """Habilita al track durante la marca de tiempo actual"""
        if not is_numeric(n):
            return
        try:
            self.cancion.track_on(int(n))
        except IndexError:
            print('No existe tal track en la canción')
        except AttributeError:
            print("No hay marca")
    def do_TRACKOFF(self,n):
        """Desabilita al track durante la marca de tiempo actual"""
        if not is_numeric(n):
            return
        self.cancion.track_off(int(n))
    def do_PLAY(self,params=None):
        """Reproduce la marca actual."""
        self.cancion.play()
    def do_PLAYALL(self,params=None):
        """Reproduce la cancion completa desde el inicio."""
        self.cancion.play_all()
    def do_PLAYMARKS(self,n):
        """Reproduce las proximas n marcas desde la posicion actual."""
        if not is_numeric(n):
            return
        self.cancion.play_marks(int(n))
    def do_PLAYSECONDS(self,n):
        """Reproduce los proximos segundos desde la posicion actual."""
        if not is_numeric(n):
            return
        self.cancion.play_seconds(int(n))
    def actualizar_cancion(self,cancion):
        """Actualiza la cancion de la Shell"""
        self.cancion = cancion

def is_numeric(cadena):
    """ Devuelve True si recibe una cadena numerica, False en otro caso. Imprime un mensaje de error si no recibe un numero"""
    if not cadena.replace('.','').isdigit():
        print("Ha ingresado un parametro incorrectamente")
        return False
    return True

def load_cancion(file,shell=None):
    """Carga la cancion desde el archivo. Reemplaza la cancion en edicion
    actual si es que la hay.
    Parametros:
        file (string) Debe tener el nombre del archivo junto con su extencion (.plp)
        shell (object) Objeto de la clase Shell para actualizar la cancion"""
    cancion = Cancion()
    primer_marca = True
    try:
        with open(file,"r") as f:
            for linea in f:
                campo,valor = linea.rstrip("\n").split(",")
                if campo == "S":
                    funcion,frecuencia,volumen = valor.split("|")
                    cancion.track_add(funcion,int(frecuencia),float(volumen))
                elif campo == "T":
                    duracion = float(valor)
                elif campo == "N":
                    #Siempre hay un tipo 'T' antes, donde se define duracion
                    if primer_marca:
                        cancion.mark_add(duracion)
                    else:
                        cancion.mark_add_next(duracion)
                    primer_marca = False
                    cancion.step()
                    for posicion,caracter in enumerate(valor):
                        if caracter == "#":
                            cancion.track_on(posicion)
    except IOError as e:
        return "I/O error({0}): {1}".format(e.errno, e.strerror)
    if shell:
        shell.actualizar_cancion(cancion) # Actualizamos el atributo del objeto shell
    return "Cancion cargada con exito"

Shell().cmdloop()
