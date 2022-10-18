//Libreria de entrada y salida de datos
#include<stdio.h>

//Maximo numero de elementos de una pila 
#define MAXIMO 5

// Definicion de la estructura de la pila
struct pila {
   int valores[MAXIMO];
   int tope;
};

// Inicializacion de una pila
void inicializarPila(struct pila *instancia) {
   instancia->tope = -1;
}


//Verifica si la pila esta llena
int pilaLlena(struct pila *instancia) 
{
   if(instancia->tope == MAXIMO-1){
   	  printf("La pila esta llena\n");
   	  return 1;
   } 
   else
      return 0;
}

//Verifica si la pila esta vacia
int pilaVacia(struct pila *instancia) 
{
   if(instancia->tope == -1){
   	  printf("La pila esta vacia\n");
      return 1;
   }  
   else
      return 0;
}

// Añadir elementos a la pila siguiendo el principio LIFO
void push(struct pila *instancia, int numero) 
{
   printf("Nuevo elemento en la pila: %d\n",numero);	
   if (pilaLlena(instancia)==1) 
      return;
   instancia->tope++;
   instancia->valores[instancia->tope]=numero;
}

//Borrar elementos de la pila.
void pop(struct pila *instancia) 
{
   int num;
    printf("Eliminando de la pila: %d\n",instancia->valores[instancia->tope]);
   if (pilaVacia(instancia)==1) 
      return;
   instancia->valores[instancia->tope]=0;
   instancia->tope--;
}
 
 
//Imprime todos los elementos de una pila 
void mostrarElementosPila(struct pila *instancia) 
{
   int i;
   printf("Elementos en la pila:\n");
   for (i = instancia->tope; i >= 0; i--)
      printf("Elemento[%d]=%d\n",i,instancia->valores[i]);
}



//Programa principal 
void main() {
   struct pila instanciaMain;
   printf("Uso de una pila de datos estatica\n\n");
   inicializarPila(&instanciaMain);
   printf("Operaciones \"push\"\n");
   push(&instanciaMain, 1);
   push(&instanciaMain, 2);
   push(&instanciaMain, 3);
   push(&instanciaMain, 4);
   mostrarElementosPila(&instanciaMain);
   printf("\n");
   printf("Operaciones \"pop\"\n");
   pop(&instanciaMain);
   pop(&instanciaMain);
   mostrarElementosPila(&instanciaMain);
   printf("\n");
   printf("Operaciones \"push\"\n");
   push(&instanciaMain, 3);
   push(&instanciaMain, 4);
   mostrarElementosPila(&instanciaMain);
}

