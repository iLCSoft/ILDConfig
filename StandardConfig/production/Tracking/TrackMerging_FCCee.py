#!/usr/bin/env python3

from Configurables import MarlinProcessorWrapper, TrackMerger  # , CellIDEncodingFiller
from Gaudi.Configuration import INFO  # , DEBUG

# ---------------------------------------------------------------------------
# Hot Fix: Missing CellID encodings
# ---------------------------------------------------------------------------

# _ENCODING_STR = (
#     "system:0:5,module:5:3,stave:8:4,tower:12:4,layer:16:6,"
#     "wafer:22:6,slice:28:4,cellX:32:-16,cellY:48:-16"
# )
# MISSING_ENCODINGS = {
#     key: _ENCODING_STR
#     for key in [
#         "EcalEndcapsCollectionGapHits",
#         "EcalEndcapsCollection",
#         "EcalEndcapsCollectionDigi",
#         "EcalEndcapsCollectionRec",
#         "EcalBarrelCollection",
#         "EcalBarrelCollectionDigi",
#         "EcalBarrelCollectionRec",
#         "EcalBarrelCollectionGapHits",
#         "EcalEndcapRingCollectionDigi",
#         "EcalEndcapRingCollectionRec",
#         "HcalBarrelCollectionDigi",
#         "HcalBarrelCollectionRec",
#         "HcalEndcapsCollectionDigi",
#         "HcalEndcapsCollectionRec",
#         "HcalEndcapRingCollectionDigi",
#         "HcalEndcapRingCollectionRec",
#         "LCAL",
#         "MUON",
#     ]
# }

# ---------------------------------------------------------------------------
# Track collection names
# ---------------------------------------------------------------------------

SI_TRACK_COLL_NAME = "SiTracksCT"
CLU_TRACK_COLL_NAME = "ClupatraTracks"
CLU_W_SI_TRACK_COLL_NAME = "MarlinTrkTracks"
MCP_COLL_NAME = "MCParticles"

# ---------------------------------------------------------------------------
# Track variations
# Each entry has:
#   "collections": input/output collection names
#   "merger":      merger-specific settings (None = no merger step)
#   "refitter":    refitter-specific settings
# ---------------------------------------------------------------------------

TRACK_VARIATIONS = {
    "Greedy": {
        "collections": {
            "merge_candidates": "CandidateGreedyMergedTracks",
            "refit_output": "RefittedGreedyMergedTracks",
            "refit_rel": "RefittedGreedyMergedTrackRelations",
        },
        "merger": {
            "enabled": True,
            "greedy": True,
        },
        "refitter": {
            "enabled": True,
        },
    },
    "Ambiguous": {
        "collections": {
            "merge_candidates": "CandidateAmbiguousMergedTracks",
            "refit_output": "RefittedAmbiguousMergedTracks",
            "refit_rel": "RefittedAmbiguousMergedTrackRelations",
        },
        "merger": {
            "enabled": True,
            "greedy": False,
        },
        "refitter": {
            "enabled": True,
        },
    },
    "CluWithSi": {
        "collections": {
            "merge_candidates": CLU_W_SI_TRACK_COLL_NAME,  # already exists, no merger
            "refit_output": "RefittedCluWithSiTracks",
            "refit_rel": "RefittedCluWithSiTrackRelations",
        },
        "merger": {
            "enabled": False,
        },
        "refitter": {
            "enabled": True,
        },
    },
}

TrackMerging_FCCeeSequence = []

# ------------------------------------------------------------------
# CellIDEncodingFiller
# ------------------------------------------------------------------

# MyFiller = CellIDEncodingFiller("CellIDEncodingFiller")
# MyFiller.CellIDEncodings = MISSING_ENCODINGS
# TrackMerging_FCCeeSequence.append(MyFiller)

# ------------------------------------------------------------------
# Track Merging
# ------------------------------------------------------------------

for track_type, var in TRACK_VARIATIONS.items():
    if not var["merger"]["enabled"]:
        continue
    colls = var["collections"]
    merger = TrackMerger(
        f"{track_type}TrackMerger",
        InputSiTracks=SI_TRACK_COLL_NAME,
        InputCluTracks=CLU_TRACK_COLL_NAME,
        OutTracks=colls["merge_candidates"],
        Greedy=var["merger"]["greedy"],
    )
    merger.OutputLevel = INFO
    TrackMerging_FCCeeSequence.append(merger)

# ------------------------------------------------------------------
# Refitting
# ------------------------------------------------------------------

SHARED_REFITTING_CONFIG = {
    "EnergyLossOn": ["true"],
    "FitDirection": ["+1"],
    "InitialTrackErrorD0": ["1e+06"],
    "InitialTrackErrorOmega": ["0.00001"],
    "InitialTrackErrorPhi0": ["100"],
    "InitialTrackErrorTanL": ["100"],
    "InitialTrackErrorZ0": ["1e+06"],
    "InitialTrackState": ["-1"],
    "TrackSystemName": ["DDKalTest"],
    "InputTrackRelCollection": [],
}

for track_type, var in TRACK_VARIATIONS.items():
    if not var["refitter"]["enabled"]:
        continue
    colls = var["collections"]
    refitter = MarlinProcessorWrapper(f"{track_type}Refitter")
    refitter.ProcessorType = "RefitProcessor"
    refitter.Parameters = SHARED_REFITTING_CONFIG | {
        "InputTrackCollectionName": [colls["merge_candidates"]],
        "OutputTrackCollectionName": [colls["refit_output"]],
        "OutputTrackRelCollection": [colls["refit_rel"]],
    }
    refitter.OutputLevel = INFO
    TrackMerging_FCCeeSequence.append(refitter)

# ------------------------------------------------------------------
