/*Programa que obtiene
 la secuencia de valores
 entre dos numeros*/

#include <stdio.h>
int main()
{
 int num1, num2,x;
 printf("Primer número:");
 scanf("%d",&num1);
 printf("Segundo número:");
 scanf("%d",&num2);
 if (num1>num2){
  printf("Valores incorrectos \n");
 }
 else
 {
  for (x=num1;x<=num2;x++){
    if (x%2==0)
       printf("%d\n",x);
  }
 }
return 0;
}
