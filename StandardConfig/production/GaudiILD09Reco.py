import os
from Gaudi.Configuration import *

from Configurables import LcioEvent, EventDataSvc, MarlinProcessorWrapper
from k4MarlinWrapper.parseConstants import *
algList = []
evtsvc = EventDataSvc()


CONSTANTS = {
             'lcgeo_DIR': os.environ["lcgeo_DIR"],
             'DetectorModel': "ILD_l5_o1_v09",
             'CompactFile': "%(lcgeo_DIR)s/ILD/compact/%(DetectorModel)s/%(DetectorModel)s.xml",
             'CalibrationFile': "Calibration/Calibration_%(DetectorModel)s.xml",
             'RunOverlay': "false",
             'CMSEnergy': "Unknown",
             'EnergyParametersFile': "Config/Parameters%(CMSEnergy)sGeV.xml",
             'RunBeamCalReco': "true",
             'BeamCalCalibrationFactor': "79.6",
             'PFAtype': "_SiILD",
             'EcalBarrelMip': "0.0001575",
             'EcalEndcapMip': "0.0001575",
             'EcalRingMip': "0.0001575",
             'HcalBarrelMip': "0.0004925",
             'HcalEndcapMip': "0.0004725",
             'HcalRingMip': "0.0004875",
             'EcalBarrelEnergyFactors': ["0.0063520964756", "0.012902699188"],
             'EcalEndcapEnergyFactors': ["0.0067218419842", "0.013653744940"],
             'EcalRingEnergyFactors': ["0.0066536339", "0.0135151972"],
             'HcalBarrelEnergyFactors': "0.0287783798145",
             'HcalEndcapEnergyFactors': "0.0285819096797",
             'HcalRingEnergyFactors': "0.0349940637704",
             'MuonCalibration': "56.7",
             'PandoraEcalToMip': "153.846",
             'PandoraHcalToMip': "37.1747",
             'PandoraMuonToMip': "10.5263",
             'PandoraEcalToEMScale': "1.0",
             'PandoraHcalToEMScale': "1.0",
             'PandoraEcalToHadBarrelScale': "1.17344504717",
             'PandoraEcalToHadEndcapScale': "1.17344504717",
             'PandoraHcalToHadScale': "1.02821419758",
             'PandoraSoftwareCompensationWeights': ["1.59121", "-0.0281982", "0.000250616", "-0.0424222", "0.000335128", "-2.06112e-05", "0.148549", "0.199618", "-0.0697277"],
             'ApplyPhotonPFOCorrections': "true",
             'EcalTechnology': "SiWEcal",
             'HcalTechnology': "AHcal",
             'PandoraSettingsFile': "PandoraSettings/PandoraSettingsDefault.xml",
             'DropCollectionsECal': ["ECalBarrelScHitsEven", "ECalBarrelScHitsOdd", "ECalEndcapScHitsEven", "ECalEndcapScHitsOdd"],
             'DropCollectionsHCal': ["HCalBarrelRPCHits", "HCalEndcapRPCHits", "HCalECRingRPCHits"],
             'AdditionalDropCollectionsREC': ["%(DropCollectionsECal)s", "%(DropCollectionsHCal)s"],
             'dEdXErrorFactor': "7.55",
             'dEdXSmearingFactor': "0.029",
             'PidPDFFile': "HighLevelReco/PIDFiles/LikelihoodPID_Standard_l5_v01.root",
             'PidWeightFiles': ["HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_02GeVP_clusterinfo.weights.xml", "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_03GeVP_clusterinfo.weights.xml", "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_04GeVP_clusterinfo.weights.xml", "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_05GeVP_clusterinfo.weights.xml", "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_06GeVP_clusterinfo.weights.xml", "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_07GeVP_clusterinfo.weights.xml", "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_08GeVP_clusterinfo.weights.xml", "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_09GeVP_clusterinfo.weights.xml", "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_10GeVP_clusterinfo.weights.xml", "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_11GeVP_clusterinfo.weights.xml", "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_12GeVP_clusterinfo.weights.xml", "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_13GeVP_clusterinfo.weights.xml", "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_14GeVP_clusterinfo.weights.xml", "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_15GeVP_clusterinfo.weights.xml", "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_16GeVP_clusterinfo.weights.xml", "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_17GeVP_clusterinfo.weights.xml", "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_18GeVP_clusterinfo.weights.xml", "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_19GeVP_clusterinfo.weights.xml", "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_20GeVP_clusterinfo.weights.xml"],
             'ECalBarrelSimHitCollections': ["ECalBarrelSiHitsEven", "ECalBarrelSiHitsOdd"],
             'ECalEndcapSimHitCollections': ["ECalEndcapSiHitsEven", "ECalEndcapSiHitsOdd"],
             'ECalRingSimHitCollections': "EcalEndcapRingCollection",
             'HCalBarrelSimHitCollections': "HcalBarrelRegCollection",
             'HCalEndcapSimHitCollections': "HcalEndcapsCollection",
             'HCalRingSimHitCollections': "HcalEndcapRingCollection",
             'ECalSimHitCollections': ["%(ECalBarrelSimHitCollections)s", "%(ECalEndcapSimHitCollections)s", "%(ECalRingSimHitCollections)s"],
             'HCalSimHitCollections': ["%(HCalBarrelSimHitCollections)s", "%(HCalEndcapSimHitCollections)s", "%(HCalRingSimHitCollections)s"],
             'BeamCalBackgroundFile': "HighLevelReco/BeamCalBackground/BeamCalBackground-E%(CMSEnergy)s-B3.5-RealisticNominalAntiDid.root",
             'ExpectedBgWW': "0",
             'ExpectedBgWB': "0",
             'ExpectedBgBW': "0",
             'ExpectedBgBB': "0",
             'LCFIPlusBeamspotConstraint': "false",
             'BeamSizeX': "0",
             'BeamSizeY': "0",
             'BeamSizeZ': "0",
             'OutputBaseName': "StandardReco",
             'AIDAFileName': "%(OutputBaseName)s_AIDA",
             'RECOutputFile': "%(OutputBaseName)s_REC.slcio",
             'DSTOutputFile': "%(OutputBaseName)s_DST.slcio",
             'PfoOutputFile': "%(OutputBaseName)s_PfoAnalysis.root",
}

parseConstants(CONSTANTS)

read = LcioEvent()
read.OutputLevel = INFO
read.Files = ["None"]
algList.append(read)

MyAIDAProcessor = MarlinProcessorWrapper("MyAIDAProcessor")
MyAIDAProcessor.OutputLevel = INFO
MyAIDAProcessor.ProcessorType = "AIDAProcessor"
MyAIDAProcessor.Parameters = {
                              "Compress": ["1"],
                              "FileName": ["%(AIDAFileName)s" % CONSTANTS],
                              "FileType": ["root"]
                              }

InitDD4hep = MarlinProcessorWrapper("InitDD4hep")
InitDD4hep.OutputLevel = INFO
InitDD4hep.ProcessorType = "InitializeDD4hep"
InitDD4hep.Parameters = {
                         "DD4hepXMLFile": ["%(CompactFile)s" % CONSTANTS]
                         }

MyStatusmonitor = MarlinProcessorWrapper("MyStatusmonitor")
MyStatusmonitor.OutputLevel = INFO
MyStatusmonitor.ProcessorType = "Statusmonitor"
MyStatusmonitor.Parameters = {
                              "HowOften": ["1"]
                              }

BgOverlayWW = MarlinProcessorWrapper("BgOverlayWW")
BgOverlayWW.OutputLevel = INFO
BgOverlayWW.ProcessorType = "Overlay"
BgOverlayWW.Parameters = {
                          "InputFileNames": ["undefined.slcio"],
                          "NumberOverlayEvents": ["0"],
                          "expBG": ["%(ExpectedBgWW)s" % CONSTANTS]
                          }

