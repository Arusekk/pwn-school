#!/bin/sh

dir=$1
curusr=pwn$2
nxtusr=pwn$((1+$2))

passw() {
  # echo $2 | passwd --stdin $1
  echo "$1:$2" | chpasswd
}

[ -f $dir/prog ] || exit
if [ $2 -eq 1 ]; then
  passw $curusr 'pwnme2day'
fi

dd if=/dev/urandom bs=64 count=1 | md5sum | cut -d' ' -f1 > $dir/password
passw $nxtusr $(cat $dir/password)

chown -R $curusr:$curusr $dir
chown $nxtusr:$nxtusr $dir/prog*
chown $nxtusr:$nxtusr $dir/solution*
chown $nxtusr:$nxtusr $dir/password*

chmod -R 1551 $dir
chmod -R 0775 $dir/workspace
chmod 6555 $dir/prog
chmod 0440 $dir/prog.* $dir/solution* $dir/password*
grep -qi password $dir/prog.* || chmod 0444 $dir/prog.*

