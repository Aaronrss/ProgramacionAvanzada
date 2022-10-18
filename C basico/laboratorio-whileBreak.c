/* Programa que obtiene
todos los numero de una 
serie de enteros hasta que
estos sean negativos*/

#include <stdio.h>

void main (void)
{
    int num=0;
    printf ("Dar un numero: ");
    scanf ("%d", &num);
    while (1)
    {
     if(num<0)
	 {
	   printf("Error, Valor negativo");
	   break;	
	 }	
     printf ("Numero %d\n",num);
     num--;
    }
}
