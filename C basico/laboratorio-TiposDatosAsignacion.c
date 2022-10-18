#include <stdio.h>
int main()
{
 int a = 10,b=20,temp;
 printf("Valor de a: %d \n",a);
 printf("Valor de b: %d \n",b);
 printf("Intercambio de valores\n");
 temp=a;
 a=b;
 b=temp;
 printf("Nuevo valor de a: %d \n",a);
 printf("Nuevo valor de b: %d \n",b);
}
