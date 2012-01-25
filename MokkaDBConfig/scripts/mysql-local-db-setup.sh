#!/bin/bash

###############################################################################
# utility to setup a local mysql database
#
# author: Jan Engels - DESY IT
#
# $Id: mysql-local-db-setup.sh 1545 2011-05-20 16:16:42Z engels $
###############################################################################

# set some default settings
MAX_SOCKET_RETRIES=20   # max number of seconds for opening mysql socket
uid="mysql-$USER-$(date +%F--%H-%M-%S)-$$"
prefix="${TMPDIR:-/tmp}/$uid"
socket_name="mysql.sock"
# socket needs to live in /tmp (causes problems with long paths)
# another possible solution is to place a symlink in /tmp pointing to the long path
# where the real socket lives ($prefix/mysql.sock) and call mysqld_safe with the
# option --socket=/tmp/symlink/mysql.sock
export MYSQL_UNIX_PORT="/tmp/$uid.sock"
export MYSQL_TCP_PORT=3306
admin_script_name="mysql-admin.sh"
admin_script="$prefix/$admin_script_name"
log_file_name="mysql-setup.log"
# per default socket is not visible on the network
skip_networking="--skip-networking"
# root pass generated per default
rootpwd="$(echo $USER | tr a-zA-Z N-Za-mn-z-A-M).${RANDOM:-387634}"


warning(){
cat << EOT

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! WARNING !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!  A random generated password is used for setting up the database and   !!!
!!!  gets stored (without encryption) in the ADMIN script (see above)      !!!
!!!  if you are concerned about security please consider changing the root !!!
!!!  password or erasing it from the admin script. If you do this, be      !!!
!!!  aware that the admin script will not work unless called with the -p   !!!
!!!  ROOT_PASSWORD option.                                                 !!!
!!!  This is also true if INIT_DB_SETUP_FILE changes the root password.    !!!
!!!                                                                        !!!
!!!  DO NOT FORGET TO CLEANUP THE DATABASE WHEN YOU DO NOT NEED IT ANYMORE !!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

EOT
}

