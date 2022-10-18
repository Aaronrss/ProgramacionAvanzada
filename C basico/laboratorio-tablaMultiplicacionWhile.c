/* Programa que obtiene
la tabla de multiplicar de 
un numero dado*/

#include <stdio.h>

void main (void)
{
    int tabla, por=0;
    printf ("Que tabla quieres sacar: ");
    scanf ("%d", &tabla);
    while (por<11)
    {
     printf ("%d x %d = %d\n", tabla, por, tabla*por);
     por++;
    }
}
