// Libreria de entrada y salida de datos
#include <stdio.h>
// Libreria para el manejo de memoria
#include <stdlib.h>

// Definicion de la estructura de un nodo en la lista
struct nodo
{
	int valor;
	struct nodo *siguiente;
	struct nodo *anterior;
};

// Elemento que apunta a la parte inicial de la lista
struct nodo *inicio = NULL;
// Elemento que apunta a la parte final de la lista
struct nodo *fin = NULL;

// Verifica si la lista esta vacia
int listaVacia()
{
	if (inicio == NULL)
		return 1;
	else
		return 0;
}

// Devuelve la longitud de una lista
int longitudLista()
{
	struct nodo *temporal;
	int longitud;
	temporal = inicio;
	while (temporal != NULL)
	{
		longitud++;
		temporal = temporal->siguiente;
	}
	return longitud;
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
		elemento->anterior = NULL;
		elemento->siguiente = NULL;
		inicio = elemento;
		fin = elemento;
	}
	else
	{
		elemento->valor = numero;
		elemento->siguiente = NULL;
		elemento->anterior = fin;
		fin->siguiente = elemento;
		fin = elemento;
	}
}
// Inserta un elemento al inicio de una lista
void insertaInicioLista(int numero)
{
	printf("Nuevo elemento en el inicio de la lista: %d \n", numero);
	struct nodo *elemento = malloc(sizeof(struct nodo));
	if (elemento == NULL)
	{
		printf("No se puede crear un elemento en la lista");
		return;
	}
	if (listaVacia() == 1)
	{
		elemento->valor = numero;
		elemento->anterior = NULL;
		elemento->siguiente = NULL;
		inicio = elemento;
		fin = elemento;
	}
	else
	{
		inicio->anterior = elemento;
		elemento->valor = numero;
		elemento->siguiente = inicio;
		elemento->anterior = NULL;
		inicio = elemento;
	}
}

// Eliminar un elemento de la lista
void eliminaLista(int numero)
{
	if (listaVacia() == 1)
	{
		printf("La lista esta vacia\n");
		return;
	}
	struct nodo *indiceAnterior = NULL;
	struct nodo *indiceActual = inicio;
	struct nodo *indiceSiguiente = inicio->siguiente;
	struct nodo *temporal;
	// recorrer la lista
	while (indiceActual != NULL)
	{
		if (indiceActual->valor == numero)
		{
			// primer elemento en la lista
			if (indiceAnterior == NULL && indiceSiguiente == NULL)
			{
				temporal = indiceActual;
				inicio = indiceActual->siguiente;
				inicio->anterior = NULL;
				printf("Eliminando: %d\n", temporal->valor);
				free(temporal);
				return;
			}
			// elemento a eliminar va en medio o al final
			else
			{
				temporal = indiceActual;
				printf("Eliminando: %d\n", temporal->valor);
				if (indiceActual == fin)
				{
					indiceAnterior->siguiente = NULL;
					fin = indiceAnterior;
				}
				else
				{
					indiceAnterior->siguiente = indiceSiguiente;
					indiceSiguiente->anterior = indiceAnterior;
				}

				free(temporal);
				return;
			}
		}
		indiceAnterior = indiceActual;
		indiceActual = indiceActual->siguiente;
		indiceSiguiente = indiceSiguiente->siguiente;
	}
	printf("Elemento: %d no se puede eliminar\n", numero);
}

// Imprime todos los elementos de una lista desde el inicio
void mostrarElementosListaInicio()
{
	int i = 0;
	struct nodo *temporal;
	temporal = inicio;
	printf("Elementos en la lista:\n");
	while (temporal != NULL)
	{
		printf("Elemento[%d]=%d\n", i, temporal->valor);
		temporal = temporal->siguiente;
		i++;
	}
}

// Imprime todos los elementos de una lista desde el fin
void mostrarElementosListaFin()
{
	int i = longitudLista();
	struct nodo *temporal;
	temporal = fin;
	printf("Elementos en la lista:\n");
	while (temporal != NULL)
	{
		printf("Elemento[%d]=%d\n", i, temporal->valor);
		temporal = temporal->anterior;
		i--;
	}
}

// Programa principal
int main()
{
	printf("Uso de una lista doblemente ligada\n\n");
	printf("Operaciones \"insercion al final\"\n");
	insertaFinalLista(4);
	insertaFinalLista(5);
	insertaFinalLista(6);
	printf("\n");
	printf("Operaciones \"insercion al inicio\"\n");
	insertaInicioLista(1);
	insertaInicioLista(2);
	insertaInicioLista(3);
	printf("\n");
	printf("Operaciones \"eliminar\"\n");
	eliminaLista(6);
	eliminaLista(5);
	eliminaLista(4);
	printf("\n");
	printf("Operacion \"mostrar desde inicio\"\n");
	mostrarElementosListaInicio();
	printf("\n");
	printf("Operacion \"mostrar desde final\"\n");
	mostrarElementosListaFin();
	printf("\n");
}
