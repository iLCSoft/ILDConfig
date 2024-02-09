import os
from Gaudi.Configuration import *

from Configurables import LcioEvent, MarlinProcessorWrapper, k4DataSvc
from k4MarlinWrapper.parseConstants import *

from k4FWCore.parseArgs import parser

parser.add_argument(
    "--compactFile",
    help="Compact detector file to use",
    default=f"{os.environ['K4GEO']}/ILD/compact/ILD_l5_v02/ILD_l5_v02.xml",
)
parser.add_argument(
    "--outputFileBase",
    help="Base name of all the produced output files",
    default="StandardReco",
)
reco_args = parser.parse_known_args()[0]

algList = []
svcList = []


evtsvc = k4DataSvc("EventDataSvc")
svcList.append(evtsvc)

from Configurables import GeoSvc

geoSvc = GeoSvc("GeoSvc")
geoSvc.detectors = [
    reco_args.compactFile,
]
geoSvc.OutputLevel = INFO
geoSvc.EnableGeant4Geo = False
svcList.append(geoSvc)


CONSTANTS = {
    "CMSEnergy": "250",
    "RunBeamCalReco": "true",
    "BeamCalCalibrationFactor": "79.6",
    "EcalBarrelMip": "0.0001575",
    "EcalEndcapMip": "0.0001575",
    "EcalRingMip": "0.0001575",
    "HcalBarrelMip": "0.0004925",
    "HcalEndcapMip": "0.0004725",
    "HcalRingMip": "0.0004875",
    "EcalBarrelEnergyFactors": ["0.0063520964756", "0.012902699188"],
    "EcalEndcapEnergyFactors": ["0.0067218419842", "0.013653744940"],
    "EcalRingEnergyFactors": ["0.0066536339", "0.0135151972"],
    "HcalBarrelEnergyFactors": "0.0287783798145",
    "HcalEndcapEnergyFactors": "0.0285819096797",
    "HcalRingEnergyFactors": "0.0349940637704",
    "MuonCalibration": "56.7",
    "PandoraEcalToMip": "153.846",
    "PandoraHcalToMip": "37.1747",
    "PandoraMuonToMip": "10.5263",
    "PandoraEcalToEMScale": "1.0",
    "PandoraHcalToEMScale": "1.0",
    "PandoraEcalToHadBarrelScale": "1.17344504717",
    "PandoraEcalToHadEndcapScale": "1.17344504717",
    "PandoraHcalToHadScale": "1.02821419758",
    "PandoraSoftwareCompensationWeights": [
        "1.59121",
        "-0.0281982",
        "0.000250616",
        "-0.0424222",
        "0.000335128",
        "-2.06112e-05",
        "0.148549",
        "0.199618",
        "-0.0697277",
    ],
    "ApplyPhotonPFOCorrections": "true",
    "EcalTechnology": "SiWEcal",
    "HcalTechnology": "AHcal",
    "PandoraSettingsFile": "PandoraSettings/PandoraSettingsDefault.xml",
    "DropCollectionsECal": [
        "ECalBarrelScHitsEven",
        "ECalBarrelScHitsOdd",
        "ECalEndcapScHitsEven",
        "ECalEndcapScHitsOdd",
    ],
    "DropCollectionsHCal": [
        "HCalBarrelRPCHits",
        "HCalEndcapRPCHits",
        "HCalECRingRPCHits",
    ],
    "AdditionalDropCollectionsREC": [
        "%(DropCollectionsECal)s",
        "%(DropCollectionsHCal)s",
    ],
    "dEdXErrorFactor": "7.55",
    "dEdXSmearingFactor": "0.029",
    "PidPDFFile": "HighLevelReco/PIDFiles/LikelihoodPID_Standard_l5_v01.root",
    "PidWeightFiles": [
        "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_02GeVP_clusterinfo.weights.xml",
        "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_03GeVP_clusterinfo.weights.xml",
        "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_04GeVP_clusterinfo.weights.xml",
        "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_05GeVP_clusterinfo.weights.xml",
        "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_06GeVP_clusterinfo.weights.xml",
        "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_07GeVP_clusterinfo.weights.xml",
        "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_08GeVP_clusterinfo.weights.xml",
        "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_09GeVP_clusterinfo.weights.xml",
        "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_10GeVP_clusterinfo.weights.xml",
        "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_11GeVP_clusterinfo.weights.xml",
        "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_12GeVP_clusterinfo.weights.xml",
        "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_13GeVP_clusterinfo.weights.xml",
        "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_14GeVP_clusterinfo.weights.xml",
        "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_15GeVP_clusterinfo.weights.xml",
        "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_16GeVP_clusterinfo.weights.xml",
        "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_17GeVP_clusterinfo.weights.xml",
        "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_18GeVP_clusterinfo.weights.xml",
        "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_19GeVP_clusterinfo.weights.xml",
        "HighLevelReco/PIDFiles/LowMomMuPiSeparation/TMVAClassification_BDTG_l5_20GeVP_clusterinfo.weights.xml",
    ],
    "ECalBarrelSimHitCollections": ["ECalBarrelSiHitsEven", "ECalBarrelSiHitsOdd"],
    "ECalEndcapSimHitCollections": ["ECalEndcapSiHitsEven", "ECalEndcapSiHitsOdd"],
    "ECalRingSimHitCollections": "EcalEndcapRingCollection",
    "HCalBarrelSimHitCollections": "HcalBarrelRegCollection",
    "HCalEndcapSimHitCollections": "HcalEndcapsCollection",
    "HCalRingSimHitCollections": "HcalEndcapRingCollection",
    "ECalSimHitCollections": [
        "%(ECalBarrelSimHitCollections)s",
        "%(ECalEndcapSimHitCollections)s",
        "%(ECalRingSimHitCollections)s",
    ],
    "HCalSimHitCollections": [
        "%(HCalBarrelSimHitCollections)s",
        "%(HCalEndcapSimHitCollections)s",
        "%(HCalRingSimHitCollections)s",
    ],
    "BeamCalBackgroundFile": "HighLevelReco/BeamCalBackground/BeamCalBackground-E%(CMSEnergy)s-B3.5-RealisticNominalAntiDid.root",
    "ExpectedBgWW": "0.1256495436",
    "ExpectedBgWB": "0.297459204",
    "ExpectedBgBW": "0.29722665",
    "ExpectedBgBB": "0.829787658",
    "LCFIPlusBeamspotConstraint": "true",
    "BeamSizeX": "313.e-6",
    "BeamSizeY": "3.14e-6",
    "BeamSizeZ": "202.e-3",
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
    "FileName": [f"{reco_args.outputFileBase}_AIDA"],
    "FileType": ["root"],
}

MyStatusmonitor = MarlinProcessorWrapper("MyStatusmonitor")
MyStatusmonitor.OutputLevel = INFO
MyStatusmonitor.ProcessorType = "Statusmonitor"
MyStatusmonitor.Parameters = {"HowOften": ["1"]}

BgOverlayWW = MarlinProcessorWrapper("BgOverlayWW")
BgOverlayWW.OutputLevel = INFO
BgOverlayWW.ProcessorType = "Overlay"
BgOverlayWW.Parameters = {
    "InputFileNames": ["undefined.slcio"],
    "NumberOverlayEvents": ["0"],
    "expBG": ["%(ExpectedBgWW)s" % CONSTANTS],
}

