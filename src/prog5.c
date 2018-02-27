// compile with: -O0 -Wall -Wextra ${CC_PIE} -fstack-protector-all
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void unused_remainder_from_old_version()
{
  system("/bin/sh");
}

void disclosure()
{
  unsigned long long tab[2]={0xcc, 0xdd};
  int i;
  puts("But wait! My boss wanted me to give you these:");
  for (i=0; i<9; i++)
    printf("%llu\n", tab[i]);
}

int main()
{
  puts("Now everything is soo safe!");

  disclosure();

  char name[1];
  read(STDIN_FILENO, name, 32);
  printf("You entered: %s\n", name);

  return 0;
}
