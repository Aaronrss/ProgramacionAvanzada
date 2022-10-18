#include <stdio.h>
#include <string.h>
 
struct estudiante 
{
     int id;
     char nombre[30];
     float porcentaje;
};
 
int main() 
{
     int i;
     struct estudiante record[2];
 
     record[0].id=1;
     strcpy(record[0].nombre, "Raul");
     record[0].porcentaje = 86.5;
     
     record[1].id=2;
     strcpy(record[1].nombre, "Susana");
     record[1].porcentaje = 90.5;
 
     record[2].id=3;
     strcpy(record[2].nombre, "Tomas");
     record[2].porcentaje = 81.5;
 
     for(i=0; i<3; i++)
     {
      printf(" Record de estudiante: %d \n", i+1);
      printf(" Id: %d \n", record[i].id);
      printf(" Nombre: %s \n", record[i].nombre);
      printf(" Porcentaje: %f\n\n",record[i].porcentaje);
     }
     return 0;
}