BgOverlayWB = MarlinProcessorWrapper("BgOverlayWB")
BgOverlayWB.OutputLevel = INFO
BgOverlayWB.ProcessorType = "Overlay"
BgOverlayWB.Parameters = {
    "InputFileNames": ["undefined.slcio"],
    "NumberOverlayEvents": ["0"],
    "expBG": ["%(ExpectedBgWB)s" % CONSTANTS],
}

BgOverlayBW = MarlinProcessorWrapper("BgOverlayBW")
BgOverlayBW.OutputLevel = INFO
BgOverlayBW.ProcessorType = "Overlay"
BgOverlayBW.Parameters = {
    "InputFileNames": ["undefined.slcio"],
    "NumberOverlayEvents": ["0"],
    "expBG": ["%(ExpectedBgBW)s" % CONSTANTS],
}

BgOverlayBB = MarlinProcessorWrapper("BgOverlayBB")
BgOverlayBB.OutputLevel = INFO
BgOverlayBB.ProcessorType = "Overlay"
BgOverlayBB.Parameters = {
    "InputFileNames": ["undefined.slcio"],
    "NumberOverlayEvents": ["0"],
    "expBG": ["%(ExpectedBgBB)s" % CONSTANTS],
}

PairBgOverlay = MarlinProcessorWrapper("PairBgOverlay")
PairBgOverlay.OutputLevel = INFO
PairBgOverlay.ProcessorType = "Overlay"
PairBgOverlay.Parameters = {
    "ExcludeCollections": ["BeamCalCollection"],
    "InputFileNames": ["undefined.slcio"],
    "NumberOverlayEvents": ["0"],
}

MySplitCollectionByLayer = MarlinProcessorWrapper("MySplitCollectionByLayer")
MySplitCollectionByLayer.OutputLevel = INFO
MySplitCollectionByLayer.ProcessorType = "SplitCollectionByLayer"
MySplitCollectionByLayer.Parameters = {
    "InputCollection": ["FTDCollection"],
    "OutputCollections": [
        "FTD_PIXELCollection",
        "0",
        "1",
        "FTD_STRIPCollection",
        "2",
        "6",
    ],
}

VXDPlanarDigiProcessor_CMOSVXD5 = MarlinProcessorWrapper(
    "VXDPlanarDigiProcessor_CMOSVXD5"
)
VXDPlanarDigiProcessor_CMOSVXD5.OutputLevel = INFO
VXDPlanarDigiProcessor_CMOSVXD5.ProcessorType = "DDPlanarDigiProcessor"
VXDPlanarDigiProcessor_CMOSVXD5.Parameters = {
    "ForceHitsOntoSurface": ["true"],
    "IsStrip": ["false"],
    "ResolutionU": ["0.003", "0.003", "0.003", "0.003", "0.003", "0.003"],
    "ResolutionV": ["0.003", "0.003", "0.003", "0.003", "0.003", "0.003"],
    "SimTrackHitCollectionName": ["VXDCollection"],
    "SimTrkHitRelCollection": ["VXDTrackerHitRelations"],
    "SubDetectorName": ["VXD"],
    "TrackerHitCollectionName": ["VXDTrackerHits"],
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
    "TrackerHitCollectionName": ["SITTrackerHits"],
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
    "TrackerHitCollectionName": ["FTDPixelTrackerHits"],
}

FTDStripPlanarDigiProcessor = MarlinProcessorWrapper("FTDStripPlanarDigiProcessor")
FTDStripPlanarDigiProcessor.OutputLevel = INFO
FTDStripPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
FTDStripPlanarDigiProcessor.Parameters = {
    "ForceHitsOntoSurface": ["true"],
    "IsStrip": ["true"],
    "ResolutionU": ["0.007"],
    "ResolutionV": ["0.0"],
    "SimTrackHitCollectionName": ["FTD_STRIPCollection"],
    "SimTrkHitRelCollection": ["FTDStripTrackerHitRelations"],
    "SubDetectorName": ["FTD"],
    "TrackerHitCollectionName": ["FTDStripTrackerHits"],
}

FTDDDSpacePointBuilder = MarlinProcessorWrapper("FTDDDSpacePointBuilder")
FTDDDSpacePointBuilder.OutputLevel = INFO
FTDDDSpacePointBuilder.ProcessorType = "DDSpacePointBuilder"
FTDDDSpacePointBuilder.Parameters = {
    "SimHitSpacePointRelCollection": ["FTDSpacePointRelations"],
    "SpacePointsCollection": ["FTDSpacePoints"],
    "StripLength": ["2.500000000e+02"],
    "SubDetectorName": ["FTD"],
    "TrackerHitCollection": ["FTDStripTrackerHits"],
    "TrackerHitSimHitRelCollection": ["FTDStripTrackerHitRelations"],
}

SETPlanarDigiProcessor = MarlinProcessorWrapper("SETPlanarDigiProcessor")
SETPlanarDigiProcessor.OutputLevel = INFO
SETPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
SETPlanarDigiProcessor.Parameters = {
    "ForceHitsOntoSurface": ["true"],
    "IsStrip": ["true"],
    "ResolutionU": ["0.007"],
    "ResolutionV": ["0"],
    "SimTrackHitCollectionName": ["SETCollection"],
    "SimTrkHitRelCollection": ["SETTrackerHitRelations"],
    "SubDetectorName": ["SET"],
    "TrackerHitCollectionName": ["SETTrackerHits"],
}

SETDDSpacePointBuilder = MarlinProcessorWrapper("SETDDSpacePointBuilder")
SETDDSpacePointBuilder.OutputLevel = INFO
SETDDSpacePointBuilder.ProcessorType = "DDSpacePointBuilder"
SETDDSpacePointBuilder.Parameters = {
    "SimHitSpacePointRelCollection": ["SETSpacePointRelations"],
    "SpacePointsCollection": ["SETSpacePoints"],
    "StripLength": ["9.200000000e+01"],
    "SubDetectorName": ["SET"],
    "TrackerHitCollection": ["SETTrackerHits"],
    "TrackerHitSimHitRelCollection": ["SETTrackerHitRelations"],
}

MyTPCDigiProcessor = MarlinProcessorWrapper("MyTPCDigiProcessor")
MyTPCDigiProcessor.OutputLevel = INFO
MyTPCDigiProcessor.ProcessorType = "DDTPCDigiProcessor"
MyTPCDigiProcessor.Parameters = {
    "DiffusionCoeffRPhi": ["0.025"],
    "DiffusionCoeffZ": ["0.08"],
    "DoubleHitResolutionRPhi": ["2"],
    "DoubleHitResolutionZ": ["5"],
    "HitSortingBinningRPhi": ["2"],
    "HitSortingBinningZ": ["5"],
    "MaxClusterSizeForMerge": ["3"],
    "N_eff": ["22"],
    "PointResolutionPadPhi": ["0.9"],
    "PointResolutionRPhi": ["0.05"],
    "PointResolutionZ": ["0.4"],
    "RejectCellID0": ["1"],
    "SimTrkHitRelCollection": ["TPCTrackerHitRelations"],
    "TPCEndPlateModuleGapPhi": ["1."],
    "TPCEndPlateModuleGapR": ["1."],
    "TPCEndPlateModuleNumbers": ["14", "18", "23", "28", "32", "37", "42", "46"],
    "TPCEndPlateModulePhi0s": [
        "0",
        "0.17453292519943298",
        "0.030350516853376176",
        "0.2108457469509264",
        "0.11998920441304516",
        "0.1600004647682326",
        "0.02051011203843622",
        "0.062176216344090166",
    ],
    "TPCLowPtCollectionName": ["TPCLowPtCollection"],
    "TPCPadRowHitCollectionName": ["TPCCollection"],
    "TPCSpacePointCollectionName": ["TPCSpacePointCollection"],
    "TPCTrackerHitsCol": ["TPCTrackerHits"],
}

