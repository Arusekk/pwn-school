// compile with: -O2 -Wall -Wextra -fPIE -pie -fno-stack-protector -D_FORTIFY_SOURCE=0 -z execstack
#include <stdio.h>
#include <stdlib.h>

int main()
{
  char name[1];
  printf("In case you need, name is at %p\n", name);
  puts("Gimme your input");
  fgets(name, 128, stdin);
  return 0;
}
