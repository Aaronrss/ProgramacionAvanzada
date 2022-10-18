/*Programa ejemplo de switch
que realiza una suma o una
resta*/
#include <stdio.h>
int main()
{
	int opcion=0,a=0,b=0,resultado=0;
	printf("Ingrese un numero: ");
	scanf("%d",&a);
	printf("Ingrese un numero: ");
	scanf("%d",&b);
	printf("1. Sumar\n");
	printf("2. Restar\n");
	printf("Elija una operacion: ");
	scanf("%d",&opcion);
	switch(opcion)
	{
		case 1:
			resultado=a+b;
			printf("%d + %d = %d\n",a,b,resultado);
			break;
		case 2:
			resultado=a-b;
			printf("%d - %d = %d\n",a,b,resultado);
			break;
		default:
			printf("Opcion no valida\n");
			break;
	}
	return 0;
}