MyClupatraProcessor = MarlinProcessorWrapper("MyClupatraProcessor")
MyClupatraProcessor.OutputLevel = INFO
MyClupatraProcessor.ProcessorType = "ClupatraProcessor"
MyClupatraProcessor.Parameters = {
    "Chi2Cut": ["100"],
    "CreateDebugCollections": ["false", "true"],
    "DistanceCut": ["40"],
    "DuplicatePadRowFraction": ["0.1"],
    "EnergyLossOn": ["true"],
    "MaxDeltaChi2": ["35"],
    "MaxStepWithoutHit": ["6"],
    "MinLayerFractionWithMultiplicity": ["0.5"],
    "MinLayerNumberWithMultiplicity": ["3"],
    "MinimumClusterSize": ["6"],
    "MultipleScatteringOn": ["false", "true"],
    "NumberOfZBins": ["150"],
    "OutputCollection": ["ClupatraTracks"],
    "PadRowRange": ["15"],
    "SITHitCollection": ["SITTrackerHits"],
    "SegmentCollectionName": ["ClupatraTrackSegments"],
    "SmoothOn": ["false"],
    "TPCHitCollection": ["TPCTrackerHits"],
    "TrackEndsOuterCentralDist": ["25"],
    "TrackEndsOuterForwardDist": ["40"],
    "TrackIsCurlerOmega": ["0.001"],
    "TrackStartsInnerDist": ["25"],
    "TrackSystemName": ["DDKalTest"],
    "VXDHitCollection": ["VXDTrackerHits"],
    "pickUpSiHits": ["false"],
}

MySiliconTracking_MarlinTrk = MarlinProcessorWrapper("MySiliconTracking_MarlinTrk")
MySiliconTracking_MarlinTrk.OutputLevel = INFO
MySiliconTracking_MarlinTrk.ProcessorType = "SiliconTracking_MarlinTrk"
MySiliconTracking_MarlinTrk.Parameters = {
    "AngleCutForMerging": ["0.1"],
    "AplySimpleUpdatedCoreBin": ["true"],
    "CheckForDelta": ["1"],
    "Chi2FitCut": ["120"],
    "Chi2PrefitCut": ["1e+10"],
    "Chi2WRphiQuartet": ["1"],
    "Chi2WRphiSeptet": ["1"],
    "Chi2WRphiTriplet": ["1"],
    "Chi2WZQuartet": ["0.5"],
    "Chi2WZSeptet": ["0.5"],
    "Chi2WZTriplet": ["0.5"],
    "CutOnD0": ["100"],
    "CutOnPt": ["0.05"],
    "CutOnZ0": ["100"],
    "EnergyLossOn": ["true"],
    "FTDPixelHitCollectionName": ["FTDPixelTrackerHits"],
    "FTDSpacePointCollection": ["FTDSpacePoints"],
    "FastAttachment": ["0"],
    "InitialTrackErrorD0": ["1e+06"],
    "InitialTrackErrorOmega": ["0.0001"],
    "InitialTrackErrorPhi0": ["100"],
    "InitialTrackErrorTanL": ["100"],
    "InitialTrackErrorZ0": ["1e+06"],
    "LayerCombinations": [
        "8",
        "6",
        "5",
        "8",
        "6",
        "4",
        "8",
        "6",
        "3",
        "8",
        "6",
        "2",
        "8",
        "5",
        "3",
        "8",
        "5",
        "2",
        "8",
        "4",
        "3",
        "8",
        "4",
        "2",
        "6",
        "5",
        "3",
        "6",
        "5",
        "2",
        "6",
        "4",
        "3",
        "6",
        "4",
        "2",
        "6",
        "3",
        "1",
        "6",
        "3",
        "0",
        "6",
        "2",
        "1",
        "6",
        "2",
        "0",
        "5",
        "3",
        "1",
        "5",
        "3",
        "0",
        "5",
        "2",
        "1",
        "5",
        "2",
        "0",
        "4",
        "3",
        "1",
        "4",
        "3",
        "0",
        "4",
        "2",
        "1",
        "4",
        "2",
        "0",
        "3",
        "2",
        "1",
        "3",
        "2",
        "0",
        "2",
        "1",
        "0",
    ],
    "LayerCombinationsFTD": [
        "13",
        "11",
        "9",
        "13",
        "11",
        "8",
        "13",
        "10",
        "9",
        "13",
        "10",
        "8",
        "12",
        "11",
        "9",
        "12",
        "11",
        "8",
        "12",
        "10",
        "9",
        "12",
        "10",
        "8",
        "11",
        "9",
        "7",
        "11",
        "9",
        "6",
        "11",
        "8",
        "7",
        "11",
        "8",
        "6",
        "10",
        "9",
        "7",
        "10",
        "9",
        "6",
        "10",
        "8",
        "7",
        "10",
        "8",
        "6",
        "9",
        "7",
        "5",
        "9",
        "7",
        "4",
        "9",
        "6",
        "5",
        "9",
        "6",
        "4",
        "8",
        "7",
        "5",
        "8",
        "7",
        "4",
        "8",
        "6",
        "5",
        "8",
        "6",
        "4",
        "7",
        "5",
        "3",
        "7",
        "5",
        "2",
        "7",
        "4",
        "3",
        "7",
        "4",
        "2",
        "6",
        "5",
        "3",
        "6",
        "5",
        "2",
        "6",
        "4",
        "3",
        "6",
        "4",
        "2",
        "5",
        "3",
        "1",
        "5",
        "3",
        "0",
        "5",
        "2",
        "1",
        "5",
        "2",
        "0",
        "4",
        "3",
        "1",
        "4",
        "3",
        "0",
        "4",
        "2",
        "1",
        "4",
        "2",
        "0",
    ],
    "MaxChi2PerHit": ["100"],
    "MaxHitsPerSector": ["100"],
    "MinDistCutAttach": ["2.5"],
    "MinDistToDelta": ["0.25"],
    "MinLayerToAttach": ["-1"],
    "MinimalHits": ["3"],
    "MultipleScatteringOn": ["true"],
    "NDivisionsInPhi": ["80"],
    "NDivisionsInPhiFTD": ["30"],
    "NDivisionsInTheta": ["80"],
    "NHitsChi2": ["5"],
    "RunMarlinTrkDiagnostics": ["false"],
    "SITHitCollectionName": ["SITTrackerHits"],
    "SiTrackCollectionName": ["SiTracks"],
    "SmoothOn": ["false"],
    "TrackSystemName": ["DDKalTest"],
    "UseEventDisplay": ["false"],
    "UseSIT": ["1"],
    "UseSimpleAttachHitToTrack": ["true"],
    "VTXHitCollectionName": ["VXDTrackerHits"],
}

