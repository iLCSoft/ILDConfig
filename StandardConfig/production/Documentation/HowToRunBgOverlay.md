

## Running the simulation

The samples from whizard can be found here :

*/pnfs/desy.de/ilc/prod/ilc/mc-dbd/generated/500-TDR_ws/aa_lowpt*

Use the following command line to get the latest (up-to-date) files :

```shell
ll /pnfs/desy.de/ilc/prod/ilc/mc-dbd/generated/500-TDR_ws/aa_lowpt | grep 'Aug 19'
```

To find the samples for WW, WB, BW or BB sample type, use the following commands on nafhh :

```shell
ll /pnfs/desy.de/ilc/prod/ilc/mc-dbd/generated/500-TDR_ws/aa_lowpt | grep 'Aug 19' | grep eW.pW | awk '{print $9}'
ll /pnfs/desy.de/ilc/prod/ilc/mc-dbd/generated/500-TDR_ws/aa_lowpt | grep 'Aug 19' | grep eW.pB | awk '{print $9}'
ll /pnfs/desy.de/ilc/prod/ilc/mc-dbd/generated/500-TDR_ws/aa_lowpt | grep 'Aug 19' | grep eB.pW | awk '{print $9}'
ll /pnfs/desy.de/ilc/prod/ilc/mc-dbd/generated/500-TDR_ws/aa_lowpt | grep 'Aug 19' | grep eB.pB | awk '{print $9}'
```

The following explanations suppose ilcsoft version v01-19-05 and detector model ILD_l5_o1_v02 as an example.

1. Running the Overlay Bg for GG background samples

Here is the table for the vertex displacement/smearing and expected bacground events, for the different GG processes at 500 GeV CMS :

<table>
  <tr>
    <td> Process </td>
    <td> Vertex z offset (mm) </td>
    <td> Vertex z sigma (mm) </td>
    <td> Expected background </td>
  </tr>
  <tr>
    <td> WW </td>
    <td> 0 </td>
    <td> 0.1968 </td>
    <td> 0.211 </td>
  </tr>
  <tr>
    <td> WB </td>
    <td> -0.04222 </td>
    <td> 0.186 </td>
    <td> 0.24605 </td>
  </tr>
  <tr>
    <td> BW </td>
    <td> +0.04222 </td>
    <td> 0.186 </td>
    <td> 0.243873 </td>
  </tr>
  <tr>
    <td> BB </td>
    <td> 0 </td>
    <td> 0.16988 </td>
    <td> 0.35063 </td>
  </tr>
</table>
 

For run the WW (virtual-virtual) simulation, e.g, for one file :

```shell
ddsim \
  --inputFiles /pnfs/desy.de/ilc/prod/ilc/mc-dbd/generated/500-TDR_ws/aa_lowpt/E0500-TDR_ws.Paaddhad.Gwhizard-1.95.eW.pW.I39212.01.stdhep \
  --outputFile sv01-19-05_lcgeo.mILD_l5_o1_v02.E0500-TDR_ws.Paaddhad.Gwhizard-1.95.eW.pW.I39212.01.stdhep.ddsim.slcio \
  --compactFile $lcgeo_DIR/ILD/compact/ILD_l5_o1_v02/ILD_l5_o1_v02.xml \
  --vertexSigma  0 0 0.1968 0 \
  --vertexOffset 0 0 0 0 \
  --steeringFile ddsim_steer.py
```

For run the WB (virtual-beam) simulation, e.g, for one file :

```shell
ddsim \
  --inputFiles /pnfs/desy.de/ilc/prod/ilc/mc-dbd/generated/500-TDR_ws/aa_lowpt/E0500-TDR_ws.Paaddhad.Gwhizard-1.95.eW.pB.I39213.01.stdhep \
  --outputFile sv01-19-05_lcgeo.mILD_l5_o1_v02.E0500-TDR_ws.Paaddhad.Gwhizard-1.95.eW.pB.I39213.01.stdhep.ddsim.slcio \
  --compactFile $lcgeo_DIR/ILD/compact/ILD_l5_o1_v02/ILD_l5_o1_v02.xml \
  --vertexSigma  0 0 0.186 0 \
  --vertexOffset 0 0 -0.04222 0 \
  --steeringFile ddsim_steer.py
```

For run the BW (beam-virtual) simulation, e.g, for one file :

```shell
ddsim \
  --inputFiles /pnfs/desy.de/ilc/prod/ilc/mc-dbd/generated/500-TDR_ws/aa_lowpt/E0500-TDR_ws.Paaddhad.Gwhizard-1.95.eB.pW.I39214.01.stdhep \
  --outputFile sv01-19-05_lcgeo.mILD_l5_o1_v02.E0500-TDR_ws.Paaddhad.Gwhizard-1.95.eB.pW.I39214.01.stdhep.ddsim.slcio \
  --compactFile $lcgeo_DIR/ILD/compact/ILD_l5_o1_v02/ILD_l5_o1_v02.xml \
  --vertexSigma  0 0 0.186 0 \
  --vertexOffset 0 0 0.04222 0 \
  --steeringFile ddsim_steer.py
```

For run the BB (beam-beam) simulation, e.g, for one file :

