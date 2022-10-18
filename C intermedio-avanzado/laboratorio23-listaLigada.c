// Libreria de entrada y salida de datos
#include <stdio.h>
// Libreria para el manejo de memoria
#include <stdlib.h>

// Definicion de la estructura de un nodo en la lista
struct nodo
{
	int valor;
	struct nodo *siguiente;
};

// Elemento que apunta a la parte inicial de la lista
struct nodo *indice = NULL;

// Verifica si la lista esta vacia
int listaVacia()
{
	if (indice == NULL)
		return 1;
	else
		return 0;
}

// Devuelve la longitud de una lista
void longitudLista()
{
	struct nodo *temporal;
	int longitud;
	temporal = indice;
	while (temporal != NULL)
	{
		longitud++;
		temporal = temporal->siguiente;
	}
	printf("Longitud de la lista: %d\n", longitud);
}

// Inserta un elemento al final de una lista
void insertaFinalLista(int numero)
{
	printf("Nuevo elemento en el final de la lista: %d \n", numero);
	struct nodo *elemento = malloc(sizeof(struct nodo));
	if (elemento == NULL)
	{
		printf("No se puede crear un elemento en la lista");
		return;
	}
	if (listaVacia() == 1)
	{
		elemento->valor = numero;
		elemento->siguiente = indice;
		indice = elemento;
		return;
	}
	struct nodo *indiceActual = indice;
	struct nodo *indiceAnterior = NULL;
	while (indiceActual != NULL)
	{
		indiceAnterior = indiceActual;
		indiceActual = indiceActual->siguiente;
	}
	elemento->valor = numero;
	elemento->siguiente = NULL;
	indiceAnterior->siguiente = elemento;
}

// Eliminar un elemento de la lista
void eliminaLista(int numero)
{
	if (listaVacia() == 1)
	{
		printf("La lista esta vacia\n");
		return;
	}
	struct nodo *indiceActual = indice;
	struct nodo *indiceAnterior = NULL;
	struct nodo *temporal;
	// recorrer la lista
	while (indiceActual != NULL)
	{
		if (indiceActual->valor == numero)
		{
			// primer elemento en la lista
			if (indiceAnterior == NULL)
			{
				temporal = indiceActual;
				indice = indiceActual->siguiente;
				printf("Eliminando: %d\n", temporal->valor);
				free(temporal);
				return;
			}
			// elemento a eliminar va en medio o al final
			else
			{
				temporal = indiceActual;
				printf("Eliminando: %d\n", temporal->valor);
				indiceAnterior->siguiente = indiceActual->siguiente;
				free(temporal);
				return;
			}
		}
		indiceAnterior = indiceActual;
		printf("%d\n", indiceActual->valor);
		indiceActual = indiceActual->siguiente;
	}
	printf("Elemento: %d no se puede eliminar\n", numero);
}

// Imprime todos los elementos de una pila dinamica
void mostrarElementosLista()
{
	int i = 0;
	struct nodo *temporal;
	temporal = indice;
	printf("Elementos en la lista:\n");
	while (temporal != NULL)
	{
		printf("Elemento[%d]=%d\n", i, temporal->valor);
		temporal = temporal->siguiente;
		i++;
	}
}

// Programa principal
int main()
{
	printf("Uso de una lista de datos dinamica\n\n");
	printf("Operaciones \"insercion\"\n");
	insertaFinalLista(1);
	insertaFinalLista(2);
	insertaFinalLista(3);
	insertaFinalLista(4);
	insertaFinalLista(5);
	mostrarElementosLista();
	printf("\n");
	printf("Operacion \"longitud\"\n");
	longitudLista();
	printf("\n");
	printf("Operacion \"eliminar\"\n");
	eliminaLista(2);
	eliminaLista(4);
	eliminaLista(5);

	eliminaLista(2);
	eliminaLista(4);
	eliminaLista(5);

	mostrarElementosLista();
}
