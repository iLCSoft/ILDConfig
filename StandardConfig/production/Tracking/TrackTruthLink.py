#!/usr/bin/env python3

# Track-only truth linking for ILD@ILC, loaded instead of HighLevelReco.py when running with --trackingOnly.
# It creates only the track <-> MCParticle links: all cluster/PFO related outputs are switched off,
# since there are no clusters or PFOs without the calorimetry and particle flow.

from Configurables import MarlinProcessorWrapper

MyRecoMCTruthLinker = MarlinProcessorWrapper("MyRecoMCTruthLinker")
MyRecoMCTruthLinker.ProcessorType = "RecoMCTruthLinker"
MyRecoMCTruthLinker.Parameters = {
    "MCParticleCollection": ["MCParticle"],
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
    "MCTruthTrackLinkName": ["MCTruthMarlinTrkTracksLink"],
    "TrackerHitsRelInputCollections": [
        "VXDTrackerHitRelations",
        "SITTrackerHitRelations",
        "FTDPixelTrackerHitRelations",
        "FTDSpacePointRelations",
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

TrackTruthLinkSequence = [
    MyRecoMCTruthLinker,
]
