/*
    A nice example of using fork.
    Copied from:
    http://www.it.uu.se/education/course/homepage/os/vt18/module-2/process-management/
*/

#include <stdio.h>  // perror()
#include <stdlib.h> // exit(), EXIT_SUCCESS, EXIT_FAILURE
#include <unistd.h> // fork()

void child();
void parent(pid_t pid);

int main(void) {
  pid_t pid;

  switch (pid = fork()) {
    case -1:
      // On error fork() returns -1.
      perror("fork failed");
      exit(EXIT_FAILURE);
    case 0:
      // On success fork() returns 0 in the child.
      child();
    default:
      // On success fork() returns the pid of the child to the parent.
      parent(pid);
  }
}

void child() {
  printf(" CHILD <%ld> I'm alive! My PID is <%ld> and my parent got PID <%ld>.\n",
         (long) getpid(), (long) getpid(), (long) getppid());
  printf(" CHILD <%ld> Goodbye!\n",
         (long) getpid());
  exit(EXIT_SUCCESS);
}

void parent(pid_t pid) {
  printf("PARENT <%ld> My PID is <%ld> and I spawned a child with PID <%ld>.\n",
         (long) getpid(), (long) getpid(), (long) pid);
  printf("PARENT <%ld> Goodbye!\n",
         (long) getpid());
  exit(EXIT_SUCCESS);
}
