/*Programa que muestra
el uso de funciones 3*/

#include <stdio.h>

int sumar(int a, int b){
 int resultado = a + b;
 return (resultado);
}

float promedio (int a, int b){
  return ((a+b)/2.0);
}


int main() 
{
   printf("Res: %f\n",promedio(sumar(1,2),sumar(2,3)));
   printf("Res: %f\n",promedio(sumar(5,6),sumar(7,8)));
   printf("Res: %f\n",promedio(sumar(9,10),sumar(11,12)));
}