usage(){
cat << EOT

Utility to setup local mysql database (\$Revision: 1545 $)


USAGE:

    $(basename $0) [OPTIONS]


OPTIONS:

    -p PREFIX
        define prefix to setup the local database. If not set, installation
        is done on a unique generated directory in \$TMPDIR (if set) or in
        /tmp otherwise, e.g.:
        [ $prefix ]

    -s SYMLINK
        create a symbolic link of the database installation directory in a
        more convenient place given by SYMLINK e.g.: \$HOME/mysql-localdb
        This option is deprecated, please use option -p PREFIX

    -d SQL_DUMP_FILE
        dump file to be imported into database
        tarballs with extension .tgz or .tar.gz are also valid

    -i INIT_DB_SETUP_FILE
        sql file for initializing the database setup (users/privileges/...)
        (please check the WARNING below !!!)

    -P TCP_PORT
        make database visible on the network on the given TCP PORT. The
        default port for mysql is 3306.

    -v VERBOSE_LEVEL
        choose level of verbosity (DEBUG INFO WARNING ERROR)
        DEFAULT: [ INFO ]



ENVIRONMENT VARIABLES:

    TMPDIR: Per default the database is installed to \$TMPDIR (if set) or to
        /tmp inside a unique generated directory, example:
        [ $prefix ]

    MYSQL_UNIX_PORT: If set to the database socket path you may leave out the
        --socket option when connecting to the db

    MYSQL_TCP_PORT: If set to the TCP_PORT (only if option -n is used) you may
        leave out the --port option when connecting to the db

    MYSQL_HOME: This variable may be set to use a custom installation of mysql
        export MYSQL_HOME=/path/to/mysql/installation



USERS AND PRIVILEGES:

    Some examples you might consider adding to your INIT_DB_SETUP_FILE or
    manually enter in the database after the socket is running:

    -- add simple read-only user to a db (without password)
    GRANT SELECT ON <dbname>.* TO 'reader'@'<host>';

    -- add user with simple write permissions to all tables within a db
    GRANT SELECT, UPDATE, INSERT, DELETE ON <dbname>.* TO 'writer'@'<host>'
        IDENTIFIED BY 'password';

    -- add admin user to a db
    GRANT ALL ON <dbname>.* TO '<user>'@'<host>' IDENTIFIED BY 'password';

    -- add super user
    GRANT ALL PRIVILEGES ON *.* TO '<user>'@'<host>' IDENTIFIED BY 'password'
        WITH GRANT OPTION;

    -- remove all user privileges to a db
    REVOKE ALL ON <dbname>.* FROM '<user>'@'<host>';

    -- wipe out user
    DROP USER '<user>'@'<host>';

    -- what should i put into <host> ?

      * 'localhost'   - user can only connect from the local machine where
                        the db is running

      * '123.abc.net' - user can only connect from host 123.abc.net

      * '123'         - user can only connect from host 123 in the same
                        network where db is running

      * '%'           - user can connect from ANY host



CLEANUP / WIPEOUT LOCAL DATABASE:

    After your job has finished and you do not need to use the database
    anymore you should run the admin script generated inside the PREFIX
    directory to shutdown the database socket and remove all remaining rests,
    example:
    $admin_script cleanup



FINAL NOTES:

    If you experience problems connecting to the database make sure you are
    using option --no-defaults in your mysql commandos and that permissions
    were set correctly (in case option -i INIT_DB_SETUP_FILE was used).

    After the database has been successfully installed there will be a socket
    created inside /tmp which you can use to connect to the database, e.g.:
    [ $MYSQL_UNIX_PORT ]

    The socket must live in /tmp because of possible problems when exceeding
    the unix max socket path length.

    Some of the following commands are useful to check for open mysql
    sockets/ports/processes running on your machine:
    netstat -ln | grep mysql      # check for open mysql sockets
    netstat -netap | grep mysql   # check for open mysql tcp/ip ports (linux)
    lsof -nPi | grep mysql        # same as before (but also works on mac)
    ps x | grep [m]ysqld          # mysqld* processes running (current user)
    ps -ef | grep [m]ysqld        # mysqld* processes running (all users)

$(warning)

EOT
}

# flag for cleaning up in the exit trap
cleanup_after_exit=1

cleanup(){
    # save exit code
    exit_code=$?

    if [ $exit_code -eq 2 ] ; then
        usage
        exit $exit_code
    fi

    # test if an error ocurred
    if [ $cleanup_after_exit -eq 1 ] ; then

        echo -e "\n\n\n\n\n" >&2
        echo "*** ERROR OCCURRED [ $(date) ]" >&2
        echo "*** ERROR LOG FILE [ $MSG_LOG_FILE ]:" >&2
        echo >&2
        test -e "$MSG_LOG_FILE" && cat "$MSG_LOG_FILE" >&2
        echo >&2
        echo >&2
        test -e "$admin_script" && $admin_script cleanup
        echo >&2
        echo "mysql sockets running on $HOSTNAME:" >&2
        netstat -ln 2>/dev/null | grep "mysql" >&2
        echo "ports used by mysql on $HOSTNAME:" >&2
        lsof -nPi 2>/dev/null | grep "mysqld" >&2
    fi

    exit $exit_code
}

# some notes on traps:
# EXIT (or 0) means the trap is ALWAYS called despite how your script ends (except kill -9).
# this means: trap is called if you press CTRL-C, if you exit the terminal or if your script just happilly runs through
# but this also means that:
#   EXIT INT ends up calling the trap TWICE (if CTRL-C is pressed) and only once if script runs through
#   EXIT HUP ends up calling the trap TWICE (if terminal is closed) and only once if script runs through
#
# also keep in mind that gnome-terminal does NOT kill your running process with SIGHUP if you close the terminal (unlike xterm)
# some useful help:
# kill -l
# man kill
# man 7 signal

