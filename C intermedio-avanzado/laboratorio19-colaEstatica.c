//Libreria de entrada y salida de datos
#include<stdio.h>

//Maximo numero de elementos de la cola  
#define MAXIMO 5

// Definicion de la estructura de la cola
struct cola {
   int valores[MAXIMO];
   int frente;
   int atras;
};

// Inicializacion de la cola estatica
void inicializarCola(struct cola *instancia) {
   instancia->frente = 0;
   instancia->atras=0; 
}


//Verifica si la cola estatica esta vacia
int colaVacia(struct cola *instancia) 
{
   if(instancia->frente == instancia->atras){
   	printf("La cola esta vacia\n");
   	return 1;
   }
   else
   	 return 0;  
}

//Verifica si la cola estatica esta llena
int colaLlena(struct cola *instancia) 
{
   if(instancia->atras == MAXIMO){
   	printf("La cola esta llena\n");
   	return 1;
   } 
   else
   	return 0; 
}

// Añadir elementos a la cola estatica siguiendo el principio FIFO
void queue(struct cola *instancia, int numero) 
{
  printf("Nuevo elemento en la cola: %d\n",numero);	 	
  if (colaLlena(instancia)==1)
  	return;
  else{
  	instancia->valores[instancia->atras] = numero;
  	instancia->atras++;
  }	
}


//Borrar elementos de la cola estatica
void dequeue(struct cola *instancia) 
{
   printf("Eliminando de la cola: %d\n",instancia->valores[instancia->frente]);	
   if (colaVacia(instancia)==1)
	 return;			
   else
   {
   	 int i;
   	 instancia->valores[instancia->frente] = 0;
   	 for (i = 0; i < (instancia->atras-1); i++)  
        instancia->valores[i] = instancia->valores[i+1]; 
     instancia->atras--;        
   }   
}

//Imprime todos los elementos de una cola estatica 
void mostrarElementosCola(struct cola *instancia) 
{
   printf("Elementos en la cola:\n");	
   if (colaVacia(instancia)==1)
	   return;
   else{
   	int i;
   	for (i = instancia->frente; i < instancia->atras; i++)
      printf("Elemento[%d]=%d\n",i,instancia->valores[i]);
   }
}

//Programa principal 
void main() {
   struct cola instanciaMain;
   printf("Uso de una cola de datos estatica\n\n");
   inicializarCola(&instanciaMain);
   printf("Operaciones \"queue\"\n");
   queue(&instanciaMain, 1);
   queue(&instanciaMain, 2);
   queue(&instanciaMain, 3);
   queue(&instanciaMain, 4);
   mostrarElementosCola(&instanciaMain);
   printf("\n");
   printf("Operaciones \"dequeue\"\n");
   dequeue(&instanciaMain);
   dequeue(&instanciaMain);
   mostrarElementosCola(&instanciaMain);
   printf("\n");
   printf("Operaciones \"queue\"\n");
   queue(&instanciaMain, 3);
   queue(&instanciaMain, 4);
   queue(&instanciaMain, 5);
   mostrarElementosCola(&instanciaMain);
}
