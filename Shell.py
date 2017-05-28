from Cancion import Cancion
import cmd

class Shell(cmd.Cmd):
    intro = "Bienvenido a mi Sounds of Cyber City.\n Ingrese help o ? para listar los comandos.\n"
    prompt = "*>> "
    cancion = Cancion()
    def do_COMANDO(self,parametros):
        """Este metodo ejecuta un comando"""
        print(self.cancion)
        print("COMANDO - Parametros: ",parametros)

Shell().cmdloop()
