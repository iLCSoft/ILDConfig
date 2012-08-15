#! /bin/bash

###############################################################################
# run reconstruction job on the Grid.
#
# parts of this script were adopted from the original runjob.sh written by
# D. Martsch and from the modified runjobMarlin.sh (I. Marchesini)
#
# Jan Engels, DESY - IT
# 2012/02/10
###############################################################################


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




# ----- recjob settings ------------------------------------------------------
ARCH=x86_64_gcc41_sl5
# ----------------------------------------------------------------------------




###############################################################################
# FUNCTION DEFINITIONS
###############################################################################

usage(){
    cat << EOT
    usage: $(basename $0) ARGS
        ARGS:
            JOB_ID                # the job database id
            JOB_PREFIX            # prefix for naming the job output files
            SW_VER                # the ILCSoft version to use
            CFG_VER               # the ILDConfig version to use
            START_EVENT           # the start event number (used for checking the LAST_EVENT)
            TOTAL_EVENTS          # total number of events to be reconstructed
            RANDOM_SEED           # random seed
            OUTPUT_DIR            # directory for storing output files
            LOG_OUTPUT_DIR        # directory for storing log files
            STORAGE_ELEMENT       # storage element for storing output files
            INPUT_FILES           # comma separated list of input files (NO SPACES)
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
    cp -vf *.{sh,log,tgz,xml,root,txt} $LOG_FILE_DIR

    # copy stdout and stderr
    cp -vf $JOB_STARTDIR/std{out,err} $LOG_FILE_DIR

    # no need to copy job-wrapper.sh
    rm -vf $LOG_FILE_DIR/job-wrapper.sh

    # create tarball
    tar czf $LOG_FILE_NAME $LOG_FILE_DIR
    tar_rc=$?
    # --------------------------------------------------------------------

    # make sure to unlock any shared resources
    resource_sharing_cleanup

    # copy log tarball to SE and update database
    # only for grid jobs and if marlin has been executed
    if [ -n "$GRID_JOB" -a -n "$marlin_exit_code" ] ; then
        
        # -------------- copy log tarball to the grid ------------------------
        if [ $tar_rc -eq 0 ] ; then
            echo "uploading log tarball to the grid"

            lfc-mkdir -p $LOG_OUTPUT_DIR
            grid-ul-file.py --timeout 9000 --overwrite=$LOG_FILE_OVERWRITE --storage-element=$STORAGE_ELEMENT $LOG_FILE_NAME $LOG_FILE
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
    # --------------------------------------------------------------------

    
    echo "====================== job end =============================="
    exit $exit_code
}
trap cleanup EXIT

##### END OF FUNCTION DEFINITIONS #############################################



# -----------------------------------------------------------------------------
# check script syntax
# -----------------------------------------------------------------------------

