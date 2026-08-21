#!/usr/bin/env python3

from Configurables import MarlinProcessorWrapper, TrackMerger
from Gaudi.Configuration import INFO  # , DEBUG

# ---------------------------------------------------------------------------
# Track collection names
# ---------------------------------------------------------------------------

SI_TRACK_COLL_NAME = "SiTracksCT"
CLU_TRACK_COLL_NAME = "ClupatraTracks"
CLU_W_SI_TRACK_COLL_NAME = "ClupatraFCCTracks"
MCP_COLL_NAME = "MCParticles"

# ---------------------------------------------------------------------------
# Track variations
# Each entry has:
#   "collections": input/output collection names
#   "merger":      merger-specific settings (None = no merger step)
#   "refitter":    refitter-specific settings
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# TrackMerger matching tolerances
#
# TrackMerger considers two tracks a match if the differences of their track
# parameters at the adjoining hit are within the configured tolerances. Each
# of the 5 track parameters (D0, Z0, phi, omega, tanLambda) has its own
# tolerance property; a negative value disables that parameter, i.e. it is
# not considered for matching. The properties are:
#   D0Tolerance, Z0Tolerance, PhiTolerance, OmegaTolerance, TanLambdaTolerance
#
# The defaults set in TrackMerger.cpp reproduce the original criterion
# (D0Tolerance=0.5, Z0Tolerance=2.5, everything else negative/disabled), so
# this dict only needs entries for parameters you want to override, e.g.
# {"PhiTolerance": 0.05} to also require phi compatibility, or
# {"D0Tolerance": -1} to turn the D0 check off.
# ---------------------------------------------------------------------------

TRACK_VARIATIONS = {
    "Greedy": {
        "collections": {
            "merge_candidates": "CandidateGreedyMergedTracks",
            "refit_output": "RefittedGreedyMergedTracks",
            "refit_rel": "RefittedGreedyMergedTrackRelations",
        },
        "merger": {
            "enabled": track_merging,
            "greedy": True,
            "thresholds": {},  # empty -> use TrackMerger defaults (D0Tolerance=0.5, Z0Tolerance=2.5)
        },
        "refitter": {
            "enabled": track_merging,
        },
    },
    "Ambiguous": {
        "collections": {
            "merge_candidates": "CandidateAmbiguousMergedTracks",
            "refit_output": "RefittedAmbiguousMergedTracks",
            "refit_rel": "RefittedAmbiguousMergedTrackRelations",
        },
        "merger": {
            "enabled": track_merging,
            "greedy": False,
            "thresholds": {},  # empty -> use TrackMerger defaults (D0Tolerance=0.5, Z0Tolerance=2.5)
        },
        "refitter": {
            "enabled": track_merging,
        },
    },
    "CluWithSi": {
        "collections": {
            "merge_candidates": CLU_W_SI_TRACK_COLL_NAME,  # already exists, no merger
            "refit_output": "MarlinTrkTracks",
            "refit_rel": "MarlinTrkTrackRelation",
        },
        "merger": {
            "enabled": False,
        },
        "refitter": {
            "enabled": True,  # always refit MarlinTrkTracks, regardless of --trackMerge flag
        },
    },
}

TrackMerging_FCCeeSequence = []

# ------------------------------------------------------------------
# Track Merging
# ------------------------------------------------------------------

for track_type, var in TRACK_VARIATIONS.items():
    if not var["merger"]["enabled"]:
        continue
    colls = var["collections"]
    merger = TrackMerger(
        f"{track_type}TrackMerger",
        InputInnerTracks=SI_TRACK_COLL_NAME,
        InputOuterTracks=CLU_TRACK_COLL_NAME,
        OutTracks=colls["merge_candidates"],
        Greedy=var["merger"]["greedy"],
        **var["merger"].get("thresholds", {}),
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
