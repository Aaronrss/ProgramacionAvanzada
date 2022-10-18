#include<stdio.h>

// por qué se declara así, sigo pensando que es un constructor
int incrementar(int *numero);

int main(int argc, char const *argv[])
{
	int numero = 10;
	printf("Antes de la funcion, numero es %d\n", numero);
	incrementar(&numero);
	printf("Despues de la funcion, numero es %d", numero);
}


int incrementar(int *numero){
	(*numero) = (*numero) + 1;
}
