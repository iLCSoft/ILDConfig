#!/bin/bash

ILCSOFT=/cvmfs/clicdp.cern.ch/iLCSoft/builds/current/CI_gcc
source $ILCSOFT/init_ilcsoft.sh

cd /Package/StandardConfig/production

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
  
  if [ ! -f "bbudsc_3evt_SIM_test_${detector}.slcio" ]
  then
    ls -lthr
    echo "-- ERROR - DDSim ${detector}: No output file found (bbudsc_3evt_SIM_test_${detector}.slcio)"
  fi
done




