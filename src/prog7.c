// compile with: -O2 -Wall -Wextra -fPIE -pie -fno-stack-protector -D_FORTIFY_SOURCE=0 -z execstack
#include <stdio.h>
#include <stdlib.h>

int main()
{
  char name[1];
  puts("What is your name?");
  printf("Name is somewhere at %p\n", (void*)(((long long)name)&-0x20000));
  fgets(name, 20, stdin);
  printf("Hello, %s\n", name);
  return 0;
}
