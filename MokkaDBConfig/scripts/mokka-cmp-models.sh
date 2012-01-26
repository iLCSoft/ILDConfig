#!/bin/bash

########################################
# small utility script for comparing
# mokka models from the database
# author: J. Engels, Desy - IT
########################################

TMPDIR=/tmp
diffcmd="diff -u"
type colordiff >/dev/null 2>&1 && diffcmd="color$diffcmd"

cleanup(){
    # save exit code
    exit_code=$?

    rm -f $TMPDIR/mokka_cmp_models.*

    exit $exit_code
}

# cleanup @ exit (or kill)
trap cleanup EXIT

if [ "$#" -ne 2 ]
then
    echo "Usage: $(basename "$0") ModelA ModelB" 1>&2
    echo "Example: $(basename "$0") ILD_00 ILD_O1_v01" 1>&2
    exit 1
fi

MYSQL_USER="consult"
MYSQL_PASS="consult"
#MYSQL_HOST=pollin1.in2p3.fr
MYSQL_HOST=polui01.in2p3.fr
MYSQL_DB="models03"
MYSQL_OPT="-h${MYSQL_HOST} -u${MYSQL_USER} -p${MYSQL_PASS} ${MYSQL_DB}"

#echo "using mysql options: mysql $MYSQL_OPT"

sql="select name from model group by 1;"
mysql ${MYSQL_OPT} -e "$sql" > $TMPDIR/mokka_cmp_models.list.$$

grep -q $1 $TMPDIR/mokka_cmp_models.list.$$ || { cat $TMPDIR/mokka_cmp_models.list.$$ ; echo ; echo "-- INVALID MODEL: $1 --" ; echo ; echo "Error: Please choose a valid model from the list above" ; echo ; exit 1 ; }
grep -q $2 $TMPDIR/mokka_cmp_models.list.$$ || { cat $TMPDIR/mokka_cmp_models.list.$$ ; echo ; echo "-- INVALID MODEL: $2 --" ; echo ; echo "Error: Please choose a valid model from the list above" ; echo ; exit 1 ; }

echo
echo "========================================="
echo "   comparing ingredients"
echo "========================================="
echo "-----------------------------------------"
sql="select sub_detector, build_order from ingredients where model like 'MODEL' order by sub_detector;"
mysql ${MYSQL_OPT} -e "${sql/MODEL/$1}" > $TMPDIR/mokka_cmp_models.$1.$$
mysql ${MYSQL_OPT} -e "${sql/MODEL/$2}" > $TMPDIR/mokka_cmp_models.$2.$$
$diffcmd $TMPDIR/mokka_cmp_models.$1.$$ $TMPDIR/mokka_cmp_models.$2.$$
echo "-----------------------------------------"
echo
echo


echo
echo "========================================="
echo "   comparing model parameters"
echo "========================================="
echo "-----------------------------------------"
sql="select parameter, default_value from model_parameters where model like 'MODEL' order by parameter;" 
mysql ${MYSQL_OPT} -e "${sql/MODEL/$1}" > $TMPDIR/mokka_cmp_models.$1.$$
mysql ${MYSQL_OPT} -e "${sql/MODEL/$2}" > $TMPDIR/mokka_cmp_models.$2.$$
$diffcmd $TMPDIR/mokka_cmp_models.$1.$$ $TMPDIR/mokka_cmp_models.$2.$$
echo "-----------------------------------------"
echo
echo

# EOF

