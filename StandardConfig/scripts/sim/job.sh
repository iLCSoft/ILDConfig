#! /bin/bash

##############################################################################
# run simulation job on the Grid.
#
# in case of errors user defined exit codes are used in range from 64 to 113
#
# parts of this script were adopted from the original runjob.sh written by
# D. Martsch and from the modified runjob.sh (I. Marchesini)
#
# Jan Engels, DESY - IT
# 2012/02/10
##############################################################################


#set -e # exit in case any command fails
#set -x # debug modus

echo
echo "======================== starting $0 =================================="
echo

# ----- check for required tools ---------------------------------------------
type wget || { echo "failed to find wget" ; exit 65 ; }
# ----------------------------------------------------------------------------




# ----- grid settings --------------------------------------------------------
VO_NAME="ilc"
type lcg-infosites &>/dev/null
if [ $? -eq 0 ] ; then
    export LFC_HOST=$(lcg-infosites --vo $VO_NAME lfc 2>/dev/null)
fi
if [ -z "$LFC_HOST" ] ; then
    echo "setting LFC_HOST to default: grid-lfc.desy.de"
    export LFC_HOST="grid-lfc.desy.de"
fi
export LFC_HOME="/grid/$VO_NAME"
export LCG_GFAL_VO=$VO_NAME
# ----------------------------------------------------------------------------



# ----- global job settings --------------------------------------------------
uid="$VO_NAME-$USER-$(date +%F--%H-%M-%S)-$$"
JOB_TMPDIR=${JOB_TMPDIR:-"${TMPDIR:-/tmp}/$uid"}
JOB_STARTDIR=$PWD
LOG_FILE_OVERWRITE=${LOG_FILE_OVERWRITE:-force} # abort
OUTPUT_FILE_OVERWRITE=${OUTPUT_FILE_OVERWRITE:-force} # abort
# ----------------------------------------------------------------------------




# ----- simjob settings ------------------------------------------------------
ARCH=x86_64_gcc41_sl5
# in some sites SOCKET MUST BE CREATED IN /tmp !! $TMPDIR or $HOME DO NOT WORK !!
export MOKKA_TMP_DIR="$TMPDIR/mokkadb$$"
test -n "$GRID_JOB" && export MOKKA_TMP_DIR="$HOME/mokkadb$$"
# ----------------------------------------------------------------------------




##############################################################################
# FUNCTION DEFINITIONS
##############################################################################

usage(){
    cat << EOT
    usage: $(basename $0) ARGS
        ARGS:
            JOB_ID                # the job database id
            JOB_PREFIX            # prefix for naming the job output files
            SW_VER                # the ILCSoft version to use
            CFG_VER               # the ILDConfig version to use
            START_EVENT           # the start event number
            TOTAL_EVENTS          # total number of events to be reconstructed
            PROCESS               # process string
            ENERGY                # energy
            POL_EP                # polarisation ep
            POL_EM                # polarisation em
            CROSS_SECTION         # cross section
            DETECTOR_MODEL        # detector model
            PHYSICS_LIST          # the physics list used for the simulation
            RANDOM_SEED           # random seed
            OUTPUT_DIR            # directory for storing output files
            LOG_OUTPUT_DIR        # directory for storing log files
            STORAGE_ELEMENT       # storage element for storing output files
            INPUT_FILE            # input file
EOT
}

# FIXME put in hepshlib
normpath(){
    echo "$(python -c "import os,sys; print os.path.normpath(sys.argv[1])" "$1")"
}

