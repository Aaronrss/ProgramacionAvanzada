/*Programa que imprime
 los numeros pares del 1 al 100
 e imprime cuantos hay*/

#include <stdio.h>
int main()
{
    int x,sum=0;
    for (x=1;x<=50;x++)
    {
      if (x%2==0){
        printf("%d\n",x);
        sum+=x;
      }
    }
    printf("Suma de numeros pares: %d\n",sum);
    return 0;
}
