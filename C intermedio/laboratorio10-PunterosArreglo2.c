#include <stdio.h>
int main ()
{
    int array[] = { 45, 67, 89};
    int *array_ptr = &array[1];
    int x;	
	for(x=0;x<=2;x++){
	  printf("%d\n", array_ptr[x]);	
	}
    return 0;
}
