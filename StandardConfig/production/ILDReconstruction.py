import os
import sys
from Gaudi.Configuration import *

from Configurables import (
    LcioEvent,
    MarlinProcessorWrapper,
    k4DataSvc,
    PodioInput,
    PodioOutput,
    EDM4hep2LcioTool,
    Lcio2EDM4hepTool,
)
from k4MarlinWrapper.parseConstants import *

DETECTOR_MODELS = (
    "ILD_l2_v02",
    "ILD_l4_o1_v02",
    "ILD_l4_o2_v02",
    "ILD_l5_o1_v02",
    "ILD_l5_o1_v03",
    "ILD_l5_o1_v04",
    "ILD_l5_o1_v05",
    "ILD_l5_o1_v06",
    "ILD_l5_o2_v02",
    "ILD_l5_o3_v02",
    "ILD_l5_o4_v02",
    "ILD_s2_v02",
    "ILD_s4_o1_v02",
    "ILD_s4_o2_v02",
    "ILD_s5_o1_v02",
    "ILD_s5_o1_v03",
    "ILD_s5_o1_v04",
    "ILD_s5_o1_v05",
    "ILD_s5_o1_v06",
    "ILD_s5_o2_v02",
    "ILD_s5_o3_v02",
    "ILD_s5_o4_v02",
)


from k4FWCore.parseArgs import parser

parser.add_argument(
    "--inputFiles",
    action="extend",
    nargs="+",
    metavar=["file1", "file2"],
    help="One or multiple input files",
)
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
parser.add_argument(
    "--lcioOutput",
    help="Choose whether to still create LCIO output (off by default)",
    choices=["off", "on", "only"],
    default="off",
    type=str,
)
parser.add_argument(
    "--cmsEnergy",
    help="The center-of-mass energy to assume for reconstruction in GeV",
    choices=(250, 350, 500, 1000),
    type=int,
    default=250,
)
parser.add_argument(
    "--detectorModel",
    help="Which detector model to run reconstruction for",
    choices=DETECTOR_MODELS,
    type=str,
    default="ILD_l5_o1_v02",
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
    "CMSEnergy": str(reco_args.cmsEnergy),
    "RunBeamCalReco": "true",
    "BeamCalCalibrationFactor": "79.6",
}

from k4FWCore.utils import import_from


def import_with_constants(filename):
    """Import a configuration bit using the approriate calibration constants for
    the current run"""
    return import_from(filename, global_vars={"CONSTANTS": CONSTANTS})


det_calib_constants = import_from(
    f"Calibration/Calibration_{reco_args.detectorModel}.cfg"
).CONSTANTS
CONSTANTS.update(det_calib_constants)

parseConstants(CONSTANTS)

cms_energy_config = import_from(
    f"Config/Parameters{reco_args.cmsEnergy}GeV.cfg"
).PARAMETERS


def create_reader(input_files):
    """Create the appropriate reader for the input files"""
    if input_files[0].endswith(".slcio"):
        if any(not f.endswith(".slcio") for f in input_files):
            print("All input files need to have the same format (LCIO)")
            sys.exit(1)

        read = LcioEvent()
        read.Files = reco_args.inputFiles
    else:
        if any(not f.endswith(".root") for f in input_files):
            print("All input files need to have the same format (EDM4hep)")
            sys.exit(1)
        read = PodioInput("PodioInput")
        global evtsvc
        evtsvc.inputs = input_files

    return read


read = create_reader(reco_args.inputFiles)
read.OutputLevel = INFO
algList.append(read)


MyAIDAProcessor = MarlinProcessorWrapper("MyAIDAProcessor")
MyAIDAProcessor.OutputLevel = INFO
MyAIDAProcessor.ProcessorType = "AIDAProcessor"
MyAIDAProcessor.Parameters = {
    "Compress": ["1"],
    "FileName": [f"{reco_args.outputFileBase}_AIDA"],
    "FileType": ["root"],
}
algList.append(MyAIDAProcessor)

# We need to convert the inputs in case we have EDM4hep input
if isinstance(read, PodioInput):
    EDM4hep2LcioInput = EDM4hep2LcioTool("InputConversion")
    EDM4hep2LcioInput.convertAll = True
    # Adjust for the different naming conventions
    EDM4hep2LcioInput.collNameMapping = {"MCParticles": "MCParticle"}
    MyAIDAProcessor.EDM4hep2LcioTool = EDM4hep2LcioInput


MyStatusmonitor = MarlinProcessorWrapper("MyStatusmonitor")
MyStatusmonitor.OutputLevel = INFO
MyStatusmonitor.ProcessorType = "Statusmonitor"
MyStatusmonitor.Parameters = {"HowOften": ["1"]}
algList.append(MyStatusmonitor)

