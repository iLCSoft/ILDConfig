#!/bin/bash

ILCSOFT=/cvmfs/clicdp.cern.ch/iLCSoft/builds/current/CI_gcc
source $ILCSOFT/init_ilcsoft.sh

cd /Package/StandardConfig/production

##
## Test DDSim
##
echo "-- Running DDSim ${SIM_MODEL} ..."
ddsim \
  --inputFiles Examples/bbudsc_3evt/bbudsc_3evt.stdhep \
  --outputFile bbudsc_3evt_SIM_test_${SIM_MODEL}.slcio \
  --compactFile $lcgeo_DIR/ILD/compact/${SIM_MODEL}/${SIM_MODEL}.xml \
  --steeringFile ddsim_steer.py > travis-ci.log 2>&1

ddsimStatus=$?

if [[ $ddsimStatus != 0 ]]
then
  cat travis-ci.log
  echo "-- ERROR - DDSim ${SIM_MODEL}: 3 events test failed"
  exit $ddsimStatus
else
  echo "-- DDSim ${SIM_MODEL}: test passing !"
fi

# test presence of output file
if [ ! -f "bbudsc_3evt_SIM_test_${SIM_MODEL}.slcio" ]
then
  ls -lthr
  echo "-- ERROR - DDSim ${SIM_MODEL}: No output file found (bbudsc_3evt_SIM_test_${SIM_MODEL}.slcio)"
  exit 1
fi


##
## Test Marlin reconstruction
##
outputBaseName="bbudsc_3evt_RECNoBG_Test_${REC_MODEL}"

echo "-- Running Marlin ${REC_MODEL} no bg ..."
Marlin MarlinStdReco.xml \
	--constant.lcgeo_DIR=$lcgeo_DIR \
  --constant.DetectorModel=${REC_MODEL} \
  --constant.OutputBaseName=${outputBaseName} \
  --constant.RunBeamCalReco=false \
  --global.LCIOInputFiles=bbudsc_3evt_SIM_test_${SIM_MODEL}.slcio > travis-ci.log 2>&1

marlinStatus=$?

if [[ $marlinStatus != 0 ]]
then
  cat travis-ci.log
  echo "-- ERROR - Marlin ${REC_MODEL} no bg: 3 events test failed"
  exit $marlinStatus
else
  echo "-- Marlin ${REC_MODEL} no bg: test passing !"
fi

# test presence of different output files
checkFileList="${outputBaseName}_REC.slcio \
               ${outputBaseName}_DST.slcio \
               ${outputBaseName}_PfoAnalysis.root \
               ${outputBaseName}_AIDA.root"
for checkFile in ${checkFileList}
do
  if [ ! -f ${checkFile} ]
  then
    ls -lthr
    echo "-- ERROR - Marlin ${REC_MODEL} no bg: Missing output file ${checkFile}"
    exit 1
  else
    echo "-- Marlin ${REC_MODEL} no bg: ${checkFile} present ..."
  fi
done

