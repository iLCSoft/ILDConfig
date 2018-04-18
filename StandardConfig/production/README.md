# Running ILD standard simulation and reconstruction

(F.Gaede, R.Ete, DESY)

<!---	  
   06/2015  F.G:  updated to use lcgeo/ddsim
   12/2011: F.G.: updated to new ILD_01_dev model 
   06/2012: J.E.: updated to new ILD_o{1,2,3}_v01 models
   11/2017: R.E.: updated to run in production mode
-->

This document describes :
- How this directory is structured
- How to run a DDSim simulation
- How to directly run the reconstruction chain
- How to generate a steering file for Marlin using our template

For more information on the iLCSoft tools refer to the [iLCSoft Portal](http://ilcsoft.desy.de) or directly to the [source code documentation](https://github.com/iLCSoft/ilcsoftDoc/blob/master/CodeDocumentation.md) of the individual packages.

## Structure of this directory

The structure of this directory relies on a functionality introduced in Marlin v01-14 that allows to include xml file within the top-level Marlin steering file. The different sub-directories are thus used for splitting the reconstruction in smaller blocks: Tracking Digi and Reco, CaloDigi, PFA, HLR, etc ...

Currently you can find the following sub-directories for usual processors :

- *Tracking* : The tracking digitization and reconstruction processors
- *CaloDigi* : The calorimeter digitizer (Ecal, Hcal, Fcal and Muon system) processors
- *ParticleFlow* : The PandoraPFA processor(s)
- *HighLevelReco* : The high level reconstruction (PID, vertexing, cluster shape, MC truth linker) processors
- *BeamCalReco* : The BeamCal reconstruction settings

In addition, you may find the following sub-directories :

- *Config* : Specific configuration files that may depends on CMS energy or detector models
- *Calibration* : The calibration constants for the different detector flavors currently under study. Constants are mainly related to energy calibration, dEdX, and particle identification.
- *Examples* : Example scripts to run 3 ttbar events simulation and reconstruction
- *Gear* : The geometry files of the (deprecated) GEAR package of the detector geometries currently under study
- *PandoraSettings* : A directory containing the PandoraPFA steering files
- *RootMacros* : A set of root macros for quick checks of output files
- *Documentation* : Additional documentation on ILDConfig on overlay background and production parameters

Most of these directories are used by the top-level Marlin steering file *MarlinStdReco.xml* as include sources. Please to not move them except if you know what you are doing.


## Running the simulation and reconstruction chain

### 1. Initialize the current ilcsoft release
   
```shell
source /afs/desy.de/project/ilcsoft/sw/x86_64_gcc49_sl6/v01-19-06/init_ilcsoft.sh
```

### 2. Run the lcgeo/ddsim simulation: the 3 ttbar example 

```shell
ddsim \
  --inputFiles Examples/bbudsc_3evt/bbudsc_3evt.stdhep \
  --outputFile bbudsc_3evt_SIM.slcio \
  --compactFile $lcgeo_DIR/ILD/compact/ILD_l5_v02/ILD_l5_v02.xml \
  --steeringFile ddsim_steer.py
```

this creates the file: *bbudsc_3evt_SIM.slcio*

You can now examine the collections in the file:

```shell
anajob bbudsc_3evt_SIM.slcio
```

### 3. Run the full reconstruction

```shell
Marlin MarlinStdReco.xml \
	--constant.lcgeo_DIR=$lcgeo_DIR \
  --constant.DetectorModel=ILD_l5_o1_v02 \
  --constant.OutputBaseName=bbudsc_3evt \
  --global.LCIOInputFiles=bbudsc_3evt_SIM.slcio
```

This will create the 4 following files :
- *bbudsc_3evt_AIDA.root* : Check plots from various processors
- *bbudsc_3evt_REC.slcio* : Output lcio file containing all collections from the reconstruction chain
- *bbudsc_3evt_DST.slcio* : Output file file containing the collections suited for physics analysis (PFO, cluster, rec hits, etc ...)
- *bbudsc_3evt_PfoAnalysis.root* : A root file with a simple analysis of produced PFO. It is mainly used to study single particle performance and calibration or JER performances

For single particles reconstruction you may also want to switch off the BeamCal reconstruction (time consuming) if you don't shoot in this region and/or if you have time processing constraints. To do this you can add the argument `--constant.RunBeamCalReco=false`. Example:

```shell
Marlin MarlinStdReco.xml \
	--constant.lcgeo_DIR=$lcgeo_DIR \
  --constant.DetectorModel=ILD_l5_o1_v02 \
  --constant.OutputBaseName=bbudsc_3evt \
  --constant.RunBeamCalReco=false \
  --global.LCIOInputFiles=bbudsc_3evt_SIM.slcio
```

### 4. View the result in the event display

Here two solutions :

- start the event display (server) first and view REC or DST events:

```shell
# Start the server
glced &
# Run the REC viewer
Marlin MarlinStdRecoViewer.xml \
  --global.GearXMLFile=Gear/gear_ILD_l5_o1_v02.xml \
  --global.LCIOInputFiles=bbudsc_3evt_REC.slcio
# Or run the DST viewer
Marlin MarlinStdRecoViewerDST.xml \
  --global.GearXMLFile=Gear/gear_ILD_l5_o1_v02.xml \
  --global.LCIOInputFiles=bbudsc_3evt_DST.slcio
```

- start both, glced and Marlin in one go:
```shell
# Option -s 1 to display also tracking surfaces
ced2go -s 1 -d $lcgeo_DIR/ILD/compact/ILD_l5_o1_v02/ILD_l5_o1_v02.xml bbudsc_3evt_REC.slcio
```

### 5. Create a ROOT TTree for analysis

```shell
Marlin MarlinStdRecoLCTuple.xml \
  --global.LCIOInputFiles=bbudsc_3evt_DST.slcio \
  --MyAIDAProcessor.FileName=bbudsc_3evt_LCTuple
```

This will produce the file *bbudsc_3evt_LCTuple.root*


## Generating one/multiple steering files

Even if the current top-level Marlin steering file *MarlinStdReco.xml* can be run as it is, it's sometimes more convenient to have a (almost) standalone steering file without includes. The python script *GenerateSteeringFiles.py* helps you to generate a new steering file from the default top level one. The help command is the following :

```shell
python GenerateSteeringFiles.py --help
usage: Steering file generate: [-h] [--lcgeo_DIR LCGEO_DIR]
                               [--detectorModels DETECTORMODELS [DETECTORMODELS ...]]
                               [--outputDirectory OUTPUTDIRECTORY]
                               [--steeringFile STEERINGFILE]

optional arguments:
  -h, --help            show this help message and exit
  --lcgeo_DIR LCGEO_DIR
                        The path to lcgeo directory (default taken from env vars)
  --detectorModels DETECTORMODELS [DETECTORMODELS ...]
                        The detector models to process
  --outputDirectory OUTPUTDIRECTORY
                        The output directory in which the output files will go
  --steeringFile STEERINGFILE
                        The input template steering file
```
By default, the detector models are the ones under studies. You can choose one model or many by using the --detectorModels option. The option --lcgeo_DIR allows you to set a particular lcgeo version to use. By default, the environment variable lcgeo_DIR (defined after sourcing a particular ilcsoft version) is used. The --steeringFile option is the top-level Marlin steering file to process (by default MarlinStdReco.xml).

You can, for example generate the 4 flavors of option 5 with large and small TPC radius by running the following command :

```shell
mkdir GeneratedFiles
python GenerateSteeringFiles.py \
  --detectorModels ILD_l5_o1_v02 ILD_l5_o2_v02 ILD_s5_o1_v02 ILD_s5_o2_v02 \
  --outputDirectory ./GeneratedFiles
```

This will produces 4 files :

```shell
ls GeneratedFiles
# -> MarlinStdReco_ILD_l5_o1_v02.xml  MarlinStdReco_ILD_l5_o2_v02.xml  MarlinStdReco_ILD_s5_o1_v02.xml  MarlinStdReco_ILD_s5_o2_v02.xml
```