BgOverlayWB = MarlinProcessorWrapper("BgOverlayWB")
BgOverlayWB.OutputLevel = INFO
BgOverlayWB.ProcessorType = "Overlay"
BgOverlayWB.Parameters = {
                          "InputFileNames": ["undefined.slcio"],
                          "NumberOverlayEvents": ["0"],
                          "expBG": ["%(ExpectedBgWB)s" % CONSTANTS]
                          }

BgOverlayBW = MarlinProcessorWrapper("BgOverlayBW")
BgOverlayBW.OutputLevel = INFO
BgOverlayBW.ProcessorType = "Overlay"
BgOverlayBW.Parameters = {
                          "InputFileNames": ["undefined.slcio"],
                          "NumberOverlayEvents": ["0"],
                          "expBG": ["%(ExpectedBgBW)s" % CONSTANTS]
                          }

BgOverlayBB = MarlinProcessorWrapper("BgOverlayBB")
BgOverlayBB.OutputLevel = INFO
BgOverlayBB.ProcessorType = "Overlay"
BgOverlayBB.Parameters = {
                          "InputFileNames": ["undefined.slcio"],
                          "NumberOverlayEvents": ["0"],
                          "expBG": ["%(ExpectedBgBB)s" % CONSTANTS]
                          }

PairBgOverlay = MarlinProcessorWrapper("PairBgOverlay")
PairBgOverlay.OutputLevel = INFO
PairBgOverlay.ProcessorType = "Overlay"
PairBgOverlay.Parameters = {
                            "ExcludeCollections": ["BeamCalCollection"],
                            "InputFileNames": ["undefined.slcio"],
                            "NumberOverlayEvents": ["0"]
                            }

MySplitCollectionByLayer = MarlinProcessorWrapper("MySplitCollectionByLayer")
MySplitCollectionByLayer.OutputLevel = INFO
MySplitCollectionByLayer.ProcessorType = "SplitCollectionByLayer"
MySplitCollectionByLayer.Parameters = {
                                       "InputCollection": ["FTDCollection"],
                                       "OutputCollections": ["FTD_PIXELCollection", "0", "1", "FTD_STRIPCollection", "2", "6"]
                                       }

VXDPlanarDigiProcessor_CMOSVXD5 = MarlinProcessorWrapper("VXDPlanarDigiProcessor_CMOSVXD5")
VXDPlanarDigiProcessor_CMOSVXD5.OutputLevel = INFO
VXDPlanarDigiProcessor_CMOSVXD5.ProcessorType = "DDPlanarDigiProcessor"
VXDPlanarDigiProcessor_CMOSVXD5.Parameters = {
                                              "ForceHitsOntoSurface": ["true"],
                                              "IsStrip": ["false"],
                                              "ResolutionU": ["0.003"],
                                              "ResolutionV": ["0.003"],
                                              "SimTrackHitCollectionName": ["VXDCollection"],
                                              "SimTrkHitRelCollection": ["VXDTrackerHitRelations"],
                                              "SubDetectorName": ["VXD"],
                                              "TrackerHitCollectionName": ["VXDTrackerHits"]
                                              }

SITPlanarDigiProcessor = MarlinProcessorWrapper("SITPlanarDigiProcessor")
SITPlanarDigiProcessor.OutputLevel = INFO
SITPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
SITPlanarDigiProcessor.Parameters = {
                                     "ForceHitsOntoSurface": ["true"],
                                     "IsStrip": ["false"],
                                     "ResolutionU": ["0.005"],
                                     "ResolutionV": ["0.005"],
                                     "SimTrackHitCollectionName": ["SITCollection"],
                                     "SimTrkHitRelCollection": ["SITTrackerHitRelations"],
                                     "SubDetectorName": ["SIT"],
                                     "TrackerHitCollectionName": ["SITTrackerHits"]
                                     }

FTDPixelPlanarDigiProcessor = MarlinProcessorWrapper("FTDPixelPlanarDigiProcessor")
FTDPixelPlanarDigiProcessor.OutputLevel = INFO
FTDPixelPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
FTDPixelPlanarDigiProcessor.Parameters = {
                                          "ForceHitsOntoSurface": ["true"],
                                          "IsStrip": ["false"],
                                          "ResolutionU": ["0.003"],
                                          "ResolutionV": ["0.003"],
                                          "SimTrackHitCollectionName": ["FTD_PIXELCollection"],
                                          "SimTrkHitRelCollection": ["FTDPixelTrackerHitRelations"],
                                          "SubDetectorName": ["FTD"],
                                          "TrackerHitCollectionName": ["FTDPixelTrackerHits"]
                                          }

FTDStripPlanarDigiProcessor = MarlinProcessorWrapper("FTDStripPlanarDigiProcessor")
FTDStripPlanarDigiProcessor.OutputLevel = INFO
FTDStripPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
FTDStripPlanarDigiProcessor.Parameters = {
                                          "ForceHitsOntoSurface": ["true"],
                                          "IsStrip": ["false"],
                                          "ResolutionU": ["0.007"],
                                          "ResolutionV": ["0.0"],
                                          "SimTrackHitCollectionName": ["FTD_STRIPCollection"],
                                          "SimTrkHitRelCollection": ["FTDStripTrackerHitRelations"],
                                          "SubDetectorName": ["FTD"],
                                          "TrackerHitCollectionName": ["FTDStripTrackerHits"]
                                          }

OuterPlanarDigiProcessor = MarlinProcessorWrapper("OuterPlanarDigiProcessor")
OuterPlanarDigiProcessor.OutputLevel = INFO
OuterPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
OuterPlanarDigiProcessor.Parameters = {
                                       "IsStrip": ["false"],
                                       "ResolutionU": ["0.007"],
                                       "ResolutionV": ["0.09"],
                                       "SimTrackHitCollectionName": ["OuterTrackerBarrelCollection"],
                                       "SimTrkHitRelCollection": ["OuterTrackerBarrelHitsRelations"],
                                       "SubDetectorName": ["OuterTrackers"],
                                       "TrackerHitCollectionName": ["OTrackerHits"]
                                       }

OuterEndcapPlanarDigiProcessor = MarlinProcessorWrapper("OuterEndcapPlanarDigiProcessor")
OuterEndcapPlanarDigiProcessor.OutputLevel = INFO
OuterEndcapPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
OuterEndcapPlanarDigiProcessor.Parameters = {
                                             "IsStrip": ["false"],
                                             "ResolutionU": ["0.007"],
                                             "ResolutionV": ["0.09"],
                                             "SimTrackHitCollectionName": ["OuterTrackerEndcapCollection"],
                                             "SimTrkHitRelCollection": ["OuterTrackerEndcapHitsRelations"],
                                             "SubDetectorName": ["OuterTrackers"],
                                             "TrackerHitCollectionName": ["OTrackerEndcapHits"]
                                             }

