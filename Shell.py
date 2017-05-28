from Cancion import Cancion
from ListaEnlazada import ListaEnlazada
import cmd

class Shell(cmd.Cmd):
    intro = "Bienvenido a mi Sounds of Cyber City.\n Ingrese help o ? para listar los comandos.\n"
    prompt = "*>> "
    cancion = Cancion()
    def do_LOAD(self,file):
        self.cancion.load(file)
    def do_STORE(self):
        self.cancion.store()
    def do_STEP(self):
        self.cancion.step(file)
    def do_STEPM(self,n):
        self.cancion.stepm(n)
    def do_BACK(self):
        self.cancion.back()
    def do_BACKM(self,n):
        self.cancion.load(n)
    def do_TRACKADD(self,funcion,frecuencia,volumen):
        self.cancion.track_add(funcion,frecuencia,volumen)
    def do_TRACKDEL(self,n):
        self.cancion.track_del(n)
    def do_MARKADD(self,duracion):
        self.cancion.mark_add(duracion)
    def do_MARKADDNEXT(self,duracion):
        self.cancion.mark_add_next(duracion)
    def do_MARKADDPREV(self,duracion):
        self.cancion.mark_add_PREV(duracion)
    def do_TRACKON(self,n):
        self.cancion.track_on(n)
    def do_TRACKOFF(self,n):
        self.cancion.track_off(n)
    def do_PLAY(self):
        self.cancion.play()
    def do_PLAYALL(self):
        self.cancion.play_all()
    def do_PLAYMARKS(self,n):
        self.cancion.play_marks(n)
    def do_PLAYSECONDS(self,n):
        self.cancion.play_seconds(n)

Shell().cmdloop()
