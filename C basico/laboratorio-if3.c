//Programa que crea una condicion if-else anidado
#include <stdio.h>
int main()
{
 if (5 > 3 && 10 <= 10 )
 {
  printf("Instruccion dentro de if\n");
  if (5 >= 3){ printf("Instruccion anidada dentro de if\n"); }
  else {printf("Instruccion anidada dentro de else\n");}
 }
 else
 {
  printf("Instruccion dentro de else\n");	
 }
 printf("Instruccion fuera de if-else\n");
 return 0;
}
