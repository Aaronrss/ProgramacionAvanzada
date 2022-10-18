/* Programa que suma
los numeros pares e 
impares*/

#include <stdio.h>

void main (void)
{
    int num=0,sumPares=0,sumImpares=0,total=0;
    printf("Numero de enteros: ");
    scanf("%d",&total);
    while (num <= total)
    {
       if(num%2==0)
         sumPares=sumPares+num;
       else 
	     sumImpares=sumImpares+num; 
       num++;   
    }
    printf ("suma de numeros pares: %d\n",sumPares);
    printf ("suma de numeros impares: %d\n",sumImpares);
}