```shell
ddsim \
  --inputFiles /pnfs/desy.de/ilc/prod/ilc/mc-dbd/generated/500-TDR_ws/aa_lowpt/E0500-TDR_ws.Paaddhad.Gwhizard-1.95.eB.pB.I39215.01.stdhep \
  --outputFile sv01-19-05_lcgeo.mILD_l5_o1_v02.E0500-TDR_ws.Paaddhad.Gwhizard-1.95.eB.pB.I39215.01.stdhep.ddsim.slcio \
  --compactFile $lcgeo_DIR/ILD/compact/ILD_l5_o1_v02/ILD_l5_o1_v02.xml \
  --vertexSigma  0 0 0.16988 0 \
  --vertexOffset 0 0 0 0 \
  --steeringFile ddsim_steer.py
```

2. Running the Overlay Bg for pair background samples

The input file for pair background can be found here :

*/nfs/dust/ilc/user/berggren/blub/E500-TDR_ws.PBeamstr-seeablepairs.GGuineaPig-v1-4-4.I230001.0001.slcio*

and the command to run the ddsim simulation for pair background is the following :


```shell
ddsim \
  --inputFiles /nfs/dust/ilc/user/berggren/blub/E500-TDR_ws.PBeamstr-seeablepairs.GGuineaPig-v1-4-4.I230001.0001.slcio \
  --outputFile sv01-19-05_lcgeo.mILD_l5_o1_v02.E500-TDR_ws.PBeamstr-seeablepairs.GGuineaPig-v1-4-4.I230001.0001.simulated.slcio \
  --compactFile $lcgeo_DIR/ILD/compact/ILD_l5_o1_v02/ILD_l5_o1_v02.xml \
  --steeringFile ddsim_steer.py \
  --lcio.mcParticleCollectionName MCParticles
```

3. Running the main simulation

We first need to simulate events from a physics process. Here we use our usual 3 events ttbar test sample. We assume to be in the ILDConfig *StandardConfig/production* directory.  Note that the vertex offset and sigma for L and R electron/positron is same as W.

First run the simulation as usual :

```shell
ddsim \
  --inputFiles Examples/bbudsc_3evt/bbudsc_3evt.stdhep \
  --outputFile bbudsc_3evt.slcio \
  --compactFile $lcgeo_DIR/ILD/compact/ILD_l5_o1_v02/ILD_l5_o1_v02.xml \
  --vertexSigma  0 0 0.1968 0 \
  --vertexOffset 0 0 0 0 \
  --steeringFile ddsim_steer.py
```

and get the simulation output file as *bbudsc_3evt.slcio*, to be used as input for the reconstruction.

## Running the reconstruction with the overlay background

To run the reconstruction with the background overlay, you need to specify which CMS energy you want to use and where the simulated background files are located. The expected number of background events for each CMS energy can be found in the *Config* directory in different files. Assuming that all the produced background samples located in the directory 

*/nfs/dust/ilc/group/ild/eteremi/SIM/bg/*

are copied locally, one can run the following command to reconstruct events with the 500 GeV background overlay :

```shell
Marlin MarlinStdReco.xml \
  --constant.lcgeo_DIR=$lcgeo_DIR \
  --constant.DetectorModel=ILD_l5_o1_v02 \
  --global.LCIOInputFiles=bbudsc_3evt.slcio \
  --constant.OutputBaseName=bbudsc_3evt \
  --constant.RunOverlay=true \
  --constant.CMSEnergy=500 \
  --BgOverlayWW.InputFileNames=sv01-19-05_lcgeo.mILD_l5_o1_v02.E0500-TDR_ws.Paaddhad.Gwhizard-1.95.eW.pW.I39212.01.stdhep.slcio \
  --BgOverlayWB.InputFileNames=sv01-19-05_lcgeo.mILD_l5_o1_v02.E0500-TDR_ws.Paaddhad.Gwhizard-1.95.eW.pB.I39213.01.stdhep.slcio \
  --BgOverlayBW.InputFileNames=sv01-19-05_lcgeo.mILD_l5_o1_v02.E0500-TDR_ws.Paaddhad.Gwhizard-1.95.eB.pW.I39214.01.stdhep.slcio \
  --BgOverlayBB.InputFileNames=sv01-19-05_lcgeo.mILD_l5_o1_v02.E0500-TDR_ws.Paaddhad.Gwhizard-1.95.eB.pB.I39215.01.stdhep.slcio \
  --PairBgOverlay.InputFileNames=sv01-19-05_lcgeo.mILD_l5_o1_v02.E500-TDR_ws.PBeamstr-seeablepairs.GGuineaPig-v1-4-4.I230001.0001.simulated.slcio
```

This outputs the following output files : 

- bbudsc_3evt_AIDA.root : the AIDA root file
- bbudsc_3evt_REC.slcio : the REC file with all reconstructed collections
- bbudsc_3evt_DST.slcio : the DSL file with the collection suitable for physics analysis only
- bbudsc_3evt_PfoAnalysis.root : A root file with useful information on reconstructed particles for monitoring, calibration and uds performance

Note that the ee pair background overlay is not performed in the BeamCal as the BeamCal reconstruction already take this into account.