MyConformalTracking = MarlinProcessorWrapper("MyConformalTracking")
MyConformalTracking.OutputLevel = INFO
MyConformalTracking.ProcessorType = "ConformalTrackingV2"
MyConformalTracking.Parameters = {
                                  "DebugHits": ["DebugHits"],
                                  "DebugPlots": ["false"],
                                  "DebugTiming": ["false"],
                                  "MCParticleCollectionName": ["MCParticle"],
                                  "MaxHitInvertedFit": ["6"],
                                  "MinClustersOnTrackAfterFit": ["3"],
                                  "RelationsNames": ["VXDTrackerHitRelations", "FTDPixelTrackerHitRelations", "FTDStripTrackerHitRelations", "SITTrackerHitRelations", "OuterTrackerBarrelHitsRelations", "OuterTrackerEndcapHitsRelations"],
                                  "RetryTooManyTracks": ["false"],
                                  "SiTrackCollectionName": ["SiTracksCT"],
                                  "SortTreeResults": ["true"],
                                  "Steps": ["[VXDBarrel]", "@Collections", ":", "VXDTrackerHits", "@Parameters", ":", "MaxCellAngle", ":", "0.005;", "MaxCellAngleRZ", ":", "0.005;", "Chi2Cut", ":", "100;", "MinClustersOnTrack", ":", "4;", "MaxDistance", ":", "0.04;", "SlopeZRange:", "10.0;", "HighPTCut:", "10.0;", "@Flags", ":", "HighPTFit,", "VertexToTracker", "@Functions", ":", "CombineCollections,", "BuildNewTracks", "[VXDEncap]", "@Collections", ":", "FTDPixelTrackerHits", "@Parameters", ":", "MaxCellAngle", ":", "0.005;", "MaxCellAngleRZ", ":", "0.005;", "Chi2Cut", ":", "100;", "MinClustersOnTrack", ":", "4;", "MaxDistance", ":", "0.04;", "SlopeZRange:", "10.0;", "HighPTCut:", "0.0;", "@Flags", ":", "HighPTFit,", "VertexToTracker", "@Functions", ":", "CombineCollections,", "ExtendTracks", "[LowerCellAngle1]", "@Collections", ":", "VXDTrackerHits,", "FTDPixelTrackerHits", "@Parameters", ":", "MaxCellAngle", ":", "0.025;", "MaxCellAngleRZ", ":", "0.025;", "Chi2Cut", ":", "100;", "MinClustersOnTrack", ":", "4;", "MaxDistance", ":", "0.04;", "SlopeZRange:", "10.0;", "HighPTCut:", "10.0;", "@Flags", ":", "HighPTFit,", "VertexToTracker,", "RadialSearch", "@Functions", ":", "CombineCollections,", "BuildNewTracks", "[LowerCellAngle2]", "@Collections", ":", "@Parameters", ":", "MaxCellAngle", ":", "0.05;", "MaxCellAngleRZ", ":", "0.05;", "Chi2Cut", ":", "2000;", "MinClustersOnTrack", ":", "4;", "MaxDistance", ":", "0.04;", "SlopeZRange:", "10.0;", "HighPTCut:", "10.0;", "@Flags", ":", "HighPTFit,", "VertexToTracker,", "RadialSearch", "@Functions", ":", "BuildNewTracks,", "SortTracks", "[Tracker]", "@Collections", ":", "SITTrackerHits,", "FTDStripTrackerHits,", "OTrackerHits,", "OTrackerEndcapHits", "@Parameters", ":", "MaxCellAngle", ":", "0.05;", "MaxCellAngleRZ", ":", "0.1;", "Chi2Cut", ":", "2000;", "MinClustersOnTrack", ":", "4;", "MaxDistance", ":", "0.04;", "SlopeZRange:", "10.0;", "HighPTCut:", "0.0;", "@Flags", ":", "HighPTFit,", "VertexToTracker,", "RadialSearch", "@Functions", ":", "CombineCollections,", "ExtendTracks", "[Displaced]", "@Collections", ":", "VXDTrackerHits,", "FTDPixelTrackerHits,", "SITTrackerHits,", "FTDStripTrackerHits,", "OTrackerHits,", "OTrackerEndcapHits", "@Parameters", ":", "MaxCellAngle", ":", "0.1;", "MaxCellAngleRZ", ":", "0.1;", "Chi2Cut", ":", "1000;", "MinClustersOnTrack", ":", "5;", "MaxDistance", ":", "0.035;", "SlopeZRange:", "10.0;", "HighPTCut:", "10.0;", "@Flags", ":", "OnlyZSchi2cut,", "RadialSearch", "@Functions", ":", "CombineCollections,", "BuildNewTracks"],
                                  "ThetaRange": ["0.05"],
                                  "TooManyTracks": ["100000"],
                                  "TrackerHitCollectionNames": ["VXDTrackerHits", "FTDPixelTrackerHits", "FTDStripTrackerHits", "SITTrackerHits", "OTrackerHits", "OTrackerEndcapHits"],
                                  "trackPurity": ["0.7"]
                                  }

ClonesAndSplitTracksFinder = MarlinProcessorWrapper("ClonesAndSplitTracksFinder")
ClonesAndSplitTracksFinder.OutputLevel = INFO
ClonesAndSplitTracksFinder.ProcessorType = "ClonesAndSplitTracksFinder"
ClonesAndSplitTracksFinder.Parameters = {
                                         "EnergyLossOn": ["true"],
                                         "InputTrackCollectionName": ["SiTracksCT"],
                                         "MultipleScatteringOn": ["true"],
                                         "OutputTrackCollectionName": ["SiTracks"],
                                         "SmoothOn": ["false"],
                                         "extrapolateForward": ["true"],
                                         "maxSignificancePhi": ["3"],
                                         "maxSignificancePt": ["2"],
                                         "maxSignificanceTheta": ["3"],
                                         "mergeSplitTracks": ["true"],
                                         "minTrackPt": ["1"]
                                         }

Refit = MarlinProcessorWrapper("Refit")
Refit.OutputLevel = INFO
Refit.ProcessorType = "RefitFinal"
Refit.Parameters = {
                    "EnergyLossOn": ["true"],
                    "InputRelationCollectionName": ["SiTrackRelations"],
                    "InputTrackCollectionName": ["SiTracks"],
                    "Max_Chi2_Incr": ["1.79769e+30"],
                    "MinClustersOnTrackAfterFit": ["3"],
                    "MultipleScatteringOn": ["true"],
                    "OutputRelationCollectionName": ["SiTracks_Refitted_Relation"],
                    "OutputTrackCollectionName": ["SiTracks_Refitted"],
                    "ReferencePoint": ["-1"],
                    "SmoothOn": ["false"],
                    "extrapolateForward": ["true"]
                    }

MergeCollectionsEcalBarrelHits = MarlinProcessorWrapper("MergeCollectionsEcalBarrelHits")
MergeCollectionsEcalBarrelHits.OutputLevel = INFO
MergeCollectionsEcalBarrelHits.ProcessorType = "MergeCollections"
MergeCollectionsEcalBarrelHits.Parameters = {
                                             "InputCollections": ["ECalBarrelSiHitsEven", "ECalBarrelSiHitsOdd"],
                                             "OutputCollection": ["EcalBarrelCollection"]
                                             }

MergeCollectionsEcalEndcapHits = MarlinProcessorWrapper("MergeCollectionsEcalEndcapHits")
MergeCollectionsEcalEndcapHits.OutputLevel = INFO
MergeCollectionsEcalEndcapHits.ProcessorType = "MergeCollections"
MergeCollectionsEcalEndcapHits.Parameters = {
                                             "InputCollections": ["ECalEndcapSiHitsEven", "ECalEndcapSiHitsOdd"],
                                             "OutputCollection": ["EcalEndcapsCollection"]
                                             }

MyEcalBarrelDigi = MarlinProcessorWrapper("MyEcalBarrelDigi")
MyEcalBarrelDigi.OutputLevel = INFO
MyEcalBarrelDigi.ProcessorType = "RealisticCaloDigiSilicon"
MyEcalBarrelDigi.Parameters = {
                               "CellIDLayerString": ["layer"],
                               "calibration_mip": ["%(EcalBarrelMip)s" % CONSTANTS],
                               "inputHitCollections": ["EcalBarrelCollection"],
                               "outputHitCollections": ["EcalBarrelCollectionDigi"],
                               "outputRelationCollections": ["EcalBarrelRelationsSimDigi"],
                               "threshold": ["0.5"],
                               "timingCut": ["1"]
                               }

MyEcalBarrelReco = MarlinProcessorWrapper("MyEcalBarrelReco")
MyEcalBarrelReco.OutputLevel = INFO
MyEcalBarrelReco.ProcessorType = "RealisticCaloRecoSilicon"
MyEcalBarrelReco.Parameters = {
                               "CellIDLayerString": ["layer"],
                               "calibration_factorsMipGev": ["%(EcalBarrelEnergyFactors)s" % CONSTANTS],
                               "calibration_layergroups": ["20", "11"],
                               "inputHitCollections": ["EcalBarrelCollectionDigi"],
                               "inputRelationCollections": ["EcalBarrelRelationsSimDigi"],
                               "outputHitCollections": ["EcalBarrelCollectionRec"],
                               "outputRelationCollections": ["EcalBarrelRelationsSimRec"]
                               }

