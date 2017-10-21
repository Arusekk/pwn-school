// compile with: -Os -Wall -Wextra -lssl -lcrypto
#include <openssl/sha.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

unsigned long long arr[2]={12345, 67890};

char s1[33], s2[33];

void genpwd()
{
  char taj[20];
  sprintf(taj, "%d", (((int)time(0)/60)-2137)*5);

  SHA1((unsigned char*)taj, strlen(taj), (unsigned char*)s1);
}

int main()
{
  int i;
  puts("Input password:");

  fgets(s2, 33, stdin);

  fputs("Checking", stdout);
  struct timespec tim, tim2;
  for (i=0; i<15; i++) {
    putchar('.');
    tim.tv_sec = 0;
    tim.tv_nsec = 500000000;
    nanosleep(&tim, &tim2);
  }
  puts("");

  genpwd();

  if (strcmp(s1, s2) == 0) {
    puts("Access granted.");
    system("/bin/sh");
  }
  else
    puts("Access denied.");

  return 0;
}
