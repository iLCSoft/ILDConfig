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
from k4MarlinWrapper.parseConstants import parseConstants

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
    "--compactFile", help="Compact detector file to use", type=str, default=""
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

det_model = reco_args.detectorModel

if reco_args.compactFile:
    compact_file = reco_args.compactFile
else:
    compact_file = f"{os.environ['K4GEO']}/ILD/compact/{det_model}/{det_model}.xml"


from Configurables import GeoSvc

geoSvc = GeoSvc("GeoSvc")
geoSvc.detectors = [compact_file]
geoSvc.OutputLevel = INFO
geoSvc.EnableGeant4Geo = False
svcList.append(geoSvc)


CONSTANTS = {
    "CMSEnergy": str(reco_args.cmsEnergy),
    "RunBeamCalReco": "true",
    "BeamCalCalibrationFactor": "79.6",
}

from k4FWCore.utils import import_from


det_calib_constants = import_from(f"Calibration/Calibration_{det_model}.cfg").CONSTANTS
CONSTANTS.update(det_calib_constants)

parseConstants(CONSTANTS)


cms_energy_config = import_from(
    f"Config/Parameters{reco_args.cmsEnergy}GeV.cfg"
).PARAMETERS


def add_sequence(sequence: str, alg_list: list):
    """Add a sequence to the list of algorithms.

    This function dynamically imports a Python module based on the provided
    sequence name, extracts the sequence defined in there and appends all
    algorithms defined in that sequence to the provided list of algorithms. The
    module is imported with on-the-fly configuration by providing global
    calibraation values (`CONSTANTS` and `cms_energy_config`).

    The path for the module import is determined via f'{sequence}.py' and the
    name of the imported sequence is the same as the filename replacing `.py`
    with `Sequence`, see the examples below.

    Args:
        sequence (str): The name of the sequence to be added. This name is used
            to dynamically create the filename and sequence class name. The
            sequence file should be a `.py` file located in the working
            directory or accessible in the Python path.
        alg_list (list): The list to which the sequence of algorithms will be
            appended. This list is modified in-place.

    Examples:
        >>> alg_list = []
        >>> add_sequence("Tracking/TrackingDigi", alg_list)

        This will import `Tracking.TrackingDigi` and add the algorithms in
        `TrackingDigiSequence` to the `alg_list`
    """
    filename = f"{sequence}.py"
    seq_name = f"{sequence.split('/')[-1]}Sequence"

    seq_module = import_from(
        filename,
        global_vars={"CONSTANTS": CONSTANTS, "cms_energy_config": cms_energy_config},
    )
    seq = getattr(seq_module, seq_name)
    alg_list.extend(seq)


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


ecal_technology = CONSTANTS["EcalTechnology"]
hcal_technology = CONSTANTS["HcalTechnology"]

add_sequence("Tracking/TrackingDigi", algList)
add_sequence("Tracking/TrackingReco", algList)
add_sequence(f"CaloDigi/{ecal_technology}Digi", algList)
add_sequence(f"CaloDigi/{hcal_technology}Digi", algList)
add_sequence("CaloDigi/FcalDigi", algList)
add_sequence("CaloDigi/MuonDigi", algList)
add_sequence("ParticleFlow/PandoraPFA", algList)
add_sequence("HighLevelReco/BeamCalReco", algList)
add_sequence("HighLevelReco/HighLevelReco", algList)


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


if reco_args.lcioOutput != "only":
    lcioToEDM4hepOutput = Lcio2EDM4hepTool("OutputConversion")
    # Take care of the different naming conventions
    lcioToEDM4hepOutput.collNameMapping = {"MCParticle": "MCParticles"}
    lcioToEDM4hepOutput.OutputLevel = INFO
    # Attach the conversion to the last non-output processor that is always run
    MyPfoAnalysis.Lcio2EDM4hepTool = lcioToEDM4hepOutput

    edm4hepOutput = PodioOutput("EDM4hepOutput")
    edm4hepOutput.filename = f"{reco_args.outputFileBase}_REC.edm4hep.root"
    edm4hepOutput.outputCommands = ["keep *"]
    algList.append(edm4hepOutput)


if reco_args.lcioOutput in ("on", "only"):
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

    algList.append(MyLCIOOutputProcessor)
    algList.append(DSTOutput)

algList.append(MyPfoAnalysis)

from Configurables import ApplicationMgr

ApplicationMgr(
    TopAlg=algList, EvtSel="NONE", EvtMax=3, ExtSvc=svcList, OutputLevel=INFO
)