MyEcalBarrelGapFiller = MarlinProcessorWrapper("MyEcalBarrelGapFiller")
MyEcalBarrelGapFiller.OutputLevel = INFO
MyEcalBarrelGapFiller.ProcessorType = "BruteForceEcalGapFiller"
MyEcalBarrelGapFiller.Parameters = {
                                    "CellIDLayerString": ["layer"],
                                    "CellIDModuleString": ["module"],
                                    "CellIDStaveString": ["stave"],
                                    "applyInterModuleCorrection": ["false"],
                                    "expectedInterModuleDistance": ["7.0"],
                                    "inputHitCollection": ["EcalBarrelCollectionRec"],
                                    "outputHitCollection": ["EcalBarrelCollectionGapHits"]
                                    }

MyEcalEndcapDigi = MarlinProcessorWrapper("MyEcalEndcapDigi")
MyEcalEndcapDigi.OutputLevel = INFO
MyEcalEndcapDigi.ProcessorType = "RealisticCaloDigiSilicon"
MyEcalEndcapDigi.Parameters = {
                               "CellIDLayerString": ["layer"],
                               "calibration_mip": ["%(EcalEndcapMip)s" % CONSTANTS],
                               "inputHitCollections": ["EcalEndcapsCollection"],
                               "outputHitCollections": ["EcalEndcapsCollectionDigi"],
                               "outputRelationCollections": ["EcalEndcapsRelationsSimDigi"],
                               "threshold": ["0.5"],
                               "timingCut": ["1"]
                               }

MyEcalEndcapReco = MarlinProcessorWrapper("MyEcalEndcapReco")
MyEcalEndcapReco.OutputLevel = INFO
MyEcalEndcapReco.ProcessorType = "RealisticCaloRecoSilicon"
MyEcalEndcapReco.Parameters = {
                               "CellIDLayerString": ["layer"],
                               "calibration_factorsMipGev": ["%(EcalEndcapEnergyFactors)s" % CONSTANTS],
                               "calibration_layergroups": ["20", "11"],
                               "inputHitCollections": ["EcalEndcapsCollectionDigi"],
                               "inputRelationCollections": ["EcalEndcapsRelationsSimDigi"],
                               "outputHitCollections": ["EcalEndcapsCollectionRec"],
                               "outputRelationCollections": ["EcalEndcapsRelationsSimRec"]
                               }

MyEcalEndcapGapFiller = MarlinProcessorWrapper("MyEcalEndcapGapFiller")
MyEcalEndcapGapFiller.OutputLevel = INFO
MyEcalEndcapGapFiller.ProcessorType = "BruteForceEcalGapFiller"
MyEcalEndcapGapFiller.Parameters = {
                                    "CellIDLayerString": ["layer"],
                                    "CellIDModuleString": ["module"],
                                    "CellIDStaveString": ["stave"],
                                    "applyInterModuleCorrection": ["false"],
                                    "expectedInterModuleDistance": ["7.0"],
                                    "inputHitCollection": ["EcalEndcapsCollectionRec"],
                                    "outputHitCollection": ["EcalEndcapsCollectionGapHits"]
                                    }

MyEcalRingDigi = MarlinProcessorWrapper("MyEcalRingDigi")
MyEcalRingDigi.OutputLevel = INFO
MyEcalRingDigi.ProcessorType = "RealisticCaloDigiSilicon"
MyEcalRingDigi.Parameters = {
                             "CellIDLayerString": ["layer"],
                             "calibration_mip": ["%(EcalRingMip)s" % CONSTANTS],
                             "inputHitCollections": ["EcalEndcapRingCollection"],
                             "outputHitCollections": ["EcalEndcapRingCollectionDigi"],
                             "outputRelationCollections": ["EcalEndcapRingRelationsSimDigi"],
                             "threshold": ["0.5"],
                             "timingCut": ["1"]
                             }

MyEcalRingReco = MarlinProcessorWrapper("MyEcalRingReco")
MyEcalRingReco.OutputLevel = INFO
MyEcalRingReco.ProcessorType = "RealisticCaloRecoSilicon"
MyEcalRingReco.Parameters = {
                             "CellIDLayerString": ["layer"],
                             "calibration_factorsMipGev": ["%(EcalRingEnergyFactors)s" % CONSTANTS],
                             "calibration_layergroups": ["20", "11"],
                             "inputHitCollections": ["EcalEndcapRingCollectionDigi"],
                             "inputRelationCollections": ["EcalEndcapRingRelationsSimDigi"],
                             "outputHitCollections": ["EcalEndcapRingCollectionRec"],
                             "outputRelationCollections": ["EcalEndcapRingRelationsSimRec"]
                             }

MyHcalBarrelDigi = MarlinProcessorWrapper("MyHcalBarrelDigi")
MyHcalBarrelDigi.OutputLevel = INFO
MyHcalBarrelDigi.ProcessorType = "RealisticCaloDigiScinPpd"
MyHcalBarrelDigi.Parameters = {
                               "CellIDLayerString": ["layer"],
                               "calibration_mip": ["%(HcalBarrelMip)s" % CONSTANTS],
                               "inputHitCollections": ["HcalBarrelRegCollection"],
                               "outputHitCollections": ["HcalBarrelCollectionDigi"],
                               "outputRelationCollections": ["HcalBarrelRelationsSimDigi"],
                               "ppd_mipPe": ["15"],
                               "ppd_npix": ["2000"],
                               "ppd_npix_uncert": ["0"],
                               "ppd_pix_spread": ["0"],
                               "threshold": ["0.5"],
                               "thresholdUnit": ["MIP"],
                               "timingCut": ["1"]
                               }

MyHcalBarrelReco = MarlinProcessorWrapper("MyHcalBarrelReco")
MyHcalBarrelReco.OutputLevel = INFO
MyHcalBarrelReco.ProcessorType = "RealisticCaloRecoScinPpd"
MyHcalBarrelReco.Parameters = {
                               "CellIDLayerString": ["layer"],
                               "calibration_factorsMipGev": ["%(HcalBarrelEnergyFactors)s" % CONSTANTS],
                               "calibration_layergroups": ["100"],
                               "inputHitCollections": ["HcalBarrelCollectionDigi"],
                               "inputRelationCollections": ["HcalBarrelRelationsSimDigi"],
                               "outputHitCollections": ["HcalBarrelCollectionRec"],
                               "outputRelationCollections": ["HcalBarrelRelationsSimRec"],
                               "ppd_mipPe": ["15"],
                               "ppd_npix": ["2000"]
                               }

MyHcalEndcapDigi = MarlinProcessorWrapper("MyHcalEndcapDigi")
MyHcalEndcapDigi.OutputLevel = INFO
MyHcalEndcapDigi.ProcessorType = "RealisticCaloDigiScinPpd"
MyHcalEndcapDigi.Parameters = {
                               "CellIDLayerString": ["layer"],
                               "calibration_mip": ["%(HcalEndcapMip)s" % CONSTANTS],
                               "inputHitCollections": ["HcalEndcapsCollection"],
                               "outputHitCollections": ["HcalEndcapsCollectionDigi"],
                               "outputRelationCollections": ["HcalEndcapsRelationsSimDigi"],
                               "ppd_mipPe": ["15"],
                               "ppd_npix": ["2000"],
                               "ppd_npix_uncert": ["0"],
                               "ppd_pix_spread": ["0"],
                               "threshold": ["0.5"],
                               "thresholdUnit": ["MIP"],
                               "timingCut": ["1"]
                               }

MyHcalEndcapReco = MarlinProcessorWrapper("MyHcalEndcapReco")
MyHcalEndcapReco.OutputLevel = INFO
MyHcalEndcapReco.ProcessorType = "RealisticCaloRecoScinPpd"
MyHcalEndcapReco.Parameters = {
                               "CellIDLayerString": ["layer"],
                               "calibration_factorsMipGev": ["%(HcalEndcapEnergyFactors)s" % CONSTANTS],
                               "calibration_layergroups": ["100"],
                               "inputHitCollections": ["HcalEndcapsCollectionDigi"],
                               "inputRelationCollections": ["HcalEndcapsRelationsSimDigi"],
                               "outputHitCollections": ["HcalEndcapsCollectionRec"],
                               "outputRelationCollections": ["HcalEndcapsRelationsSimRec"],
                               "ppd_mipPe": ["15"],
                               "ppd_npix": ["2000"]
                               }