#trap cleanup EXIT HUP INT QUIT ABRT TERM    # just need to trap EXIT (see notes above)
#trap cleanup 0 1 2 3 6 15
trap cleanup EXIT 

# parse script arguments
# prefix getopt string with colon for quiet mode
while getopts ":v:d:p:s:i:P:h" o ; do
    #echo "DEBUG: $o $OPTARG"
    case "$o" in
        'v') MSG_LOG_LEVEL=$OPTARG ;;
        'd') sqldump=$OPTARG ;;
        'p') prefix=$OPTARG ;;
        's') symlink=$OPTARG ;;
        'i') user_init_sql_file=$OPTARG ;;
        'P') unset skip_networking ; export MYSQL_TCP_PORT=$OPTARG ;;
        'h') exit 2 ;;
        '?') exit 2 ;;
        ':') echo "$0: option -$OPTARG requires an argument!" ; exit 2 ;;
        *) echo "unknown option: $OPTARG" ; exit 2 ;;
    esac
done

# set $1 to first non-option argument
shift $(( $OPTIND - 1 ))

# if OPTIND is not reset to 1 it can lead to strange behaviour when running
# the bash script more than once (ghost options set from previous run)
OPTIND=1 # reset OPTIND

# needed arguments number
#test $# -ne 1 && exit 2

mkdir -vp $prefix || { echo "failed to create installation directory [ $prefix ] " >&2 ; exit 1 ; }

# expand prefix to absolute path
pushd $prefix >/dev/null
prefix=$PWD
popd >/dev/null

# set some internal variables
datadir="$prefix/data"
pidfile="$prefix/$HOSTNAME.pid"
logfile="$prefix/$HOSTNAME.log"
logerrfile="$prefix/$HOSTNAME.err"
admin_script="$prefix/$admin_script_name"
cleanup_script="$prefix/mysql-cleanup.sh"
env_init_script="$prefix/mysql-env-init.sh"

# mysql_install_db tries to create a test file in $TMPDIR before setting up
# initial database settings. If TMPDIR is set to a non-existing directory
# or points to an exotic file system it may cause problems therefore an
# option --tmpdir exists in mysql versions >= 5.0.45 but does not work with
# older versions. Simplest solution is to just unset TMPDIR before running
# mysql_install_db
unset TMPDIR

#mysql_install_db_options="--tmpdir=/tmp"
# --log-warnings=2
mysql_install_db_options="--no-defaults $skip_networking --datadir=$datadir"
mysqld_safe_options="--no-defaults $skip_networking --datadir=$datadir --pid-file=$pidfile --log=$logfile --log-error=$logerrfile --user=$USER"
mysqladmin_options="--no-defaults"
mysql_options="--no-defaults"

# since MYSQL_UNIX_PORT is set we can skip option --socket
#mysqladmin_options="$mysqladmin_options --socket=$MYSQL_UNIX_PORT"
#mysqld_safe_options="$mysqld_safe_options --socket=$MYSQL_UNIX_PORT"
#mysql_options="$mysql_options --socket=$MYSQL_UNIX_PORT"


# for backwards compatibility
test -d "$MYSQL" && export MYSQL_HOME="$MYSQL"

if test -d "$MYSQL_HOME" ; then

    # set environment for using mysql installation in $MYSQL_HOME
    export PATH=$MYSQL_HOME/bin:$PATH
    export LD_LIBRARY_PATH=$MYSQL_HOME/lib:$MYSQL_HOME/lib/mysql:$LD_LIBRARY_PATH

    # use basedir option to avoid FATAL ERROR:
    # Could not find SQL file '/opt/products/mysql/5.0.45/share/mysql/mysql_system_tables.sql'
    # FIXME do we need --basedir if MYSQL_HOME is set ?
    mysql_install_db_options="$mysql_install_db_options --basedir=$MYSQL_HOME"
    mysqld_safe_options="$mysqld_safe_options --basedir=$MYSQL_HOME"
