/*Programa que calcula
la suma de los cuadrados
de los primeros 100
numeros*/

#include <stdio.h>

int main(void)
{
 int x,sum;          
 sum=0;
 for (x=1;x<=100;x++) { sum=sum+(x*x); }          
 printf("Suma de los cuadrados de los primeros 100 numeros: %d\n",sum);        
 return 0;
}

