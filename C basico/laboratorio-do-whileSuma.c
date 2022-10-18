/*Programa que muestra
 la suma de numeros
 hasta encontrar un cero
 usando un ciclo do-while*/
#include <stdio.h>
int main()
{
 int num, suma=0;
 do {
     printf("Dar numero: ");
     scanf("%d",&num);
     suma += num;
    }while (num != 0);
 printf("suma=%d\n",suma);
 return 0;
}