fi


# use bash logger
MSG_LOG_FILE=${MSG_LOG_FILE:-"$prefix/$log_file_name"}
MSG_EXIT_ON_CRITICAL_ERROR=1
. $(dirname $0)/bash_logger.sh || { echo "bash_logger.sh not found" ; exit 1; }

# ---------------- script begin ------------------------

msg INFO "running $(basename $0) (\$Revision: 1545 $)"

# check if required mysql commands are available
for cmd in mysql mysql_install_db mysqld_safe mysqladmin ; do
    type $cmd &>/dev/null || msg CRITICAL "$cmd not available!"
done

# test if data dir already exists
test -e "$datadir" && { cleanup_after_exit=0 ; msg CRITICAL "PREFIX [ $datadir ] already exists!" ; }

# test if symlink dir already exists
test -e "$symlink" && msg CRITICAL "SYMLINK [ $symlink ] already exists!"

msg INFO "installing mysql database to [ $prefix ] ..."

msg INFO "creating mysql env init script [ $env_init_script ] ..."
# ---------------------------------------------------------------------------
cat > $env_init_script << EOF
set -x
export MYSQL_UNIX_PORT=$MYSQL_UNIX_PORT
export MYSQL_TCP_PORT=$MYSQL_TCP_PORT
set +x
EOF
# ---------------------------------------------------------------------------

msg INFO "creating admin script [ $admin_script ] ..."
# ---------------------------------------------------------------------------
cat > $admin_script << EOF
#!/bin/sh
ROOT_PASSWORD="$rootpwd"

usage(){
cat << EOT

Utility to administrate your local mysql database (\\\$Revision: 1545 $)


USAGE:

    $(basename $0) [OPTIONS] MODE


MODE:
    startup
    shutdown
    cleanup


OPTIONS:
    
    -p ROOT_PASSWORD
        use this if you have changed the default generated root password
 

EOT
}

# parse script arguments
# prefix getopt string with colon for quiet mode
while getopts ":p:h" o ; do
    #echo "DEBUG: \$o \$OPTARG"
    case "\$o" in
        'p') ROOT_PASSWORD=\$OPTARG ;;
        'h') usage ; exit 2 ;;
        '?') usage ; exit 2 ;;
        ':') echo "\$0: option -\$OPTARG requires an argument!" ; usage ; exit 2 ;;
        *) echo "unknown option: \$OPTARG" ; usage; exit 2 ;;
    esac
done

# set \$1 to first non-option argument
shift \$(( \$OPTIND - 1 ))

# if OPTIND is not reset to 1 it can lead to strange behaviour when running
# the bash script more than once (ghost options set from previous run)
OPTIND=1 # reset OPTIND

# needed arguments number
test \$# -ne 1 && { usage; exit 2 ; }

case "\$1" in
    st*) mode=startup ;;
    sh*) mode=shutdown ;;
    c*) mode=cleanup ;;
    *) echo "unknown option: \$1" ; usage; exit 2 ;;
esac

export PATH="$PATH:\$PATH"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:\$LD_LIBRARY_PATH"
export MYSQL_UNIX_PORT=$MYSQL_UNIX_PORT
export MYSQL_TCP_PORT=$MYSQL_TCP_PORT

if [ "\$mode" = "startup" ] ; then
    mysqld_safe $mysqld_safe_options &
    test \$? -eq 0 || { echo "failed to execute mysqld_safe" ; exit 1 ; }
fi

if [ "\$mode" = "shutdown" -o "\$mode" = "cleanup" ] ; then
    socket_grep=\$(netstat -ln 2>/dev/null | grep "\$MYSQL_UNIX_PORT")
    if [ -n "\$socket_grep" ] ; then
        echo "shutdown mysql socket [\$MYSQL_UNIX_PORT]"
        mysqladmin $mysqladmin_options -uroot -p\$ROOT_PASSWORD shutdown >/dev/null 2>&1
    fi
    sleep 1
    pidfile=$pidfile
    test -e "\$pidfile" && pidnum=\$(cat \$pidfile)
    test -n "\$pidnum" && { echo "kill process of db daemon [ \$pidnum ]" && kill \$pidnum ; }
    sleep 1