MyHcalRingDigi = MarlinProcessorWrapper("MyHcalRingDigi")
MyHcalRingDigi.OutputLevel = INFO
MyHcalRingDigi.ProcessorType = "RealisticCaloDigiScinPpd"
MyHcalRingDigi.Parameters = {
                             "CellIDLayerString": ["layer"],
                             "calibration_mip": ["%(HcalRingMip)s" % CONSTANTS],
                             "inputHitCollections": ["HcalEndcapRingCollection"],
                             "outputHitCollections": ["HcalEndcapRingCollectionDigi"],
                             "outputRelationCollections": ["HcalEndcapRingRelationsSimDigi"],
                             "ppd_mipPe": ["15"],
                             "ppd_npix": ["2000"],
                             "ppd_npix_uncert": ["0"],
                             "ppd_pix_spread": ["0"],
                             "threshold": ["0.5"],
                             "thresholdUnit": ["MIP"],
                             "timingCut": ["1"]
                             }

MyHcalRingReco = MarlinProcessorWrapper("MyHcalRingReco")
MyHcalRingReco.OutputLevel = INFO
MyHcalRingReco.ProcessorType = "RealisticCaloRecoScinPpd"
MyHcalRingReco.Parameters = {
                             "CellIDLayerString": ["layer"],
                             "calibration_factorsMipGev": ["%(HcalRingEnergyFactors)s" % CONSTANTS],
                             "calibration_layergroups": ["100"],
                             "inputHitCollections": ["HcalEndcapRingCollectionDigi"],
                             "inputRelationCollections": ["HcalEndcapRingRelationsSimDigi"],
                             "outputHitCollections": ["HcalEndcapRingCollectionRec"],
                             "outputRelationCollections": ["HcalEndcapRingRelationsSimRec"],
                             "ppd_mipPe": ["15"],
                             "ppd_npix": ["2000"]
                             }

MySimpleBCalDigi = MarlinProcessorWrapper("MySimpleBCalDigi")
MySimpleBCalDigi.OutputLevel = INFO
MySimpleBCalDigi.ProcessorType = "SimpleFCalDigi"
MySimpleBCalDigi.Parameters = {
                               "CalibrFCAL": ["%(BeamCalCalibrationFactor)s" % CONSTANTS],
                               "CaloID": ["bcal"],
                               "CellIDLayerString": ["layer"],
                               "FCALCollections": ["BeamCalCollection"],
                               "FCALOutputCollection": ["BCAL"],
                               "FcalThreshold": ["5e-05"],
                               "RelationOutputCollection": ["RelationBCalHit"]
                               }

MySimpleLCalDigi = MarlinProcessorWrapper("MySimpleLCalDigi")
MySimpleLCalDigi.OutputLevel = INFO
MySimpleLCalDigi.ProcessorType = "SimpleFCalDigi"
MySimpleLCalDigi.Parameters = {
                               "CalibrFCAL": ["89.0"],
                               "CaloID": ["lcal"],
                               "CellIDLayerString": ["layer"],
                               "FCALCollections": ["LumiCalCollection"],
                               "FCALOutputCollection": ["LCAL"],
                               "FcalThreshold": ["0.4e-04"],
                               "RelationOutputCollection": ["RelationLcalHit"]
                               }

MySimpleLHCalDigi = MarlinProcessorWrapper("MySimpleLHCalDigi")
MySimpleLHCalDigi.OutputLevel = INFO
MySimpleLHCalDigi.ProcessorType = "SimpleFCalDigi"
MySimpleLHCalDigi.Parameters = {
                                "CalibrFCAL": ["150"],
                                "CaloID": ["lhcal"],
                                "CellIDLayerString": ["layer"],
                                "FCALCollections": ["LHCalCollection"],
                                "FCALOutputCollection": ["LHCAL"],
                                "FcalThreshold": ["1.7e-04"],
                                "RelationOutputCollection": ["RelationLHcalHit"]
                                }

MyDDSimpleMuonDigi = MarlinProcessorWrapper("MyDDSimpleMuonDigi")
MyDDSimpleMuonDigi.OutputLevel = INFO
MyDDSimpleMuonDigi.ProcessorType = "DDSimpleMuonDigi"
MyDDSimpleMuonDigi.Parameters = {
                                 "CalibrMUON": ["%(MuonCalibration)s" % CONSTANTS],
                                 "CellIDLayerString": ["layer"],
                                 "DetectorNameBarrel": ["YokeBarrel"],
                                 "DetectorNameEndcap": ["YokeEndcap"],
                                 "MUONCollections": ["YokeBarrelCollection", "YokeEndcapsCollection"],
                                 "MUONOutputCollection": ["MUON"],
                                 "MaxHitEnergyMUON": ["2.0"],
                                 "MuonThreshold": ["0.025"],
                                 "MuonTimeThreshold": ["0.025"],
                                 "RelationOutputCollection": ["RelationMuonHit"]
                                 }

MyDDMarlinPandora = MarlinProcessorWrapper("MyDDMarlinPandora")
MyDDMarlinPandora.OutputLevel = INFO
MyDDMarlinPandora.ProcessorType = "DDPandoraPFANewProcessor"
MyDDMarlinPandora.Parameters = {
                                "ClusterCollectionName": ["PandoraClusters"],
                                "CoilName": ["Coil"],
                                "CreateGaps": ["false"],
                                "DigitalMuonHits": ["0"],
                                "ECalBarrelDetectorName": ["EcalBarrel"],
                                "ECalCaloHitCollections": ["EcalBarrelCollectionRec", "EcalBarrelCollectionGapHits", "EcalEndcapsCollectionRec", "EcalEndcapsCollectionGapHits", "EcalEndcapRingCollectionRec"],
                                "ECalEndcapDetectorName": ["EcalEndcap"],
                                "ECalMipThreshold": ["0.5"],
                                "ECalOtherDetectorNames": ["EcalPlug", "Lcal", "BeamCal"],
                                "ECalToEMGeVCalibration": ["%(PandoraEcalToEMScale)s" % CONSTANTS],
                                "ECalToHadGeVCalibrationBarrel": ["%(PandoraEcalToHadBarrelScale)s" % CONSTANTS],
                                "ECalToHadGeVCalibrationEndCap": ["%(PandoraEcalToHadEndcapScale)s" % CONSTANTS],
                                "ECalToMipCalibration": ["%(PandoraEcalToMip)s" % CONSTANTS],
                                "FinalEnergyDensityBin": ["30"],
                                "HCalBarrelDetectorName": ["HcalBarrel"],
                                "HCalCaloHitCollections": ["HcalBarrelCollectionRec", "HcalEndcapsCollectionRec", "HcalEndcapRingCollectionRec"],
                                "HCalEndcapDetectorName": ["HcalEndcap"],
                                "HCalMipThreshold": ["0.3"],
                                "HCalOtherDetectorNames": ["HcalRing", "LHcal"],
                                "HCalToEMGeVCalibration": ["%(PandoraHcalToEMScale)s" % CONSTANTS],
                                "HCalToHadGeVCalibration": ["%(PandoraHcalToHadScale)s" % CONSTANTS],
                                "HCalToMipCalibration": ["%(PandoraHcalToMip)s" % CONSTANTS],
                                "KinkVertexCollections": ["KinkVertices"],
                                "LCalCaloHitCollections": ["LCAL"],
                                "LHCalCaloHitCollections": ["LHCAL"],
                                "MCParticleCollections": ["MCParticle"],
                                "MaxBarrelTrackerInnerRDistance": ["105.0"],
                                "MaxClusterEnergyToApplySoftComp": ["1000"],
                                "MaxHCalHitHadronicEnergy": ["1000000."],
                                "MinCleanCorrectedHitEnergy": ["0.1"],
                                "MinCleanHitEnergy": ["0.5"],
                                "MinCleanHitEnergyFraction": ["0.01"],
                                "MuonBarrelDetectorName": ["YokeBarrel"],
                                "MuonCaloHitCollections": ["MUON"],
                                "MuonEndcapDetectorName": ["YokeEndcap"],
                                "MuonOtherDetectorNames": [],
                                "MuonToMipCalibration": ["%(PandoraMuonToMip)s" % CONSTANTS],
                                "NEventsToSkip": ["0"],
                                "PFOCollectionName": ["PandoraPFOs"],
                                "PandoraSettingsXmlFile": ["%(PandoraSettingsFile)s" % CONSTANTS],
                                "ProngVertexCollections": ["ProngVertices"],
                                "RelCaloHitCollections": ["EcalBarrelRelationsSimRec", "EcalEndcapsRelationsSimRec", "EcalEndcapRingRelationsSimRec", "HcalBarrelRelationsSimRec", "HcalEndcapsRelationsSimRec", "HcalEndcapRingRelationsSimRec", "RelationMuonHit", "RelationLHcalHit", "RelationLcalHit"],
                                "RelTrackCollections": ["SiTracksMCP"],
                                "SoftwareCompensationEnergyDensityBins": ["0", "2", "5", "7.5", "9.5", "13", "16", "20", "23.5", "28"],
                                "SoftwareCompensationWeights": ["%(PandoraSoftwareCompensationWeights)s" % CONSTANTS],
                                "SplitVertexCollections": ["SplitVertices"],
                                "StartVertexAlgorithmName": ["PandoraPFANew"],
                                "StartVertexCollectionName": ["PandoraPFANewStartVertices"],
                                "TrackCollections": ["SiTracks"],
                                "TrackCreatorName": ["DDTrackCreatorCLIC"],
                                "TrackerBarrelDetectorNames": ["OuterTrackers"],
                                "TrackerEndcapDetectorNames": ["FTD"],
                                "UseDD4hepField": ["false"],
                                "UseOldTrackStateCalculation": ["0", "1"],
                                "V0VertexCollections": ["V0Vertices"],
                                "VertexBarrelDetectorName": ["VXD"],
                                "YokeBarrelNormalVector": ["0", "1", "0"]
                                }

