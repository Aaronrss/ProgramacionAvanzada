// Libreria de entrada y salida de datos
#include <stdio.h>
// Libreria para el manejo de memoria
#include <stdlib.h>

// Definicion de la estructura de un elemento de la pila
struct nodo
{
  int valor;
  struct nodo *siguiente;
};

// Elemento que apunta al tope de la pila dinamica
struct nodo *tope = NULL;

// Verifica si la pila dinamica esta vacia
int pilaVacia()
{
  if (tope == NULL)
  {
    printf("La pila esta vacia\n");
    return 1;
  }
  else
    return 0;
}

// Nuevo elemento a la pila dinamica siguiendo el principio LIFO
void push(int numero)
{
  printf("Nuevo elemento en la pila: %d\n", numero);
  struct nodo *elemento = malloc(sizeof(struct nodo));
  if (elemento == NULL)
  {
    printf("No se puede crear un elemento en la pila");
    return;
  }
  elemento->valor = numero;
  elemento->siguiente = tope;
  tope = elemento;
}

// Borra un elemento de la pila dinamica
void pop()
{
  if (pilaVacia() == 1)
    return;
  else
  {
    struct nodo *temporal;
    temporal = tope;
    tope = tope->siguiente;
    printf("Eliminando de la pila: %d\n", temporal->valor);
    free(temporal);
  }
}

// Imprime todos los elementos de una pila dinamica
void mostrarElementosPila()
{
  int i = 0;
  struct nodo *temporal;
  temporal = tope;
  printf("Elementos en la pila:\n");
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
  printf("Uso de una pila de datos dinamica\n\n");
  printf("Operaciones \"push\"\n");
  push(1);
  push(2);
  push(3);
  push(4);
  mostrarElementosPila();
  printf("\n");
  printf("Operaciones \"pop\"\n");
  pop();
  pop();
  mostrarElementosPila();
  printf("\n");
  printf("Operaciones \"push\"\n");
  push(3);
  push(4);
  push(5);
  mostrarElementosPila();
}
