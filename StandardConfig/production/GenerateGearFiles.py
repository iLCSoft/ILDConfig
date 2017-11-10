#!/usr/bin/python
"""
Python script utility to generate a set of GEAR files given a set of detector models, one for each model.
Use :

    python GenerateGearFiles.py --help

to get the different input/output options.

@author: Remi ete, DESY
"""

import subprocess
import os, sys
import argparse

DEVNULL = open(os.devnull, 'wb')
radius = ["l", "s"]
shortOptions = ["1", "2"]
longOptions = ["1", "2", "3", "4"]

detectorModels = []
detectorModels.extend( ["ILD_{0}4_o{1}_v02".format(r, o) for r in radius for o in shortOptions] )
detectorModels.extend( ["ILD_{0}5_o{1}_v02".format(r, o) for r in radius for o in longOptions] )

if __name__ == "__main__":
    parser = argparse.ArgumentParser("GEAR file generator:", formatter_class=argparse.RawTextHelpFormatter, add_help=True)
    
    parser.add_argument("--lcgeo_DIR", action="store", default=os.environ["lcgeo_DIR"],
                            help="The path to lcgeo directory (default taken from env vars)", required = False)
                            
    parser.add_argument("--detectorModels", action="store", default=detectorModels, nargs='+',
                            help="The detector models to process", required = False)
                            
    parser.add_argument("--outputDirectory", action="store", default="./",
                            help="The output directory in which the output files will go", required = False)   
 
                            
    parsed = parser.parse_args()

    print "Processing :"
    print " - detector models     : {0}".format(parsed.detectorModels)
    print " - output directory    : {0}".format(parsed.outputDirectory)
    print " - lcgeo directory     : {0}".format(parsed.lcgeo_DIR)
    
    for detectorModel in parsed.detectorModels:
        # compact file
        compactFile = os.path.join(parsed.lcgeo_DIR, "ILD/compact", detectorModel, detectorModel + ".xml")
        outputGearFile = os.path.join(parsed.outputDirectory, "gear_" + detectorModel + ".xml")
        
        convertCmd = [
            "convertToGear", 
            "default",
            compactFile, 
            outputGearFile]
        
        print "Running convertToGear:"
        print " - command line         : " + " ".join(convertCmd)
        print " - output GEAR file : " + outputGearFile
        print ""
        
        process = subprocess.Popen(args = convertCmd, stdin=subprocess.PIPE, stdout=DEVNULL, stderr=DEVNULL)
        process.wait()
    
    