# ----------------------------------------------------------------------------
# define a trap for cleaning up stuff and copy log tarball when script ends
# ----------------------------------------------------------------------------
cleanup(){
    # save exit code
    exit_code=$?

    # print usage
    if [ $exit_code -eq 2 ] ; then
        usage
        exit $exit_code
    fi

    echo
    echo ending: $0
    echo exitcode: $exit_code
    echo time: $(date -u)
    echo
    echo "==================== cleanup trap ==========================="
    echo

    # remove annoying log files...
    rm -f {RECV,SENT,TEST}.log

    # show directory contents
    c="\ls -lA"
    echo ; echo "> $c" ; eval $c ; echo


    # -------------- create log tarball for this job ---------------------
    echo "create tarball of logfiles"

    mkdir -v $LOG_FILE_DIR

    # job specific stuff
    cp -vf *.{sh,log,tgz,xml,steer,g4macro} $LOG_FILE_DIR

    # no need to copy job-wrapper.sh and MokkaDBConfig.tgz
    rm -vf $LOG_FILE_DIR/job-wrapper.sh
    rm -vf $LOG_FILE_DIR/MokkaDBConfig.tgz

    # create tarball
    tar czf $LOG_FILE_NAME $LOG_FILE_DIR
    tar_rc=$?
    # --------------------------------------------------------------------


    # copy log tarball to SE and update database
    # only for grid jobs and if mokka has been executed
    if [ -n "$GRID_JOB" -a -n "$mokka_exit_code" ] ; then

        # -------------- copy log tarball to the grid ------------------------
        if [ $tar_rc -eq 0 ] ; then
            echo "uploading log tarball to the grid"

            lfc-mkdir -p $LOG_OUTPUT_DIR
            grid-ul-file.py --timeout 3600 --overwrite=$LOG_FILE_OVERWRITE --storage-element=$STORAGE_ELEMENT $LOG_FILE_NAME $LOG_FILE
            test $? -ne 0 && { echo "ERROR: failed to upload log tarball, setting exit code from $exit_code to 87 !!" >&2 ; exit_code=87 ; }

        else
            echo "ERROR: failed to create log tarball, setting exit code from $exit_code to 87 !!" >&2
            exit_code=87
        fi
        # --------------------------------------------------------------------


        # -------------- update database -------------------------------------
        job_status='c'
        test $exit_code -ne 0 && job_status='f'
        test -n "$uses_sql" && sql_write "call check_job( $JOB_ID, '$job_status', $exit_code )"
        # --------------------------------------------------------------------

    fi

    # -------------- cleanup rests ---------------------------------------
    test -d "$JOB_TMPDIR" -a -n "$GRID_JOB" && rm -rf "$JOB_TMPDIR"
    test -d "$MOKKA_TMP_DIR" && rm -rf "$MOKKA_TMP_DIR"
    # --------------------------------------------------------------------


    echo "====================== job end =============================="
    exit $exit_code
}
trap cleanup EXIT

##### END OF FUNCTION DEFINITIONS ############################################



# ----------------------------------------------------------------------------
# check script syntax
# ----------------------------------------------------------------------------

