from Cancion import Cancion
from ListaEnlazada import ListaEnlazada,_IteradorListaEnlazada
import cmd

class Shell(cmd.Cmd):
    intro = "Bienvenido a Sounds of Cyber City.\n Ingrese help o ? para listar los comandos.\n"
    prompt = "*>> "
    cancion = Cancion()
    def do_LOAD(self,file):
        load_cancion(file,self)
    def do_STORE(self,name):
        try:
            self.cancion.store(name)
        except ValueError as e:
            print(e.strerror)
    def do_STEP(self,params=None):
        self.cancion.step()
    def do_STEPM(self,n):
        self.cancion.stepm(convert_num(n))
    def do_BACK(self,params=None):
        self.cancion.back()
    def do_BACKM(self,n):
        self.cancion.load(n)
    def do_TRACKADD(self,params):
        lista_parametros = params.split()
        if not len(lista_parametros) == 3:
            print("No ingreso los 3 parametros correctamente")
            return
        funcion,frecuencia,volumen = lista_parametros
        self.cancion.track_add(funcion,convert_num(frecuencia),convert_num(volumen,True))
    def do_TRACKDEL(self,n):
        self.cancion.track_del(convert_num(n))
    def do_MARKADD(self,duracion):
        self.cancion.mark_add(convert_num(duracion,True))
    def do_MARKADDNEXT(self,duracion):
        self.cancion.mark_add_next(convert_num(duracion,True))
    def do_MARKADDPREV(self,duracion):
        self.cancion.mark_add_PREV(convert_num(duracion,True))
    def do_TRACKON(self,n):
        try:
            self.cancion.track_on(convert_num(n))
        except IndexError:
            print('No existe tal track en la canción')
    def do_TRACKOFF(self,n):
        self.cancion.track_off(convert_num(n))
    def do_PLAY(self,params=None):
        self.cancion.play()
    def do_PLAYALL(self,params=None):
        self.cancion.play_all()
    def do_PLAYMARKS(self,n):
        self.cancion.play_marks(convert_num(n))
    def do_PLAYSECONDS(self,n):
        self.cancion.play_seconds(convert_num(n))
    def actualizar_cancion(self,cancion):
        self.cancion = cancion

def convert_num(cadena,isfloat=False):
    """ Convierte una cadena en un int o float segun corresponda. Imprime un mensaje de error si no recibe un numero"""
    if not cadena.replace('.','').isdigit():
        print("Ha ingresado un parametro incorrectamente")
        return
    if isfloat:
        return float(cadena)
    return int(cadena)

def load_cancion(file,shell=None):
    """Carga la cancion desde el archivo. Reemplaza la cancion en edicion
    actual si es que la hay.
    Parametros:
        file (string) Debe tener el nombre del archivo junto con su extencion (.plp)
        shell (object) Objeto de la clase Shell para actualizar la cancion"""
    cancion = Cancion()
    try:
        with open(file,"r") as f:
            for linea in f:
                campo,valor = linea.rstrip("\n").split(",")
                if campo == "S":
                    funcion,frecuencia,volumen = valor.split("|")
                    cancion.track_add(funcion,convert_num(frecuencia),convert_num(volumen,True))
                elif campo == "T":
                    duracion = float(valor)
                elif campo == "N":
                    cancion.mark_add_next(duracion) #Siempre hay un tipo 'T' antes, donde se define duracion
                    for posicion,caracter in enumerate(valor):
                        if caracter == "#":
                            cancion.track_on(posicion)
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        return
    if shell:
        shell.actualizar_cancion(cancion) # Actualizamos el atributo del objeto shell
    print("Cancion cargada con exito")

Shell().cmdloop()
