/*
    Program that creates other processes using "fork"
    provided by: Gilberto Echeverria
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main()
{
   	int pid = 0;
                
  	printf("Making the fork\n");
	pid = fork();
	printf("PID = %d | PPID = %d | 'fork' returned =  %d\n", getpid(), getppid(), pid);
	
    // The parent process
    if (pid > 0)
    {
        printf("The parent:\n");
    }
    // The child process
    else if (pid == 0)
    {
        printf("The child:\n");
    }
    // Fork failed and did not create another process
    else
    {
        perror("Could not create a child process\n");
        exit(EXIT_FAILURE);
    }

    // Both parent and child will change to become the program 'ls'
	execl("/bin/ls", "ls", "-l", "-h", (char *)NULL);

	printf("This line will NEVER be printed\n");
   
	return 0;
}
