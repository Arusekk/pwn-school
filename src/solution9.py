from pwn import *

context.clear(arch='amd64')

e = ELF('./prog')

tempor = '/tmp/pwn-%d'%os.getpid()

a = e.functions.main.disasm()
e.write(e.got.strcmp, e.read(e.got.puts, e.bytes))
e.save(tempor)

del e

os.chmod(tempor, 0775)
p = process(tempor)
p.readline()
p.sendline('')
p.readline()
ans = p.readline()
os.unlink(tempor)

p = process('./prog')
p.sendline(ans)
p.interactive()
