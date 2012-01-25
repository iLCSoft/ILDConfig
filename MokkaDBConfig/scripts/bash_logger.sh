#!/bin/bash

##############################################################################
# logging methods for bash
#
# author: Jan Engels - DESY IT
#
# $Id: bash_logger.sh 689 2010-01-05 14:13:55Z engels $
##############################################################################

BASH_LOGGER_VERSION="\$Rev: 731 $"
MSG_LOG_LEVEL=${MSG_LOG_LEVEL:-"INFO"}
MSG_LOG_FILE=${MSG_LOG_FILE:-"${TMPDIR:-/tmp}/${USER}-$(basename $0)-$(date +%F--%H-%M-%S)-$$.log"}

# format prefixes of log messages
MSG_LOG_FILE_PREFIX=${MSG_LOG_FILE_PREFIX:-"[ \$(date +%F--%H-%M-%S) ] - [ \${MSG_LEVEL} ]\\\t"}
#MSG_LOG_FILE_PREFIX=${MSG_LOG_FILE_PREFIX:-"[ \$(date +%F--%H-%M-%S) ] - [ \${MSG_LEVEL:0:1} ]\\\t"}
MSG_STDOUT_PREFIX=${MSG_STDOUT_PREFIX:-"[ \${MSG_LEVEL} ]\\\t"}
MSG_STDERR_PREFIX=${MSG_STDERR_PREFIX:-"$MSG_STDOUT_PREFIX"}

# enable if script should exit in case of a critical error
MSG_EXIT_ON_CRITICAL_ERROR=${MSG_EXIT_ON_CRITICAL_ERROR:-0}


#---------------------------------------------------------------
# helper function to emulate enumeration for log levels
# returns the index for a give level (see table below)
#
# index - level
#   1   - [D]EBUG
#   2   - [I]NFO
#   3   - [W]ARNING
#   4   - [E]RROR
#   5   - [C]RITICAL
#
msg_level_index(){
    #return $(expr index "DIWEC" "$(echo ${1:0:1} | tr a-z A-Z)")
    #return $(expr index "DIWEC" "$1")
    # MAC OS X does not know expr index
    index=${MSG_VERBOSITY_LEVELS#*$1}
    return $(( $MSG_VERBOSITY_LEVELS_LENGTH - ${#index} ))
}

#---------------------------------------------------------------
# internal variables (do not change!)
MSG_VERBOSITY_LEVELS="DIWEC"
MSG_VERBOSITY_LEVELS_LENGTH=${#MSG_VERBOSITY_LEVELS}
MSG_VERBOSITY_INDEX=$(msg_level_index "${MSG_LOG_LEVEL:0:1}")$?
MSG_ERRORS=0
#---------------------------------------------------------------

msg(){

    MSG_LEVEL="$(tr a-z A-Z <<< $1)"
    shift

    MSG_TXT="$*"

    MSG_LEVEL_INDEX=$(msg_level_index "${MSG_LEVEL:0:1}")$?

    # left outside for better performance, implies that user has to
    # define MSG_LOG_LEVEL before sourcing this script
    #MSG_VERBOSITY_INDEX=$(msg_level_index "${MSG_LOG_LEVEL:0:1}")$?

    # append all messages to log file
    eval echo -e ${MSG_ECHO_OPTIONS} "${MSG_LOG_FILE_PREFIX}\${MSG_TXT}" >> $MSG_LOG_FILE

    if [ $MSG_LEVEL_INDEX -ge $MSG_VERBOSITY_INDEX ] ; then
        eval echo -e ${MSG_ECHO_OPTIONS} "${MSG_STDOUT_PREFIX}\${MSG_TXT}"
    fi

    # 4 = index of ERROR
    if [ $MSG_LEVEL_INDEX -ge 4 ] ; then
        MSG_ERRORS=$(( $MSG_ERRORS + 1 ))
        eval echo -e ${MSG_ECHO_OPTIONS} "${MSG_STDERR_PREFIX}\${MSG_TXT}" >&2
        
        # 5 = index of CRITICAL ERROR
        test $MSG_LEVEL_INDEX -eq 5 -a $MSG_EXIT_ON_CRITICAL_ERROR -eq 1 && exit 1
    fi

}

# skip newline (echo -n)
msg_n(){
    MSG_ECHO_OPTIONS='-n'
    msg $*
    unset MSG_ECHO_OPTIONS
}

# disable interpretation of backslash escapes (default echo behaviour)
msg_E(){
    MSG_ECHO_OPTIONS='-E'
    msg $*
    unset MSG_ECHO_OPTIONS
}

#msg debug "I'm a DEBUG msg :)"
#msg info  "I'm an INFO msg :)"
#msg warning  "I'm a WARNING msg :|"
#msg error  "I'm an ERROR msg :("
#msg critical  "I'm a CRITICAL ERROR msg :("
#
#msg DEBUG "I'm also a DEBUG msg :)"
#msg DEB "I'm also a DEBUG msg :)"
#msg deb "I'm also a DEBUG msg :)"
#msg D "I'm also a DEBUG msg :)"
#msg d "I'm also a DEBUG msg :)"
#msg i "I'm an INFO msg :)"
#msg warn  "I'm a WARNING msg :|"
#
#echo
#echo "CONTENTS OF LOG FILE:"
#echo
#
#cat $MSG_LOG_FILE
#
#rm -vf ${MSG_LOG_FILE}
