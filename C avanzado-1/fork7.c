/*
    Program that runs another application, using the "system" call
    This is the same as calling: fork, execl, waitpid

    provided by: Gilberto Echeverria
*/

#include <stdio.h>
#include <stdlib.h>
// To be able to get the process id
#include <unistd.h>

#define STR_LEN 80

int main()
{
    char command[STR_LEN];

    // Get the Process ID's for this process and its parent
    printf("My Process ID is: %d\n", getpid());
    printf("My parent ID is: %d\n", getppid());

    // Construct the command we wish to exectue
    sprintf(command, "gcc %s -o 01-system_calls -Wall -g", __FILE__);

    printf("THIS IS MY PROGRAM\n");

    printf("About to execute '%s'\n", command);

    system(command);

    printf("Files in the current directory: \n");
    system("ls -l");

    // When the other commands finish, keep executing this code
    printf("There you go. That's what you have\n");
    printf("BACK TO MY PROGRAM\n");

    return 0;
}
