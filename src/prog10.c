// compile with: -Os -Wall -Wextra ${CC_NO_PIE} -fstack-protector-all -D_FORTIFY_SOURCE=0
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char format[]="You have a %.2f chance to win.\n";
char input[]="Some text.";

void maybe_unused()
{
  system("/bin/sh");
}

void chances(float chance)
{
  printf(format, chance);
}

int main()
{
  char name[20]="";
  unsigned i;
  puts("What's your name?");
  fgets(name, 20, stdin);
  printf("Hello, %s\n", name);
  puts("What's your last name?");

  for (i=0; i<=strlen(input); i++) {
    input[i] = getchar();
    if (input[i] == '\n')
      input[i] = '\0';
  }

  printf("Hello, %s\n", input);
  chances(0.3);
  exit(0);
}
