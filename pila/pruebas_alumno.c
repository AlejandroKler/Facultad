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
	print_test("Ver tope 1", pila_ver_tope(pila) == NULL);
	print_test("Desapilar 1",pila_desapilar(pila) == NULL);
	print_test("Apilar 1",pila_apilar(pila,&uno) );
	//print_test("Redimension 1",(int)pila->capacidad == 2 );
	print_test("Apilar 2",pila_apilar(pila,&dos));
	//print_test("Redimension 2",(int)pila->capacidad == 2 );
	print_test("Apilar 3",pila_apilar(pila,&tres));
	void* test = pila_ver_tope(pila);
	print_test("Ver tope 2", test == 3);
	//print_test("Redimension 3",(int)pila->capacidad == 4 );
	/*print_test("Apilar 4",pila_apilar(pila,&cuatro));
	//print_test("Redimension 4",(int)pila->capacidad == 8 );
	print_test("Apilar 5",pila_apilar(pila,&cinco));
	print_test("Ver tope 3",pila_ver_tope(pila) == 5);
	print_test("Apilar 6",pila_apilar(pila,&seis));
	print_test("Apilar 7",pila_apilar(pila,&siete));
	print_test("Apilar 8",pila_apilar(pila,&ocho));
	print_test("Apilar 9",pila_apilar(pila,&nueve));
	//print_test("Redimension 5",(int)pila->capacidad* == 8 );
	print_test("Desapilar 2",pila_desapilar(pila) == 9);
	print_test("Desapilar 3",pila_desapilar(pila) == 8);
	print_test("Desapilar 4",pila_desapilar(pila) == 7);
	print_test("Ver tope 4",pila_ver_tope(pila) == 6);
	print_test("Desapilar 5",pila_desapilar(pila) == 6);
	print_test("Desapilar 1",pila_desapilar(pila) == 5);
	print_test("Ver tope 5",pila_ver_tope(pila) == 4);
	print_test("Desapilar 6",pila_desapilar(pila) == 4);
	print_test("Desapilar 7",pila_desapilar(pila) == 3);
	//print_test("Redimension 6",(int)pila->capacidad == 8 );
	print_test("Desapilar 8",pila_desapilar(pila) == 2);
	//print_test("Redimension 7",(int)pila->capacidad == 4 );
	print_test("Desapilar 9",pila_desapilar(pila) == 1);
	print_test("Desapilar 10",pila_desapilar(pila) == NULL);
	//print_test("Redimension 8",(int)pila->capacidad == 2 );
	print_test("Desapilar 11",pila_desapilar(pila) == NULL);
	print_test("Ver tope 6", pila_ver_tope(pila) == NULL);*/
	pila_destruir(pila);
}
