#!/bin/bash

ILCSOFT=/cvmfs/clicdp.cern.ch/iLCSoft/builds/current/CI_gcc
source $ILCSOFT/init_ilcsoft.sh

cd /Package/StandardConfig/production

ddsim \
  --inputFiles Examples/bbudsc_3evt/bbudsc_3evt.stdhep \
  --outputFile bbudsc_3evt_SIM_test_ILD_l5_v02.slcio \
  --compactFile $lcgeo_DIR/ILD/compact/ILD_l5_v02/ILD_l5_v02.xml \
  --steeringFile ddsim_steer.py

ddsimStatus=$?

if [[ ddsimStatus != 0 ]]
then
  echo "DDSim ILD_l5_v02: 3 events test failed"
  exit $ddsimStatus
else
  echo "-- DDSim ILD_l5_v02: passing !"
fi