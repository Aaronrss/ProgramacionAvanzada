/*Programa ejemplo de switch
que imprime los dias de la
semana*/
#include <stdio.h>
int main(void)
{
  int numero=0;
  printf("Introduzca numero del 1 al 5: ");
  scanf("%d",&numero);
  switch(numero){
    case 1:
      printf ("Lunes\n"); break;
    case 2:
      printf ("Martes\n"); break;
    case 3:
      printf ("Miercoles\n"); break;
    case 4:
      printf ("Jueves\n"); break;
    case 5:
      printf ("Viernes\n"); break;
    default:
      printf ("Opcion no válida\n"); break;
    }
    return 0;
}