MyForwardTracking = MarlinProcessorWrapper("MyForwardTracking")
MyForwardTracking.OutputLevel = INFO
MyForwardTracking.ProcessorType = "ForwardTracking"
MyForwardTracking.Parameters = {
    "BestSubsetFinder": ["SubsetSimple"],
    "Chi2ProbCut": ["0.0"],
    "Crit2_DeltaPhi_max": ["30", "0.8"],
    "Crit2_DeltaPhi_min": ["0", "0"],
    "Crit2_DeltaRho_max": ["150"],
    "Crit2_DeltaRho_min": ["20"],
    "Crit2_RZRatio_max": ["1.08"],
    "Crit2_RZRatio_min": ["1.002"],
    "Crit2_StraightTrackRatio_max": ["1.02", "1.01"],
    "Crit2_StraightTrackRatio_min": ["0.9", "0.99"],
    "Crit3_3DAngle_max": ["10", "0.35"],
    "Crit3_3DAngle_min": ["0", "0"],
    "Crit3_ChangeRZRatio_max": ["1.015", "1.001"],
    "Crit3_ChangeRZRatio_min": ["0.995", "0.999"],
    "Crit3_IPCircleDist_max": ["20", "1.5"],
    "Crit3_IPCircleDist_min": ["0", "0"],
    "Crit3_PT_max": ["99999999"],
    "Crit3_PT_min": ["0.1"],
    "Crit4_3DAngleChange_max": ["1.3", "1.01"],
    "Crit4_3DAngleChange_min": ["0.8", "0.99"],
    "Crit4_DistToExtrapolation_max": ["1.0", "0.05"],
    "Crit4_DistToExtrapolation_min": ["0", "0"],
    "Criteria": [
        "Crit2_DeltaPhi",
        "Crit2_DeltaRho",
        "Crit2_RZRatio",
        "Crit2_StraightTrackRatio",
        "Crit3_3DAngle",
        "Crit3_ChangeRZRatio",
        "Crit3_IPCircleDist",
        "Crit3_PT",
        "Crit4_DistToExtrapolation",
        "Crit4_3DAngleChange",
    ],
    "EnergyLossOn": ["true"],
    "FTDHitCollections": ["FTDPixelTrackerHits", "FTDSpacePoints"],
    "ForwardTrackCollection": ["ForwardTracks"],
    "HelixFitMax": ["500"],
    "HitsPerTrackMin": ["3"],
    "MaxConnectionsAutomaton": ["100000"],
    "MaxHitsPerSector": ["1000"],
    "MultipleScatteringOn": ["true"],
    "OverlappingHitsDistMax": ["3.5"],
    "SmoothOn": ["false"],
    "TakeBestVersionOfTrack": ["true"],
    "TrackSystemName": ["DDKalTest"],
}

MyTrackSubsetProcessor = MarlinProcessorWrapper("MyTrackSubsetProcessor")
MyTrackSubsetProcessor.OutputLevel = INFO
MyTrackSubsetProcessor.ProcessorType = "TrackSubsetProcessor"
MyTrackSubsetProcessor.Parameters = {
    "EnergyLossOn": ["true"],
    "MultipleScatteringOn": ["true"],
    "Omega": ["0.75"],
    "RemoveShortTracks": ["true"],
    "SmoothOn": ["false"],
    "TrackInputCollections": ["ForwardTracks", "SiTracks"],
    "TrackOutputCollection": ["SubsetTracks"],
    "TrackSystemName": ["DDKalTest"],
}

MyFullLDCTracking_MarlinTrk = MarlinProcessorWrapper("MyFullLDCTracking_MarlinTrk")
MyFullLDCTracking_MarlinTrk.OutputLevel = INFO
MyFullLDCTracking_MarlinTrk.ProcessorType = "FullLDCTracking_MarlinTrk"
MyFullLDCTracking_MarlinTrk.Parameters = {
    "AngleCutForForcedMerging": ["0.05"],
    "AngleCutForMerging": ["0.1"],
    "AssignETDHits": ["0"],
    "AssignFTDHits": ["1"],
    "AssignSETHits": ["1"],
    "AssignSITHits": ["1"],
    "AssignTPCHits": ["0"],
    "AssignVTXHits": ["1"],
    "Chi2FitCut": ["100"],
    "CutOnSiHits": ["4"],
    "CutOnTPCHits": ["10"],
    "CutOnTrackD0": ["500"],
    "CutOnTrackZ0": ["500"],
    "D0CutForForcedMerging": ["50"],
    "D0CutForMerging": ["500"],
    "D0CutToMergeTPCSegments": ["100"],
    "Debug": ["0"],
    "DeltaPCutToMergeTPCSegments": ["0.1"],
    "EnergyLossOn": ["true"],
    "FTDHitToTrackDistance": ["2"],
    "FTDPixelHitCollectionName": ["FTDPixelTrackerHits"],
    "FTDSpacePointCollection": ["FTDSpacePoints"],
    "ForbidOverlapInZComb": ["0"],
    "ForbidOverlapInZTPC": ["0"],
    "ForceSiTPCMerging": ["1"],
    "ForceTPCSegmentsMerging": ["0"],
    "InitialTrackErrorD0": ["1e+06"],
    "InitialTrackErrorOmega": ["0.00001"],
    "InitialTrackErrorPhi0": ["100"],
    "InitialTrackErrorTanL": ["100"],
    "InitialTrackErrorZ0": ["1e+06"],
    "LDCTrackCollection": ["MarlinTrkTracks"],
    "MaxChi2PerHit": ["200"],
    "MinChi2ProbForSiliconTracks": ["0.00001"],
    "MultipleScatteringOn": ["true"],
    "NHitsExtrapolation": ["35"],
    "OmegaCutForForcedMerging": ["0.15"],
    "OmegaCutForMerging": ["0.25"],
    "PtCutToMergeTPCSegments": ["1.2"],
    "RunMarlinTrkDiagnostics": ["false"],
    "SETHitCollection": ["SETSpacePoints"],
    "SETHitToTrackDistance": ["50"],
    "SITHitCollection": ["SITTrackerHits"],
    "SITHitToTrackDistance": ["2"],
    "SiTracks": ["SubsetTracks"],
    "SiTracksMCPRelColl": ["SubsetTracksMCTruthLink"],
    "SmoothOn": ["true"],
    "TPCHitCollection": ["TPCTrackerHits"],
    "TPCHitToTrackDistance": ["15"],
    "TPCTracks": ["ClupatraTracks"],
    "TPCTracksMCPRelColl": ["TPCTracksMCTruthLink"],
    "TrackSystemName": ["DDKalTest"],
    "VTXHitCollection": ["VXDTrackerHits"],
    "VTXHitToTrackDistance": ["1.5"],
    "Z0CutForForcedMerging": ["200"],
    "Z0CutForMerging": ["1000"],
    "Z0CutToMergeTPCSegments": ["5000"],
    "cosThetaCutHighPtMerge": ["0.99"],
    "cosThetaCutSoftHighPtMerge": ["0.998"],
    "hitDistanceCutHighPtMerge": ["25"],
    "maxFractionOfOutliersCutHighPtMerge": ["0.95"],
    "maxHitDistanceCutHighPtMerge": ["50"],
    "momDiffCutHighPtMerge": ["0.01"],
    "momDiffCutSoftHighPtMerge": ["0.25"],
}

