// compile with: -Os -Wall -Wextra -fPIE -pie -fno-stack-protector
#include <assert.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

unsigned long long arr[2]={12345, 67890};
char ans[16];

int main()
{
  int n;
  puts("Now the time has come for global variables.");

  puts("Which element to get?");
  scanf("%d", &n);
  assert(n < 2);
  printf("%lld\n", arr[n]);

  puts("Which element to set?");
  scanf("%d", &n);
  assert(n < 2);
  printf("Gimme your favorite number: ");
  scanf("%llu", &arr[n]);

  puts("Do you like pwn-ing?");

  scanf(" ");
  fgets(ans, 16, stdin);

  if (strcmp(ans, "YES, of course") == 0)
    puts("Me too!");
  else {
    puts("So sad");
    exit(0);
  }

  return 0;
}
