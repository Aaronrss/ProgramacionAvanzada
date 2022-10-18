#include <stdio.h>

int main()
{

int array[10]={0,2,3,5,5,6,7,8,9,0}; 
int *puntero = &array[0]; 
int i; 

for (i=0;i<10;i++)
printf("%d\n",*(puntero+i));

return 0;
}