MyCompute_dEdxProcessor = MarlinProcessorWrapper("MyCompute_dEdxProcessor")
MyCompute_dEdxProcessor.OutputLevel = INFO
MyCompute_dEdxProcessor.ProcessorType = "Compute_dEdxProcessor"
MyCompute_dEdxProcessor.Parameters = {
    "AngularCorrectionParameters": ["0.635762", "-0.0573237"],
    "EnergyLossErrorTPC": ["0.054"],
    "LDCTrackCollection": ["MarlinTrkTracks"],
    "LowerTruncationFraction": ["0.08"],
    "NumberofHitsCorrectionParameters": ["1.468"],
    "StrategyCompHist": ["false"],
    "StrategyCompHistFiles": ["dEdx_Histo_Strategy"],
    "StrategyCompHistWeight": ["false"],
    "UpperTruncationFraction": ["0.3"],
    "Write_dEdx": ["true"],
    "dEdxErrorScalingExponents": ["-0.34", "-0.45"],
    "dxStrategy": ["1"],
    "isSmearing": ["true"],
    "smearingFactor": ["%(dEdXSmearingFactor)s" % CONSTANTS],
}

MyV0Finder = MarlinProcessorWrapper("MyV0Finder")
MyV0Finder.OutputLevel = INFO
MyV0Finder.ProcessorType = "V0Finder"
MyV0Finder.Parameters = {
    "MassRangeGamma": ["0.01"],
    "MassRangeK0S": ["0.02"],
    "MassRangeL0": ["0.02"],
    "TrackCollection": ["MarlinTrkTracks"],
}

MyKinkFinder = MarlinProcessorWrapper("MyKinkFinder")
MyKinkFinder.OutputLevel = INFO
MyKinkFinder.ProcessorType = "KinkFinder"
MyKinkFinder.Parameters = {
    "DebugPrinting": ["0"],
    "TrackCollection": ["MarlinTrkTracks"],
}

MyRefitProcessorKaon = MarlinProcessorWrapper("MyRefitProcessorKaon")
MyRefitProcessorKaon.OutputLevel = INFO
MyRefitProcessorKaon.ProcessorType = "RefitProcessor"
MyRefitProcessorKaon.Parameters = {
    "EnergyLossOn": ["true"],
    "FitDirection": ["-1"],
    "InitialTrackErrorD0": ["1e+06"],
    "InitialTrackErrorOmega": ["0.00001"],
    "InitialTrackErrorPhi0": ["100"],
    "InitialTrackErrorTanL": ["100"],
    "InitialTrackErrorZ0": ["1e+06"],
    "InitialTrackState": ["3"],
    "InputTrackCollectionName": ["MarlinTrkTracks"],
    "InputTrackRelCollection": [],
    "OutputTrackCollectionName": ["MarlinTrkTracksKaon"],
    "OutputTrackRelCollection": ["MarlinTrkTracksKaonMCP"],
    "ParticleMass": ["0.493677"],
    "TrackSystemName": ["DDKalTest"],
}

MyRefitProcessorProton = MarlinProcessorWrapper("MyRefitProcessorProton")
MyRefitProcessorProton.OutputLevel = INFO
MyRefitProcessorProton.ProcessorType = "RefitProcessor"
MyRefitProcessorProton.Parameters = {
    "EnergyLossOn": ["true"],
    "FitDirection": ["-1"],
    "InitialTrackErrorD0": ["1e+06"],
    "InitialTrackErrorOmega": ["0.00001"],
    "InitialTrackErrorPhi0": ["100"],
    "InitialTrackErrorTanL": ["100"],
    "InitialTrackErrorZ0": ["1e+06"],
    "InitialTrackState": ["3"],
    "InputTrackCollectionName": ["MarlinTrkTracks"],
    "InputTrackRelCollection": [],
    "OutputTrackCollectionName": ["MarlinTrkTracksProton"],
    "OutputTrackRelCollection": ["MarlinTrkTracksProtonMCP"],
    "ParticleMass": ["0.93828"],
    "TrackSystemName": ["DDKalTest"],
}

MergeCollectionsEcalBarrelHits = MarlinProcessorWrapper(
    "MergeCollectionsEcalBarrelHits"
)
MergeCollectionsEcalBarrelHits.OutputLevel = INFO
MergeCollectionsEcalBarrelHits.ProcessorType = "MergeCollections"
MergeCollectionsEcalBarrelHits.Parameters = {
    "InputCollections": ["ECalBarrelSiHitsEven", "ECalBarrelSiHitsOdd"],
    "OutputCollection": ["EcalBarrelCollection"],
}

MergeCollectionsEcalEndcapHits = MarlinProcessorWrapper(
    "MergeCollectionsEcalEndcapHits"
)
MergeCollectionsEcalEndcapHits.OutputLevel = INFO
MergeCollectionsEcalEndcapHits.ProcessorType = "MergeCollections"
MergeCollectionsEcalEndcapHits.Parameters = {
    "InputCollections": ["ECalEndcapSiHitsEven", "ECalEndcapSiHitsOdd"],
    "OutputCollection": ["EcalEndcapsCollection"],
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
    "timingCut": ["1"],
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
    "outputRelationCollections": ["EcalBarrelRelationsSimRec"],
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
    "outputHitCollection": ["EcalBarrelCollectionGapHits"],
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
    "timingCut": ["1"],
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
    "outputRelationCollections": ["EcalEndcapsRelationsSimRec"],
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
    "outputHitCollection": ["EcalEndcapsCollectionGapHits"],
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
    "timingCut": ["1"],
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
    "outputRelationCollections": ["EcalEndcapRingRelationsSimRec"],
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
    "timingCut": ["1"],
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
    "ppd_npix": ["2000"],
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
    "timingCut": ["1"],
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
    "ppd_npix": ["2000"],
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
    "timingCut": ["1"],
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
    "ppd_npix": ["2000"],
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
    "RelationOutputCollection": ["RelationBCalHit"],
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
    "RelationOutputCollection": ["RelationLcalHit"],
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
    "RelationOutputCollection": ["RelationLHcalHit"],
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
    "RelationOutputCollection": ["RelationMuonHit"],
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
    "ECalCaloHitCollections": [
        "EcalBarrelCollectionRec",
        "EcalBarrelCollectionGapHits",
        "EcalEndcapsCollectionRec",
        "EcalEndcapsCollectionGapHits",
        "EcalEndcapRingCollectionRec",
    ],
    "ECalEndcapDetectorName": ["EcalEndcap"],
    "ECalMipThreshold": ["0.5"],
    "ECalOtherDetectorNames": ["EcalPlug", "Lcal", "BeamCal"],
    "ECalToEMGeVCalibration": ["%(PandoraEcalToEMScale)s" % CONSTANTS],
    "ECalToHadGeVCalibrationBarrel": ["%(PandoraEcalToHadBarrelScale)s" % CONSTANTS],
    "ECalToHadGeVCalibrationEndCap": ["%(PandoraEcalToHadEndcapScale)s" % CONSTANTS],
    "ECalToMipCalibration": ["%(PandoraEcalToMip)s" % CONSTANTS],
    "FinalEnergyDensityBin": ["30"],
    "HCalBarrelDetectorName": ["HcalBarrel"],
    "HCalCaloHitCollections": [
        "HcalBarrelCollectionRec",
        "HcalEndcapsCollectionRec",
        "HcalEndcapRingCollectionRec",
    ],
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
    "RelCaloHitCollections": [
        "EcalBarrelRelationsSimRec",
        "EcalEndcapsRelationsSimRec",
        "EcalEndcapRingRelationsSimRec",
        "HcalBarrelRelationsSimRec",
        "HcalEndcapsRelationsSimRec",
        "HcalEndcapRingRelationsSimRec",
        "RelationMuonHit",
        "RelationLHcalHit",
        "RelationLcalHit",
    ],
    "RelTrackCollections": ["MarlinTrkTracksMCTruthLink"],
    "SoftwareCompensationEnergyDensityBins": [
        "0",
        "2",
        "5",
        "7.5",
        "9.5",
        "13",
        "16",
        "20",
        "23.5",
        "28",
    ],
    "SoftwareCompensationWeights": [
        "%(PandoraSoftwareCompensationWeights)s" % CONSTANTS
    ],
    "SplitVertexCollections": ["SplitVertices"],
    "StartVertexAlgorithmName": ["PandoraPFANew"],
    "StartVertexCollectionName": ["PandoraPFANewStartVertices"],
    "TrackCollections": ["MarlinTrkTracks"],
    "TrackCreatorName": ["DDTrackCreatorILD"],
    "TrackerBarrelDetectorNames": ["TPC"],
    "TrackerEndcapDetectorNames": ["FTD"],
    "UseDD4hepField": ["false"],
    "UseOldTrackStateCalculation": ["0", "1"],
    "V0VertexCollections": ["V0Vertices"],
    "VertexBarrelDetectorName": ["VXD"],
    "YokeBarrelNormalVector": ["0", "1", "0"],
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
    "UseConstPadCuts": ["false"],
}

