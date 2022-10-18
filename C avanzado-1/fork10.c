/*
    Program to compute the factorial of different numbers
    Each function will be executed by a different process
    Shows returning the resulting value as the exit condition of the child

    provided by: Gilberto Echeverria

*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

void userMenu();
void createProcess(int number);
unsigned long int factorial(int number);

int main()
{
    printf("\nPROGRAM TO COMPUTE FACTORIALS (in separate processes)\n");

    userMenu();

    return 0;
}

void userMenu()
{
    int number = 0;

    while (number >= 0)
    {
        printf("\nEnter a number to compute its factorial (enter a negative number to finish): ");
        scanf("%d", &number);

        if (number >= 0)
        {
            createProcess(number);
        }
    }
}

void createProcess(int number)
{
    pid_t pid;
    int status;

    pid = fork();

    // Parent process
    if (pid > 0)
    {
        if ( waitpid(pid, &status, 0) != -1 )
        {
            if (WIFEXITED(status))
            {
                printf("The factorial of %d is %d, and status is %d\n", number, WEXITSTATUS(status), status);
            }
        }
    }
    // Child process
    else if (pid == 0)
    {
        exit( factorial(number) );
    }
    // No proces created ( negative pid )
    else
    {
        perror("Unable to create a new process\n");
        exit(EXIT_FAILURE);
    }
}

unsigned long int factorial(int number)
{
    unsigned long int result = 1;
    for (; number > 0; number--)
    {
        result *= number;
    }
    return result;
}
