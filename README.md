# pwn-school
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/948cfcc9b9ac498b9545c42a2fb2bd76)](https://app.codacy.com/app/Arusekk/pwn-school?utm_source=github.com&utm_medium=referral&utm_content=Arusekk/pwn-school&utm_campaign=badger)
[![Build Status](https://travis-ci.org/Arusekk/pwn-school.svg?branch=master)](https://travis-ci.org/Arusekk/pwn-school)

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
To install them all using `pip`, just type:
```sh
pip install pwn peda ropper
```
* if python module capstone complains about its shared library, install its new version using
```sh
pip install capstone==3.0.5rc2
```


# Building
	make && make install
