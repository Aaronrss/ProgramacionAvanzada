/*
    Program to create a series of child processes
    Each process will wait for a random time before finishing
    The parent will wait for all of its children to finish
    Based on an exercise by Vicente Cubells

    provided by: Gilberto Echeverria
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <sys/wait.h>

#define MAX_CHILDREN 100
#define MAX_MILLISECONDS 5000


void processCreation();

int main()
{
    printf("\nMULTIPLE CHILD PROCESSES, WITH RANDOM DELAYS\n");

    processCreation();

    return 0;
}

void processCreation()
{
    int pids[MAX_CHILDREN];
    int children = 0;
    int status;
    
    printf("Enter the number of processes to create: ");
    scanf("%d", &children);

    for (int i=0; i<children; i++)
    {
        pids[i] = fork();

        // No proces created
        if (pids[i] < 0)
        {
            perror("Unable to create a new process\n");
            exit(EXIT_FAILURE);
        }
        // Parent process
        if (pids[i] > 0)
        {
            // Since the order of the pids is fixed, they will be printed here in order
            if ( waitpid(pids[i], &status, 0) != -1 )
            {
                if (WIFEXITED(status))
                {
                    printf("Child %d (PID %d) finished after %d seconds\n", i, pids[i], WEXITSTATUS(status));
                }
            }
        }
        // Child process
        else
        {
            // Number of milliseconds to wait
            unsigned int millis;
            // Variable to make the program wait a number of milliseconds
            struct timespec ts;

            // Initialize the random seed for each process
            srand(time(NULL));

            // Get a random number
            millis = rand() % MAX_MILLISECONDS + 1; 
            // Fill the time structure
            ts.tv_sec = millis / 1000;      // Seconds
            ts.tv_nsec = millis * 1000;     // Nanoseconds

            // Wait a number of nanoseconds
            nanosleep(&ts, NULL);

            exit(ts.tv_sec);
        }
    }

    printf("\nAll children have finished!!\n");
}
