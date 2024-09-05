# v02-03-03

* 2024-03-11 tmadlener ([PR#140](https://github.com/iLCSoft/ILDConfig/pull/140))
  - Update the README to point to the `v02-03-03` release
  - Add brief description of how to get an ILDConfig that is consistent with the release

* 2024-03-11 tmadlener ([PR#137](https://github.com/iLCSoft/ILDConfig/pull/137))
  - Add a Gaudi options file to run the standard reconstruction with some command line arguments to configure what to run
    - Created via automatic conversion of the Marlin steering file plus the necessary adaptions to make it run 
    - Run from LCIO or EDM4hep inputs (mutually exlusive), use `--inputFiles`
    - Produce EDM4hep output only by default, but allow to add LCIO output as well or switch to that using `--lcioOutput`.
    - Read the README section to see all available command line arguments
  - The overall reconstruction chain is modularized effectively in the same way as it was previously done for Marlin.
    - Different parts of the chain live in different files, where each file defines part of the whole chain as a sequence.
    - These sequences are dynamically loaded and configured depending on calibration constants, which depend on the CMS energy as well as the detector model.
  - Calibration for the different detector models is also split into different `.cfg` files which essentially all just define a single dictionary with all calibration constants. The same approach is followed by the CMS energy dependent config parameters.

* 2024-03-08 tmadlener ([PR#139](https://github.com/iLCSoft/ILDConfig/pull/139))
  - Make sure standard workflow still runs with default PFA by ensuring the `PFAtype` constant is non empty.
  - Rename the default PFA configuration to `PandoraPFAStd.xml`

* 2024-02-23 Ulrich Einhaus ([PR#138](https://github.com/iLCSoft/ILDConfig/pull/138))
  Add CPID calibration for ILD MC production of 2020, one based on training with single particles and one based on 2-fermion-Z-hadronic events.
  
  This includes the weight files and the reference files which point to the weight files. In addition, the CPID steering is added to the MarlinRecoMiniDST.xml. Paths are relative and only work if executed from the StandardConfig/production folder!

* 2024-01-10 Gerald Grenier ([PR#135](https://github.com/iLCSoft/ILDConfig/pull/135))
  Add option to run different PFA type in Standard Reco and add an xml file to run perfect PandoraPFA based on MC truth.

# v02-03-02

* 2023-02-24 Jan Klamka ([PR#134](https://github.com/iLCSoft/iLDConfig/pull/134))
  - Digitisation including the hits from CLIC-like outer tracker and changes for the FTD, allowing for further use of the Conformal Tracking
  - Conformal tracking with input collections from the new ILD_l5_v09 model, parameters setup as in CLIC config.

# v02-03-02

* 2023-02-24 Jan Klamka ([PR#134](https://github.com/iLCSoft/ILDConfig/pull/134))
  - Digitisation including the hits from CLIC-like outer tracker and changes for the FTD, allowing for further use of the Conformal Tracking
  - Conformal tracking with input collections from the new ILD_l5_v09 model, parameters setup as in CLIC config.

# v02-03

* 2022-06-29 Gerald Grenier ([PR#131](https://github.com/iLCSoft/ILDConfig/pull/131))
  - Add Calibration files to be able to run standard Marlin reconstruction on ILD simulation with Videau geometry.
  - For this first pass, files are only link to current ILD option 2 model from hybrid TESLA geometry.
  - Verification that Marlin runs on both small and large ILD Videau geometry have been done.

* 2022-04-20 Bohdan Dudar ([PR#133](https://github.com/iLCSoft/ILDConfig/pull/133))
  - Added TrackLength processor in the HighLevelReco chain.

* 2022-03-14 Bohdan Dudar ([PR#132](https://github.com/iLCSoft/ILDConfig/pull/132))
  - All steering parameters of `TOFEstimators` are explicitly specified in the steering file w/o any modification to the behaviour

# v02-02-03

* 2021-07-28 YONAMINE Ryo ([PR#130](https://github.com/iLCSoft/ILDConfig/pull/130))
  - Add a new weight/vtxprob set trained with 2f processes at 250 GeV (MC2020).

* 2021-07-28 Daniel Heuchel ([PR#128](https://github.com/iLCSoft/ILDConfig/pull/128))
  - Corrected Collection Name Track-MCTruth Link

* 2021-07-28 Thomas Madlener ([PR#127](https://github.com/iLCSoft/ILDConfig/pull/127))
  - Introduce the `lcgeo_DIR` constant into the mini-DST workflow. This makes it possible to set this value from the outside without having to rely on an envrionment variable being resolved automatically.

* 2021-07-20 Thomas Madlener ([PR#129](https://github.com/iLCSoft/ILDConfig/pull/129))
  - Update  the README to use the `v02-02-02` release

# v02-02-02

* 2021-06-16 tmadlener ([PR#126](https://github.com/iLCSoft/iLDConfig/pull/126))
  - Rename the `mini-DST-maker.xml` steering file to `MarlinStdRecoMiniDST` and make it a bit easier to configure from the outside
    - Add short description of some available configuration parameters to the miniDST README. 
  - Add processors to run angular dEdx correction (see iLCSoft/MarlinReco#91). Make it possible to disable this via a parameter.
  - Unpack a default LCFIPlus weights tarball to make it possible to run the miniDST workflow with a minimal default configuration.
  - Copy the `IsolatedLeptonTagger` weights to `ILDConfig` from `MarlinReco/Analysis/IsolatedLeptonTagging`
    - Consider removing them from `MarlinReco/Analysis/IsolatedLeptonTagging` as they are "configuration" parameters that should be in `ILDConfig`
    - Easier to use in the miniDST creation example
  - Add `run_standard_workflow.sh` for testing of iLCSoft installations
    - Runs 3 evt SIM and RECO steps to produce DST files, which are then also used to make an LCTuple file as well as a mini-DST from it.

* 2021-06-15 shkawada ([PR#125](https://github.com/iLCSoft/iLDConfig/pull/125))
  - added mini-DST-maker.xml: for the mini-DST file production
  - README_mini-DST.md: readme file for mini-DST-maker.xml

* 2021-02-02 Remi Ete ([PR#124](https://github.com/iLCSoft/iLDConfig/pull/124))
  - Updated dE/dx parameters in Likelihood PID processor

# v02-00-02

* 2018-08-24 Frank Gaede ([PR#91](https://github.com/ilcsoft/ILDconfig/pull/91))
  - add missing (Sim)CalorimterHit collections to the event display steering file MarlinStdRecoViewer.xml

* 2018-08-21 Ete Remi ([PR#90](https://github.com/ilcsoft/ILDconfig/pull/90))
  - Added BeamCal maps for BeamReco at 1 TeV (l5 and s5)
  - Added missing BeamCal for BeamReco at 500 GeV for s5 model (4T)
  - Filled numbers for 1 TeV
     - Expected background rates for gg_lowpt overlay (BB, BW, WB and WW)
     - Beam size for LCFIPlus vertex fit constraint (x, y and z)
  - Filled numbers for 250 GeV 
     - Beam size for LCFIPlus vertex fit constraint (x, y **but not z**), from [ILC new 250 GeV baseline](https://arxiv.org/pdf/1711.00568.pdf)
  - Filled numbers for 350 GeV 
     - Beam size for LCFIPlus vertex fit constraint (x, y **but not z**), taken from [ILC TDR](https://arxiv.org/ftp/arxiv/papers/1306/1306.6327.pdf)
  - Changed numbers for 500 GeV
     - Beam size for LCFIPlus vertex fit constraint (x, y), taken from [ILC TDR](https://arxiv.org/ftp/arxiv/papers/1306/1306.6327.pdf)
  - Make BeamCal map file dependant on CMS energy and detector model
     - Moved constant `BeamCalBackgroundFile` into calibration files

* 2018-08-21 Akiya Miyamoto ([PR#87](https://github.com/ilcsoft/ILDconfig/pull/87))
  Missing 1 TeV vertex parameters, reported by Mikael and agreeded at the ILD Coftware Conveners meeting on 4 July, were added. In addition, ILC machine parameter names corresponding to the vertex parameters are included .

* 2018-07-19 Shaojun Lu ([PR#89](https://github.com/ilcsoft/ILDconfig/pull/89))
  - Do not apply senDetFilter for TPC.
    - because the TPC sensitive driver need every G4Step information to find out when the track cross the boundary.

* 2018-06-06 Ete Remi ([PR#85](https://github.com/ilcsoft/ILDconfig/pull/85))
  - Added symbolic link for calibration constants of v03,4,5,6 models pointing on the v02 model ones

* 2018-06-06 Shaojun Lu ([PR#84](https://github.com/ilcsoft/ILDconfig/pull/84))
  - Update documentation for users to use the correct version of ILCSoft.
     - the processor "TOFEstimators" is available in ILCSoft v02-00-01.

# v02-00-01

* 2018-05-18 Ete Remi ([PR#83](https://github.com/ilcsoft/ILDConfig/pull/83))
  - PfoAnalysis processor config :
     - Switch off the calibration details, saving time and nasty printouts in log files for production

# v02-00

* 2018-04-12 Ete Remi ([PR#78](https://github.com/ilcsoft/ILDConfig/pull/78))
  - TravisCI
      - Restrict simulation and reconstruction to ILD_l5_o1_v02 to avoid timeout in TravisCI
  - MarlinStdReco.xml
      - Changed default `DetectorModel` constant to none causing error if user don't specify it

* 2018-04-18 Ete Remi ([PR#82](https://github.com/ilcsoft/ILDConfig/pull/82))
  - Removed the full lcgeo_current directory as it is not maintained anymore. Bye bye Mokka world !

* 2018-04-18 Ete Remi ([PR#81](https://github.com/ilcsoft/ILDConfig/pull/81))
  - Overlay settings moved to Config directory
  - Created new constants, energy dependant, for beam size parameters
  - High level reco: vertexing
     - Get beam size parameters depending on the CMS energy
     - Use beamspot smearing only if a CMS energy is specified with `--constant.CMSEnergy=...`
  - TravisCI test
     - Run simulation for ILD_l/s5_v02 and reconstruction for ILD_l/s5_o1/o2_v02
     - Switch off BeamCalReco to avoid TravisCI timeout and test failure
  - Fixed wrong HCal sim calo hit collection names in Calibration file for ILD_s5_o2_v02 model

* 2018-04-16 Akiya Miyamoto ([PR#79](https://github.com/ilcsoft/ILDConfig/pull/79))
  - Background overlay documentation :
     - Fixed wrong sigmaZ value (cm to mm)
     - Added sigmaZ value to ddsim command line of signal simulation

* 2018-04-17 Frank Gaede ([PR#80](https://github.com/ilcsoft/ILDConfig/pull/80))
  - add TOF estimators for 0, 10 and 50 ps resolution
  - add numbers for vertex fit constraints from GuineaPig (500 GeV)

# v01-19-06-p01

* 2018-03-30 Remi Ete ([PR#76](https://github.com/iLCSoft/ILDConfig/pull/76))
  - PandoraPFA.xml
     - switch back to fixed BField values read from steering file instead of DD4hep B field

# v01-19-06


* 2018-03-28 Remi Ete ([PR#74](https://github.com/iLCSoft/ILDConfig/pull/74))
  - BeamCal calibration:
     - moved calibration constant of BeamCal in a Marlin constant
     - use Marlin constant in the BeamCal digitizer and the BeamCalClusterReco
     - energy calibration constant updated to 79.6 (old was 72)

# v01-19-05-p01

* 2017-11-22 Ete Remi ([PR#42](https://github.com/ilcsoft/ILDConfig/pull/42))
  - Re-generate production steering files, with OutputSteeringFile parameter empty

* 2017-11-29 Ete Remi ([PR#46](https://github.com/ilcsoft/ILDConfig/pull/46))
  - Moved Init and Output processors back in the top-level steering file
  - OverlayBg : 
    - Only one group of processors kept
    - Moved back to top-level steering file
    - Expected background values written in different constants file
    - To run overlay background use the constant RunOverlay=true/false and CMSEnergy=500 (250, 350, or 1000) to select the correct parameters
  - DDSim directory removed : 
    - ddsim_steer.py moved back into top-level directory (to make ILCDirac happy)
    - ddsim_steer_default.py removed (not used)
  - Generated steering files removed, as ILCDirac can now run on the top-level steering file 
  - Updated documentation on background overlay
  - Updated README.md file

* 2017-11-29 Ete Remi ([PR#43](https://github.com/ilcsoft/ILDConfig/pull/43))
  - Switch from SimpleMuonDigi to DDSimpleMuonDigi processor. 
  - Updated steering file configuration to run DDSimpleMuonDigi (detector names from lcgeo)


# v01-19-05

* 2017-11-16 Ete Remi ([PR#36](https://github.com/ilcsoft/ILDconfig/pull/36))
  - Updated SDHcal reconstruction config
    - Updated digitizer config to match the new version. See PR  [iLCSoft/MarlinReco/30](https://github.com/iLCSoft/MarlinReco/pull/30)
    - Updated SDHcal calibration constants
    - Moved Pandora settings file constant definition to Calibration directory files, as it is calorimeter dependant 
  - Removed GearXMLFile parameter as it is not needed anymore
  - Added Documentation for : 
    - DST content
    - how to run bg overlay
    - ILD MC production settings
  - Set ILD_l5_o1_v02 as default model in steering files and documentation

* 2017-11-15 Ete Remi ([PR#35](https://github.com/ilcsoft/ILDconfig/pull/35))
  - Setup overlay config for each center of mass energy into processor groups : 
    - added condition to execute a given overlay group by using a constant
    - removed file names and expBG configuration from constants section
    - set expBG values for 500 GeV to known values
    - set expBG values for 250, 350 and 1000 GeV to -1 (not communicated yet)
  
  Example to run at 500 GeV : 
  ```shell
  Marlin --constant.RunOverlay500GeV=true \
  --BgOverlayWW500GeV.InputFileNames=WWfile.slcio \
  --BgOverlayWB500GeV.InputFileNames=WBfile.slcio \
  --BgOverlayBW500GeV.InputFileNames=BWfile.slcio \
  --BgOverlayBB500GeV.InputFileNames=BBfile.slcio \
  --PairBgOverlay500GeV.InputFileNames=Pairfile.slcio \
  ./ProductionSteeringFiles/MarlinStdReco_ILD_l5_o1_v02.xml
  ```

* 2017-11-13 Ete Remi ([PR#33](https://github.com/ilcsoft/ILDconfig/pull/33))
  - Added Gear files for current detector models
  - New directory *ProductionSteeringFiles* containing Marlin XML generated files for production (generated from v01-19-05-pre04 from cvmfs)

* 2017-10-17 Ete Remi ([PR#25](https://github.com/iLCSoft/ILDConfig/pull/25))
  - FCAL MIP thresholds updated (BCAL, LCAL, LHCAL) using ILD_l4_model and a 0.5 cut from MIP peak

* 2017-10-17 Ete Remi ([PR#23](https://github.com/iLCSoft/ILDConfig/pull/23))
  - Removed software compensation weights from Pandora settings file
  - Added software compensation input parameters in DDMarlinPandora processor : 
    - SoftwareCompensationWeights : the sc weights
    - SoftwareCompensationEnergyDensityBins : the energy density bins
    - FinalEnergyDensityBin : the final energy density value

* 2017-10-12 Frank Gaede ([PR#24](https://github.com/iLCSoft/ILDConfig/pull/24))
  - set ForceSiTPCMerging=1 in FillLDCTracking

* 2017-10-28 Frank Gaede ([PR#26](https://github.com/iLCSoft/ILDConfig/pull/26))
  - switch back to using SiliconTracking rather than CellsAutomatonMV
        - this fixes the degraded impact parameter resolution at 20 deg 
        - reason is that no link is made from the VXD to the FTD and no SiTracks are created at this angle, which results in a large number of tracks having no VXD hits ...

* 2017-08-31 Ete Remi ([PR#13](https://github.com/iLCSoft/ILDConfig/pull/13))
  - new calibration and software compensation for ILD_l4_v02
       - Updated calibration constants in main Marlin file: bbudsc_3evt_stdreco_dd4hep.xml
       - Updated software compensation parameters in all Pandora settings files
       - Added calibration report files for easy comparison with incoming re-calibrations

* 2017-09-26 Bo Li ([PR#20](https://github.com/iLCSoft/ILDConfig/pull/20))
  - The calibration constants of SDHCAL are re-calculated for ILD detector model.

* 2017-09-26 Shaojun Lu ([PR#19](https://github.com/iLCSoft/ILDConfig/pull/19))
  - Fix ILD DDCellsAutomatonMV inputs.
      - Added the inputs in the steering file from ILD_l4_v02 (VXD, SIT and SET) for the tracker detector elements.

* 2017-11-02 Ete Remi ([PR#29](https://github.com/iLCSoft/ILDConfig/pull/29))
  - Fixed a bug in GenerateSteeringFiles.py (detectorModels arg option)
  - Updated README.md

* 2017-11-02 Ete Remi ([PR#28](https://github.com/iLCSoft/ILDConfig/pull/28))
  - Complete re-structure of lcgeo_current steering files in a new "production" directory : 
     - Main Marlin steering file split into many sub-steering files (Digit, Tracking, PFA, HLR, etc ...)
     - Tidy up of directory by removing un-used steering files
  - Added utility python script to generate simpler steering file per detector flavor

* 2017-11-02 Shaojun Lu ([PR#27](https://github.com/iLCSoft/ILDConfig/pull/27))
  - Update "lcgeo_current/README.md" for ILD_l4_v02 and ilcsoft_v01-19-04
      -  added additional documentation for DESY Green Ubuntu Desktops users.

* 2017-11-11 Ete Remi ([PR#32](https://github.com/iLCSoft/ILDConfig/pull/32))
  - Added GEAR file generator to quickly produce gear files for the current detector models
  - Updated Overlay processors : 
    - All processors unified in one include : Overlay.xml. All the others are deleted
    - Pair background overlay processor added
    - Overlay run under condition : react on true/false of the constant RunOverlay
    - Remove collection mapping as all the collection have to be overlaid in production mode 
  - Top level marlin steering file : 
    - Comments in file header updated
    - Externalized background overlay settings in the constants section (expBG and file names)
  - Removed HighLevelReco/execute.xml (unused)

* 2017-08-23 Bo Li ([PR#11](https://github.com/iLCSoft/ILDConfig/pull/11))
  - Added example of steering file for sdhcal digitizer

* 2017-11-08 Ete Remi ([PR#30](https://github.com/iLCSoft/ILDConfig/pull/30))
  - Added MergeCollection processors for hybrid ecal reconstruction : 
    - Merge collection of odd/even ecal hits in a unique collection, one for the barrel, one for the endcap
    - No effect on non-hybrid reconstruction, as the odd/even input collections do not exist in this case

* 2017-11-09 Shaojun Lu ([PR#31](https://github.com/iLCSoft/ILDConfig/pull/31))
  - merged all ILD CalorimeterHit which include the information after ILD calorimeters reconstruction.
  - added ILD CalorimeterHits into the LCTuple
      - named as "scpox, scpoy, scpoz", sc... for SimCalorimeterHits after simulation
      - named as "capox,capoy,capoz, catim", ca... for CalorimeterHits after reconstruction

* 2017-09-14 Frank Gaede ([PR#17](https://github.com/iLCSoft/ILDConfig/pull/17))
  - update bbudsc_3evt_stdreco_dd4hep.xml:
       - reduce InitialTrackErrorOmega for FullLDCTracking
        - update doc for bbudsc_3evt_stdreco_dd4hep.xml
        - use ILD_l4_v02 as default model

* 2017-09-14 Ete Remi ([PR#15](https://github.com/iLCSoft/ILDConfig/pull/15))
  - Software compensation weights re-tuned

* 2017-08-29 Frank Gaede ([PR#12](https://github.com/iLCSoft/ILDConfig/pull/12))
  - bug fix for RecoMCTruthLinker information in REC/DST files
           - replace PandoraClustersHack w/ PandoraClusters
              in all relevant steering files

* 2017-09-29 Shaojun Lu ([PR#22](https://github.com/iLCSoft/ILDConfig/pull/22))
  - Change ILD default central silicon tracking reconstruction.
      - Mini-vectors are created connecting two hits in neighbouring vertex barrel layers.
      - Cellular automaton is used to produce tracks from these mini-vectors which has been implemented into MarlinProcessor "DDCellsAutomatonMV".
      - It shows better tracking efficiency for the ILD. ILD will use it together with MarlinProcessor "ExtrToSIT" as default ILDConfig to replace MarlonProcessor "SiliconTracking_MarlinTrk".

* 2017-09-29 Ete Remi ([PR#21](https://github.com/iLCSoft/ILDConfig/pull/21))
  - Updated sdhcal Pandora settings file for SDHCAL reconstruction
  - Updated sdhcal Marlin steering file for SDHCAL reconstruction

# v01-19-04

* 2017-07-26 Frank Gaede ([PR#10](https://github.com/iLCSoft/ILDConfig/pull/10))
  - add stdreco file for ILD_ls5_v02 models w/ hybrid ecal
        - merge collections from even and odd layers for Ecal barrel and endcap
           before digitization
         - requires LCTuple > v01-08  ( for correct collection parameters )

* 2017-07-21 Ete Remi ([PR#9](https://github.com/iLCSoft/ILDConfig/pull/9))
  - Updated Ecal calibration constants to reflect the ecal sensitive layer thickness change (+5%) in this ILD model
  - Changed mip calibration constant in digitizer
  - Changed ecal energy factors in digitizers
  - Changed ECal mip scale in DDMarlinPandora accordingly
  - Changed ECalToEmGeV in DDMarlinPandora to 1 to reflect what is done in the calibration procedure


Frank Gaede 2017-07-19
  - add gear files for ILD_l/s_4/5_v02 models
  - supress DEBUG printout from EcalBarrelDigi in stdreco
  - replace SITSpacePointRelations w/ SITTrackerHitRelations

Frank Gaede 2017-07-17
  - increase MaxChi2PerHit in FullLDCTracking for SiTPC-merging

# v01-19-03

Frank Gaede 2017-07-07 
  - add old stdreco as bbudsc_3evt_stdreco_dd4hep_stripSIT.xml
  - use pixel readout for SIT in stdreco ( no SpacePointBuilder)
  - changed ecal calibration back to 20 thin layers

Frank Gaede 2017-06-29 
  - update phi-offsets in TPCEndPlateModulePhi0 for DDTPCDigi s

Shaojun Lu 2017-07-03 
  -  Follow the ECAL driver update, and change the ECAL 'calibration_layergroups' configuration.

Frank Gaede 2017-06-28 
  - add TPC endplate to DDTPCDigi in stdreco

Frank Gaede 2017-06-24 
  - use DDTPCDigiProcessor in bbudsc_3evt_stdreco_dd4hep

Frank Gaede 2017-06-12 
  - use DDCellsAutomatonMV rather than CellsAutomatonMV

Frank Gaede 2017-05-12 
  - add ddsim_steer_default.py as reference
  - update ddsim_steer.py based on complete default steering file
  - fix indentation in README.md


# v01-19-02

Shaojun Lu 2017-04-04 
  - Update ddsim_steer.py

Marko Petric 2017-03-23 
  - Add CONTRIBUTING.md and PULL_REQUEST_TEMPLATE

Frank Gaede 2017-03-21 
  - add AUTHORS file

Marko Petric 2017-03-21 
  - Remove badge for CI
  - add LICENCE

Shaojun Lu 2017-03-10 
  -  Added parameter 'MaxBarrelTrackerInnerRDistance' into the Marlin processor 'MyDDMarlinPandora', and over write the defalt value to accept most of the TCP only track hits as charge track for PFO.

Shaojun Lu 2017-03-06 
  -  Need further investigation about the mini-vector. For the time being we should thus use the 'DBD' tracking as default reconstruction.

Shaojun Lu 2017-02-21 
  -  Fix a typo about the collection name, 'HcalEndcapsRelationsSimRec', which is generated in Marlin processor 'MyHcalEndcapReco', and is needed by Marlin processor 'MyDDMarlinPandora'.
  -  Comment out 'MyBeamCalClusterReco', need more expert validation work.

Shaojun Lu 2017-02-15 
  -  Cleanup steering file: Remove unused old 'SpacePointBuilde', use the up-to-date 'DDSpacePointBuilder' for DD4hep reconstruction.
  -  Apply Marlin processor 'BeamCalClusterReco' as standard reconstruction, and updated the parameters from BeamCal expert.

Shaojun Lu 2017-02-10 
  -  Updated the standard reconstruction steering file for the Marlin processor 'BgOverlay', removed '...preShower' collections in the CollectionMap, and updated the gamma-gamma background sample file.


# v01-19-01

Shaojun Lu 2017-01-19 
  -  use mini-vecotrs processor CellsAutomatonMV (w/o SIT) and ExtrToSIT for SIT as the default stdreco steering configuration, which provide the better tracking efficiency for the forward region than DBD-style tracking.

Frank Gaede 2017-01-18 
  - update for v01-19-01

Huong Lan Tran 2017-01-11 
  - Update calibration constants after fixing bug in Muon cluster association algorithm

Huong Lan Tran 2016-12-22 
  - Update Pandora steering files to cope with changes in MuonClusterAssociationAlgorithm

# v01-19

Frank Gaede 2016-11-25 
  -  remove duplicate xml comments
  -  - use gear_ILD_l1_v01_dd4hep.xml
  -  - deactivate BgOverlay

Frank Gaede 2016-11-24 
  -  - remove obsoelte reco config files  - update versions to v01-19
  -  - remove old, obsolete directories:     - MokkaDBConfig     - LCFI_MokkaBasedNets     - StandardConfig        - clic_cdr, current, scripts  - updated README ( now README.md )

Shaojun Lu 2016-11-21 
  -  comment out the Ecal 'PreShowerSDAction' to follow the update in the new 'SEcal05' drivers which  are used 'ILD_l1_v01' and 'ILD_s1_v01'.

Shaojun Lu 2016-11-09 
  -  Updated README.md by replacing 'Simplified_ILD_o1_v05' with 'ILD_o1_v05' in the example.

Shaojun Lu 2016-10-21 
  -  Apply the new implementation DDSpacePointBuilder for SIT, SET and FTD, which using DD4hep/DDRec, and no gear needed.



# Older releases

Georgios Voutsinas 2016-09-22 
  - adding the updated beamcal bg files from Moritz
  - adding the updated beamcal bg files from Moritz

Shaojun Lu 2016-08-05 
  -  Fix the wrong execute order. Marlin processor 'BgOverlay' should be executed before Marlin processor 'MySplitCollectionByLayer'.

Georgios Voutsinas 2016-08-05 
  - updating CA processor parameters

Frank Gaede 2016-08-05 
  -  - re-activated LCIOOutputProcessor writing REC file

Shaojun Lu 2016-08-03 
  -  Update 'BgOverlay' processor CollectionMap and InputFileNames. The background file is generated with DD4hep ILD_o1_v05 module in lcgeo, and have the identicial encoding for each collection in the CollectionMap.

Huong Lan Tran 2016-08-03 
  - Correct input file bbudsc_3evt.slcio
  - Update dd4hep steering file with new realistic calo digi and new calibration constants with software compensation

Georgios Voutsinas 2016-08-01 
  - running BgOverlay after the SplitCollectionByLayer

Georgios Voutsinas 2016-07-31 
  - updating minivector tracking processor paraneters to accomodate SIT mini vectors

Georgios Voutsinas 2016-07-15 
  - and adding the necessary root files that forgot to add before...
  - activating - updating likelihood pid for dd4hep based sim...

Georgios Voutsinas 2016-07-14 
  - add weightFiles for Low Momentum Mu Pi Separation at lcgeo current

Georgios Voutsinas 2016-07-13 
  - updated calibration constants by Lan

Masakazu Kurata 2016-07-13 
  - add some parameters for PID

Shaojun Lu 2016-07-04 
  -  Fix the collection names for sub-detecor Yoke.
  -  Fix the collection names, case sensitive issue.

Andre Sailer 2016-06-30 
  - make the steering file valid XML

Georgios Voutsinas 2016-06-29 
  - change back the BackgroundMEthod in BeamCalClusterReco from parametrised to gaussian in dd4hep steering file, cause it causes a runtime error

Georgios Voutsinas 2016-06-28 
  - updating standard config file wrt to latest modifications on sw compensation from Lan

Georgios Voutsinas 2016-06-22 
  - updating BeamCalClusterReco parameters & some provisional changes

Georgios Voutsinas 2016-06-10 
  - consistency between xml files for mokka & dd4hep based sim, concerning tracking and HLR tools
  - adding HLR tools at dd4hep based std reconstruction steering file

Shaojun Lu 2016-05-27 
  -  HCALThreshold has been changed as 0.3MIP is 0.0001462GeV.
  -  Updated calibration constants for the ILD_o1_v05 in DD4hep/lcgeo, which obtained with 'LCPandoraAnalysis' from 10GeV Gamma, 10 GeV Muon and 20 GeV Kaon0L. Note: 'G4_W' was used as absorber material in SiWEcal.

Masakazu Kurata 2016-05-25 
  - add PID histgram templetes

Shaojun Lu 2016-05-24 
  -  Fix the Muon collection names. They come from the detectors now in  DD4hep/lcgeo: YokeBarrelCollection YokeEndcapsCollection.

Frank Gaede 2016-04-08 
  -  - add symbolic link to README.md
  -  - replaced README with README.md

Georgios Voutsinas 2016-02-24 
  - updating minivector steering file

Frank Gaede 2016-02-20 
  -  - added steering sections for DDCaloDigi and DDMarlinPandora    copied from the latest version in current/bbudsc_3evt_stdreco.xml   -> not used for now - needs checking ...

Frank Gaede 2016-02-18 
  -  - added BeamCalReco bg file
  -  - renamed bbudsc_3evt_ddsim.steer to ddsim_steer.py
  -  - moved the commented out file on pnfs outside of <parameter/> tag

Steven Green 2016-02-18 
  - Correcting typo in previous update to MarlinPandora and to BeamCalClusterReco steering.
  - Updated the settings in the digitsation and MarlinPandora processors specified in bbudsc_3evt_stdreco.xml.
  -  - updated README file  - added example for creating and analyzing an n-tuple
  -  - enabled BeamCalClusterReco in bbudsc_3evt_stdreco_dd4hep.xml  - removed onsolete ddsim.py  - added example for using particle gun to bbudsc_3evt_ddsim.steer
  -  - switched to Gaussian from Parameterised fro BeamCalReco

Jenny List 2016-02-16 
  - updated bbudsc_3evt_stdreco.xml to new BeamCalReco, added ClusterProperties and neutral PFO convariances for both PandoraPFOs and BeamCalPFOs, added pi0 finding and DistilledPFOs. No detailed testing yet, and many warnings from root via BeamReco

Frank Gaede 2016-02-16 
  -  - updated Pandora steering files also for the    old reconstruction ( new photon reco from Bono)

Shaojun Lu 2016-02-15 
  -  Update README for the current changes in ./StandardConfig/lcgeo_current folder.

Georgios Voutsinas 2016-02-05 
  - importing os so we can add the particle table
  - adding rad to the system of units

Shaojun Lu 2016-02-04 
  -  Update the PandoraPFA steering files according to the current development of PhotonReconstructionAlgorithm in PandoraPFA. We copy the new steering files from 'https://github.com/PandoraPFA/MarlinPandora/tree/master/scripts' with 'git clone https://github.com/PandoraPFA/MarlinPandora.git'.

Frank Gaede 2016-02-04 
  -  - added crossing angle and particle table to bbudsc_3evt_ddsim.steer  - added RemoveShortTracks in SubsetProcessor to bbudsc_3evt_stdreco_dd4hep.xml

Frank Gaede 2016-01-22 
  -  - added range cut to physics list  - changed to using physics.list  - changed to Geant4TrackerWeightedAction    without using weights as default for trackers

Constantino Calancha 2016-01-20 
  - Fixed syntactic errors in xml files.

Jenny List 2016-01-19 
  - enabled AddClusterProperties, changed overlay expectation value to 1.7 (500 GeV DBD)

Shaojun Lu 2016-01-15 
  -  Fix the calorimeters collection name order in stringVec for input and output.
  -  Fix forward calorimeter collection name, updated 'LHcalCollection' to 'LHCalCollection'.

Frank Gaede 2016-01-14 
  -  - force Si hits onto the tracking surface for all Si    trackers in DDPlanarDigi
  -  - updated tracker action for ddsim  - added StatusMonitor

Shaojun Lu 2016-01-08 
  -  Update few DDCaloDigi parameters value according to the steering 'ILD_o1_v05_SiW_5x5_Garlic_XXXX.xml'
  -  Update parameter 'CalibrECAL' - the Ecal calibration constant values in DDCaloDigi.
  -  Added 'DDCaloDigi' Marlin processor into 'bbudsc_3evt_stdreco_dd4hep.xml' standard reconstruction steering file. Try to replace 'NewLDCCaloDigi' Marlin processor, and to use 'DDCaloDigi' for standard reconstruction within DD4hep/lcgeo framework.

Frank Gaede 2016-01-07 
  -  - fixed skipEvents
  -  - added debug section for writing events and geometry to PandoraSettingsDefault  - added skipEvents to ddsim steering file

Frank Gaede 2016-01-04 
  -  - updated README to use ddsim  - fixed layer number for Ecal pre-shower layer    in bbudsc_3evt_ddsim.steer  - fixed ecal layer number for calo digi in  bbudsc_3evt_stdreco_dd4hep.xml

Masakazu Kurata 2015-12-18 
  - Add a parameter of Particle ID

Masakazu Kurata 2015-12-17 
  - Add parameters of LikelihoodPIDProcessor

Mikael Berggren 2015-12-13 
  - Added AddClusterProperties stanza. The execute one is out-commented at the moment, awaiting full tests.

Shaojun Lu 2015-12-11 
  -  Update the 'bbudsc_3evt_stdreco.xml' standard reconstrction steering file according to the revision 5164 updated by marshall, 'PandoraSettingsDefaultNewPhoton.xml' does not exist after '5164'. and Marshall has included the new photon fragment merging algorithms from B. Xu in the 'PandoraSettingsDefault.xml'.

Frank Gaede 2015-11-13 
  -  - updated steering file for ddsim

Frank Gaede 2015-11-12 
  -  - steering file for running ddsim

Georgios Voutsinas 2015-11-01 
  - Updating steering file that uses FPCCD tracking in order to be compatible with latest sw

Frank Gaede 2015-09-29 
  -  - enable CaloPreShowerSDAction for Ecals  - enable debug geometry dump from pandora  - fixed some collection names

Frank Gaede 2015-09-23 
  -  - copy updated PandoraSettingsDefault.xml from ./current  - update bbudsc_3evt_stdreco_dd4hep.xml to new calo surfaces  - include new collection names in bbudsc_3evt_viewer.xml

John Marshall 2015-09-10 
  - Remove placeholder PandoraSettings file containing the new photon fragment merging algorithms.
  - PandoraSettings update - include new photon fragment merging algorithms from B. Xu.

Frank Gaede 2015-09-09 
  -  - updated to latest DDMarlinPandora     - runs w/o crashing     - no reasonable results however ...  - use DDPlanarDigi for FTD and SET

Shaojun Lu 2015-09-03 
  -  Added one 'MyDDPandoraPFANewProcessor' configuration.

Frank Gaede 2015-07-31 
  -  - updated parameters for RecoMCTruthlinker

Frank Gaede 2015-07-30 
  -  - replaced TrackerCombineAction w/ TrackerAction

Frank Gaede 2015-07-25 
  -   - set default SD actions to Geant4TrackerCombineAction' and 'Geant4ScintillatorCalorimeterAction   - fixed FCalDigi parameter names

Frank Gaede 2015-07-24 
  -  - fixed capitalization of FcalThreshold parameter

Frank Gaede 2015-07-20 
  -  - renamed SimpleL(H)CalDigi to SimpleFCalDigi
  -   - use DDMarlinPandora in bbudsc_3evt_stdreco_dd4hep.xml   - updated viewer

Jenny List 2015-07-20 
  - adapted stdreco to new FCalDigi and removed BcalFix from redst

Frank Gaede 2015-07-15 
  -  - added bbudsc_3evt_stdreco_dd4hep ( incomplete )

Jenny List 2015-07-14 
  - stdreco now using SimpleLHCalDigi also for BeamCal. For LumiCal, using the new digitiser (thus writing a relation collection) crashes RecoMCTruthLink, thus LumiCal for now uses SimpleLCalDigi as before

Junping Tian 2015-07-14 
  - a list of reference post dst processors for analysis
  - adding config files for garlic option and fixed redst.xml to have MCParticlesSkimmedNew on the DST
  - stdreco.xml now with full RecoMCTruthLink

Hale Sert 2015-07-13 
  - updated reco steering files
  - reco steering file is updated to use PID mu-pi weights
  - weightfiles fow low mu-pi separation

Jenny List 2015-07-10 
  - added a redst.xml - still needs tracks to be updatable
  - now also Garlic read-in option works for Pandora
  - prototype of postDST.xml. For now just taufinder, rest to be added

Taikan Suehara 2015-07-09 
  - New steering in v3 for new jet clustering

Jenny List 2015-07-09 
  - now also with covariance matrix for charged PFOs
  - first version of new standard steering file with SiTracking options, Pandora options, Taufinding, ClusterShapes etc pp

Georgios Voutsinas 2015-07-09 
  - xml file for pair bkg overlay added
  - I forgot to switch off by default the additional VXD digitisers in the minivector steering file
  - adding different VXD digitiser options, corresponding to different CMOS VXD models, to minivector tracking steering file

Georgios Voutsinas 2015-07-08 
  - updating mini-vector & FPCCD tracking steering files according to developments made in HLR week

Frank Gaede 2015-07-07 
  -   - add pandora steering file for new photon finder algorithm     from Boruo Xu (Bono)   - use this as new default in bbudsc_3evt_stdreco.xml

Frank Gaede 2015-07-06 
  -  - updated Pandora parameters ( absorber and int. lengths) from S.Green/J.Marshall  - added (commented out ) PFOAnalyis processor for JER studies     -> uncomment if needed

Frank Gaede 2015-06-25 
  -  - added modifued ddsim.py for 3 evt example

Frank Gaede 2015-06-24 
  -  - remove thislcgeo.sh from instructions    -> now included in init_ilcsoft.sh

Masakazu Kurata 2015-06-24 
  - change parameter names for shower profile

Masakazu Kurata 2015-06-19 
  - added new processors for dedx, cluster shower profile, and particle identification

Frank Gaede 2015-06-15 
  -  - updated Readme and steering file for    reconstructing DD4hep based simulation with    the 'old' standard reconstruction

Taikan Suehara 2015-06-15 
  - Description for v3 functions added.

Frank Gaede 2015-06-09 
  -  - added copy of standrad config files - to be modified   for dd4hep ...

Georgios Voutsinas 2015-06-04 
  - updating README file with comments for the alternative reconstruction steering files

Georgios Voutsinas 2015-06-03 
  - Adding Marlin steering file which runs the FPCCD tracking algorithm Experimental - not yet fully validated
  - adding a reconstruction file which uses a mini-vector algorithm, based on cellular automaton tools, for pattern recognition at the VXD-SIT still experimental - not fully validated According to the examined VXD design, the user should set the proper time resolution for pair bkg overlay and spatial resolution at the VXDPlanarDigiProcessor

Taikan Suehara 2015-04-08 
  - training files v03/vtxprob files v2 added

John Marshall 2015-02-16 
  - Restore PandoraSettingsBasic.xml to repository. Add to list of cheated neutral hadrons in PandoraSettingsPerfectPhotonNeutronK0L.xml Update readme.

Georgios Voutsinas 2015-01-23 
  - Updating pandora xml files to run std reco

John Marshall 2014-07-30 
  - Copy across latest Pandora settings to prevent divergence (minor modifications only).

Christoph Rosemann 2013-10-24 
  - updated some convenience stuff for initialization

Christoph Rosemann 2013-08-06 
  - add line for new model; allows simple copy&paste for starting

Jan Engels 2012-12-18 
  - added -U option (needed for /Mokka/init/globalModelParameter FieldPropagator_LargestAcceptableStep 10)

Gerald Grenier 2012-12-10 
  - add ILD_o2_v05 gearfile
  - add ILD_o2_v05 reconstruction steering file

Jan Engels 2012-11-23 
  - added fix by A. Sailer (FieldPropagator_LargestAcceptableStep)

Jan Engels 2012-11-07 
  - changed path of BgOverlay file for making example runnable by everyone

Tomohiko Tanabe 2012-10-25 
  - fix typo..
  - fix steering files for v02 add 1 TeV weight files

Tomohiko Tanabe 2012-10-17 
  - training files v02 added
  - added more explanation
  - added more weight files, packed as tarball to save space

Tomohiko Tanabe 2012-10-15 
  - remove duplicated entries (does not affect performance)
  - update stdreco.xml to be consistent with LCFIPlus training weights
  - LCFIPlusConfig first release

Steven Aplin 2012-10-11 
  - restore RecoMCTruthLink

Jan Engels 2012-10-11 
  - fixed for storing DSTs outside of tape (files are too small)

Jan Engels 2012-10-08 
  - added bg map for 500 GeV (A. Rosca)

Frank Gaede 2012-10-05 
  -    - activate BgOverlay (now default !)

Frank Gaede 2012-10-01 
  -  - updated bg map from A.Rosca for 1 TeV    and new/updated map for 500 GeV

Robin Glattauer 2012-09-30 
  - parameters for ForwardTracking

Frank Gaede 2012-09-27 
  -    - updated LCFIPlus Vertex finder steering section      as suggested by T.Suehara: merged parameters from      LCFIPlus/steer/vertex.xml

Jan Engels 2012-09-27 
  - removed hardcoded timeout values (set as the default values from corresponding scripts)

Robin Glattauer 2012-09-26 
  - ForwardTracking: Set chi2prob cut to 0.

Jan Engels 2012-09-26 
  - fixed bug with whitespaces

Jan Engels 2012-09-25 
  - added BG_OVERLAY_FILE optional command line parameter
  - added optional BG_OVERLAY_FILE

Frank Gaede 2012-09-25 
  -    - set SuppressCheck false again ---- v01-15-02-p00 ---

John Marshall 2012-09-25 
  - Reduce MarlinPandora ECALToHAD and HCALToHAD calibration constants by factor of 0.96. This represents a calibration optimised for jet energy resolution, rather than for the reconstruction of single hadrons.

Frank Gaede 2012-09-21 
  -    - changed the point resolution for the FTD      to res_pixel = 0.003 and res_strip = 0.007
  -    - include SET hits in tracking again    - turn off ForceTPCSegmentsMerging

Frank Gaede 2012-09-20 
  -   - turned ForceTPCSegmentsMerging on again
  -   - remove SET hits from FullLDCTracking
  -   - turned ForceTPCSegmentsMerging off

Frank Gaede 2012-09-19 
  -  - increased SETHitToTrackDistance to 50 mm    in order to take parallax into account    when assignint SET hits to tracks

Frank Gaede 2012-09-14 
  -  - do not run check() method (workaround for BCal bug)

Jan Engels 2012-09-13 
  - switched to use new beamcal background file from A.Rosca: bg_aver.sv01-14-p00.mILD_o1_v05.E1000-B1b_ws.PBeamstr-pairs.I210000.root

Frank Gaede 2012-09-13 
  -   - switched to use new beamcal background file from A.Rosca:     bg_aver.sv01-14-p00.mILD_o1_v05.E1000-B1b_ws.PBeamstr-pairs.I210000.root

Jan Engels 2012-09-12 
  - added missing setting of RandomSeed

Frank Gaede 2012-09-11 
  -    - added section for BGOverlay to overlay      gamma gamma -> hadrons background (4.1 evts/BX)      currently commented out

Steven Aplin 2012-09-07 
  - Removed old depreacted digitizers. Added SET digi and spacepoint builder. Set new tracking as default.
  - renamed SimplePlanarTestDigiProcessor PlanarDigiProcessor

Tomohiko Tanabe 2012-09-07 
  - Added BuildUpVertex_V0 as a collection to keep for standard DST, needed for LCFIPlus

Frank Gaede 2012-09-06 
  -  - updated resolution parameters for the VXD according to    the table given in the DBD draft:      ResolutionU:  0.0028 0.006 0.004 0.004 0.004 0.004      ResolutionV:  0.0028 0.006 0.004 0.004 0.004 0.004

Jan Engels 2012-09-05 
  - fixed polarisation values

Steven Aplin 2012-08-30 
  - changed MCPRelColl names in FullLDCTracking

Steven Aplin 2012-08-28 
  - corrected FTD TrackerHit collection name parameter. It would have had no effect before as the default would have always been used.

Frank Gaede 2012-08-20 
  - - added BCalParticles in CEDViewer

Steven Aplin 2012-08-17 
  - Added SimTrackerHitCollections to MyRecoMCTruthLinker
  - Do not assign left over TPC hits. Clupatra is good enough.

Jan Engels 2012-08-15 
  - added PandoraLikelihoodData9EBin.xml and renamed PandoraSettings.xml to PandoraSettingsDefault.xml
  - deactivated TruthTracker
  - updated ilcsoft versin
  - updated mokka version
  - increased timeout values

Steven Aplin 2012-08-02 
  - corrected SITSpacePointRelations in RecoMCTruthLinker

John Marshall 2012-07-04 
  - Update reconstruction steering file to use pandora photon clustering algorithm. Add pandora steering file README.

Jan Engels 2012-07-02 
  - copy stdout and stderr to tarball

John Marshall 2012-06-28 
  - Remove MuonCoilCorrection plugin energy correction function.

Jan Engels 2012-06-28 
  - fixed bug initializing MokkaDBConfig
  - added info message

Jan Engels 2012-06-27 
  - regenerate steering file when running job.rerun
  - copy mokka.steer.in to log tarball
  - copy particle.tbl to log tarball
  - added -o ignore switch to grid-dl-file.py
  - changed to download ilcsoft binary tarballs from SE

John Marshall 2012-06-26 
  - By default, choose to copy stored fitter track states to pandora tracks, rather than calculate the track states manually.

Jan Engels 2012-06-25 
  - commented out primaryVertexSpreadZ

Steven Aplin 2012-06-25 
  - commented out primaryVertexSpreadZ

Steven Aplin 2012-06-21 
  - switched back to truth tracker for now
  - updated parameters for SiliconTracking_MarlinTrk and FullLDCTracking_MarlinTrk. Switch to using these instead of TruthTracker for testing

Frank Gaede 2012-06-20 
  -  - updated to ILD_o1_v05 detector model

Jan Engels 2012-06-20 
  - added PandoraSettingsMuon.xml

Jan Engels 2012-06-19 
  - synchronized mokka steering file

Frank Gaede 2012-06-19 
  -   - added BCALParticles to DST
  -  - added sqrt(2) to spread of zvertex
  -  - added  /Mokka/init/primaryVertexSpreadZ 0.300 mm to Mokka steering file
  -   - keep BuildUpVertex_RP and PrimaryVertex_RP collections on DST
  -  - updated release notes with changes in bbudsc_stdreco.xml
  -  - fixed name of UseOldTrackStateCalculation parameter for MarlinPandora
  -  - turn on UseIterativeFitting for TruthTracker
  -  - merged in new calibration constants form J.Marshall (branch ucam_2012)  - added new pandora settings: PandoraSettingsMuon.xml
  - updated release notes
  - added new mokka dump: mokka-08-00-dbdump.sql.tgz (2012-06-19 - 16:38:53) - last commit was broken
  - added new mokka dump: mokka-08-00-dbdump.sql.tgz (2012-06-19 - 16:28:17)
  -  - fixed syntax for <if condition/> for switching between tracking algorithms

Steven Aplin 2012-06-19 
  - changed model naming from ILD_OX_v0X to ILD_oX_v05
  -  - use TruthTracker instead of SiliconTracking/FullLDCTracking for now
  -  - switched Pandora to not use TracksTate @ Calorimeter
  -  - enabled KinkFinder  - removed local Verbosity parameters
  - added parameter /Mokka/init/mcRunNumber
  - added \*.py files into log tarball
  - added ./ for calling mokka-steer-gen.py
  - added mokka-steer-gen.py
  - added mokka parameter /Mokka/init/mcRunNumber

Jan Engels 2012-06-15 
  -  ----- v01-13-07-p02 -----
  - updated GearOutput.xml for mokka-07-07-p11
  - added new mokka dump: mokka-07-07-p11-dbdump.sql.tgz (2012-06-15 - 11:51:54)

Jan Engels 2012-06-12 
  -  ----- tagged v01-13-07-p01 -----
  - updated gear file for mokka-07-07-p10
  - added new mokka dump: mokka-07-07-p10-dbdump.sql.tgz (2012-06-12 - 16:32:57)

Jan Engels 2012-06-09 
  - added parameter /Mokka/init/lcioDetailedTRKHitMode SETCollection

Jan Engels 2012-06-08 
  - updated ilcsoft version and detector model
  - --- pre-tagged v01-13-07-p00 ---
  - updated GearOutput.xml to ILD_O1_v04
  - added new mokka dump: mokka-07-07-p09-dbdump.sql.tgz (2012-06-08 - 20:41:54)

Jan Engels 2012-06-04 
  - removed -a switch from copy command

Jan Engels 2012-05-24 
  - added GearOutput.xml
  - re-added GearOutput.xml (symlink to current)
  - removed GearOutput.xml
  - fixed unpacking of ilcsoft tarball

Robin Glattauer 2012-05-24 
  - ForwardTracking: updated to the latest steering

Jan Engels 2012-05-16 
  -  ------ v01-13-06 ---------
  - updated mokka dump: mokka-07-07-p08-dbdump.sql.tgz (2012-05-16 - 18:33:52)
  - updated ILD_O1_v02 to ILD_O1_v03

Frank Gaede 2012-05-16 
  -  - updated Clupatra steering parameters to v00-06

Jan Engels 2012-05-11 
  - fixed: call mysql-cleanup before anything else to make sure mysql socket is always cleaned up

Jan Engels 2012-05-10 
  - updated mokka dump: mokka-07-07-p08-dbdump.sql.tgz (2012-05-10 - 14:40:29)
  - added resource sharing

Jan Engels 2012-05-08 
  - added new mokka dump: mokka-07-07-p08-dbdump.sql.tgz (2012-05-08 - 14:35:40)

Robin Glattauer 2012-05-07 
  - changed steering parameters for the Cellular Automaton in ForwardTracking

Jan Engels 2012-05-02 
  - fixed error codes
  - fixed ILCSOFT path in job.sh
  - added MokkaDBConfig init.sh script
  - fixed number of arguments in job.sh

Jan Engels 2012-04-25 
  - added scripts to run sim/rec jobs on the grid
  - moved particle.tbl from MokkaDBConfig to StandardConfig/current

Steven Aplin 2012-04-24 
  - updated TruthTracker parameters

Robin Glattauer 2012-04-24 
  - removed the "works only for single particles, so far" comment for the TruthTracker, as it is outdated
  - modified some steering parameters of ForwardTracking

Robin Glattauer 2012-04-19 
  - Added TrackSubsetProcessor to the standard steer. It combines the tracks of SiliconTracking_MarlinTrk and ForwardTracking to one collection of tracks. This collections is then passed to FullLDCTracking_MarlinTrk

Robin Glattauer 2012-04-18 
  - corrected wrong comment in ForwardTracking steering

Frank Gaede 2012-04-16 
  -  - release notes fro version v01-13-05 -------

Robin Glattauer 2012-04-11 
  - reactivated ForwardTracking and changed steering parameter BestSubsetFinder to SubsetHopfieldNN

Jan Engels 2012-04-02 
  - removed duplicate BatchMode parameter

Jan Engels 2012-03-29 
  - updated README
  - added new mokka dump: mokka-07-07-p07-dbdump.sql.tgz (2012-03-29 - 17:56:36)

Frank Gaede 2012-03-29 
  -  - updated CLupatra steering section

Steven Aplin 2012-03-29 
  - updated planar digitiser and RecoMCTruthLinker for silicon strip hits
  -  - activated lcioDetailedTRKHitMode for all tracking detectors

Robin Glattauer 2012-03-29 
  - Slight corrections for the steering of ForwardTracking

Robin Glattauer 2012-03-16 
  - Added steering param to ForwardTracking: TakeBestVersionOfTrack

Robin Glattauer 2012-03-14 
  - Added steering parameter to ForwardTracking. It steers which method is used to find the best subset of tracks

Robin Glattauer 2012-03-13 
  - updated ForwardTracking parameter for hit collections

Steven Aplin 2012-03-02 
  - updated mokka-dbdump to mokka-07-07-p06
  - updated FTDCollection name to FTD_PIXELCollection and FTD_STRIPCollection

Frank Gaede 2012-03-02 
  -  --- updated release notes for v00-02
  -  - changed CutOnTPCHits from 35 to 10 for FullLDCTracking
  -  - added track-truth relations to RecoMCTruthLinker  - turned off drawing of helices
  -  - added optional stdhep test file with 1TeV tth events
  - updated tracking parameters

Jan Engels 2012-02-16 
  - changed mokka-wrapper to exit with the status returned by Mokka

Robin Glattauer 2012-02-16 
  - new TruthTracker steering parameters

Jan Engels 2012-02-01 
  - updated simple planar digitiser parameters for VXD to use CellID0 as written in the simhits (S. Aplin) * (r3055 merged from old location of Standardconfig)

Jan Engels 2012-01-26 
  - added utility to compare mokka models from the DB

Frank Gaede 2012-01-26 
  -  - added curren Mokka models

Frank Gaede 2012-01-25 
  -  - initial version
  -   - fixed LCIO types that need should be dropped form DST     - keep all ReconstructedParticles, and       remove all TrackerHit(Plane/ZCylinder) and LCGenericObject

Jan Engels 2012-01-25 
  - added MokkaDBConfig and LCFI_MokkaBasedNets
  - added StandardConfig
  - created new package ILDConfig
