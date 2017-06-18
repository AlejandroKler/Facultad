from Shell import Shell

def load(file,shell=None):
    """Carga la cancion desde el archivo. Reemplaza la cancion en edicion
    actual si es que la hay.
    Parametros:
        file (string) Debe tente el nombre del archivo junto con su extencion (.plp)"""
    cancion = Cancion()
    try:
        with open(file,"r") as f:
            for linea in f:
                campo,valor = linea.rstrip("\n").split(",")
                if campo == "S":
                    funcion,frecuencia,volumen = valor.split("|")
                    cancion.track_add(funcion,frecuencia,volumen)
                if campo == "T":
                    duracion = valor
                if campo == "N":
                    cancion.mark_add(duracion)
                    posicion = 0
                    for caracter in valor:
                        if caracter == "#":
                            cancion.track_on(posicion)
                        posicion += 1
    except IOError as e:
        return "I/O error({0}): {1}".format(e.errno, e.strerror)
    if shell:
        shell.cancion = cancion # Actualizamos el atributo del objeto shell
    return "Cancion cargada con exito"

Shell().cmdloop()
