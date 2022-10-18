#include <stdio.h>
#include <conio.h>
int main()
{
 int num1, num2, res1, res2;
 printf("Anote el primer numero\n"); 
 scanf("%i",&num1);
 printf("Anote el segundo numero\n");
 scanf("%i",&num2);
 res1=num1+num2;
 res2=res1*2;
 printf("El resultado de la suma es: %i \n y el de la multiplicación es: %i",res1, res2);
 getch();
 return 0;
} 
