#!/bin/bash

ILCSOFT=/cvmfs/clicdp.cern.ch/iLCSoft/builds/current/CI_gcc
source $ILCSOFT/init_ilcsoft.sh

cd /Package/StandardConfig/production

##
## Test DDSim for our current detector models
##
for detector in ILD_l5_v02 ILD_s5_v02
do
  echo "-- Running DDSim ${detector} ..."
  ddsim \
    --inputFiles Examples/bbudsc_3evt/bbudsc_3evt.stdhep \
    --outputFile bbudsc_3evt_SIM_test_${detector}.slcio \
    --compactFile $lcgeo_DIR/ILD/compact/${detector}/${detector}.xml \
    --steeringFile ddsim_steer.py > travis-ci.log 2>&1

  ddsimStatus=$?

  if [[ $ddsimStatus != 0 ]]
  then
    cat travis-ci.log
    echo "-- ERROR - DDSim ${detector}: 3 events test failed"
    exit $ddsimStatus
  else
    echo "-- DDSim ${detector}: test passing !"
  fi
  
  # test presence of output file
  if [ ! -f "bbudsc_3evt_SIM_test_${detector}.slcio" ]
  then
    ls -lthr
    echo "-- ERROR - DDSim ${detector}: No output file found (bbudsc_3evt_SIM_test_${detector}.slcio)"
    exit 1
  fi
done


##
## Test Marlin reconstruction for our current detector models 
##
for largeOrSmall in l5 s5
do
  for detectorOption in o1 o2
  do
    simDetector="ILD_${largeOrSmall}_v02"
    recDetector="ILD_${largeOrSmall}_${detectorOption}_v02"
    outputBaseName="bbudsc_3evt_RECNoBG_Test_${recDetector}"
    
    echo "-- Running Marlin ${recDetector} no bg ..."
    Marlin MarlinStdReco.xml \
    	--constant.lcgeo_DIR=$lcgeo_DIR \
      --constant.DetectorModel=${recDetector} \
      --constant.OutputBaseName=${outputBaseName} \
      --global.LCIOInputFiles=bbudsc_3evt_SIM_test_${simDetector}.slcio > travis-ci.log 2>&1
    
    marlinStatus=$?

    if [[ $marlinStatus != 0 ]]
    then
      cat travis-ci.log
      echo "-- ERROR - Marlin ${recDetector} no bg: 3 events test failed"
      exit $marlinStatus
    else
      echo "-- Marlin ${recDetector} no bg: test passing !"
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
        echo "-- ERROR - Marlin ${recDetector} no bg: Missing output file ${checkFile}"
        exit 1
      else
        echo "-- Marlin ${recDetector} no bg: ${checkFile} present ..."
      fi
    done
  done
done