MyAdd4MomCovMatrixCharged = MarlinProcessorWrapper("MyAdd4MomCovMatrixCharged")
MyAdd4MomCovMatrixCharged.OutputLevel = INFO
MyAdd4MomCovMatrixCharged.ProcessorType = "Add4MomCovMatrixCharged"
MyAdd4MomCovMatrixCharged.Parameters = {"InputPandoraPFOsCollection": ["PandoraPFOs"]}

MyAddClusterProperties = MarlinProcessorWrapper("MyAddClusterProperties")
MyAddClusterProperties.OutputLevel = INFO
MyAddClusterProperties.ProcessorType = "AddClusterProperties"
MyAddClusterProperties.Parameters = {
    "ClusterCollection": ["PandoraClusters"],
    "PFOCollectionName": ["PandoraPFOs"],
}

MyComputeShowerShapesProcessor = MarlinProcessorWrapper(
    "MyComputeShowerShapesProcessor"
)
MyComputeShowerShapesProcessor.OutputLevel = INFO
MyComputeShowerShapesProcessor.ProcessorType = "ComputeShowerShapesProcessor"
MyComputeShowerShapesProcessor.Parameters = {
    "ClusterCollectionName": ["PandoraClusters"],
    "Debug": ["0"],
    "MoliereRadius_Ecal": ["9.00"],
    "MoliereRadius_Hcal": ["17.19"],
    "PFOCollection": ["PandoraPFOs"],
    "RadiationLength_Ecal": ["3.50"],
    "RadiationLength_Hcal": ["17.57"],
}

MyphotonCorrectionProcessor = MarlinProcessorWrapper("MyphotonCorrectionProcessor")
MyphotonCorrectionProcessor.OutputLevel = INFO
MyphotonCorrectionProcessor.ProcessorType = "photonCorrectionProcessor"
MyphotonCorrectionProcessor.Parameters = {
    "energyCor_Linearise": ["0.987", "0.01426"],
    "energyCorr_barrelPhi": [
        "0.412249",
        "0.0142289",
        "-0.0933687",
        "0.01345",
        "0.0408156",
    ],
    "energyCorr_costh": [
        "-0.09",
        "0.",
        "0.235",
        "0.007256",
        "-0.0369648",
        "0.",
        "0.588",
        "0.0121604",
        "-0.0422968",
        "0.774",
        "0.009",
        "1.002",
    ],
    "energyCorr_endcap": ["-0.025", "855.", "23.", "-0.07", "1489.", "18."],
    "inputCollection": ["PandoraPFOs"],
    "modifyPFOdirection": ["%(ApplyPhotonPFOCorrections)s" % CONSTANTS],
    "modifyPFOenergies": ["%(ApplyPhotonPFOCorrections)s" % CONSTANTS],
    "nominalEnergy": ["200"],
    "phiCorr_barrel": [
        "2.36517e-05",
        "1.32090e-04",
        "-3.86883e+00",
        "-1.67809e-01",
        "2.28614e-05",
        "6.03495e-05",
        "0.419",
        "0.00728",
        "0.025",
        "0.00",
        "2.86667e-05",
        "2.49371e-05",
        "-7.71684e-06",
        "-1.48118e-05",
        "-5.63786e-06",
        "-9.38376e-06",
        "-4.96296e-06",
        "2.91262e-06",
    ],
    "thetaCorr_barrel": ["-0.000166568", "-7.119e-05", "0.000223618", "-3.95915e-05"],
    "thetaCorr_endcap": [
        "0.000129478",
        "-3.73863e-05",
        "-0.000847783",
        "0.000153646",
        "0.000806605",
        "-0.000132608",
    ],
    "validationPlots": ["false"],
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
    "Printing": ["0"],
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
    "Printing": ["0"],
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
    "Printing": ["0"],
}

MyGammaGammaSolutionFinder = MarlinProcessorWrapper("MyGammaGammaSolutionFinder")
MyGammaGammaSolutionFinder.OutputLevel = INFO
MyGammaGammaSolutionFinder.ProcessorType = "GammaGammaSolutionFinder"
MyGammaGammaSolutionFinder.Parameters = {
    "InputParticleCollectionName1": ["GammaGammaCandidatePi0s"],
    "InputParticleCollectionName2": ["GammaGammaCandidateEtas"],
    "InputParticleCollectionName3": ["GammaGammaCandidateEtaPrimes"],
    "OutputParticleCollectionName": ["GammaGammaParticles"],
    "Printing": ["0"],
}

MyDistilledPFOCreator = MarlinProcessorWrapper("MyDistilledPFOCreator")
MyDistilledPFOCreator.OutputLevel = INFO
MyDistilledPFOCreator.ProcessorType = "DistilledPFOCreator"
MyDistilledPFOCreator.Parameters = {
    "InputParticleCollectionName1": ["PandoraPFOs"],
    "InputParticleCollectionName2": ["GammaGammaParticles"],
    "OutputParticleCollectionName": ["DistilledPFOs"],
    "Printing": ["0"],
}

