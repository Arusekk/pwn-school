// compile with: -Os -Wall -Wextra $(pkg-config --cflags --libs libssl libcrypto)
#include <openssl/sha.h>
#include <openssl/bn.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

unsigned long long arr[2]={12345, 67890};

char s1[65], s2[65];

void genpwd()
{
  char taj[20];
  unsigned char rak[33];
  sprintf(taj, "%d", (((int)time(0)/60)-2137)*5);

  SHA1((unsigned char*)taj, strlen(taj), rak);
  BIGNUM* lel = NULL;
  lel = BN_bin2bn(rak, SHA_DIGEST_LENGTH, lel);
  strcpy(s1, BN_bn2hex(lel));
}

int main()
{
  int i;
  puts("Input password:");

  fgets(s2, 65, stdin);

  fputs("Checking", stdout);
  struct timespec tim, tim2;
  for (i=0; i<15; i++) {
    putchar('.');
    fflush(stdout);
    tim.tv_sec = 0;
    tim.tv_nsec = 500000000;
    nanosleep(&tim, &tim2);
  }
  puts("");

  genpwd();

  if (memcmp(s1, s2, strlen(s1)) == 0) {
    puts("Access granted.");
    system("/bin/sh");
  }
  else
    puts("Access denied.");

  return 0;
}
