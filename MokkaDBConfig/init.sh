
script_name="init_mokka_wrapper.sh"

if test -n "$BASH" ; then
    #echo "BASH_ARGV ${BASH_ARGV}"
    #echo "BASH_SOURCE ${BASH_SOURCE}"
    if test -z "${BASH_SOURCE}" ; then
        if test ! -s "./$script_name" ; then
            echo "ERROR: cd to where $script_name is and source it from there"
            return 1
        fi
    else
        cded="bash"
        cd $(dirname ${BASH_SOURCE})
    fi
else
    cded="zsh"
    cd $(dirname $0)
fi
unset script_name

MOKKADBCONFIG=$PWD

if test -n "$cded"; then
    cd $OLDPWD
    unset cded
fi

export PATH=$MOKKADBCONFIG/scripts:$PATH
export MOKKA_DUMP_FILE=$MOKKADBCONFIG/mokka-dbdump.sql.tgz

echo "MOKKADBCONFIG set to $MOKKADBCONFIG"
echo "MOKKA_DUMP_FILE set to $MOKKA_DUMP_FILE"

