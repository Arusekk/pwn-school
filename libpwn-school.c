#define _GNU_SOURCE
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

static void printaction(int sig, siginfo_t *pinfo, void *ucontext) {
  psignal(sig, "signaled");
  psiginfo(pinfo, "signaled: details");
  fprintf(stderr, "si_addr = %p \"%s\"", pinfo->si_addr, pinfo->si_addr);
  abort();
}

typedef struct sigaction sigaction_t;

static const sigaction_t segvact = {
  .sa_sigaction = printaction,
  .sa_mask = 0,
  .sa_flags = SA_ONSTACK|SA_SIGINFO
};

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

  if (sigaction(SIGSEGV, &segvact, NULL)==-1)
    perror("libpwn: sigaction");
}
