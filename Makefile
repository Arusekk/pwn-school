MAXNUM := 10
LDFLAGS-pwn := $(LDFLAGS) -L. -lpwn-school
#-Wl,-rpath=$(DESTDIR)/var/pwn-school
CP ?= cp
RM ?= rm -f
CC ?= cc
prefix ?= /usr
exec_prefix ?= $(prefix)
libdir ?= $(exec_prefix)/lib64

NUMBERS := $(shell seq 1 $(MAXNUM))
TESTHOMES := $(addprefix test-home-,$(NUMBERS))
ALLHOMES := $(addprefix all-home-,$(NUMBERS))

default-target: all
.PHONY: default-target

libpwn-school.so: libpwn-school.c
	$(CC) $(CFLAGS) -shared -fPIC -o $@ $< $(LDFLAGS)

all: libpwn-school.so $(ALLHOMES)
.PHONY: all

homes/%/workspace:
	mkdir -p $@
homes/%/.bashrc: bashrc
	$(CP) -a $< $@
homes/%/.bash_profile: bash_profile
	$(CP) -a $< $@
homes/pwn%/prog.c: src/prog%.c
	$(CP) -a $< $@
homes/%/prog: homes/%/prog.c
	$(CC) $(CFLAGS) -o $@ $< `head -1 $< |cut -d: -f2-` $(LDFLAGS-pwn)
homes/pwn%/solution: src/solution%.py
	$(CP) -a $< $@
homes/pwn%/motd: src/motd%
	$(CP) -a $< $@

$(ALLHOMES): all-home-%: homes/pwn%/workspace homes/pwn%/.bashrc homes/pwn%/.bash_profile \
             homes/pwn%/prog.c homes/pwn%/prog homes/pwn%/solution homes/pwn%/motd
.PHONY: $(ALLHOMES)

test: $(TESTHOMES)
.PHONY: test
$(TESTHOMES): test-home-%: homes/pwn%/prog homes/pwn%/solution
	@( ulimit -t 18; cd homes/pwn$*;\
	    touch .lock; \
	    (echo id; i=1; while [ -f .lock ] && [ $$i -lt 90 ]; do sleep 0.1; i=$$((i+1)); done; echo) | \
	    LC_ALL=C python solution 2>&1 |tee outp | \
	    (grep -q groups; e=$$?; $(RM) .lock; exit $$e) \
	  ) && echo $@: PASS||(echo $@: FAIL; cat homes/pwn$*/outp; $(RM) .lock; exit 0)
.PHONY: $(TESTHOMES)

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