MyBeamCalClusterReco = MarlinProcessorWrapper("MyBeamCalClusterReco")
MyBeamCalClusterReco.OutputLevel = INFO
MyBeamCalClusterReco.ProcessorType = "BeamCalClusterReco"
MyBeamCalClusterReco.Parameters = {
                                   "BackgroundMethod": ["Gaussian"],
                                   "BeamCalCollectionName": ["BCAL"],
                                   "CreateEfficiencyFile": ["false"],
                                   "DetectorName": ["BeamCal"],
                                   "DetectorStartingLayerID": ["1"],
                                   "ETCluster": ["0.06"],
                                   "ETPad": ["5e-5"],
                                   "EfficiencyFilename": ["TaggingEfficiency.root"],
                                   "InputFileBackgrounds": ["%(BeamCalBackgroundFile)s" % CONSTANTS],
                                   "LinearCalibrationFactor": ["%(BeamCalCalibrationFactor)s" % CONSTANTS],
                                   "LogWeightingConstant": ["-1."],
                                   "MCParticleCollectionName": ["MCParticle"],
                                   "MaxPadDistance": ["1e10"],
                                   "MinimumTowerSize": ["6"],
                                   "NShowerCountingLayers": ["3"],
                                   "NumberOfBX": ["1"],
                                   "PrintThisEvent": ["1"],
                                   "ReadoutName": ["BeamCalCollection"],
                                   "RecoClusterCollectionname": ["BCalClusters"],
                                   "RecoParticleCollectionname": ["BCalRecoParticle"],
                                   "SigmaCut": ["2"],
                                   "StartLookingInLayer": ["2"],
                                   "StartingRing": ["0"],
                                   "SubClusterEnergyID": ["5"],
                                   "TowerChi2ndfLimit": ["2."],
                                   "UseChi2Selection": ["false"],
                                   "UseConstPadCuts": ["false"]
                                   }

MyAdd4MomCovMatrixCharged = MarlinProcessorWrapper("MyAdd4MomCovMatrixCharged")
MyAdd4MomCovMatrixCharged.OutputLevel = INFO
MyAdd4MomCovMatrixCharged.ProcessorType = "Add4MomCovMatrixCharged"
MyAdd4MomCovMatrixCharged.Parameters = {
                                        "InputPandoraPFOsCollection": ["PandoraPFOs"]
                                        }

MyAddClusterProperties = MarlinProcessorWrapper("MyAddClusterProperties")
MyAddClusterProperties.OutputLevel = INFO
MyAddClusterProperties.ProcessorType = "AddClusterProperties"
MyAddClusterProperties.Parameters = {
                                     "ClusterCollection": ["PandoraClusters"],
                                     "PFOCollectionName": ["PandoraPFOs"]
                                     }

MyComputeShowerShapesProcessor = MarlinProcessorWrapper("MyComputeShowerShapesProcessor")
MyComputeShowerShapesProcessor.OutputLevel = INFO
MyComputeShowerShapesProcessor.ProcessorType = "ComputeShowerShapesProcessor"
MyComputeShowerShapesProcessor.Parameters = {
                                             "ClusterCollectionName": ["PandoraClusters"],
                                             "Debug": ["0"],
                                             "MoliereRadius_Ecal": ["9.00"],
                                             "MoliereRadius_Hcal": ["17.19"],
                                             "PFOCollection": ["PandoraPFOs"],
                                             "RadiationLength_Ecal": ["3.50"],
                                             "RadiationLength_Hcal": ["17.57"]
                                             }

MyphotonCorrectionProcessor = MarlinProcessorWrapper("MyphotonCorrectionProcessor")
MyphotonCorrectionProcessor.OutputLevel = INFO
MyphotonCorrectionProcessor.ProcessorType = "photonCorrectionProcessor"
MyphotonCorrectionProcessor.Parameters = {
                                          "energyCor_Linearise": ["0.987", "0.01426"],
                                          "energyCorr_barrelPhi": ["0.412249", "0.0142289", "-0.0933687", "0.01345", "0.0408156"],
                                          "energyCorr_costh": ["-0.09", "0.", "0.235", "0.007256", "-0.0369648", "0.", "0.588", "0.0121604", "-0.0422968", "0.774", "0.009", "1.002"],
                                          "energyCorr_endcap": ["-0.025", "855.", "23.", "-0.07", "1489.", "18."],
                                          "inputCollection": ["PandoraPFOs"],
                                          "modifyPFOdirection": ["%(ApplyPhotonPFOCorrections)s" % CONSTANTS],
                                          "modifyPFOenergies": ["%(ApplyPhotonPFOCorrections)s" % CONSTANTS],
                                          "nominalEnergy": ["200"],
                                          "phiCorr_barrel": ["2.36517e-05", "1.32090e-04", "-3.86883e+00", "-1.67809e-01", "2.28614e-05", "6.03495e-05", "0.419", "0.00728", "0.025", "0.00", "2.86667e-05", "2.49371e-05", "-7.71684e-06", "-1.48118e-05", "-5.63786e-06", "-9.38376e-06", "-4.96296e-06", "2.91262e-06"],
                                          "thetaCorr_barrel": ["-0.000166568", "-7.119e-05", "0.000223618", "-3.95915e-05"],
                                          "thetaCorr_endcap": ["0.000129478", "-3.73863e-05", "-0.000847783", "0.000153646", "0.000806605", "-0.000132608"],
                                          "validationPlots": ["false"]
                                          }