MyLikelihoodPID = MarlinProcessorWrapper("MyLikelihoodPID")
MyLikelihoodPID.OutputLevel = INFO
MyLikelihoodPID.ProcessorType = "LikelihoodPIDProcessor"
MyLikelihoodPID.Parameters = {
    "CostMatrix": [
        "1.0e-50",
        "1.0",
        "1.5",
        "1.0",
        "1.5",
        "1.0",
        "1.0e-50",
        "3.0",
        "1.0",
        "1.0",
        "1.0",
        "1.0",
        "1.0e-50",
        "1.0",
        "3.0",
        "1.0",
        "1.0",
        "4.0",
        "1.0e-50",
        "2.0",
        "1.0",
        "1.0",
        "5.0",
        "1.0",
        "1.0e-50",
    ],
    "Debug": ["0"],
    "EnergyBoundaries": ["0", "1.0e+07"],
    "FilePDFName": ["%(PidPDFFile)s" % CONSTANTS],
    "FileWeightFormupiSeparationName": ["%(PidWeightFiles)s" % CONSTANTS],
    "RecoParticleCollection": ["PandoraPFOs"],
    "UseBayesian": ["2"],
    "UseLowMomentumMuPiSeparation": ["true"],
    "dEdxErrorFactor": ["%(dEdXErrorFactor)s" % CONSTANTS],
    "dEdxNormalization": ["1.350e-7"],
    "dEdxParameter_electron": [
        "-1.28883368e-02",
        "2.72959919e+01",
        "1.10560871e+01",
        "-1.74534200e+00",
        "-9.84887586e-07",
    ],
    "dEdxParameter_kaon": [
        "7.52235689e-02",
        "1.59710415e+04",
        "1.79625604e+06",
        "3.15315795e-01",
        "2.30414997e-04",
    ],
    "dEdxParameter_muon": [
        "6.49143971e-02",
        "1.55775592e+03",
        "9.31848047e+08",
        "2.32201725e-01",
        "2.50492066e-04",
    ],
    "dEdxParameter_pion": [
        "6.54955215e-02",
        "8.26239081e+06",
        "1.92933904e+05",
        "2.52743206e-01",
        "2.26657525e-04",
    ],
    "dEdxParameter_proton": [
        "7.92251260e-02",
        "6.38129720e+04",
        "3.82995071e+04",
        "2.80793601e-01",
        "7.14371743e-04",
    ],
}

MyRecoMCTruthLinker = MarlinProcessorWrapper("MyRecoMCTruthLinker")
MyRecoMCTruthLinker.OutputLevel = INFO
MyRecoMCTruthLinker.ProcessorType = "RecoMCTruthLinker"
MyRecoMCTruthLinker.Parameters = {
    "ClusterCollection": ["PandoraClusters"],
    "ClusterMCTruthLinkName": ["ClusterMCTruthLink"],
    "FullRecoRelation": ["true"],
    "KeepDaughtersPDG": ["22", "111", "310", "13", "211", "321"],
    "MCParticleCollection": ["MCParticle"],
    "MCParticlesSkimmedName": ["MCParticlesSkimmed"],
    "MCTruthClusterLinkName": ["MCTruthClusterLink"],
    "MCTruthRecoLinkName": ["MCTruthRecoLink"],
    "MCTruthTrackLinkName": ["MCTruthMarlinTrkTracksLink"],
    "RecoMCTruthLinkName": ["RecoMCTruthLink"],
    "RecoParticleCollection": ["PandoraPFOs"],
    "SimCaloHitCollections": [
        "BeamCalCollection",
        "LHCalCollection",
        "LumiCalCollection",
        "%(ECalSimHitCollections)s" % CONSTANTS,
        "%(HCalSimHitCollections)s" % CONSTANTS,
        "YokeBarrelCollection",
        "YokeEndcapsCollection",
    ],
    "SimCalorimeterHitRelationNames": [
        "EcalBarrelRelationsSimRec",
        "EcalEndcapRingRelationsSimRec",
        "EcalEndcapsRelationsSimRec",
        "HcalBarrelRelationsSimRec",
        "HcalEndcapRingRelationsSimRec",
        "HcalEndcapsRelationsSimRec",
        "RelationLHcalHit",
        "RelationMuonHit",
        "RelationLcalHit",
        "RelationBCalHit",
    ],
    "SimTrackerHitCollections": [
        "VXDCollection",
        "SITCollection",
        "FTD_PIXELCollection",
        "FTD_STRIPCollection",
        "TPCCollection",
        "SETCollection",
    ],
    "TrackCollection": ["MarlinTrkTracks"],
    "TrackMCTruthLinkName": ["MarlinTrkTracksMCTruthLink"],
    "TrackerHitsRelInputCollections": [
        "VXDTrackerHitRelations",
        "SITTrackerHitRelations",
        "FTDPixelTrackerHitRelations",
        "FTDSpacePointRelations",
        "TPCTrackerHitRelations",
        "SETSpacePointRelations",
    ],
    "UseTrackerHitRelations": ["true"],
    "UsingParticleGun": ["false"],
}

VertexFinder = MarlinProcessorWrapper("VertexFinder")
VertexFinder.OutputLevel = INFO
VertexFinder.ProcessorType = "LcfiplusProcessor"
VertexFinder.Parameters = {
    "Algorithms": ["PrimaryVertexFinder", "BuildUpVertex"],
    "BeamSizeX": ["%(BeamSizeX)s" % CONSTANTS],
    "BeamSizeY": ["%(BeamSizeY)s" % CONSTANTS],
    "BeamSizeZ": ["%(BeamSizeZ)s" % CONSTANTS],
    "BuildUpVertex.AssocIPTracks": ["1"],
    "BuildUpVertex.AssocIPTracksChi2RatioSecToPri": ["2.0"],
    "BuildUpVertex.AssocIPTracksMinDist": ["0."],
    "BuildUpVertex.MassThreshold": ["10."],
    "BuildUpVertex.MaxChi2ForDistOrder": ["1.0"],
    "BuildUpVertex.MinDistFromIP": ["0.3"],
    "BuildUpVertex.PrimaryChi2Threshold": ["25."],
    "BuildUpVertex.SecondaryChi2Threshold": ["9."],
    "BuildUpVertex.TrackMaxD0": ["10."],
    "BuildUpVertex.TrackMaxD0Err": ["0.1"],
    "BuildUpVertex.TrackMaxZ0": ["20."],
    "BuildUpVertex.TrackMaxZ0Err": ["0.1"],
    "BuildUpVertex.TrackMinFtdHits": ["10000"],
    "BuildUpVertex.TrackMinPt": ["0.1"],
    "BuildUpVertex.TrackMinTpcHits": ["10000"],
    "BuildUpVertex.TrackMinVxdFtdHits": ["0"],
    "BuildUpVertex.TrackMinVxdHits": ["10000"],
    "BuildUpVertex.UseAVF": ["0"],
    "BuildUpVertex.UseV0Selection": ["1"],
    "BuildUpVertex.V0VertexCollectionName": ["BuildUpVertex_V0"],
    "BuildUpVertexCollectionName": ["BuildUpVertex"],
    "PFOCollection": ["PandoraPFOs"],
    "PrimaryVertexCollectionName": ["PrimaryVertex"],
    "PrimaryVertexFinder.BeamspotConstraint": [
        "%(LCFIPlusBeamspotConstraint)s" % CONSTANTS
    ],
    "PrimaryVertexFinder.BeamspotSmearing": ["0"],
    "PrimaryVertexFinder.Chi2Threshold": ["25."],
    "PrimaryVertexFinder.TrackMaxD0": ["20."],
    "PrimaryVertexFinder.TrackMaxZ0": ["20."],
    "PrimaryVertexFinder.TrackMinVtxFtdHits": ["1"],
    "PrintEventNumber": ["0"],
    "ReadSubdetectorEnergies": ["1"],
    "TrackHitOrdering": ["1"],
    "UpdateVertexRPDaughters": ["1"],
}

TrackLengthProcessor = MarlinProcessorWrapper("TrackLengthProcessor")
TrackLengthProcessor.OutputLevel = INFO
TrackLengthProcessor.ProcessorType = "TrackLengthProcessor"
TrackLengthProcessor.Parameters = {"ReconstructedParticleCollection": ["PandoraPFOs"]}

TOFEstimators0ps = MarlinProcessorWrapper("TOFEstimators0ps")
TOFEstimators0ps.OutputLevel = INFO
TOFEstimators0ps.ProcessorType = "TOFEstimators"
TOFEstimators0ps.Parameters = {
    "ExtrapolateToEcal": ["true"],
    "MaxEcalLayer": ["10"],
    "ReconstructedParticleCollection": ["PandoraPFOs"],
    "TimeResolution": ["0"],
    "TofMethod": ["closest"],
}

