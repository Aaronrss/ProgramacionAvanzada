/*Programa ejemplo de switch
que imprime la nota de un
alumno tomando su calificacion */
#include <stdio.h>
int main(void)
{
 int nota=0;
 printf("introduce tu nota\n");
 scanf("%d",&nota);
 switch(nota)
 {
  case 1:
  case 2:
  case 3:
  case 0:
  case 4:
     printf("Suspenso\n"); break;
  case 5:
  case 6:
     printf("Aprobado\n"); break;
  case 9:
  case 10:
    printf("Sobresaliente\n"); break;
  case 7:
  case 8:
    printf("Notable\n"); break;
 }
 return 0;
}