if [ $# -ne 1 -a $# -ne 18 ]; then
    exit 2
fi

JOB_ARGS="$*"
JOB_ID=$1


# ----------------------------------------------------------------------------
# job starts here
# ----------------------------------------------------------------------------


mkdir -vp $JOB_TMPDIR
cd $JOB_TMPDIR



# ----- gridtools ------------------------------------------------------------
if [ ! -d gridtools ] ; then
    if [ ! -e gridtools.tgz ] ; then
        wget "http://svnsrv.desy.de/viewvc/ilctools/mcprdsys/trunk/gridtools/?view=tar" -O gridtools.tgz
        test $? -eq 0 || { echo "failed to download gridtools" ; exit 65 ; }
    fi
    tar xzf gridtools.tgz
    test $? -eq 0 || { echo "failed to untar gridtools" ; exit 65 ; }
fi
export GRIDTOOLSDIR="$PWD/gridtools"
export PYTHONPATH="$GRIDTOOLSDIR/heppylib:$PYTHONPATH"
export PATH="$GRIDTOOLSDIR:$PATH"
# ----- logging ------
export MSG_EXIT_ON_CRITICAL_ERROR=1
export MSG_LOG_FILE=${MSG_LOG_FILE:-"$JOB_TMPDIR/job.log"}
export MSG_STDOUT_PREFIX=${MSG_STDOUT_PREFIX:-"[ \${MSG_LEVEL} ] - [\$(basename \$0)]\\\t"}
export MSG_LOG_FILE_PREFIX=${MSG_LOG_FILE_PREFIX:-"[ \$(date +%F--%H-%M-%S) ] - [ \${MSG_LEVEL} ] - [\$(basename \$0)]\\\t"}
. $GRIDTOOLSDIR/hepshlib/bash_logger.sh
# ----------------------------------------------------------------------------



usage >> $MSG_LOG_FILE
msg INFO "RUNNING: $0 $JOB_ARGS"


msg INFO "copy input files from $JOB_STARTDIR"
for i in $JOB_STARTDIR/* ; do
    test ! -d $i && { test -e $(basename $i) || cp -va $i . ; }
done

# if job-wrapper.sh was called to run this script (job.sh) we can get MokkaDBConfig from JOB_STARTDIR
test -d "$JOB_STARTDIR/MokkaDBConfig" && ln -s "$JOB_STARTDIR/MokkaDBConfig"


# ----------------------------------------------------------------------------
# parse command line arguments
# ----------------------------------------------------------------------------
if [ $# -eq 1 ]; then

    # FIXME put all this in mokka-steer-gen.py

    export uses_sql=1

    export PATH=$VO_ILC_SW_DIR/ilcsoft/mysql/5.0.45/bin:$PATH

    export SQL_CACHE_DEBUG=1
    export SQL_CACHE_RANGE=3
    . $GRIDTOOLSDIR/hepshlib/querysql.sh
    test $? -eq 0 || msg CRITICAL 67 "failed to initialize querysql"

    ping -c3 -q $SQL_CACHE_HOST
    test $? -eq 0 || msg CRITICAL 68 "failed to ping SQL_CACHE_HOST: $SQL_CACHE_HOST"

    # notify database that job is running
    if [ -n "$GRID_JOB" ] ; then
        sql_write "call check_job( $JOB_ID, 'r', NULL )"
        test $? -eq 0 || msg CRITICAL 69 "failed to update database"
    fi

    sql_cache "select * from sjob where id=$JOB_ID"

    JOB_PREFIX=$(sql_query sjob JOB_PREFIX)
    SW_VER=$(sql_query sjob SW_VER)
    CFG_VER=$(sql_query sjob CFG_VER)
    START_EVENT=$(sql_query sjob START_EVENT)
    TOTAL_EVENTS=$(sql_query sjob TOTAL_EVENTS)
    PROCESS=$(sql_query sjob PROCESS)
    ENERGY=$(sql_query sjob ENERGY)
    POL_EP=$(sql_query sjob POL_EP)
    POL_EM=$(sql_query sjob POL_EM)
    CROSS_SECTION=$(sql_query sjob CROSS_SECTION)
    DETECTOR_MODEL=$(sql_query sjob DETECTOR_MODEL)
    PHYSICS_LIST=$(sql_query sjob PHYSICS_LIST)
    RANDOM_SEED=$(sql_query sjob RANDOM_SEED)
    OUTPUT_DIR=$(sql_query sjob OUTPUT_DIR)
    LOG_OUTPUT_DIR=$(sql_query sjob LOG_OUTPUT_DIR)
    STORAGE_ELEMENT=$(sql_query sjob STORAGE_ELEMENT)
    INPUT_FILE=$(sql_query sjob INPUT_FILE)

else

    #JOB_ID=$1
    shift
    JOB_PREFIX=$1
    shift
    SW_VER=$1
    shift
    CFG_VER=$1
    shift
    START_EVENT=$1
    shift
    TOTAL_EVENTS=$1
    shift
    PROCESS=$1
    shift
    ENERGY=$1
    shift
    POL_EP=$1
    shift
    POL_EM=$1
    shift
    CROSS_SECTION=$1
    shift
    DETECTOR_MODEL=$1
    shift
    PHYSICS_LIST=$1
    shift
    RANDOM_SEED=$1
    shift
    OUTPUT_DIR=$1
    shift
    LOG_OUTPUT_DIR=$1
    shift
    #SRM_PREFIX=$1
    STORAGE_ELEMENT=$1
    shift
    INPUT_FILE=$1
    shift

fi

test -z "$GRID_JOB" && TOTAL_EVENTS=1
LOG_FILE_DIR="$JOB_PREFIX"
LOG_FILE_NAME="$LOG_FILE_DIR.tar.gz"
OUTPUT_FILE_NAME="$JOB_PREFIX.slcio"
INPUT_FILE_NAME=$(basename $INPUT_FILE)
OUTPUT_DIR=$(normpath "$OUTPUT_DIR")
LOG_OUTPUT_DIR=$(normpath "$LOG_OUTPUT_DIR")
OUTPUT_FILE=$(normpath "$OUTPUT_DIR/$OUTPUT_FILE_NAME")
LOG_FILE=$(normpath "$LOG_OUTPUT_DIR/$LOG_FILE_NAME")
# ----------------------------------------------------------------------------





# ----------------------------------------------------------------------------
# prepare for running Mokka job
# ----------------------------------------------------------------------------


# ------- run basic system tests ---------------------------------------------
msg INFO "run basic system tests..."
$GRIDTOOLSDIR/hepshlib/grid-wn-info.sh > wn_info.log
test $? -eq 0 || msg CRITICAL 70 "failed to pass basic system tests"
# ----------------------------------------------------------------------------



# ------- setup ilcsoft ------------------------------------------------------
ILCSOFT="$VO_ILC_SW_DIR/ilcsoft/$ARCH"
# check if required ilcsoft version is available on the grid
if [ ! -r "$ILCSOFT/$SW_VER" ] ; then

    # download an ilcsoft version not yet installed on the grid
    tarball=ilcsoft-$SW_VER-$ARCH-full.tar.gz
    if [ ! -d ilcsoft ] ; then
        if [ ! -e "$tarball" ] ; then
            msg INFO "downloading ilcsoft tarball..."
            wget "http://ilcsoft.desy.de/ilcsoft-bin-releases/$tarball"
            test $? -eq 0 || msg CRITICAL 71 "failed to download ilcsoft"
        fi
        msg INFO "unpacking ilcsoft tarball..."
        tar -xzf $tarball
        test $? -eq 0 || msg CRITICAL 71 "failed to unpack ilcsoft tarball"
        rm -f $tarball
    fi

    #msg INFO "applying patch..."
    #tarball=ilcsoft-$SW_VER-$ARCH-patch-0001.tgz
    #wget "http://ilcsoft.desy.de/data/production/patches/$tarball" && tar -xzvf $tarball && rm -f $tarball
    #test $? -eq 0 || msg CRITICAL 71 "failed to download ilcsoft patch"

    export ILCSOFT="$PWD/ilcsoft/$ARCH"
fi

msg INFO "initialize ilcsoft..."
. $ILCSOFT/init_ilcsoft.sh $SW_VER
test $? -eq 0 || msg CRITICAL 71 "failed to initialize ilcsoft"
# ----------------------------------------------------------------------------




# ----- setup ildconfig ------------------------------------------------------
ILDCONFIG="$VO_ILC_SW_DIR/ilcsoft/ILDConfig"
if [ ! -r "$ILDCONFIG/$CFG_VER" ] ; then
    # svn is not available on the grid.. we need to use wget
    if [ ! -r MokkaDBConfig ] ; then
        tarball=ILDConfig.tgz
        if [ ! -e "$tarball" ] ; then
            # need to use websvn due to broken symlinks when using viewvc (affects MokkaDBConfig)
            wget "http://svnsrv.desy.de/websvn/wsvn/General.marlinreco/ILDConfig/tags/$CFG_VER/?op=dl&isdir=1" -O $tarball
            test $? -eq 0 || { echo "failed to download ILDConfig" ; exit 72 ; }
        fi
        tar --strip-components 1 -xzf $tarball
        test $? -eq 0 || { echo "failed to untar ILDConfig" ; exit 72 ; }

    fi
    export ILDCONFIG=$PWD
fi
# currently only MokkaDBConfig is needed...
. $ILDCONFIG/MokkaDBConfig/init.sh
test $? -eq 0 || { echo "failed to initialize MokkaDBConfig" ; exit 72 ; }
# ----------------------------------------------------------------------------




# ------- check for existing job output --------------------------------------
msg INFO "check if job output files already exists..."
c="lfc-ls $OUTPUT_FILE 2>/dev/null"
msg DEBUG "> $c"
r=$(eval $c)
if [ -z "$r" ] ; then
    msg INFO "job output not found - OK!"
else
    msg WARNING "job output file [ $OUTPUT_FILE ] already exists"
    test "$OUTPUT_FILE_OVERWRITE" = "force" || msg CRITICAL 81 "OUTPUT_FILE_OVERWRITE=$OUTPUT_FILE_OVERWRITE"
fi
# ----------------------------------------------------------------------------




# ------- check for existing log tarball -------------------------------------
msg INFO "check if job log file already exists..."
c="lfc-ls $LOG_FILE 2>/dev/null"
msg DEBUG "> $c"
r=$(eval $c)
if [ -z "$r" ] ; then
    msg INFO "job output not found - OK!"
else
    msg WARNING "job logfile [ $LOG_FILE ] already exists"
    test "$LOG_FILE_OVERWRITE" = "force" || msg CRITICAL 81 "LOG_FILE_OVERWRITE=$LOG_FILE_OVERWRITE"
fi
# ----------------------------------------------------------------------------




# ------- generate mokka steering file ---------------------------------------
if [ ! -e "mokka.steer" ] ; then
    msg INFO "generate Mokka steering file from template..."
    mokka-steer-gen.py \
        --mokka-input-file $INPUT_FILE_NAME \
        --mokka-start-event $START_EVENT \
        --mokka-total-events $TOTAL_EVENTS \
        --mokka-detector-model $DETECTOR_MODEL \
        --mokka-physics-list $PHYSICS_LIST \
        --mokka-random-seed $RANDOM_SEED \
        --mokka-lcio-filename $OUTPUT_FILE_NAME \
        --mokka-process $PROCESS \
        --mokka-energy $ENERGY \
        --mokka-pol-ep $POL_EP \
        --mokka-pol-em $POL_EM \
        --mokka-cross-section $CROSS_SECTION \
        mokka.steer.in
    test $? -eq 0 || msg CRITICAL 74 "failed to generate Mokka steering file"
fi
# ----------------------------------------------------------------------------




# ------- copy mokka input file ----------------------------------------------
msg INFO "copy input file [ $INPUT_FILE ] ..."
timeout=$(( ($RANDOM + $RANDOM_SEED) % 600 ))
test -n "$GRID_JOB" && { echo "sleep $timeout seconds..." ; sleep $timeout ; }
c="grid-dl-file.py -o ignore --timeout 3600 $INPUT_FILE ."
msg DEBUG "> $c"
eval $c >> $MSG_LOG_FILE
test $? -ne 0 && msg CRITICAL 90 "failed to copy input file"
# TODO check number of events from INPUT_FILE
# ----------------------------------------------------------------------------




# ----------------------------------------------------------------------------
# run Mokka
# ----------------------------------------------------------------------------


# FIXME use preload @ desy
#c="export LD_PRELOAD=./libpdcap.so"
#msg DEBUG "> $c"
#eval $c

msg INFO "Mokka started on ($(date))"
#mokka-wrapper.sh mokka.steer 2>&1 > mokka.log
mokka-wrapper.sh -e ./particle.tbl mokka.steer 2>&1 > mokka.log
mokka_exit_code=$?
if [ $mokka_exit_code -ne 0 ] ; then
    msg ERROR "************* MOKKA ERROR **********************"
    tail -n 50 mokka.log >&2
    msg CRITICAL 73 "Mokka exit code ($mokka_exit_code) != 0 !!!"
fi

msg INFO "Mokka finished on ($(date))"

#c="unset LD_PRELOAD"
#msg DEBUG "> $c"
#eval $c




# -----------------------------------------------------------------------------
# check output
# -----------------------------------------------------------------------------


msg INFO "check if output file is OK..."
files=$(\ls *.slcio 2>/dev/null)
nfiles=$(wc -w <<< "$files")
test $nfiles -eq 0 && msg CRITICAL 82 "no output file was found"
msg INFO "$nfiles ouput file(s) found:"
msg INFO "$files"



# ----- check filesizes -----
MIN_OUTPUT_FILE_SIZE=500
msg INFO "check if output filesizes are greater than or equal to the minimum ($MIN_OUTPUT_FILE_SIZE)..."
for i in *.slcio ; do
    # FIXME use find . -name \*.slcio -size -$MIN_OUTPUT_FILE_SIZEk -exec msg CRITICAL 83 "{} filesize ($size) is less than the minimum ($MIN_OUTPUT_FILE_SIZE)" \;
    size=$(\ls -l $i | awk '{print $5}')
    if [ ${size:-0} -ge $MIN_OUTPUT_FILE_SIZE ] ; then
        msg INFO "$i filesize ($size) -- OK!"
    else
        msg CRITICAL 83 "$i filesize ($size) is less than the minimum ($MIN_OUTPUT_FILE_SIZE)"
    fi
done



msg INFO "check total number of events written..."

# ----- check number of events from output file -----
anajob $(ls -rt *.slcio) | tail -n700 > anajob-outputfile-tail.log
totevents=$( grep 'events read from files' anajob-outputfile-tail.log | tail -n7 | grep -oE [0-9]+)
test -z "$totevents" && msg CRITICAL 84 "failed to get total number of events"

if [ $totevents -eq $TOTAL_EVENTS ] ; then
    msg INFO "$totevents events written -- OK!"
else
    msg ERROR "total number of events ($totevents) does NOT match expected ($TOTAL_EVENTS)"
fi



msg INFO "check for last event number..."

# ----- check last event written -----
lastevent=$(grep 'EVENT: ' anajob-outputfile-tail.log | tail -n1 | cut -d' ' -f2)
test -z "$lastevent" && msg CRITICAL 85 "failed to get last event number"

LAST_EVENT=$(( $START_EVENT + $TOTAL_EVENTS - 1 ))
if [ $lastevent -eq $LAST_EVENT ] ; then
    msg INFO "last event number ($lastevent) matches expected ($LAST_EVENT) -- OK!"
else
    msg ERROR "last event number ($lastevent) does NOT match expected ($LAST_EVENT)"
fi




# -----------------------------------------------------------------------------
# check if any errors were found
# -----------------------------------------------------------------------------

if [ $MSG_ERRORS -ne 0 ] ; then
    msg CRITICAL 113 "job did not complete successfully, $MSG_ERRORS errors were found!"
fi



# -----------------------------------------------------------------------------
# rename and copy OUTPUT file to SE
# -----------------------------------------------------------------------------

if [ -n "$GRID_JOB" ] ; then
    msg INFO "copy output file [ $OUTPUT_FILE_NAME ] to grid SE..."

    lfc-mkdir -p $OUTPUT_DIR

    grid-ul-file.py --timeout 3600 --overwrite=$OUTPUT_FILE_OVERWRITE --storage-element=$STORAGE_ELEMENT $OUTPUT_FILE_NAME $OUTPUT_FILE
    test $? -eq 0 || msg CRITICAL 86 "failed to copy output file"

    #msg INFO "remove output file"
    #rm -f $OUTPUT_FILE_NAME
fi

msg INFO "job ended successfully :)"



# -----------------------------------------------------------------------------
# job ends here (cleanup trap will be called after exit for cleanup)
# -----------------------------------------------------------------------------

exit 0
# EOF

