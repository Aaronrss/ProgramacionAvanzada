/*Programa que obtiene
 una sucesion de valores
 especifica:
 1 -1 2 -2 3 -3 4 -4 5 -5
 */

#include <stdio.h>

int main()
{
    int numero;
    for ( numero = 1 ; numero <= 5 ; numero++ )
    {
        printf( "%d %d ", numero, -numero );
    }
    return 0;
}