TOFEstimators10ps = MarlinProcessorWrapper("TOFEstimators10ps")
TOFEstimators10ps.OutputLevel = INFO
TOFEstimators10ps.ProcessorType = "TOFEstimators"
TOFEstimators10ps.Parameters = {
    "ExtrapolateToEcal": ["true"],
    "MaxEcalLayer": ["10"],
    "ReconstructedParticleCollection": ["PandoraPFOs"],
    "TimeResolution": ["10."],
    "TofMethod": ["closest"],
}

TOFEstimators50ps = MarlinProcessorWrapper("TOFEstimators50ps")
TOFEstimators50ps.OutputLevel = INFO
TOFEstimators50ps.ProcessorType = "TOFEstimators"
TOFEstimators50ps.Parameters = {
    "ExtrapolateToEcal": ["true"],
    "MaxEcalLayer": ["10"],
    "ReconstructedParticleCollection": ["PandoraPFOs"],
    "TimeResolution": ["50"],
    "TofMethod": ["closest"],
}

TOFEstimators100ps = MarlinProcessorWrapper("TOFEstimators100ps")
TOFEstimators100ps.OutputLevel = INFO
TOFEstimators100ps.ProcessorType = "TOFEstimators"
TOFEstimators100ps.Parameters = {
    "ExtrapolateToEcal": ["true"],
    "MaxEcalLayer": ["10"],
    "ReconstructedParticleCollection": ["PandoraPFOs"],
    "TimeResolution": ["100"],
    "TofMethod": ["closest"],
}

MyLCIOOutputProcessor = MarlinProcessorWrapper("MyLCIOOutputProcessor")
MyLCIOOutputProcessor.OutputLevel = INFO
MyLCIOOutputProcessor.ProcessorType = "LCIOOutputProcessor"
MyLCIOOutputProcessor.Parameters = {
    "CompressionLevel": ["6"],
    "DropCollectionNames": ["%(AdditionalDropCollectionsREC)s" % CONSTANTS],
    "LCIOOutputFile": [f"{reco_args.outputFileBase}_REC.slcio"],
    "LCIOWriteMode": ["WRITE_NEW"],
}

DSTOutput = MarlinProcessorWrapper("DSTOutput")
DSTOutput.OutputLevel = INFO
DSTOutput.ProcessorType = "LCIOOutputProcessor"
DSTOutput.Parameters = {
    "CompressionLevel": ["6"],
    "DropCollectionNames": ["PandoraPFANewStartVertices"],
    "DropCollectionTypes": [
        "MCParticle",
        "SimTrackerHit",
        "SimCalorimeterHit",
        "TrackerHit",
        "TrackerHitPlane",
        "CalorimeterHit",
        "LCRelation",
        "Track",
        "LCFloatVec",
    ],
    "FullSubsetCollections": ["MCParticlesSkimmed"],
    "KeepCollectionNames": [
        "MCParticlesSkimmed",
        "MarlinTrkTracks",
        "MarlinTrkTracksProton",
        "MarlinTrkTracksKaon",
        "MCTruthMarlinTrkTracksLink",
        "MarlinTrkTracksMCTruthLink",
        "RecoMCTruthLink",
        "MCTruthRecoLink",
        "MCTruthClusterLink",
        "ClusterMCTruthLink",
    ],
    "LCIOOutputFile": [f"{reco_args.outputFileBase}_DST.slcio"],
    "LCIOWriteMode": ["WRITE_NEW"],
}

MyPfoAnalysis = MarlinProcessorWrapper("MyPfoAnalysis")
MyPfoAnalysis.OutputLevel = INFO
MyPfoAnalysis.ProcessorType = "PfoAnalysis"
MyPfoAnalysis.Parameters = {
    "BCalCollections": ["BCAL"],
    "BCalCollectionsSimCaloHit": ["BeamCalCollection"],
    "CollectCalibrationDetails": ["0"],
    "ECalBarrelCollectionsSimCaloHit": ["%(ECalBarrelSimHitCollections)s" % CONSTANTS],
    "ECalCollections": [
        "EcalBarrelCollectionRec",
        "EcalBarrelCollectionGapHits",
        "EcalEndcapsCollectionRec",
        "EcalEndcapsCollectionGapHits",
        "EcalEndcapRingCollectionRec",
    ],
    "ECalCollectionsSimCaloHit": ["%(ECalSimHitCollections)s" % CONSTANTS],
    "ECalEndCapCollectionsSimCaloHit": ["%(ECalEndcapSimHitCollections)s" % CONSTANTS],
    "ECalOtherCollectionsSimCaloHit": ["%(ECalRingSimHitCollections)s" % CONSTANTS],
    "HCalBarrelCollectionsSimCaloHit": ["%(HCalBarrelSimHitCollections)s" % CONSTANTS],
    "HCalCollections": [
        "HcalBarrelCollectionRec",
        "HcalEndcapsCollectionRec",
        "HcalEndcapRingCollectionRec",
    ],
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
    "RootFile": [f"{reco_args.outputFileBase}_PfoAnalysis.root"],
}

algList.append(MyAIDAProcessor)
algList.append(MyStatusmonitor)

# TODO: input file specification for this
# algList.append(BgOverlayWW)
# algList.append(BgOverlayWB)
# algList.append(BgOverlayBW)
# algList.append(BgOverlayBB)
# algList.append(PairBgOverlay)

algList.append(MySplitCollectionByLayer)
algList.append(VXDPlanarDigiProcessor_CMOSVXD5)
algList.append(SITPlanarDigiProcessor)
algList.append(FTDPixelPlanarDigiProcessor)
algList.append(FTDStripPlanarDigiProcessor)
algList.append(FTDDDSpacePointBuilder)
algList.append(SETPlanarDigiProcessor)
algList.append(SETDDSpacePointBuilder)
algList.append(MyTPCDigiProcessor)
algList.append(MyClupatraProcessor)
algList.append(MySiliconTracking_MarlinTrk)
algList.append(MyForwardTracking)
algList.append(MyTrackSubsetProcessor)
algList.append(MyFullLDCTracking_MarlinTrk)
algList.append(MyCompute_dEdxProcessor)
algList.append(MyV0Finder)
algList.append(MyKinkFinder)
algList.append(MyRefitProcessorKaon)
algList.append(MyRefitProcessorProton)
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
algList.append(MyPi0Finder)
algList.append(MyEtaFinder)
algList.append(MyEtaPrimeFinder)
algList.append(MyGammaGammaSolutionFinder)
algList.append(MyDistilledPFOCreator)
algList.append(MyLikelihoodPID)
algList.append(MyRecoMCTruthLinker)
algList.append(VertexFinder)
algList.append(TrackLengthProcessor)
algList.append(TOFEstimators0ps)
algList.append(TOFEstimators10ps)
algList.append(TOFEstimators50ps)
algList.append(TOFEstimators100ps)
algList.append(MyLCIOOutputProcessor)
algList.append(DSTOutput)
algList.append(MyPfoAnalysis)

from Configurables import ApplicationMgr

ApplicationMgr(
    TopAlg=algList, EvtSel="NONE", EvtMax=10, ExtSvc=svcList, OutputLevel=INFO
)
