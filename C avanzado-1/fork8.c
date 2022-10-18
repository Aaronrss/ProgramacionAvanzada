/*
   Program to test the behaviour of parent and child trying to read from stdin

   provided by: Gilberto Echeverria
   
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>     // Library to access POSIX functions

int main()
{
    printf("CALL TO FORK\n");
    pid_t new_id;

    // Create a new process
    new_id = fork();

    printf("My pid: [%d], my parent id: [%d], new_id: [%d]\n", getpid(), getppid(), new_id);

    // Parent process
    if (new_id > 0)
    {
        int var1 = 0;
        printf("PARENT TRYING TO READ A NUMBER: ");
        scanf("%d", &var1);
        printf("Parent read %d\n", var1);
    }
    // Child process
    else if (new_id == 0)
    {
        int var2 = 0;
        printf("CHILD TRYING TO READ A NUMBER: ");
        scanf("%d", &var2);
        printf("Child read %d\n", var2);
    }
    // If the new_id is negative
    else
    {
        printf("COULD NOT CREATE A NEW PROCESS\n");
    }

    return 0;
}
