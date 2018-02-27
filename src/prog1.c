// compile with: -O2 -Wall -Wextra ${CC_NO_PIE} -fstack-protector-all
#include <stdio.h>
#include <stdlib.h>

void it_is_never_used__or_is_it()
{
  system("/bin/sh");
}

int main()
{
  void (*func)();
  puts("What address to call as a function?");
  scanf("%p", &func);
  (*func)();
  return 0;
}
