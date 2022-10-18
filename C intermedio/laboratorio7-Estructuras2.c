#include <stdio.h>

struct informacionEstudiante{
    char *nombre;
    int id;
    int edad;
};
struct informacionMaterias{
    char *materia;
    int id;
    int clave;
};
int main()
{
    int count = 2;

     struct informacionEstudiante estudiante[2];
     struct informacionMaterias materia[2][2];

     estudiante[0].nombre = "Steve";
     estudiante[0].id = 1234;
     estudiante[0].edad = 30;

     estudiante[1].nombre = "Aaron";
     estudiante[1].id = 4321;
     estudiante[1].edad = 25;
     for (int i = 0; i < count; ++i)
     {
        printf("Nombre de estudiante: %s", estudiante[i].nombre);
        printf("\nId de estudiante: %d", estudiante[i].id);
        printf("\nEdad de estudiante: %d\n", estudiante[i].edad);

     }
     return 0;
}
