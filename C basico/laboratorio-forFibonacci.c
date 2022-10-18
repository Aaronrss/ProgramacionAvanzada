/*Programa que imprime
 los primeros 20 numeros
 de la serie fibonacci*/

#include <stdio.h>

int main()
{
  int x=0,y=1,z,cont;
  printf("0\n1\n");
  for (cont=1;cont<=18;cont=cont+1){
    z=x+y;
    printf("%d\n",z);
    x=y;
    y=z;
  }
  return 0;
}