if [ $# -ne 1 -a $# -ne 11 ]; then
    exit 2
fi

JOB_ARGS="$*"
JOB_ID=$1


# -----------------------------------------------------------------------------
# job starts here
# -----------------------------------------------------------------------------


mkdir -vp $JOB_TMPDIR
cd $JOB_TMPDIR



# ----- gridtools ------------------------------------------------------------
# get gridtools from JOB_STARTDIR if job-wrapper.sh was called to run this script
test -d "$JOB_STARTDIR/gridtools" && cp -a "$JOB_STARTDIR/gridtools" .
if [ ! -d gridtools ] ; then
    if [ ! -e gridtools.tgz ] ; then
        wget --no-verbose -c "http://svnsrv.desy.de/viewvc/ilctools/mcprdsys/trunk/gridtools/?view=tar" -O gridtools.tgz
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
test $? -eq 0 || { echo "failed to initialize bash_logger" ; exit 65 ; }
. $GRIDTOOLSDIR/hepshlib/resource_sharing_lockutils.sh
test $? -eq 0 || msg CRITICAL 65 "failed to initialize resource_sharing tools"
# ----------------------------------------------------------------------------


usage >> $MSG_LOG_FILE
msg INFO "RUNNING: $0 $JOB_ARGS"


msg INFO "copy input files from $JOB_STARTDIR"
for i in $JOB_STARTDIR/* ; do
    test ! -d $i && { test -e $(basename $i) || cp -v $i . ; }
done


# ----------------------------------------------------------------------------
# parse command line arguments
# ----------------------------------------------------------------------------
if [ $# -eq 1 ]; then

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

    sql_cache "select * from rjob where id=$JOB_ID"

    JOB_PREFIX=$(sql_query rjob JOB_PREFIX)
    SW_VER=$(sql_query rjob SW_VER)
    CFG_VER=$(sql_query rjob CFG_VER)
    START_EVENT=$(sql_query rjob START_EVENT)
    TOTAL_EVENTS=$(sql_query rjob TOTAL_EVENTS)
    RANDOM_SEED=$(sql_query rjob RANDOM_SEED)
    OUTPUT_DIR=$(sql_query rjob OUTPUT_DIR)
    LOG_OUTPUT_DIR=$(sql_query rjob LOG_OUTPUT_DIR)
    STORAGE_ELEMENT=$(sql_query rjob STORAGE_ELEMENT)
    INPUT_FILES=$(sql_query rjob INPUT_FILES)
    INPUT_FILES=${INPUT_FILES//,/ } # replace commas with spaces

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
    RANDOM_SEED=$1
    shift
    OUTPUT_DIR=$1
    shift
    LOG_OUTPUT_DIR=$1
    shift
    STORAGE_ELEMENT=$1
    shift
    INPUT_FILES=${1//,/ } # replace commas with spaces
    shift

fi

LAST_EVENT=$(( $START_EVENT + $TOTAL_EVENTS - 1 ))
LOG_FILE_DIR="$JOB_PREFIX"
LOG_FILE_NAME="$JOB_PREFIX.tar.gz"
OUTPUT_DIR=$(normpath "$OUTPUT_DIR")
LOG_OUTPUT_DIR=$(normpath "$LOG_OUTPUT_DIR")
LOG_FILE=$(normpath "$LOG_OUTPUT_DIR/$LOG_FILE_NAME")
# ----------------------------------------------------------------------------




# ----------------------------------------------------------------------------
# prepare for running Marlin job
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

    export ILCSOFT="$PWD/ilcsoft/$ARCH"

    if [ ! -r "$ILCSOFT/$SW_VER" ] ; then

        # download an ilcsoft version not yet installed on the grid
        tarball=ilcsoft-$SW_VER-$ARCH-full.tar.gz

        #url="http://ilcsoft.desy.de/ilcsoft-bin-releases/$tarball"
        url="/grid/ilc/ilcsoft/$tarball"
        msg INFO "downloading ilcsoft tarball..."

        resource_share_url_download "$url"
        test $? -eq 0 || msg CRITICAL 71 "failed to download $url"
        
        msg INFO "unpack ilcsoft tarball..."
        tar -xzf $resource_replica
        test $? -eq 0 || msg CRITICAL 71 "failed to unpack ilcsoft tarball"
    fi

    #msg INFO "applying patch..."
    #tarball=ilcsoft-$SW_VER-$ARCH-patch-0001.tgz
    #wget --no-verbose -c "http://ilcsoft.desy.de/data/production/patches/$tarball" && tar -xzvf $tarball && rm -f $tarball
    #test $? -eq 0 || msg CRITICAL 71 "failed to download ilcsoft patch"

fi

msg INFO "initialize ilcsoft..."
. $ILCSOFT/init_ilcsoft.sh $SW_VER
test $? -eq 0 || msg CRITICAL 71 "failed to initialize ilcsoft"
# ----------------------------------------------------------------------------




# ------- check for existing job output --------------------------------------
msg INFO "check if job output files already exists..."
c="lfc-ls $OUTPUT_DIR 2>/dev/null | grep $JOB_PREFIX"
msg DEBUG "> $c"
r=$(eval $c)
if [ -z "$r" ] ; then
    msg INFO "job output not found - OK!"
else
    msg WARNING "job output files from [ $JOB_PREFIX ] already exist in [ $OUTPUT_DIR ]"
    if [ "$OUTPUT_FILE_OVERWRITE" = "force" ] ; then
        if [ -n "$GRID_JOB" ] ; then
            msg WARNING "job output files from [ $JOB_PREFIX ] already exist in [ $OUTPUT_DIR ]"
            #msg CRITICAL 81 "job output files from [ $JOB_PREFIX ] already exist in [ $OUTPUT_DIR ]"
            # FIXME should output files be erased here?
            # for OUTPUT_FILE in $(lfc-ls ...)
            #grid-rm-file.py --timeout 9000 $OUTPUT_FILE
            #test $? -eq 0 || msg CRITICAL "failed to erase job output file"
            #msg INFO "$OUTPUT_FILE erased successfully"
        fi
    else
        msg CRITICAL 81 "job output files from [ $JOB_PREFIX ] already exist in [ $OUTPUT_DIR ]"
    fi
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
fi
# ----------------------------------------------------------------------------




# ------- generate marlin steering file --------------------------------------
#msg INFO "generate Marlin steering file from template..."
#for file in $INPUT_FILES ; do
#    INPUT_FILES_BASENAMES="$INPUT_FILES_BASENAMES $(basename $file)"
#done
#
#sed "s/\$LCIOINFILE/$INPUT_FILES_BASENAMES/;\
#    s/\$LCIOOUTFILE/$JOB_PREFIX-REC.slcio/;\
#    s/\$LCIODSTFILE/$JOB_PREFIX-DST.slcio/;\
#    s/\$RAIDAFILE/$JOB_PREFIX/;\
#    " steer.xml.in > steer.xml
#test $? -eq 0 || msg CRITICAL 74 "failed to generate Marlin steering file"
# ----------------------------------------------------------------------------




# ------- copy marlin input files --------------------------------------------
msg INFO "copy input files..."
timeout=$(( ($RANDOM + $RANDOM_SEED) % 600 ))
test "$GRID_JOB" = "1" && { echo "sleep $timeout seconds..." ; sleep $timeout ; }
for file in $INPUT_FILES ; do
    msg INFO "copy [ $file ]"
    c="grid-dl-file.py -o ignore --timeout 9000 $file ."
    msg DEBUG "> $c"
    eval $c >> $MSG_LOG_FILE
    test $? -ne 0 && msg CRITICAL 90 "failed to copy input file"
done
# ----------------------------------------------------------------------------




# ------- check input files --------------------------------------------------
msg INFO "check total number of events in input files..."
for file in $INPUT_FILES ; do
    INPUT_FILES_BASENAMES="$INPUT_FILES_BASENAMES $(basename $file)"
done
#anajob $INPUT_FILES_BASENAMES | tail -n700 > anajob-inputfile-tail.log
#totsimevents=$(grep 'events read from files' anajob-inputfile-tail.log | tail -n7 | grep -oE [0-9]+)
totsimevents=$(lcio_event_counter $INPUT_FILES_BASENAMES | tail -n1)
test -z "$totsimevents" && msg CRITICAL 91 "failed to get total number of simulated events"

if [ $totsimevents -eq $TOTAL_EVENTS ] ; then
    msg INFO "number of events in input files: $totsimevents -- OK!"
else
    msg CRITICAL 92 "total number of simulated events ($totsimevents) does NOT match expected ($TOTAL_EVENTS)"
fi
# ----------------------------------------------------------------------------




# -----------------------------------------------------------------------------
# run Marlin
# -----------------------------------------------------------------------------

export MARLIN_DLL=libMarlinReco.so:libLCFIVertex.so:libLCFIPlus.so:libOverlay.so:libMarlinPandora.so:libMarlinTrkProcessors.so:libClupatra.so:libForwardTracking.so
msg INFO "MARLIN_DLL: $MARLIN_DLL"

# FIXME use preload @ desy
#c="export LD_PRELOAD=./libpdcap.so"
#msg DEBUG "> $c"
#eval $c

msg INFO "Marlin started on ($(date))"

#c="Marlin steer.xml > marlin.log 2>&1"
c="Marlin "
#test -z "$GRID_JOB" && { export TOTAL_EVENTS=3 ; c+=" --global.MaxRecordNumber=$TOTAL_EVENTS " ; }
test -z "$GRID_JOB" && { c+="--global.SkipNEvents=$(( $TOTAL_EVENTS - 3 )) " ; export TOTAL_EVENTS=3 ; }
c+="--global.LCIOInputFiles=\"$INPUT_FILES_BASENAMES\" \
    --MyLCIOOutputProcessor.LCIOOutputFile=$JOB_PREFIX-REC.slcio  \
    --DSTOutput.LCIOOutputFile=$JOB_PREFIX-DST.slcio  \
    --MyAIDAProcessor.FileName=$JOB_PREFIX \
    stdreco.xml > marlin.log 2>&1"
msg DEBUG "> $c"
eval $c
marlin_exit_code=$?
if [ $marlin_exit_code -ne 0 ] ; then
    msg ERROR "************* Marlin ERROR **********************"
    tail -n 50 marlin.log >&2
    msg CRITICAL 73 "Marlin exit code ($marlin_exit_code) != 0 !!!"
fi


msg INFO "Marlin finished on ($(date))"

#c="unset LD_PRELOAD"
#msg DEBUG "> $c"
#eval $c




# -----------------------------------------------------------------------------
# check output
# -----------------------------------------------------------------------------


msg INFO "check number of output files found..."
recfiles=$(\ls *REC*.slcio 2>/dev/null)
dstfiles=$(\ls *DST*.slcio 2>/dev/null)
nrecfiles=$(wc -w <<< "$recfiles")
ndstfiles=$(wc -w <<< "$dstfiles")
test $ndstfiles -eq 0 && msg CRITICAL 82 "no DST file(s) were found"
test $nrecfiles -eq 0 && msg CRITICAL 82 "no REC file(s) were found"
msg INFO "$ndstfiles DST file(s) found:"
msg INFO "$dstfiles"
msg INFO "$nrecfiles REC file(s) found:"
msg INFO "$recfiles"



# ----- check filesizes -----
MIN_OUTPUT_FILE_SIZE=500
msg INFO "check if output filesizes are greater than or equal to the minimum ($MIN_OUTPUT_FILE_SIZE)..."
for i in *{REC,DST}*.slcio ; do
    # FIXME use find . -name \*.slcio -size -$MIN_OUTPUT_FILE_SIZEk -exec msg CRITICAL 83 "{} filesize ($size) is less than the minimum ($MIN_OUTPUT_FILE_SIZE)" \;
    size=$(\ls -l $i | awk '{print $5}')
    if [ ${size:-0} -ge $MIN_OUTPUT_FILE_SIZE ] ; then
        msg INFO "$i filesize ($size) -- OK!"
    else
        msg CRITICAL 83 "$i filesize ($size) is less than the minimum ($MIN_OUTPUT_FILE_SIZE)"
    fi
done




msg INFO "check total number of DST/REC events written..."


# ----- check number of events from DST files -----
anajob $(ls -rt *DST*.slcio) | tail -n700 > anajob-dst-outputfile-tail.log
totevents=$( grep 'events read from files' anajob-dst-outputfile-tail.log | tail -n7 | grep -oE [0-9]+)
test -z "$totevents" && msg CRITICAL 84 "failed to get total number of DST events"

if [ $totevents -eq $TOTAL_EVENTS ] ; then
    msg INFO "$totevents DST events written -- OK!"
else
    msg ERROR "total number of DST events ($totevents) does NOT match expected ($TOTAL_EVENTS)"
fi


# ----- check number of events from REC files -----
anajob $(ls -rt *REC*.slcio) | tail -n700 > anajob-rec-outputfile-tail.log
totevents=$(grep 'events read from files' anajob-rec-outputfile-tail.log | tail -n7 | grep -oE [0-9]+)
test -z "$totevents" && msg CRITICAL 84 "failed to get total number of REC events"

if [ $totevents -eq $TOTAL_EVENTS ] ; then 
    msg INFO "$totevents REC events written -- OK!"
else
    msg ERROR "total number of REC events written ($totevents) does NOT match expected ($TOTAL_EVENTS)"
fi




msg INFO "check for last DST/REC event numbers..."


# ----- check last DST event written -----
lastevent=$(grep 'EVENT: ' anajob-dst-outputfile-tail.log | tail -n1 | cut -d' ' -f2)
test -z "$lastevent" && msg CRITICAL 85 "failed to get last DST event number"

if [ $lastevent -eq $LAST_EVENT ] ; then
    msg INFO "last DST event number ($lastevent) matches expected ($LAST_EVENT) -- OK!"
else
    msg WARNING "last DST event number ($lastevent) does NOT match expected ($LAST_EVENT)"
fi


# ----- check last REC event written -----
lastevent=$(grep 'EVENT: ' anajob-rec-outputfile-tail.log | tail -n1 | cut -d' ' -f2)
test -z "$lastevent" && msg CRITICAL 85 "failed to get last REC event number"

if [ $lastevent -eq $LAST_EVENT ] ; then
    msg INFO "last REC event number ($lastevent) matches expected ($LAST_EVENT) -- OK!"
else
    msg WARNING "last REC event number ($lastevent) does NOT match expected ($LAST_EVENT)"
fi




# -----------------------------------------------------------------------------
# check if any errors were found
# -----------------------------------------------------------------------------

if [ $MSG_ERRORS -ne 0 ] ; then
    msg CRITICAL 113 "job did not complete successfully, $MSG_ERRORS errors were found!"
fi



# -----------------------------------------------------------------------------
# copy OUTPUT files to SE
# -----------------------------------------------------------------------------

if [ -n "$GRID_JOB" ] ; then
    msg INFO "copy output files to SE..."

    lfc-mkdir -p $OUTPUT_DIR

    for i in *{REC,DST}*.slcio ; do
        msg INFO "copy [ $i ]"
        
        grid-ul-file.py --timeout 9000 --overwrite=$OUTPUT_FILE_OVERWRITE --storage-element=$STORAGE_ELEMENT $i ${OUTPUT_DIR}/
        test $? -ne 0 && msg CRITICAL 86 "failed to copy output file"

        #msg INFO "remove output file"
        #rm -vf $i
    done
fi

msg INFO "job ended successfully :)"



# -----------------------------------------------------------------------------
# job ends here (cleanup trap will be called after exit for cleanup)
# -----------------------------------------------------------------------------

exit 0
# EOF

