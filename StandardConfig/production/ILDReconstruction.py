import os
import sys

from Configurables import (
    ApplicationMgr,
    EDM4hep2LcioTool,
    GeoSvc,
    Lcio2EDM4hepTool,
    LcioEvent,
    MarlinProcessorWrapper,
    PodioInput,
    PodioOutput,
    k4DataSvc,
)
from Gaudi.Configuration import INFO

try:
    from k4FWCore.utils import SequenceLoader, import_from
except ImportError:
    from py_utils import import_from, SequenceLoader

from k4FWCore.parseArgs import parser
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
    "ILD_l5_o1_v09",
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
    "ILD_l5_v11",
)

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
parser.add_argument(
    "--perfectPFA", help="Run perfect PandoraPFA", action="store_true", default=False
)
parser.add_argument(
    "--runOverlay",
    help="Run background overaly. NOTE: You have to make sure that the Overlay algorithms in "
    " BgOverlay/BgOverlay.py are provided with the necessary overlay files",
    action="store_true",
    default=False,
)
# BeamCal reco configuration
parser.add_argument(
    "--runBeamCalReco",
    help="Run the BeamCal reco",
    action="store_true",
    dest="runBeamCalReco",
)
parser.add_argument(
    "--noBeamCalReco",
    help="Don't run the BeamCal reco",
    action="store_false",
    dest="runBeamCalReco",
)
parser.set_defaults(runBeamCalReco=True)
parser.add_argument(
    "--beamCalCalibFactor",
    help="The BeamCal calibration constant from sim hit energy to calibrated calo hit energy",
    type=float,
    default=79.6,
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

geoSvc = GeoSvc("GeoSvc")
geoSvc.detectors = [compact_file]
geoSvc.OutputLevel = INFO
geoSvc.EnableGeant4Geo = False
svcList.append(geoSvc)


CONSTANTS = {
    "CMSEnergy": str(reco_args.cmsEnergy),
    "BeamCalCalibrationFactor": str(reco_args.beamCalCalibFactor),
}

det_calib_constants = import_from(f"Calibration/Calibration_{det_model}.cfg").CONSTANTS
CONSTANTS.update(det_calib_constants)

parseConstants(CONSTANTS)


cms_energy_config = import_from(
    f"Config/Parameters{reco_args.cmsEnergy}GeV.cfg"
).PARAMETERS

sequenceLoader = SequenceLoader(
    algList,
    global_vars={"CONSTANTS": CONSTANTS, "cms_energy_config": cms_energy_config},
)


def create_reader(input_files):
    """Create the appropriate reader for the input files"""
    if input_files[0].endswith(".slcio"):
        if any(not f.endswith(".slcio") for f in input_files):
            print("All input files need to have the same format (LCIO)")
            sys.exit(1)

        read = LcioEvent()
        read.Files = input_files
    else:
        if any(not f.endswith(".root") for f in input_files):
            print("All input files need to have the same format (EDM4hep)")
            sys.exit(1)
        read = PodioInput("PodioInput")
        global evtsvc
        evtsvc.inputs = input_files

    return read


if reco_args.inputFiles:
    read = create_reader(reco_args.inputFiles)
    read.OutputLevel = INFO
    algList.append(read)
else:
    read = None


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


# TODO: input file specification for this from command line?
if reco_args.runOverlay:
    sequenceLoader.load("BgOverlay/BgOverlay")


ecal_technology = CONSTANTS["EcalTechnology"]
hcal_technology = CONSTANTS["HcalTechnology"]

sequenceLoader.load("Tracking/TrackingDigi")
sequenceLoader.load("Tracking/TrackingReco")
# sequenceLoader.load(f"CaloDigi/{ecal_technology}Digi")
# sequenceLoader.load(f"CaloDigi/{hcal_technology}Digi")
# sequenceLoader.load("CaloDigi/FcalDigi")
# sequenceLoader.load("CaloDigi/MuonDigi")

# if reco_args.perfectPFA:
#    sequenceLoader.load("ParticleFlow/PandoraPFAPerfect")
# else:
#    sequenceLoader.load("ParticleFlow/PandoraPFA")

if reco_args.runBeamCalReco:
    sequenceLoader.load("HighLevelReco/BeamCalReco")

# sequenceLoader.load("HighLevelReco/HighLevelReco")


MyPfoAnalysis = MarlinProcessorWrapper("MyPfoAnalysis")
MyPfoAnalysis.OutputLevel = INFO
MyPfoAnalysis.ProcessorType = "PfoAnalysis"
MyPfoAnalysis.Parameters = {
    "BCalCollections": ["BCAL"],
    "BCalCollectionsSimCaloHit": ["BeamCalCollection"],
    "CollectCalibrationDetails": ["0"],
    "ECalBarrelCollectionsSimCaloHit": [CONSTANTS["ECalBarrelSimHitCollections"]],
    "ECalCollections": [
        "EcalBarrelCollectionRec",
        "EcalBarrelCollectionGapHits",
        "EcalEndcapsCollectionRec",
        "EcalEndcapsCollectionGapHits",
        "EcalEndcapRingCollectionRec",
    ],
    "ECalCollectionsSimCaloHit": [CONSTANTS["ECalSimHitCollections"]],
    "ECalEndCapCollectionsSimCaloHit": [CONSTANTS["ECalEndcapSimHitCollections"]],
    "ECalOtherCollectionsSimCaloHit": [CONSTANTS["ECalRingSimHitCollections"]],
    "HCalBarrelCollectionsSimCaloHit": [CONSTANTS["HCalBarrelSimHitCollections"]],
    "HCalCollections": [
        "HcalBarrelCollectionRec",
        "HcalEndcapsCollectionRec",
        "HcalEndcapRingCollectionRec",
    ],
    "HCalEndCapCollectionsSimCaloHit": [CONSTANTS["HCalEndcapSimHitCollections"]],
    "HCalOtherCollectionsSimCaloHit": [CONSTANTS["HCalRingSimHitCollections"]],
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

algList.append(MyPfoAnalysis)

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
    for name in CONSTANTS["AdditionalDropCollectionsREC"].split(" "):
        edm4hepOutput.outputCommands.append(f"drop {name}")

    algList.append(edm4hepOutput)


if reco_args.lcioOutput in ("on", "only"):
    MyLCIOOutputProcessor = MarlinProcessorWrapper("MyLCIOOutputProcessor")
    MyLCIOOutputProcessor.OutputLevel = INFO
    MyLCIOOutputProcessor.ProcessorType = "LCIOOutputProcessor"
    MyLCIOOutputProcessor.Parameters = {
        "CompressionLevel": ["6"],
        "DropCollectionNames": [CONSTANTS["AdditionalDropCollectionsREC"]],
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

ApplicationMgr(
    TopAlg=algList, EvtSel="NONE", EvtMax=3, ExtSvc=svcList, OutputLevel=INFO
)
