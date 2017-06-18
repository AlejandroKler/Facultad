from Shell import Shell

def load(file,shell=None):
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
                    cancion.track_add(funcion,frecuencia,volumen)
                elif campo == "T":
                    duracion = float(valor)
                elif campo == "N":
                    cancion.mark_add(duracion)
                    posicion = 0
                    for caracter in valor:
                        if caracter == "#":
                            cancion.track_on(posicion)
                        posicion += 1
    except IOError as e:
        return "I/O error({0}): {1}".format(e.errno, e.strerror)
    if shell:
        shell.actualizar_cancion(cancion) # Actualizamos el atributo del objeto shell
    return "Cancion cargada con exito"

Shell().cmdloop()
