/*Programa que obtiene informacion
del teclado de la computadora a traves 
de scanf()*/
#include <stdio.h>
int main()
{
 int a;
 printf("Dar numero \n");
 /*obtener numero del teclado 
 y alamacenarlo en una variable*/
 scanf("%d",&a);
 //imprimir numero obtenido
 printf("El numero obtenido es: %d\n", a);	
 return 0;
}
