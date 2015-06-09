PandoraPFANew Configuration
---------------------------

The configuration is firstly divided into two parts: 1). configuring the MarlinPandora client application and 2). configuring the Pandora algorithms, which perform the reconstruction.

MarlinPandora is responsible for isolating Pandora from all of the specific details about the detector and the Marlin software framework. It therefore contains configuration details such as calorimeter calibration constants, and track-quality cuts that are specific to the ILD reconstruction. These parameters are configured via the Marlin steering file in the same way as any other Marlin processor.

The Pandora reconstruction, however, is configured via the PandoraSettings.xml file (the path to this file is one of the client application parameters). This xml file describes the algorithms that will run each event. You will notice that there are many algorithms and that a number of them are "nested", i.e. parent algorithms call daughter algorithms.

The idea is that the same Pandora algorithms (and so same PandoraSettings.xml file) can be used for both ILD and SiD reconstruction, with different client applications initialising the Pandora reconstruction.

There are some useful details about the PandoraSettings.xml file at the following location:
http://www.hep.phy.cam.ac.uk/twiki/bin/view/Main/PandoraPFAQuestions

The key point is that every algorithm contains a number of configurable parameters. The default values for these parameters are hardcoded into the ReadSettings method of the algorithm, but you can override the defaults by adding the relevant xml keys to the correct algorithm in the xml file.

For example, to alter the initial clustering, you will need to find the ConeClustering section of the ClusteringParent algorithm:

<algorithm type = "ConeClustering" description = "ClusterFormation"/>

You will need to expand this (remove the closing / and add a new </algorithm> tag), then add your own values for the following example parameters (see the ReadSettings method for the full list):
    <TanConeAngleFine>0.18</TanConeAngleFine>
    <TanConeAngleCoarse>0.3</TanConeAngleCoarse>
    <AdditionalPadWidthsFine>1.5</AdditionalPadWidthsFine>
    <AdditionalPadWidthsCoarse>1.5</AdditionalPadWidthsCoarse>

These control the cone parameters used in the fine granularity region (i.e. ECAL) and the coarse granularity region (i.e. HCAL). You will notice that, because of the reclustering and muon clustering, there are actually a number of instances of the clustering algorithm in the reconstruction - modifications require some care.

---------------------------

A number of sample PandoraSettings.xml files are present in your MarlinPandora/scripts directory:

*PandoraSettingsBasic.xml - The core Pandora reconstruction, without photon clustering or standalone muon reconstruction.
*PandoraSettingsMuon.xml - The basic Pandora reconstruction, including a standalone muon reconstruction algorithm that reconstructs muons and removes them from the event before the remaining pattern recognition.
*PandoraSettingsDefault.xml - As above, but also includes a standalone photon reconstruction algorithm, which requires associated Likelihood data. Offers the best performance and is recommended for use with ILD_o1_v05/v06.

The PandoraLikelihoodData xml files are used by the standalone photon reconstruction algorithms and links to these files are specified in PandoraSettingsDefault.xml. The likelihood data has currently only been validated for ILD_o1_v05/v06. The two xml files contain likelihood PDFs for photon identification. The difference between the two files is the number of energy-bins for which separate PDFs are created. For PandoraLikelihoodData1EBin, there is only one PDF for signal and background for each likelihood variable. For PandoraLikelihoodData9EBin, there are separate PDFs for each of the energy ranges shown below (in GeV). PandoraLikelihoodData9EBin offers the best performance.
0.-0.5, 0.5-1., 1.-1.5, 1.5-2.5, 2.5-5., 5.-10., 10.-20., 20.-50., 50.+


Also available are some PandoraSettings.xml files that use MC information to cheat elements of the pattern recognition:

*PandoraSettingsPerfectPhoton.xml - Cheats the clustering of photons and subsequent tagging of these clusters as photons.
*PandoraSettingsPerfectPhotonNeutronK0L.xml - Cheats the clustering of photons, neutrons and K_longs, plus the associated particle id.
*PandoraSettingsPerfectPFA.xml - For each MC target, collects all associated tracks and clusters, thereby cheating all pattern-recognition; uses reconstructed properties to set PFO energies, etc.

---------------------------

The accompanying Marlin steering files are configured for use with Ilcsoft v01-17-05, with the detector model ILD_o1_v05/v06 and the physics list QGSP_BERT.
