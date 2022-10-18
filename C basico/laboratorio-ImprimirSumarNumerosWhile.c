/* Programa que suma los primeros
N numeros enteros*/

#include<stdio.h>

void main()
{
 int numValores=0,num=0,suma=0;
 printf("Cuantos numeros enteros desea sumar: ");
 scanf("%d",&numValores);
 while(num<=numValores)
 {
   suma = suma + num;
   printf("acumulado: %d\n",suma);
   num++;
 }
 printf("La suma es: %d\n",suma);
}
