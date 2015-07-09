*
* options for stdreco:
*
*

VXD digitizer (point res) & pair overlay (time res):
     <Xprocessor name="VXDPlanarDigiProcessor_DBDVXD"/>
      "DBD Standard"
      point resolution of layers in mm:     0.0028 0.006 0.004 0.004 0.004 0.004
      timing resolution of layers in mus: 
     <processor name="VXDPlanarDigiProcessor_CMOSVXD1"/>
      "realistic fast option"
      point resolution of layers in mm:     0.0028 0.006 0.004 0.01 0.004 0.01
      timing resolution of layers in mus:   50     2     100   7    100   7        
     <Xprocessor name="VXDPlanarDigiProcessor_CMOSVXD5"/>
      "challenging option"
      point resolution of layers in mm:     0.003 0.003 0.003 0.003 0.003 0.003
      timing resolution of layers in mus:   1     1     2     2     2     2      
     <Xprocessor name="VXDPlanarDigiProcessor_CMOSVXD5"/>
      "dream option"
      point resolution of layers in mm:     same as CMOSVXD5
      timing resolution of layers in mus:   single BX


SiliconTracking:
     <processor name="MySiliconTracking_MarlinTrk"/>  
      "DBD Standard"
     <processor name="MyCellsAutomatonMV"/>
       "Mini-vector"
     <processor name="MyFPCCDSiliconTracking_MarlinTrk"/>  
       "FPCCD"

  for these, please also choose an appropriate vertex 
  detector digitisation from above!
            
  
PANDORA:
   for Pandora, we have again three options, to be chosen in the ->> processor parameters <<-
   of MarlinRandora!!!!
  <parameter name="PandoraSettingsXmlFile" type="String"> PandoraSettingsDefault.xml </parameter>
  new best JER  Pandora
  <parameter name="PandoraSettingsXmlFile" type="String"> PandoraSettingsDefaultNewPhoton.xml </parameter>
  with improved photon finding by Bono
  <parameter name="PandoraSettingsXmlFile" type="String"> PandoraSettings_ILD_o1_v05_SiW_5x5_Garlic.xml</parameter>
  with input of Garlic photons: THIS DOES NOT WORK YET!
