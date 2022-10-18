// Dining Philosophers problem
// 5 philosophers, 5 forks
// Each philosopher needs 2 forks to eat
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>

sem_t *forks[5]; // 5 forks
sem_t *room;     // 1 room
int i;              // loop index

philosopher(int i)
{
  while (1)
  {
    think();
    take_forks(i);
    eat();
    put_forks(i);
  }
}

void think(int philosopher)
{
  int sleepTime = rand() % 3 + 1;
  printf("Philosopher %d is thinking", philosopher);
  sleep(sleepTime);
}

void take_forks(int philosopher)
{
  wait(forks[philosopher]);           // get left fork
  wait(forks[(philosopher + 1) % 5]); // get right fork
}

void put_forks(int philosopher)
{
  signal(forks[(philosopher + 1) % 5]); // put right fork
  signal(forks[philosopher]);           // put left fork
}

void eat(int philosopher)
{
  int sleepTime = rand() % 3 + 1;
  printf("Philosopher %d is eating", philosopher);
  sleep(sleepTime);
}

int main(void)
{
  int i;
  for (i = 0; i < 5; i++)
  {
    initsem(forks[i], 1);
  }
  initsem(room, 4);
  cobegin()
  {
    filosofo(0);
    filosofo(1);
    filosofo(2);
    filosofo(3);
    filosofo(4);
  };
};