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
    int count = 1;
    int counta = 1;

     struct informacionEstudiante estudiante[2][1];
     struct informacionMaterias materia[2];

     estudiante[0].nombre = "Steve";
     estudiante[0].id = 1234;
     estudiante[0].edad = 30;
     estudiante[0].materia[0].materia = "Programación Avanzada";


     estudiante[1].nombre = "Aaron";
     estudiante[1].id = 4321;
     estudiante[1].edad = 25;
     for (int i = 0; i < count; ++i)
     {
        for (int j = 0; j < counta; ++j)
        {
        printf("Nombre de estudiante: %s", estudiante[i].nombre);
        printf("\nId de estudiante: %d", estudiante[i].id);
        printf("\nEdad de estudiante: %d", estudiante[i].edad);
        printf("\nMateria: %d\n", estudiante[i].materia[j].materia);
            
        }
     }
     return 0;
}
