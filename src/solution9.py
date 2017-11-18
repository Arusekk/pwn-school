from pwn import *

context.clear(arch='amd64')

e = ELF('./prog')

tempor = '/tmp/pwn-%d'%os.getpid()

a = e.functions.main.disasm()
e.write(e.got.memcmp, e.read(e.got.puts, e.bytes))
e.write(e.got.nanosleep, p64(ROP(e).ret.address))
e.save(tempor)

del e

os.chmod(tempor, 0775)
with open('/dev/null', 'r+b') as DEVNULL:
  p = process(tempor, stdin=DEVNULL)
  p.readline()
  p.readline()
  ans = p.readline().strip()
print(ans)
os.unlink(tempor)

p = process('./prog')
p.sendline(ans)
p.interactive()
