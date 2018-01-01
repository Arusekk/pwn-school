from pwn import *

context.clear(arch='amd64')

with tempfile.NamedTemporaryFile(prefix='pwn-') as tf, open(os.devnull, 'r+b') as DEVNULL:
	tempor = tf.name
	os.dup2(DEVNULL.fileno(), tf.fileno())

	e = ELF('prog')
	e.write(e.got.memcmp, e.read(e.got.puts, e.bytes))
	e.write(e.got.nanosleep, p64(ROP(e).ret.address))
	e.save(tempor)

	os.chmod(tempor, 0500)
	p = process(tempor, stdin=DEVNULL)
	p.readline()
	p.readline()
	ans = p.readline().strip()
	print(ans)

p = e.process()
p.sendline(ans)
p.interactive()
