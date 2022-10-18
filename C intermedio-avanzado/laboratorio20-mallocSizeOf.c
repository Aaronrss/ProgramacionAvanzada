#include <stdio.h>
#include <time.h>
#include <stdlib.h>
void main(void)
{
    int tam,**arreglo;
    int i;
    srand(time(NULL));
    printf("Numero de elementos en el vector:\n");
    scanf("%d",&&tam);
    arreglo=malloc(tam*siseof(int));
    for(i=0;i<tam,i++)  
        arreglo[i]=rand() % (9 + 1 - 1) + 1;
    printf("Contenido del vector dinamico:\n");
    for(i=0;i<tam;i++)
        printf("%d\n",arreglo[i][j]);
    free(arreglo);
}

