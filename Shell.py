from Cancion import Cancion
from ListaEnlazada import ListaEnlazada,_IteradorListaEnlazada
import cmd

def convert_num(cadena,isfloat=False):
    """ Convierte una cadena en un int o float segun corresponda. Imprime un mensaje de error si no recibe un numero"""
    if not cadena.isdigit():
        print("Ha ingresado un parametro incorrectamente")
        return
    if isfloat:
        return float(cadena)
    return int(cadena)

class Shell(cmd.Cmd):
    intro = "Bienvenido a Sounds of Cyber City.\n Ingrese help o ? para listar los comandos.\n"
    prompt = "*>> "
    cancion = Cancion()
    def do_LOAD(self,file):
        print(load(file,self))
    def do_STORE(self,name):
        self.cancion.store(name)
    def do_STEP(self,params=None):
        self.cancion.step()
    def do_STEPM(self,n):
        self.cancion.stepm(convert_num(n))
    def do_BACK(self,params=None):
        self.cancion.back()
    def do_BACKM(self,n):
        self.cancion.load(n)
    def do_TRACKADD(self,params):
        funcion,frecuencia,volumen = params.split()
        self.cancion.track_add(funcion,convert_num(frecuencia),convert_num(volumen,True))
    def do_TRACKDEL(self,n):
        self.cancion.track_del(convert_num(n))
    def do_MARKADD(self,duracion):
        self.cancion.mark_add(convert_num(duracion))
    def do_MARKADDNEXT(self,duracion):
        self.cancion.mark_add_next(convert_num(duracion))
    def do_MARKADDPREV(self,duracion):
        self.cancion.mark_add_PREV(convert_num(duracion))
    def do_TRACKON(self,n):
        self.cancion.track_on(convert_num(n))
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
