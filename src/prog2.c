// compile with: -O2 -Wall -Wextra ${CC_NO_PIE} -fno-stack-protector -D_FORTIFY_SOURCE=0
#include <stdio.h>
#include <stdlib.h>

void it_is_never_used__or_is_it()
{
  system("/bin/sh");
}

int main()
{
  char name[1];
  puts("What is your name?");
  fgets(name, 24, stdin);
  printf("Hello, %s\n", name);
  return 0;
}
