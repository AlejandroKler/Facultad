#include "pila.h"
#include "testing.h"
#include <stddef.h>


/* ******************************************************************
 *                   PRUEBAS UNITARIAS ALUMNO
 * *****************************************************************/

void pruebas_pila_alumno() {
	pila_t* pila = pila_crear();
	int uno = 1;
	int dos = 2;
	int tres = 3;
	int cuatro = 4;
	int cinco = 5;
	int seis = 6;
	int siete = 7;
	int ocho = 8;
	int nueve = 9;
	int* puntero_uno = &uno;
	int* puntero_dos = &dos;
	int* puntero_tres = &tres;
	int* puntero_cuatro = &cuatro;
	int* puntero_cinco = &cinco;
	int* puntero_seis = &seis;
	int* puntero_siete = &siete;
	int* puntero_ocho = &ocho;
	int* puntero_nueve = &nueve;
	print_test("Ver tope 1", pila_ver_tope(pila) == NULL);
	print_test("Desapilar 1",pila_desapilar(pila) == NULL);
	print_test("Apilar 1",pila_apilar(pila,puntero_uno) );
	print_test("Redimension 1",(int)pila->capacidad == 2 );
	print_test("Apilar 2",pila_apilar(pila,puntero_dos));
	print_test("Redimension 2",(int)pila->capacidad == 2 );
	print_test("Apilar 3",pila_apilar(pila,puntero_tres));
	print_test("Ver tope 2", pila_ver_tope(pila) == 3);
	print_test("Redimension 3",(int)pila->capacidad == 4 );
	print_test("Apilar 4",pila_apilar(pila,puntero_cuatro));
	print_test("Redimension 4",(int)pila->capacidad == 8 );
	print_test("Apilar 5",pila_apilar(pila,puntero_cinco));
	print_test("Ver tope 3",pila_ver_tope(pila) == 5);
	print_test("Apilar 6",pila_apilar(pila,puntero_seis));
	print_test("Apilar 7",pila_apilar(pila,puntero_siete));
	print_test("Apilar 8",pila_apilar(pila,puntero_ocho));
	print_test("Apilar 9",pila_apilar(pila,puntero_nueve));
	print_test("Redimension 5",(int)pila->capacidad* == 8 );
	print_test("Desapilar 2",pila_desapilar(pila) == puntero_nueve);
	print_test("Desapilar 3",pila_desapilar(pila) == puntero_ocho);
	print_test("Desapilar 4",pila_desapilar(pila) == puntero_siete);
	print_test("Ver tope 4",pila_ver_tope(pila) == puntero_seis);
	print_test("Desapilar 5",pila_desapilar(pila) == puntero_seis);
	print_test("Desapilar 1",pila_desapilar(pila) == puntero_cinco);
	print_test("Ver tope 5",pila_ver_tope(pila) == puntero_cuatro);
	print_test("Desapilar 6",pila_desapilar(pila) == puntero_cuatro);
	print_test("Desapilar 7",pila_desapilar(pila) == puntero_tres);
	print_test("Redimension 6",(int)pila->capacidad == 8 );
	print_test("Desapilar 8",pila_desapilar(pila) == puntero_dos);
	print_test("Redimension 7",(int)pila->capacidad == 4 );
	print_test("Desapilar 9",pila_desapilar(pila) == puntero_dos);
	print_test("Desapilar 10",pila_desapilar(pila) == NULL);
	print_test("Redimension 8",(int)pila->capacidad == 2 );
	print_test("Desapilar 11",pila_desapilar(pila) == NULL);
	print_test("Ver tope 6", pila_ver_tope(pila) == NULL);
	pila_destruir(pila);
}
