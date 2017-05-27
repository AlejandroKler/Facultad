from Cancion import Cancion
from ListaEnlazada.py import ListaEnlazada
from MarcaDeTiempo.py import MarcaDeTiempo


def main(Cancion=None,posicion=None):
	if not Cancion:
		Cancion = Cancion()
	iterador = iter(Cancion.tiempos)
	while True:
		try:
			get_comand()
			MarcaDeTiempo = next(iterador)
			print(MarcaDeTiempo)
		except StopIteration:
			main(Cancion,posicion)
