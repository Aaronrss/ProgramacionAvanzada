#include <stdio.h>
#include <string.h>

int main()
{
	char nombre[]="Gustavo A. Chavarria";
	char *puntero=nombre;
	printf("%s\nIngrese otro nombre: ",puntero);
	gets(puntero); 
	printf("%s",puntero); 
}

