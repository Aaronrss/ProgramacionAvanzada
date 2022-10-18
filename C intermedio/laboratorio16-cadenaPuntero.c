#include <stdio.h>
#include <string.h>
int main()
{
	char str[] = "recorrido de un puntero";
	// por qué aquí %s
	printf("Frase original: \n%s\n",str);
	int i, j = strlen(str);
	//se esta utilizando j que se modifica en el for, se declara desde antes del for
	char *ptr=&str[j-1];
	printf("Frase invertida:\n");
	// se puede declarar la sintaxis sin corchetes
	for(i = j; i >= 0 ; i--)
		//por qué aquí %c, es por el puntero?
		printf("%c", *ptr--);
	return 0;
}
