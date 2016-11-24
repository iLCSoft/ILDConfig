

# Running ILD standard simulation and reconstruction

(F.Gaede, DESY )

<!---	  
   06/2015  F.G:  updated to use lcgeo/ddsim
   12/2011: F.G.: updated to new ILD_01_dev model 
   06/2012: J.E.: updated to new ILD_o{1,2,3}_v01 models
-->


These little examples serve as an ultra quick introduction on how to run iLCsoft 
standard simulation and reconstruction programs (for ILD).
They can also be used as a mini-test after installation of a new (complete) ilcsoft 
release.

For more information on the iLCSoft tools refer to the [iLCSoft Portal](http://ilcsoft.desy.de)
or directly to the [source code documentation](http://ilcsoft.desy.de/v01-19/package_doc.html) of the individual packages.


## 1. initialize the current ilcsoft release, e.g.
   
   
   source /afs/desy.de/project/ilcsoft/sw/x86_64_gcc48_sl6/v01-19/init_ilcsoft.sh


## 2. run the lcgeo/ddsim simulation example 

    ddsim --inputFiles ./bbudsc_3evt.stdhep --outputFile=./bbudsc_3evt.slcio --compactFile $lcgeo_DIR/ILD/compact/ILD_l1_v01/ILD_l1_v01.xml --steeringFile=./ddsim_steer.py


this creates the file:    bbudsc_3evt.slcio

You can now examine the collections in the file:

	anajob bbudsc_3evt.slcio

## 3. create a gear file for this model 

  convertToGear default $lcgeo_DIR/ILD/compact/ILD_l1_v01/ILD_l1_v01.xml gear_ILD_l1_v01_dd4hep.xml

  This creates a gear file for the ILD model and is currently still needed when running with 
  DD4hep/lcgeo as some processors have not yet been updated


## 4. reconstruct these events:

	Marlin bbudsc_3evt_stdreco_dd4hep.xml --InitDD4hep.DD4hepXMLFile=$lcgeo_DIR/ILD/compact/ILD_l1_v01/ILD_l1_v01.xml

creates:   bbudsc_3evt_REC.slcio 
and        bbudsc_3evt_DST.slcio

We can now for example dump the details of the 2nd event in the DST file: 

	dumpevent bbudsc_3evt_DST.slcio 2 | less



## 5. view the result in the event display
 
### a) start the event display (server) first:

	glced &

view REC or DST events:

	Marlin bbudsc_3evt_viewer.xml

	Marlin bbudsc_3evt_viewerDST.xml


### b) or start both, glced and Marlin in one go:

	ced2go   -d gear_ILD_l1_v01_dd4hep.xml  bbudsc_3evt_REC.slcio


### c) start CED with DD4hep geometry

Displays also the tracking surfaces: 
	
	ced2go -s 1 -d $lcgeo_DIR/ILD/compact/ILD_l1_v01/ILD_l1_v01.xml bbudsc_3evt_REC.slcio


## 6. create a ROOT TTree for analysis

  Marlin lctuple.xml

creates: bbudsc_3evt_REC_lctuple.root
which you can analyze with ROOT in the usual way - or run some examples:

	root [0] .x ./draw_simhits.C("bbudsc_3evt_REC_lctuple.root")
	root [1] .x ./draw_etot.C("bbudsc_3evt_REC_lctuple.root")



--------------------------------------------------------------------------------
