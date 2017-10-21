
dir=$1
curusr=pwn$2
nxtusr=pwn$((1+$2))

[ -f $dir/prog ] || exit
if [ $2 -eq 1 ]; then
  echo -n 'pwnme2day' | passwd --stdin $curusr
fi

dd if=/dev/urandom bs=64 count=1 | md5sum | cut -d' ' -f1 > $dir/password
passwd --stdin $nxtusr < $dir/password

chown -R $curusr:$curusr $dir
chown $nxtusr:$nxtusr $dir/prog*
chown $nxtusr:$nxtusr $dir/solution*
chown $nxtusr:$nxtusr $dir/password*

chmod -R 1551 $dir
chmod -R 0775 $dir/workspace
chmod 6555 $dir/prog
chmod 0440 $dir/prog.* $dir/solution* $dir/password*
grep -qi password $dir/prog.* || chmod 0444 $dir/prog.*
