#include <stdio.h> 
#include <sys/types.h> 
#include <unistd.h> 
#include <stdlib.h>
int main() 
{ 
    /* fork a process */
    fork(); 
    /* fork a process */
    fork(); 
    /* fork a process */
    fork(); 
    printf("Hello world!\n");
    return 0; 
} 
