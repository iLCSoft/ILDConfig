import os
import sys
from pathlib import Path
from typing import Any

from Configurables import (
    AlgTimingAuditor,
    AuditorSvc,
    EventDataSvc,
    GeoSvc,
    MarlinProcessorWrapper,
)
from Gaudi.Configuration import INFO
from k4FWCore import ApplicationMgr, IOSvc
from k4FWCore.parseArgs import parser
from k4MarlinWrapper.io_helpers import IOHandlerHelper
from k4MarlinWrapper.parseConstants import parseConstants

# Make sure we have the py_utils on the PYHTONPATH (but don't give them any more
# importance than necessary)
sys.path.append(Path(__file__).parent)
from py_utils import (
    SequenceLoader,
    get_drop_collections,
    import_from,
    parse_collection_patch_file,
)

BASELINE_DET_MOD = "ILD_l5_o1_v02"
# only non-FCCMDI models
DETECTOR_MODELS = (
    BASELINE_DET_MOD,
    "ILD_l2_v02",
    "ILD_l4_o1_v02",
    "ILD_l4_o2_v02",
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
# only FCCMDI
FCCeeMDI_DETECTOR_MODELS_common_MDI = (  # only models located in $K4GEO/FCCee/ILD_FCCee/
    "ILD_FCCee_v01",
    "ILD_FCCee_v02",
)
FCCeeMDI_DETECTOR_MODELS = (  # only add models located in $K4GEO/ILD/ here
    "ILD_l5_o1_v09",
    "ILD_l5_v11",
    *FCCeeMDI_DETECTOR_MODELS_common_MDI,
)
ALL_DETECTOR_MODELS = DETECTOR_MODELS + FCCeeMDI_DETECTOR_MODELS

REC_COLLECTION_CONTENTS_FILE = "collections_rec_level.txt"

det_mod_g = parser.add_mutually_exclusive_group(required=False)
det_mod_g.add_argument(
    "--compactFile",
    help="Path to a custom DD4hep XML compact file to define the detector geometry",
    type=str,
    default=None,
)
det_mod_g.add_argument(
    "--detectorModel",
    help="Name of a registered detector model to use for reconstruction",
    choices=ALL_DETECTOR_MODELS,
    type=str,
    default=None,
)

beam_cal_reco_g = parser.add_mutually_exclusive_group(required=False)
beam_cal_reco_g.add_argument(
    "--runBeamCalReco",
    help="Run the BeamCal reco",
    action="store_true",
    dest="runBeamCalReco",
)
beam_cal_reco_g.add_argument(
    "--noBeamCalReco",
    help="Don't run the BeamCal reco",
    action="store_false",
    dest="runBeamCalReco",
)

parser.add_argument(
    "--inputFiles",
    action="extend",
    nargs="+",
    metavar=["file1", "file2"],
    help="One or multiple input files",
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
    choices=(91, 160, 240, 250, 350, 365, 500, 1000),
    type=int,
    default=None,
)
parser.add_argument(
    "--perfectPFA",
    help="Run perfect PandoraPFA",
    action="store_true",
)
parser.add_argument(
    "--runOverlay",
    help="Run background overlay. NOTE: You have to make sure that the Overlay algorithms in "
    " BgOverlay/BgOverlay.py are provided with the necessary overlay files",
    action="store_true",
)
parser.add_argument(
    "--beamCalCalibFactor",
    help="The BeamCal calibration constant from sim hit energy to calibrated calo hit energy",
    type=float,
    default=79.6,
)
parser.add_argument(
    "--trackingOnly",
    help="Only Tracking is performed; built for reco testing purposes",
    action="store_true",
)


def get_compact_file_path(detector_model: str):
    """returns the compact file path to a specified detector model starting with the path stored in the 'K4GEO' environment variable"""
    if detector_model in FCCeeMDI_DETECTOR_MODELS_common_MDI:
        return f"{os.path.normpath(os.environ['K4GEO'])}/FCCee/ILD_FCCee/compact/{detector_model}/{detector_model}.xml"
    return f"{os.path.normpath(os.environ['K4GEO'])}/ILD/compact/{detector_model}/{detector_model}.xml"


def get_cms_energy_config(
    compact_file_path: str | Path | os.PathLike, cms_energy: int | None
) -> tuple[bool, int, Any]:
    """returns the collider type, resolved cms energy, and associated config parameters"""
    _is_FCCee_model = "FCCee" in Path(compact_file_path).parts
    # choose correct default cms energy if not specified
    energy = cms_energy or (240 if _is_FCCee_model else 250)
    # choose correct dir for chosen collider
    collider = "FCCee" if _is_FCCee_model else "ILC"
    return (
        _is_FCCee_model,
        energy,
        import_from(f"Config/{collider}/Parameters{energy:03d}GeV.cfg").PARAMETERS,
    )


reco_args = parser.parse_known_args()[0]

algList = []
svcList = []

evtsvc = EventDataSvc("EventDataSvc")
svcList.append(evtsvc)
iosvc = IOSvc()

if reco_args.compactFile:
    compact_file = reco_args.compactFile
    # Derive det_model name from the file
    det_model = Path(compact_file).stem
else:
    det_model = reco_args.detectorModel or BASELINE_DET_MOD
    compact_file = get_compact_file_path(det_model)

# Ensure the detector model is registered in the known models list.
# This is required to correctly resolve paths and select the appropriate reconstruction sequence.
assert det_model in ALL_DETECTOR_MODELS, (
    f"Detector model '{det_model}' is not registered in ALL_DETECTOR_MODELS"
)

geoSvc = GeoSvc("GeoSvc")
geoSvc.detectors = [compact_file]
geoSvc.OutputLevel = INFO
geoSvc.EnableGeant4Geo = False
svcList.append(geoSvc)

is_FCCee_model, cms_e, cms_energy_config = get_cms_energy_config(
    compact_file, reco_args.cmsEnergy
)
CONSTANTS = {
    "CMSEnergy": str(cms_e),
    "BeamCalCalibrationFactor": str(reco_args.beamCalCalibFactor),
}

det_calib_constants = import_from(f"Calibration/Calibration_{det_model}.cfg").CONSTANTS
CONSTANTS.update(det_calib_constants)

parseConstants(CONSTANTS)

sequenceLoader = SequenceLoader(
    algList,
    global_vars={"CONSTANTS": CONSTANTS, "cms_energy_config": cms_energy_config},
)

io_handler = IOHandlerHelper(algList, iosvc)
io_handler.add_reader(reco_args.inputFiles)

MyAIDAProcessor = MarlinProcessorWrapper("MyAIDAProcessor")
MyAIDAProcessor.ProcessorType = "AIDAProcessor"
MyAIDAProcessor.Parameters = {
    "Compress": ["1"],
    "FileName": [f"{reco_args.outputFileBase}_AIDA"],
    "FileType": ["root"],
}
algList.append(MyAIDAProcessor)

MyStatusmonitor = MarlinProcessorWrapper("MyStatusmonitor")
MyStatusmonitor.ProcessorType = "Statusmonitor"
MyStatusmonitor.Parameters = {"HowOften": ["1"]}
algList.append(MyStatusmonitor)


# TODO: input file specification for this from command line?
if reco_args.runOverlay:
    sequenceLoader.load("BgOverlay/BgOverlay")


ecal_technology = CONSTANTS["EcalTechnology"]
hcal_technology = CONSTANTS["HcalTechnology"]

# load relevant tracking
if det_model in FCCeeMDI_DETECTOR_MODELS:
    sequenceLoader.load("Tracking/TrackingDigi_FCCeeMDI")
    sequenceLoader.load("Tracking/TrackingReco_FCCeeMDI")
elif det_model in DETECTOR_MODELS:
    sequenceLoader.load("Tracking/TrackingDigi")
    sequenceLoader.load("Tracking/TrackingReco")

if not reco_args.trackingOnly:
    sequenceLoader.load(f"CaloDigi/{ecal_technology}Digi")
    sequenceLoader.load(f"CaloDigi/{hcal_technology}Digi")
    sequenceLoader.load("CaloDigi/FcalDigi")
    sequenceLoader.load("CaloDigi/MuonDigi")

    if reco_args.perfectPFA:
        sequenceLoader.load("ParticleFlow/PandoraPFAPerfect")
    else:
        sequenceLoader.load("ParticleFlow/PandoraPFA")

    if reco_args.runBeamCalReco:
        sequenceLoader.load("HighLevelReco/BeamCalReco")

    if not is_FCCee_model:
        sequenceLoader.load("HighLevelReco/HighLevelReco")

    MyPfoAnalysis = MarlinProcessorWrapper("MyPfoAnalysis")
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
    # Make sure that all collections are always available by patching in missing
    # ones on-the-fly
    collPatcherRec = MarlinProcessorWrapper(
        "CollPatcherREC", ProcessorType="PatchCollections"
    )
    collPatcherRec.Parameters = {
        "PatchCollections": parse_collection_patch_file(REC_COLLECTION_CONTENTS_FILE)
    }
    algList.append(collPatcherRec)

    output_commands = ["keep *"]
    output_commands.extend(get_drop_collections(CONSTANTS, True))
    io_handler.add_edm4hep_writer(
        f"{reco_args.outputFileBase}_REC.edm4hep.root", output_commands
    )


if reco_args.lcioOutput in ("on", "only"):
    MyLCIOOutputProcessor = io_handler.add_lcio_writer("MyLCIOOutputProcessor")
    MyLCIOOutputProcessor.Parameters = {
        "CompressionLevel": ["6"],
        "DropCollectionNames": get_drop_collections(CONSTANTS, False),
        "LCIOOutputFile": [f"{reco_args.outputFileBase}_REC.slcio"],
        "LCIOWriteMode": ["WRITE_NEW"],
    }

    DSTOutput = io_handler.add_lcio_writer("DSTOutput")
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

io_handler.finalize_converters()

# Use Gaudi Auditor service to get timing information on algorithm execution
auditorSvc = AuditorSvc()
svcList.append(auditorSvc)
auditorSvc.Auditors = [AlgTimingAuditor()]

app_mgr = ApplicationMgr(
    TopAlg=algList, EvtSel="NONE", EvtMax=3, ExtSvc=svcList, OutputLevel=INFO
)

app_mgr.AuditAlgorithms = True
app_mgr.AuditTools = True
app_mgr.AuditServices = True
