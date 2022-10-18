/* Programa que obtiene
los numeros impares de una 
lista de N numeros*/

#include<stdio.h>

void main()
{
 int totalNum=0,num=0;
 printf("Numero de enteros: ");
 scanf("%d",&totalNum);
 while(num<=totalNum)
 {
   if(num%2!=0)
   	printf("%d\n",num);
   num++;
 }
}
