#!/bin/bash

###############################################################################
# wrapper script to run mokka with a local database setup
#
# author: Jan Engels - DESY IT
#
# $Id: mokka-wrapper.sh 1103 2010-11-30 08:47:16Z engels $
###############################################################################

uid="mokka-$USER-$(date +%F--%H-%M-%S)-$$"
MOKKA_TMP_DIR=${MOKKA_TMP_DIR:-"${TMPDIR:-/tmp}/$uid"}

# use bash logger
#export MSG_LOG_LEVEL="DEBUG"
export MSG_LOG_FILE=${MSG_LOG_FILE:-"$MOKKA_TMP_DIR/mokka.log"}
export MSG_STDOUT_PREFIX=${MSG_STDOUT_PREFIX:-"[ \${MSG_LEVEL} ] - [\$(basename \$0)]\\\t"}
export MSG_LOG_FILE_PREFIX=${MSG_LOG_FILE_PREFIX:-"[ \$(date +%F--%H-%M-%S) ] - [ \${MSG_LEVEL} ] - [\$(basename \$0)]\\\t"}
export MSG_EXIT_ON_CRITICAL_ERROR=1
. $(dirname $0)/bash_logger.sh || { echo "bash_logger.sh not found" ; exit 1; }


usage(){
cat <<EOT
mokka wrapper script which uses a local database setup (\$Revision: 1103 $)

script requires \$MOKKA_DUMP_FILE pointing to a mokka dump file (may be .tgz or .tar.gz)
current value of \$MOKKA_DUMP_FILE [${MOKKA_DUMP_FILE:-"not set"}]

\$MOKKA_TMP_DIR is used to define where the local database should be set up
current value of \$MOKKA_TMP_DIR [${MOKKA_TMP_DIR}]

\$MOKKA_INIT_DB_SETUP_FILE may be set to an sql file to init local database privileges
this file is loaded after the dump has been imported
current value of \$MOKKA_INIT_DB_SETUP_FILE [${MOKKA_INIT_DB_SETUP_FILE:-"not set"}]

set \$MSG_LOG_FILE to where the log file should go
current value of \$MSG_LOG_FILE [${MSG_LOG_FILE:-"not set"}]

USAGE:
    export MOKKA_DUMP_FILE=/path/to/mokka_dump.sql
    $(basename $0) MOKKA_OPTIONS
EOT
}

cleanup(){
    # save exit code
    exit_code=$?

    if [ $exit_code -eq 2 ] ; then
        usage
        exit $exit_code
    fi

    if [[ $exit_code != 0 ]] ; then

        # show time and traceback log
        echo >&2
        echo >&2
        echo "*** ERROR OCCURRED [ $(date) ]" >&2
        echo "*** ERROR LOG FILE [ $MSG_LOG_FILE ]:" >&2
        echo >&2
        echo >&2
        test -e $MSG_LOG_FILE && cat $MSG_LOG_FILE >&2
        echo >&2
        echo >&2
    fi

    if [ -e "$MOKKA_TMP_DIR/mysql-cleanup.sh" ] ; then
        $MOKKA_TMP_DIR/mysql-cleanup.sh
    fi

    exit $exit_code
}

# cleanup @ exit (or kill)
trap cleanup EXIT

# needed arguments number
test $# -lt 1 && exit 2

# ---------------- script begin ------------------------

mkdir -p $MOKKA_TMP_DIR || { echo "MOKKA_TMP_DIR could not be created" ; exit 1; }

msg INFO "running $(basename $0) (\$Revision: 1103 $)"

type Mokka &>/dev/null || msg CRITICAL "Mokka not found in your \$PATH"

# TODO add cmd line option
#case "$1" in
#    --mokka-dump=*) MOKKA_DUMP_FILE=$(cut -d'=' -f2 <<< "$1") ; shift 1 ;;
#esac

if [ ! -e "$MOKKA_DUMP_FILE" ] ; then
    msg CRITICAL "please set MOKKA_DUMP_FILE to the mokka dump"
fi

msg INFO "setup local mokka database in MOKKA_TMP_DIR [ $MOKKA_TMP_DIR ] ..."
mkdir -vp $MOKKA_TMP_DIR >> $MSG_LOG_FILE 2>&1 

if [ ! -s "$MOKKA_INIT_DB_SETUP_FILE" ] ; then
    cd $(dirname $0)/../
    MOKKA_INIT_DB_SETUP_FILE=$PWD/mokka_init_privileges.sql
    cd $OLDPWD
    if [ ! -s "$MOKKA_INIT_DB_SETUP_FILE" ] ; then
        msg CRITICAL "failed to load default mokka init db script [ $MOKKA_INIT_DB_SETUP_FILE ]"
    fi
    msg INFO "using default mokka init db setup script [ $MOKKA_INIT_DB_SETUP_FILE ]"
fi

$(dirname $0)/mysql-local-db-setup.sh -p $MOKKA_TMP_DIR -d $MOKKA_DUMP_FILE -i $MOKKA_INIT_DB_SETUP_FILE
test $? -eq 0 || msg CRITICAL "failed to setup local mokka database"

if [ "$MOKKA_INIT_DB_SETUP_FILE" = "$MOKKA_TMP_DIR/mokka_init_db_setup.sql" ] ; then
    msg INFO "do a test query for user consult:consult"
    mysql --socket $MOKKA_TMP_DIR/mysql.sock -uconsult -pconsult -e "show databases;" >/dev/null
    test $? -eq 0 || msg ERROR "failed to execute test query"
fi

msg INFO "RUN MOKKA"
Mokka -hlocalhost:$MOKKA_TMP_DIR/mysql.sock $*
mokka_exit_status=$?
msg INFO "Mokka exit status: $mokka_exit_status"

exit $mokka_exit_status