BgOverlayWW = MarlinProcessorWrapper("BgOverlayWW")
BgOverlayWW.OutputLevel = INFO
BgOverlayWW.ProcessorType = "Overlay"
BgOverlayWW.Parameters = {
    "InputFileNames": ["undefined.slcio"],
    "NumberOverlayEvents": ["0"],
    "expBG": [cms_energy_config["ExpectedBgWW"]],
}

BgOverlayWB = MarlinProcessorWrapper("BgOverlayWB")
BgOverlayWB.OutputLevel = INFO
BgOverlayWB.ProcessorType = "Overlay"
BgOverlayWB.Parameters = {
    "InputFileNames": ["undefined.slcio"],
    "NumberOverlayEvents": ["0"],
    "expBG": [cms_energy_config["ExpectedBgWB"]],
}

BgOverlayBW = MarlinProcessorWrapper("BgOverlayBW")
BgOverlayBW.OutputLevel = INFO
BgOverlayBW.ProcessorType = "Overlay"
BgOverlayBW.Parameters = {
    "InputFileNames": ["undefined.slcio"],
    "NumberOverlayEvents": ["0"],
    "expBG": [cms_energy_config["ExpectedBgBW"]],
}

BgOverlayBB = MarlinProcessorWrapper("BgOverlayBB")
BgOverlayBB.OutputLevel = INFO
BgOverlayBB.ProcessorType = "Overlay"
BgOverlayBB.Parameters = {
    "InputFileNames": ["undefined.slcio"],
    "NumberOverlayEvents": ["0"],
    "expBG": [cms_energy_config["ExpectedBgBB"]],
}

PairBgOverlay = MarlinProcessorWrapper("PairBgOverlay")
PairBgOverlay.OutputLevel = INFO
PairBgOverlay.ProcessorType = "Overlay"
PairBgOverlay.Parameters = {
    "ExcludeCollections": ["BeamCalCollection"],
    "InputFileNames": ["undefined.slcio"],
    "NumberOverlayEvents": ["0"],
}

# TODO: input file specification for this
# algList.append(BgOverlayWW)
# algList.append(BgOverlayWB)
# algList.append(BgOverlayBW)
# algList.append(BgOverlayBB)
# algList.append(PairBgOverlay)


from Tracking.TrackingDigi import TrackingDigiSequence

algList.extend(TrackingDigiSequence)

TrackingRecoSequence = import_with_constants(
    "Tracking/TrackingReco.py"
).TrackingRecoSequence
algList.extend(TrackingRecoSequence)


ecal_technology = CONSTANTS["EcalTechnology"]
EcalDigiSequence = import_with_constants(
    f"CaloDigi/{ecal_technology}Digi.py",
).EcalDigiSequence
algList.extend(EcalDigiSequence)

hcal_technology = CONSTANTS["HcalTechnology"]
HcalDigiSequence = import_with_constants(
    f"CaloDigi/{hcal_technology}Digi.py",
).HcalDigiSequence
algList.extend(HcalDigiSequence)

FcalDigiSequence = import_with_constants(
    "CaloDigi/FcalDigi.py",
).FcalDigiSequence
algList.extend(FcalDigiSequence)

MuonDigiSequence = import_with_constants(
    "CaloDigi/MuonDigi.py",
).MuonDigiSequence
algList.extend(MuonDigiSequence)


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
    "BeamSizeX": [cms_energy_config["BeamSizeX"]],
    "BeamSizeY": [cms_energy_config["BeamSizeY"]],
    "BeamSizeZ": [cms_energy_config["BeamSizeZ"]],
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
        cms_energy_config["LCFIPlusBeamspotConstraint"]
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

if reco_args.lcioOutput != "only":
    lcioToEDM4hepOutput = Lcio2EDM4hepTool("OutputConversion")
    # Take care of the different naming conventions
    lcioToEDM4hepOutput.collNameMapping = {"MCParticle": "MCParticles"}
    lcioToEDM4hepOutput.OutputLevel = INFO
    # Attach the conversion to the last non-output processor that is always run
    TOFEstimators100ps.Lcio2EDM4hepTool = lcioToEDM4hepOutput

    edm4hepOutput = PodioOutput("EDM4hepOutput")
    edm4hepOutput.filename = f"{reco_args.outputFileBase}_REC.edm4hep.root"
    edm4hepOutput.outputCommands = ["keep *"]
    algList.append(edm4hepOutput)


if reco_args.lcioOutput in ("on", "only"):
    algList.append(MyLCIOOutputProcessor)
    algList.append(DSTOutput)

algList.append(MyPfoAnalysis)

from Configurables import ApplicationMgr

ApplicationMgr(
    TopAlg=algList, EvtSel="NONE", EvtMax=3, ExtSvc=svcList, OutputLevel=INFO
)
