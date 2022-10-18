//Programa de ejemplo del uso de apuntadores 1
#include <stdio.h>
int main(void)
{
 int mi_arreglo[] = {1,23,17,4,-5,100}, i;
 int *ptr;
 // que sucede aquí?
 ptr = &mi_arreglo[0]; 
 for (i = 0; i < 6; i++)
 {
   printf("mi_arreglo[%d] = %d ", i, mi_arreglo[i]); 
   printf("ptr + %d = %d\n",i, (*ptr + i));
 }
 return 0;
}

