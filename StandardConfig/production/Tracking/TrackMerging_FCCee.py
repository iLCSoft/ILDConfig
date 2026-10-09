#!/usr/bin/env python3

from Configurables import MarlinProcessorWrapper, TrackMerger
from Gaudi.Configuration import INFO  # , DEBUG

# ---------------------------------------------------------------------------
# Track collection names
# ---------------------------------------------------------------------------

SI_TRACK_COLL_NAME = "SiTracksCT"
CLU_TRACK_COLL_NAME = "ClupatraTracks"
CLU_W_SI_TRACK_COLL_NAME = "ClupatraSitSetTracks"
MCP_COLL_NAME = "MCParticles"

# ---------------------------------------------------------------------------
# Track variations
# Each entry has:
#   "collections": input/output collection names
#   "merger":      merger-specific settings (None = no merger step)
#   "refitter":    refitter-specific settings
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# TrackMerger matching criteria
#
# TrackMerger considers two tracks a match if their track parameters at the
# adjoining hit are compatible for each of the 5 parameters. A negative cut
# disables that parameter, i.e. it is not considered for matching.
# UseSignificance selects which set of cuts is applied:
#   True:  significances |diff| / sqrt(var(inner) + var(outer)) from the
#          track state covariances; omega is compared as signed pT, which
#          needs the B field from the GeoSvc. Properties:
#          D0Significance, Z0Significance, PhiSignificance, PtSignificance,
#          TanLambdaSignificance
#   False: absolute differences. Properties:
#          D0Tolerance, Z0Tolerance, PhiTolerance, OmegaTolerance,
#          TanLambdaTolerance
# ---------------------------------------------------------------------------

SIGNIFICANCE_THRESHOLDS = {
    "UseSignificance": True,
    "D0Significance": 3.0,
    "Z0Significance": 3.0,
    "PhiSignificance": 3.0,
    "PtSignificance": 3.0,
    "TanLambdaSignificance": 3.0,
}

ABSOLUTE_THRESHOLDS = {
    "UseSignificance": False,
    "D0Tolerance": 0.5,  # mm
    "Z0Tolerance": 2.5,  # mm
    "PhiTolerance": -1.0,
    "OmegaTolerance": -1.0,
    "TanLambdaTolerance": -1.0,
}

DEFAULT_THRESHOLDS = SIGNIFICANCE_THRESHOLDS

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
            "thresholds": DEFAULT_THRESHOLDS,
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
            "thresholds": DEFAULT_THRESHOLDS,
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
    "FitDirection": ["-1"],  # backward fit for a good IP track state
    "InitialTrackErrorD0": ["1e+06"],
    "InitialTrackErrorOmega": ["0.00001"],
    "InitialTrackErrorPhi0": ["100"],
    "InitialTrackErrorTanL": ["100"],
    "InitialTrackErrorZ0": ["1e+06"],
    "InitialTrackState": ["3"],  # lcio::TrackState::AtLastHit
    "SkipFailedFits": ["true"],
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
