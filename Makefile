MAXNUM := 10
LDFLAGS-pwn := $(LDFLAGS) -L. -lpwn-school
#-Wl,-rpath=$(DESTDIR)/var/pwn-school
CP ?= cp
RM ?= rm -f
CC ?= cc
prefix ?= /usr
exec_prefix ?= $(prefix)
libdir ?= $(exec_prefix)/lib64

default-target: all
.PHONY: default-target

libpwn-school.so: libpwn-school.c
	$(CC) $(CFLAGS) -shared -fPIC -o $@ $< $(LDFLAGS)

all: libpwn-school.so
	@for i in `seq 1 $(MAXNUM)`; do \
	  mkdir -p homes/pwn$$i/workspace; \
	  $(CP) -a bashrc homes/pwn$$i/.bashrc; \
	  $(CP) -a bash_profile homes/pwn$$i/.bash_profile; \
	  $(CP) -a src/prog$$i.c homes/pwn$$i/prog.c; \
	  $(CC) $(CFLAGS) -o homes/pwn$$i/prog homes/pwn$$i/prog.c `head -1 homes/pwn$$i/prog.c |cut -d: -f2-` $(LDFLAGS-pwn); \
	  $(CP) -a src/solution$$i.py homes/pwn$$i/solution; \
	  $(CP) -a src/motd$$i homes/pwn$$i/motd; \
	done
.PHONY: all

clean:
	$(RM) -r homes libpwn-school.so*
.PHONY: clean

install:
	install -Dm644 020.peda.gdb $(DESTDIR)/etc/gdbinit.d/020.peda.gdb
	$(RM) $(DESTDIR)/var/pwn-school
	install -dm755 $(DESTDIR)/var
	$(CP) -a homes $(DESTDIR)/var/pwn-school
	install -Dm644 fixperm.sh $(DESTDIR)/var/pwn-school/fixperm.sh
	install -Dm644 libpwn-school.so $(DESTDIR)$(libdir)/libpwn-school.so
.PHONY: install
