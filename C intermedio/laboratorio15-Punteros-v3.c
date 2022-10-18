#include <stdio.h>
int main()
{
	int array[10]={0,2,3,5,5,6,7,8,9,0}; 
	int array2[10]={1,2,3,4,5,6,7,8,9,10}; 
	int *puntero = &array[0]; 
	int *puntero2 = &array2[1]; 
	int i; 
	for (i=0;i<10;i++)
		printf("%d ",(*puntero+i)*(*(puntero2+i)));
	return 0;
}



