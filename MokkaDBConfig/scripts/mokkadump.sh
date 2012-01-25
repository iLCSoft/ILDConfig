#!/bin/sh
#
# Get a dump of the central Mokka geometry database server
# Adrian Vogel, version of 2007-02-20
#
# - create an empty dump file
# - get a list of all available databases
# - remove the list header and unneeded databases (information_schema, mysql, test)
# - append a header section for each database to the dump file
# - get the contents of each database with mysqldump
# - remove problematic properties (DEFAULT CHARSET, ENGINE)
# - append the database contents to the dump file

if [ "$#" -eq 0 -o "$#" -gt 2 ]
then
    echo "Usage: $(basename "$0") DUMPFILE.SQL [HOST]" 1>&2
    exit 1
fi

MYSQL_DUMP="$1"
MYSQL_USER="consult"
MYSQL_PASS="consult"
#MYSQL_HOST="${2:-pollin1.in2p3.fr}"
MYSQL_HOST="${2:-polui01.in2p3.fr}"
MYSQL_OPT="-h${MYSQL_HOST} -u${MYSQL_USER} -p${MYSQL_PASS}"
MYSQL_DUMP_OPT="--quote-names --lock-tables=false"

rm -f "${MYSQL_DUMP}"
touch "${MYSQL_DUMP}"

for MYSQL_DB in $(echo 'SHOW DATABASES;' | mysql ${MYSQL_OPT} | sed '1d;/^information_schema$/d;/^mysql$/d;/^test$/d')
do
    cat >> "${MYSQL_DUMP}" << EOT
CREATE DATABASE /*!32312 IF NOT EXISTS*/ \`${MYSQL_DB}\`;
USE ${MYSQL_DB};

EOT
    mysqldump ${MYSQL_OPT} ${MYSQL_DUMP_OPT} ${MYSQL_DB} | sed -e '
    s/ DEFAULT CHARSET=[a-zA-Z0-9]\{1,\}//g
    s/ PACK_KEYS=[a-zA-Z0-9]\{1,\}//g
    s/ ENGINE=[a-zA-Z0-9]\{1,\}//g
    s/ TYPE=[a-zA-Z0-9]\{1,\}//g
    /^\/\*!.\{1,\}\*\/;$/d
    ' | cat >> "${MYSQL_DUMP}"
done