MyV0Finder = MarlinProcessorWrapper("MyV0Finder")
MyV0Finder.OutputLevel = INFO
MyV0Finder.ProcessorType = "V0Finder"
MyV0Finder.Parameters = {
                         "InputRecoParticleCollection": ["PandoraPFOs"],
                         "MassRangeGamma": ["0.01"],
                         "MassRangeK0S": ["0.1"],
                         "MassRangeL0": ["0.1"],
                         "TrackCollection": ["MarlinTrkTracks"]
                         }

MyPi0Finder = MarlinProcessorWrapper("MyPi0Finder")
MyPi0Finder.OutputLevel = INFO
MyPi0Finder.ProcessorType = "GammaGammaCandidateFinder"
MyPi0Finder.Parameters = {
                          "GammaGammaResonanceMass": ["0.1349766"],
                          "GammaGammaResonanceName": ["Pi0"],
                          "GammaMomentumCut": ["0.5"],
                          "InputParticleCollectionName": ["PandoraPFOs"],
                          "MaxDeltaMgg": ["0.04"],
                          "OutputParticleCollectionName": ["GammaGammaCandidatePi0s"],
                          "Printing": ["0"]
                          }

MyEtaFinder = MarlinProcessorWrapper("MyEtaFinder")
MyEtaFinder.OutputLevel = INFO
MyEtaFinder.ProcessorType = "GammaGammaCandidateFinder"
MyEtaFinder.Parameters = {
                          "GammaGammaResonanceMass": ["0.547862"],
                          "GammaGammaResonanceName": ["Eta"],
                          "GammaMomentumCut": ["1.0"],
                          "InputParticleCollectionName": ["PandoraPFOs"],
                          "MaxDeltaMgg": ["0.14"],
                          "OutputParticleCollectionName": ["GammaGammaCandidateEtas"],
                          "Printing": ["0"]
                          }

MyEtaPrimeFinder = MarlinProcessorWrapper("MyEtaPrimeFinder")
MyEtaPrimeFinder.OutputLevel = INFO
MyEtaPrimeFinder.ProcessorType = "GammaGammaCandidateFinder"
MyEtaPrimeFinder.Parameters = {
                               "GammaGammaResonanceMass": ["0.95778"],
                               "GammaGammaResonanceName": ["EtaPrime"],
                               "GammaMomentumCut": ["2.0"],
                               "InputParticleCollectionName": ["PandoraPFOs"],
                               "MaxDeltaMgg": ["0.19"],
                               "OutputParticleCollectionName": ["GammaGammaCandidateEtaPrimes"],
                               "Printing": ["0"]
                               }

MyGammaGammaSolutionFinder = MarlinProcessorWrapper("MyGammaGammaSolutionFinder")
MyGammaGammaSolutionFinder.OutputLevel = INFO
MyGammaGammaSolutionFinder.ProcessorType = "GammaGammaSolutionFinder"
MyGammaGammaSolutionFinder.Parameters = {
                                         "InputParticleCollectionName1": ["GammaGammaCandidatePi0s"],
                                         "InputParticleCollectionName2": ["GammaGammaCandidateEtas"],
                                         "InputParticleCollectionName3": ["GammaGammaCandidateEtaPrimes"],
                                         "OutputParticleCollectionName": ["GammaGammaParticles"],
                                         "Printing": ["0"]
                                         }

MyDistilledPFOCreator = MarlinProcessorWrapper("MyDistilledPFOCreator")
MyDistilledPFOCreator.OutputLevel = INFO
MyDistilledPFOCreator.ProcessorType = "DistilledPFOCreator"
MyDistilledPFOCreator.Parameters = {
                                    "InputParticleCollectionName1": ["PandoraPFOs"],
                                    "InputParticleCollectionName2": ["GammaGammaParticles"],
                                    "OutputParticleCollectionName": ["DistilledPFOs"],
                                    "Printing": ["0"]
                                    }

MyLikelihoodPID = MarlinProcessorWrapper("MyLikelihoodPID")
MyLikelihoodPID.OutputLevel = INFO
MyLikelihoodPID.ProcessorType = "LikelihoodPIDProcessor"
MyLikelihoodPID.Parameters = {
                              "CostMatrix": ["1.0e-50", "1.0", "1.5", "1.0", "1.5", "1.0", "1.0e-50", "3.0", "1.0", "1.0", "1.0", "1.0", "1.0e-50", "1.0", "3.0", "1.0", "1.0", "4.0", "1.0e-50", "2.0", "1.0", "1.0", "5.0", "1.0", "1.0e-50"],
                              "Debug": ["1"],
                              "EnergyBoundaries": ["0", "1.0e+07"],
                              "FilePDFName": ["%(PidPDFFile)s" % CONSTANTS],
                              "FileWeightFormupiSeparationName": ["%(PidWeightFiles)s" % CONSTANTS],
                              "RecoParticleCollection": ["PandoraPFOs"],
                              "UseBayesian": ["2"],
                              "UseLowMomentumMuPiSeparation": ["true"],
                              "dEdxErrorFactor": ["%(dEdXErrorFactor)s" % CONSTANTS],
                              "dEdxNormalization": ["1.350e-7"],
                              "dEdxParameter_electron": ["-1.28883368e-02", "2.72959919e+01", "1.10560871e+01", "-1.74534200e+00", "-9.84887586e-07"],
                              "dEdxParameter_kaon": ["7.52235689e-02", "1.59710415e+04", "1.79625604e+06", "3.15315795e-01", "2.30414997e-04"],
                              "dEdxParameter_muon": ["6.49143971e-02", "1.55775592e+03", "9.31848047e+08", "2.32201725e-01", "2.50492066e-04"],
                              "dEdxParameter_pion": ["6.54955215e-02", "8.26239081e+06", "1.92933904e+05", "2.52743206e-01", "2.26657525e-04"],
                              "dEdxParameter_proton": ["7.92251260e-02", "6.38129720e+04", "3.82995071e+04", "2.80793601e-01", "7.14371743e-04"]
                              }

MyRecoMCTruthLinker = MarlinProcessorWrapper("MyRecoMCTruthLinker")
MyRecoMCTruthLinker.OutputLevel = INFO
MyRecoMCTruthLinker.ProcessorType = "RecoMCTruthLinker"
MyRecoMCTruthLinker.Parameters = {
                                  "BremsstrahlungEnergyCut": ["1"],
                                  "CalohitMCTruthLinkName": ["CalohitMCTruthLink"],
                                  "ClusterCollection": ["PandoraClusters"],
                                  "ClusterMCTruthLinkName": ["ClusterMCTruthLink"],
                                  "FullRecoRelation": ["false"],
                                  "InvertedNonDestructiveInteractionLogic": ["false"],
                                  "KeepDaughtersPDG": ["22", "111", "310", "13", "211", "321", "3120"],
                                  "MCParticleCollection": ["MCParticle"],
                                  "MCParticlesSkimmedName": ["MCParticlesSkimmed"],
                                  "MCTruthClusterLinkName": [],
                                  "MCTruthRecoLinkName": [],
                                  "MCTruthTrackLinkName": ["MCTruthSiTracksLink"],
                                  "RecoMCTruthLinkName": ["RecoMCTruthLink"],
                                  "RecoParticleCollection": ["MergedRecoParticles"],
                                  "SaveBremsstrahlungPhotons": ["false"],
                                  "SimCaloHitCollections": ["BeamCalCollection", "LHCalCollection", "LumiCalCollection", "%(ECalSimHitCollections)s" % CONSTANTS, "%(HCalSimHitCollections)s" % CONSTANTS, "YokeBarrelCollection", "YokeEndcapsCollection"],
                                  "SimCalorimeterHitRelationNames": ["EcalBarrelRelationsSimRec", "EcalEndcapRingRelationsSimRec", "EcalEndcapsRelationsSimRec", "HcalBarrelRelationsSimRec", "HcalEndcapRingRelationsSimRec", "HcalEndcapsRelationsSimRec", "RelationLHcalHit", "RelationMuonHit", "RelationLcalHit", "RelationBCalHit"],
                                  "SimTrackerHitCollections": ["VXDCollection", "FTD_PIXELCollection", "SITCollection", "OuterTrackerBarrelCollection", "FTD_STRIPCollection", "OuterTrackerEndcapCollection"],
                                  "TrackCollection": ["SiTracks"],
                                  "TrackMCTruthLinkName": ["SiTracksMCTruthLink"],
                                  "TrackerHitsRelInputCollections": ["VXDTrackerHitRelations", "FTDPixelTrackerHitRelations", "SITTrackerHitRelations", "OuterTrackerBarrelHitsRelations", "FTDStripTrackerHitRelations", "OuterTrackerEndcapHitsRelations"],
                                  "UseTrackerHitRelations": ["true"],
                                  "UsingParticleGun": ["false"],
                                  "daughtersECutMeV": ["10"]
                                  }

