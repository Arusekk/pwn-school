# pwn-school
Learn how to pwn badly written programs

# What is pwn-school?
A tool that teaches how to [pwn](https://en.wikipedia.org/wiki/Pwn).

Pwn School teaches how to pwn applications with errors such as off-by-one,
helps to understand stack- and heap-overflows.

Learn why:
* data buffers should always be big enough, no matter whether placed on stack, on heap or anywhere else
* user-input is to be double-, or even triple-checked before being considered safe
* functions marked as unsafe are really unsafe
* many many more...

# Dependencies
* `make`
* `libopenssl`
* sample solutions are using Python 2.x with `pwntools`, recommended are also `peda` and `ropper`.
To install them all using `pip`, just type: `pip install pwntools peda ropper`

# Building
	make && make install
