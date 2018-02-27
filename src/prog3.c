// compile with: -O2 -Wall -Wextra ${CC_PIE} -fstack-protector-all
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>

int main()
{
  puts("Gimme your favorite shellcode");
  void * mem = mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);
  read(STDIN_FILENO, mem, 4096);
  mprotect(mem, 4096, PROT_READ|PROT_EXEC);
  (*( (void(*)()) mem ))();
  return 0;
}
