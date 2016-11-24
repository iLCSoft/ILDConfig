% F.Gaede, DESY
% 11/2016

# ILDConfig 

This package contains ilcsoft configuration files for running 
simulation and reconstruction for the ILD detector 
in iLCSoft with lcio, Marlin and DD4hep.

## StandardConfig

- ./lcgeo_current
	- current example/standard configuration files for running ddsim and Marlin
	
See [./StandardConfig/lcgeo_current/README.md](./StandardConfig/lcgeo_current/README.md) for details.
Following the examples in this file is the quickest way to get started with running iLCSoft for ILD.
     
    

## LCFIPlusConfig

Input files for flavor tagging:

- ./steer
	- example steering files

- ./vtxprob
	- input histograms used for flavor tagging

- ./lcfiweights
	- TMVA weight files


 ---------------------------
 
	NB: this package is no longer compatibel with Mokka based simulation
