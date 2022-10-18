/*Programa que muestra
 N letreros usando el
 ciclo do-while*/


#include <stdio.h>
int main()
{
 int letreros=0,num=0;
 printf("Numero de letreros: ");
 scanf("%d",&letreros);
 do {
     printf("Hola mundo\n");
     num++;
    }while (num < letreros);
 return 0;
}