MyLCIOOutputProcessor = MarlinProcessorWrapper("MyLCIOOutputProcessor")
MyLCIOOutputProcessor.OutputLevel = INFO
MyLCIOOutputProcessor.ProcessorType = "LCIOOutputProcessor"
MyLCIOOutputProcessor.Parameters = {
                                    "CompressionLevel": ["6"],
                                    "DropCollectionNames": ["%(AdditionalDropCollectionsREC)s" % CONSTANTS],
                                    "LCIOOutputFile": ["%(RECOutputFile)s" % CONSTANTS],
                                    "LCIOWriteMode": ["WRITE_NEW"]
                                    }

DSTOutput = MarlinProcessorWrapper("DSTOutput")
DSTOutput.OutputLevel = INFO
DSTOutput.ProcessorType = "LCIOOutputProcessor"
DSTOutput.Parameters = {
                        "CompressionLevel": ["6"],
                        "DropCollectionNames": ["PandoraPFANewStartVertices"],
                        "DropCollectionTypes": ["MCParticle", "SimTrackerHit", "SimCalorimeterHit", "TrackerHit", "TrackerHitPlane", "CalorimeterHit", "LCRelation", "Track", "LCFloatVec"],
                        "FullSubsetCollections": ["MCParticlesSkimmed"],
                        "KeepCollectionNames": ["MCParticlesSkimmed", "MarlinTrkTracks", "MarlinTrkTracksProton", "MarlinTrkTracksKaon", "MCTruthMarlinTrkTracksLink", "MarlinTrkTracksMCTruthLink", "RecoMCTruthLink", "MCTruthRecoLink", "MCTruthClusterLink", "ClusterMCTruthLink"],
                        "LCIOOutputFile": ["%(DSTOutputFile)s" % CONSTANTS],
                        "LCIOWriteMode": ["WRITE_NEW"]
                        }

MyPfoAnalysis = MarlinProcessorWrapper("MyPfoAnalysis")
MyPfoAnalysis.OutputLevel = INFO
MyPfoAnalysis.ProcessorType = "PfoAnalysis"
MyPfoAnalysis.Parameters = {
                            "BCalCollections": ["BCAL"],
                            "BCalCollectionsSimCaloHit": ["BeamCalCollection"],
                            "CollectCalibrationDetails": ["0"],
                            "ECalBarrelCollectionsSimCaloHit": ["%(ECalBarrelSimHitCollections)s" % CONSTANTS],
                            "ECalCollections": ["EcalBarrelCollectionRec", "EcalBarrelCollectionGapHits", "EcalEndcapsCollectionRec", "EcalEndcapsCollectionGapHits", "EcalEndcapRingCollectionRec"],
                            "ECalCollectionsSimCaloHit": ["%(ECalSimHitCollections)s" % CONSTANTS],
                            "ECalEndCapCollectionsSimCaloHit": ["%(ECalEndcapSimHitCollections)s" % CONSTANTS],
                            "ECalOtherCollectionsSimCaloHit": ["%(ECalRingSimHitCollections)s" % CONSTANTS],
                            "HCalBarrelCollectionsSimCaloHit": ["%(HCalBarrelSimHitCollections)s" % CONSTANTS],
                            "HCalCollections": ["HcalBarrelCollectionRec", "HcalEndcapsCollectionRec", "HcalEndcapRingCollectionRec"],
                            "HCalEndCapCollectionsSimCaloHit": ["%(HCalEndcapSimHitCollections)s" % CONSTANTS],
                            "HCalOtherCollectionsSimCaloHit": ["%(HCalRingSimHitCollections)s" % CONSTANTS],
                            "LCalCollections": ["LCAL"],
                            "LCalCollectionsSimCaloHit": ["LumiCalCollection"],
                            "LHCalCollections": ["LHCAL"],
                            "LHCalCollectionsSimCaloHit": ["LHCalCollection"],
                            "LookForQuarksWithMotherZ": ["2"],
                            "MCParticleCollection": ["MCParticle"],
                            "MCPfoSelectionLowEnergyNPCutOff": ["1.2"],
                            "MCPfoSelectionMomentum": ["0.01"],
                            "MCPfoSelectionRadius": ["500."],
                            "MuonCollections": ["MUON"],
                            "MuonCollectionsSimCaloHit": ["YokeBarrelCollection", "YokeEndcapsCollection"],
                            "PfoCollection": ["PandoraPFOs"],
                            "Printing": ["0"],
                            "RootFile": ["%(PfoOutputFile)s" % CONSTANTS]
                            }

algList.append(MyAIDAProcessor)
algList.append(InitDD4hep)
algList.append(MyStatusmonitor)
# # algList.append(BgOverlayWW)
# # algList.append(BgOverlayWB)
# # algList.append(BgOverlayBW)
# # algList.append(BgOverlayBB)
# # algList.append(PairBgOverlay)
algList.append(MySplitCollectionByLayer)
algList.append(VXDPlanarDigiProcessor_CMOSVXD5)
algList.append(SITPlanarDigiProcessor)
algList.append(FTDPixelPlanarDigiProcessor)
algList.append(FTDStripPlanarDigiProcessor)
algList.append(OuterPlanarDigiProcessor)
algList.append(OuterEndcapPlanarDigiProcessor)
algList.append(MyConformalTracking)
algList.append(ClonesAndSplitTracksFinder)
algList.append(Refit)
algList.append(MergeCollectionsEcalBarrelHits)
algList.append(MergeCollectionsEcalEndcapHits)
algList.append(MyEcalBarrelDigi)
algList.append(MyEcalBarrelReco)
algList.append(MyEcalBarrelGapFiller)
algList.append(MyEcalEndcapDigi)
algList.append(MyEcalEndcapReco)
algList.append(MyEcalEndcapGapFiller)
algList.append(MyEcalRingDigi)
algList.append(MyEcalRingReco)
algList.append(MyHcalBarrelDigi)
algList.append(MyHcalBarrelReco)
algList.append(MyHcalEndcapDigi)
algList.append(MyHcalEndcapReco)
algList.append(MyHcalRingDigi)
algList.append(MyHcalRingReco)
algList.append(MySimpleBCalDigi)
algList.append(MySimpleLCalDigi)
algList.append(MySimpleLHCalDigi)
algList.append(MyDDSimpleMuonDigi)
algList.append(MyDDMarlinPandora)
algList.append(MyBeamCalClusterReco)
algList.append(MyAdd4MomCovMatrixCharged)
algList.append(MyAddClusterProperties)
algList.append(MyComputeShowerShapesProcessor)
algList.append(MyphotonCorrectionProcessor)
algList.append(MyV0Finder)
algList.append(MyPi0Finder)
algList.append(MyEtaFinder)
algList.append(MyEtaPrimeFinder)
algList.append(MyGammaGammaSolutionFinder)
algList.append(MyDistilledPFOCreator)
algList.append(MyLikelihoodPID)
algList.append(MyRecoMCTruthLinker)
algList.append(MyLCIOOutputProcessor)
algList.append(DSTOutput)
algList.append(MyPfoAnalysis)

from Configurables import ApplicationMgr
ApplicationMgr( TopAlg = algList,
                EvtSel = 'NONE',
                EvtMax   = 10,
                ExtSvc = [evtsvc],
                OutputLevel=INFO
              )
