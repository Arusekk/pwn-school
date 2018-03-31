from pwn import *

context.binary = 'prog'
e = context.binary

checkingtime = 8
tosleep = checkingtime - (time.time() + checkingtime)%60
if tosleep > 0:
	time.sleep(tosleep+0.5)

with tempfile.NamedTemporaryFile(prefix='pwn-') as tf, open(os.devnull, 'r+b') as DEVNULL:
	tempor = tf.name
	os.dup2(DEVNULL.fileno(), tf.fileno())

	e.pack(e.got.memcmp, e.unpack(e.got.puts))
	e.pack(e.got.nanosleep, ROP(e).ret.address)
	e.save(tempor)

	os.chmod(tempor, 0o500)
	p = process(tempor, stdin=DEVNULL)
	p.readline()
	p.readline()
	ans = p.readline().strip()
	print(ans)

p = e.process()
p.sendline(ans)
p.interactive()
