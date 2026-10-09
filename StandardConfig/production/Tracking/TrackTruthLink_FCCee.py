#!/usr/bin/env python3

# Track-only truth linking for ILD@FCCee, loaded instead of HighLevelReco_FCCee.py when running with --trackingOnly.
# It creates only the track <-> MCParticle links: all cluster/PFO related outputs are switched off,
# since there are no clusters or PFOs without the calorimetry and particle flow.

from Configurables import MarlinProcessorWrapper

_TRACK_TRUTH_LINK_SHARED_PARAMS = {
    "MCParticleCollection": ["MCParticle"],
    "SimTrackerHitCollections": [
        "VertexBarrelCollection",
        "VertexEndcapCollection",
        "InnerTrackerBarrelCollection",
        "InnerTrackerEndcapCollection",
        "TPCCollection",
        "SETCollection",
    ],
    "TrackerHitsRelInputCollections": [
        "VertexBarrelTrackerHitRelations",
        "VertexEndcapTrackerHitRelations",
        "InnerTrackerBarrelHitRelations",
        "InnerTrackerEndcapHitRelations",
        "TPCTrackerHitRelations",
        "SETSpacePointRelations",
    ],
    "UseTrackerHitRelations": ["true"],
    "UsingParticleGun": [str(using_particle_gun).lower()],
    # no clusters/PFOs in tracking-only reco: switch off the corresponding outputs
    "RecoMCTruthLinkName": [""],
    "MCTruthRecoLinkName": [""],
    "MCParticlesSkimmedName": [""],
    "ClusterMCTruthLinkName": [""],
    "MCTruthClusterLinkName": [""],
    "CalohitMCTruthLinkName": [""],
}

# Track collections to truth-link: same as in HighLevelReco_FCCee.py
TRACK_TRUTH_LINK_COLLECTIONS = [
    "MarlinTrkTracks",
    "SiTracksCT",
    "ClupatraTracks",
    "ClupatraSitTracks",
    "ClupatraSitSetTracks",
]
if track_merging:
    TRACK_TRUTH_LINK_COLLECTIONS += [
        "RefittedGreedyMergedTracks",
        "RefittedAmbiguousMergedTracks",
    ]

TrackTruthLinkers = []
for track_collection in TRACK_TRUTH_LINK_COLLECTIONS:
    linker = MarlinProcessorWrapper(f"MyRecoMCTruthLinker{track_collection}")
    linker.ProcessorType = "RecoMCTruthLinker"
    linker.Parameters = _TRACK_TRUTH_LINK_SHARED_PARAMS | {
        "TrackCollection": [track_collection],
        "TrackMCTruthLinkName": [f"{track_collection}MCTruthLink"],
        "MCTruthTrackLinkName": [f"MCTruth{track_collection}Link"],
    }
    TrackTruthLinkers.append(linker)

TrackTruthLink_FCCeeSequence = [
    *TrackTruthLinkers,
]
