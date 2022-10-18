/*Programa que muestra
 numeros aleatorios (entre 0
 y 10) hasta encontrar un 2*/

#include <stdlib.h>
#include <stdio.h>
int main()
{
 int r=0,s=0;
 do {
     r = rand();
     s = r % 2;
     printf("el rand: %d:%d\n",r,s);
     
     //printf("Numero: %d\n",r);
    }while (s != 2);
 return 0;
}
