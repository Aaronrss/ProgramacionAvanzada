// Libreria de entrada y salida de datos
#include <stdio.h>
// Libreria para el manejo de memoria
#include <stdlib.h>

// Definicion de la estructura de un elemento de la cola
struct nodo
{
  int valor;
  struct nodo *siguiente;
};

/*Elemento que apunta a la parte delatenta y
trasera de la cola dinamica*/
struct nodo *frente = NULL;
struct nodo *atras = NULL;

// Verifica si la cola dinamica esta vacia
int colaVacia()
{
  if (frente == NULL)
    return 1;
  else
    return 0;
}

/* Nuevo elemento en la cola dinamica
siguiendo el principio FIFO*/

void queue(int numero)
{
  printf("Nuevo elemento en la cola: %d\n", numero);
  struct nodo *elemento = malloc(sizeof(struct nodo));
  if (elemento == NULL)
  {
    printf("No se puede crear un elemento en la cola");
    return;
  }
  elemento->valor = numero;
  elemento->siguiente = NULL;
  if (colaVacia() == 1)
  {
    frente = elemento;
    atras = elemento;
  }
  else
  {
    atras->siguiente = elemento;
    atras = elemento;
  }
}

// Borra un elemento de la cola dinamica

void dequeue()
{
  if (colaVacia() == 1)
  {
    printf("La cola esta vacia\n");
    return;
  }
  else
  {
    struct nodo *temporal;
    temporal = frente;
    if (frente == atras)
    {
      frente = NULL;
      atras = NULL;
    }
    else
      frente = frente->siguiente;
    printf("Eliminando de la cola: %d\n", temporal->valor);
    free(temporal);
  }
}

// Imprime todos los elementos de una pila dinamica

void mostrarElementosCola()
{
  int i = 0;
  struct nodo *temporal;
  temporal = frente;
  printf("Elementos en la cola:\n");
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
  printf("Uso de una cola de datos dinamica\n\n");
  printf("Operaciones \"queue\"\n");
  queue(1);
  queue(2);
  queue(3);
  queue(4);
  mostrarElementosCola();
  printf("\n");
  printf("Operaciones \"dequeue\"\n");
  dequeue();
  dequeue();
  mostrarElementosCola();
  printf("\n");
  printf("Operaciones \"queue\"\n");
  queue(3);
  queue(4);
  queue(5);
  mostrarElementosCola();
}
