/*Programa que calcula
 el promedio de n numeros
 dados*/

#include <stdio.h>

int main()
{
  int num,i,suma=0,cantidad;
  printf("# valores a calcular su promedio: ");
  scanf("%d",&num);
  for(i=1;i<=num;i++)
  {
    printf("Numero: ");
    scanf("%d",&cantidad);
    suma=suma+cantidad;
  }
  suma=suma/num;
  printf("El promedio es: %d",suma);
  return 0;
}
