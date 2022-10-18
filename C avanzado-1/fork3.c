#include <stdio.h> 
#include <sys/types.h> 
#include <unistd.h> 
#include <stdlib.h>

int main() 
{
  /* fork a process */	
  if(fork() == 0) 
    if(fork())
      printf("Hello world!!\n");
  exit(0);
}
