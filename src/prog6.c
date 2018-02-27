// compile with: -O2 -Wall -Wextra ${CC_NO_PIE} -fno-stack-protector -D_FORTIFY_SOURCE=0
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void gadgets()
{
  __asm__ __volatile__(
#ifdef __x86_64__
    "pop %%rax;"
    "ret;"
    "pop %%rsi;"
    "ret;"
    "pop %%rdx;"
    "ret;"
    "syscall;"
    "ret;"
#elif defined(__i386__)
    "pop %%eax;"
    "ret;"
    "pop %%ebx;"
    "ret;"
    "pop %%ecx;"
    "ret;"
    "int 0x80;"
    "ret;"
#endif
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