fi

if [ "\$mode" = "cleanup" ] ; then
    test -e "$prefix" && { echo "remove directory [ $prefix ]" && rm -rf "$prefix" ; }
    test -L "\$MYSQL_UNIX_PORT" -a ! -e "\$MYSQL_UNIX_PORT" && rm -vf "\$MYSQL_UNIX_PORT"
    test -L "$symlink" -a ! -e "$symlink" && rm -vf "$symlink"
fi

exit 0
EOF
chmod -v 700 $admin_script >> $MSG_LOG_FILE
# ---------------------------------------------------------------------------

msg INFO "creating cleanup script [ $cleanup_script ] ..."
# ---------------------------------------------------------------------------
cat > $cleanup_script << EOF
#!/bin/sh
# this script is left for backwards compatibility
if [ \$# -eq 1 ] ; then
    $admin_script -p\$1 cleanup
else
    $admin_script cleanup
fi
exit 0
EOF
chmod -v 700 $cleanup_script >> $MSG_LOG_FILE
# ---------------------------------------------------------------------------



if [ -n "$sqldump" ] ; then
    test -s "$sqldump" || msg CRITICAL "SQL_DUMP_FILE [ $sqldump ] not found or corrupted!"

    if [ "${sqldump: -7}" = ".tar.gz" -o "${sqldump: -4}" = ".tgz" ] ; then
        msg DEBUG "searching for sql dump file inside tarball [ $sqldump ] ..."
        sqldumpfile=$(tar tzf $sqldump | grep '.sql' | sed q)
        if [ -z "$sqldumpfile" ] ; then
            msg CRITICAL "could not find sql dump file inside tarball [ $sqldump ]"
        else
            msg DEBUG "found sql dump file [ $sqldumpfile ] ..."
            sqldumpfile=$prefix/$sqldumpfile
        fi
        msg DEBUG "untar SQL_DUMP_FILE [ $sqldump ] ..."
        tar -C $prefix -xzvf $sqldump >> $MSG_LOG_FILE
        test $? -eq 0 || msg CRITICAL "failed to untar SQL_DUMP_FILE"
    else
        sqldumpfile=$sqldump
    fi
fi

# show mysql sockets running on this machine
for sock in $(netstat -ln 2>/dev/null | grep "mysql" | awk '{print $9}') ; do
    msg DEBUG "active mysql socket running on $HOSTNAME: $sock"
done

msg INFO "running mysql_install_db ..."
msg DEBUG "mysql_install_db $mysql_install_db_options"
mysql_install_db $mysql_install_db_options >> $MSG_LOG_FILE 2>&1
test $? -eq 0 || msg CRITICAL "failed to execute mysql_install_db"

# pushd in $MYSQL_HOME before running mysqld_safe
# more details in http://dev.mysql.com/doc/mysql/en/mysqld_safe.html
# or http://bugs.mysql.com/bug.php?id=32163
test -d "$MYSQL_HOME" && pushd $MYSQL_HOME >/dev/null

msg INFO "running mysqld_safe ..."
msg DEBUG "mysqld_safe $mysqld_safe_options &"
mysqld_safe $mysqld_safe_options >>$MSG_LOG_FILE 2>&1 &
test $? -eq 0 || msg CRITICAL "failed to execute mysqld_safe"

test -d "$MYSQL_HOME" && popd >/dev/null

msg_n INFO "waiting for socket to open ..."
while [ $(netstat -ln 2>/dev/null | grep -q "$MYSQL_UNIX_PORT")$? -ne 0 ] ; do
    echo -n .
    sleep 1
    MAX_SOCKET_RETRIES=$(( $MAX_SOCKET_RETRIES - 1 ))
    test $MAX_SOCKET_RETRIES -eq 0 && break
done
echo | tee -a $MSG_LOG_FILE
if [ $MAX_SOCKET_RETRIES -eq 0 ] ; then
    test -z "$skip_networking" && msg ERROR "port $MYSQL_TCP_PORT already in use"
    msg CRITICAL "failed to open socket"
fi

msg INFO "socket running [ $MYSQL_UNIX_PORT ] ..."

msg INFO "changing root password ..."
mysqladmin $mysqladmin_options -uroot password $rootpwd

if [ -n "$sqldumpfile" ] ; then
    msg INFO "importing SQL_DUMP_FILE [ $sqldump ] ..."
    mysql $mysql_options -uroot -p$rootpwd < $sqldumpfile
    test $? -eq 0 || msg CRITICAL "failed to import dump"
fi

msg INFO "removing anonymous user"
mysql $mysql_options -uroot -p$rootpwd <<< "DELETE FROM mysql.user WHERE User='' ; FLUSH PRIVILEGES ; "
test $? -eq 0 || msg ERROR "failed to delete anonymous user"


if [ -s "$user_init_sql_file" ] ; then
    msg INFO "loading INIT_DB_SETUP_FILE [ $user_init_sql_file ] ..."
    mysql $mysql_options -uroot -p$rootpwd < $user_init_sql_file
    test $? -eq 0 || msg CRITICAL "failed to load INIT_DB_SETUP_FILE [ $user_init_sql_file ]"

    msg DEBUG "creating symbolic link [ $prefix/$( basename $user_init_sql_file) ] ..."
    ln -sv $user_init_sql_file $prefix >> $MSG_LOG_FILE
fi

msg DEBUG "creating symbolic link [ $prefix/$socket_name ] ..."
ln -sv $MYSQL_UNIX_PORT $prefix/$socket_name >> $MSG_LOG_FILE

if [ -n "$symlink" ] ; then
    msg INFO "creating symbolic link [ $symlink ] ..."
    ln -sv $prefix $symlink >> $MSG_LOG_FILE
    test $? -eq 0 || msg CRITICAL "failed to create symbolic link [ $symlink ]"
fi

test_query_cmd="select user(), version(), current_date, current_time, now(); show databases; show variables;"
msg INFO "do a test query ..."
msg DEBUG "test query: $test_query_cmd"
mysql $mysql_options -uroot -p$rootpwd -e "$test_query_cmd" >> $MSG_LOG_FILE
test $? -eq 0 || msg CRITICAL "test query failed"

if [ "$MSG_ERRORS" != 0 ] ; then
    msg WARNING "non critical errors were found during the installation, please check [ $MSG_LOG_FILE ] for more details..."
fi

msg INFO "installation finished successfully!"

msg INFO "------------------------------------------------------------------------------"
msg INFO ""
msg INFO "connect to the database by either running mysql with the full command line options:"
msg INFO "mysql $mysql_options --socket=$MYSQL_UNIX_PORT --port=$MYSQL_TCP_PORT -uroot -p$rootpwd"
msg INFO ""
msg INFO "or by sourcing the following env script and running mysql as follows:"
msg INFO ". $env_init_script"
msg INFO "mysql $mysql_options -uroot -p$rootpwd"
msg INFO ""
msg INFO "if you are concerned about security read the WARNING by running:"
msg INFO "$0 -h"
msg INFO ""
msg INFO "------------------------------------------------------------------------------"
msg INFO "DO NOT FORGET TO CLEANUP THE DATABASE WHEN YOU DO NOT NEED IT ANYMORE!"
msg INFO "CLEANUP SCRIPT: $admin_script cleanup"
msg INFO "------------------------------------------------------------------------------"

cleanup_after_exit=0 # flag which prevents cleanup to be called in exit trap
exit 0 # exit trap gets called after this line !!

# EOF

