// compile with: -O2 -Wall -Wextra -fno-pic -no-pie -fno-stack-protector -D_FORTIFY_SOURCE=0
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void gadgets()
{
  __asm__ __volatile__(
    "pop %%rax;"
    "ret;"
    "pop %%rsi;"
    "ret;"
    "pop %%rdx;"
    "ret;"
    "syscall;"
    "ret;"
    : :
  );
}

int main()
{
  char name[1];
  printf("Now the stack is not executable, ha ha! But your name will be at %p\n", name);

  fgets(name, 400, stdin);

  if (strcmp(name, "John") == 0)
    puts("Hello, Johnny!");
  else {
    puts("I don't know you!");
    exit(0);
  }
  
  return 0;
}
