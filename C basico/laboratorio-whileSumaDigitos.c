/* Programa que suma
los digitos de un entero*/

#include <stdio.h>

void main (void)
{
    int num=0,dig=0,sum=0;
    printf ("Ingresar numero entero: ");
    scanf ("%d", &num);
    while (num != 0)
    {
     dig=num%10;
	 num=num/10;	
	 sum = sum + dig;
     printf ("digito %d\n",dig);
    }
    printf ("suma de digitos: %d\n",sum);
}
