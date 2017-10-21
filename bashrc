[ ! -f /etc/bashrc ] || . /etc/bashrc

export HISTCONTROL=ignoreboth
unset HISTFILE

cat motd
