#!/usr/bin/env python3

from Configurables import MarlinProcessorWrapper, TrackMerger
from py_utils import encode_CT_steps_dict_to_legacy_list

# some values used in conformal tracking:
CT_MAX_DIST = "0.05"  # COPYIED FROM CLDRECO, valid for vertex detector with first layer close to IP (like in CLD_o2)
MCPartColName = ["MCParticle"]  # MCParticleCollectionName
VertexBarrelHitCollectionNames = ["VertexBarrelTrackerHits"]
VertexEndcapHitCollectionNames = ["VertexEndcapTrackerHits"]

MyClupatraProcessor = MarlinProcessorWrapper("MyClupatraProcessor")
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
    "OutputCollection": ["ClupatraSETTracks"],
    "PadRowRange": ["15"],
    #"SITHitCollection": ["InnerTrackerBarrelHits"],
    #"SITDetectorName": ["InnerTrackerBarrel"],
    "SegmentCollectionName": ["MarlinTrkTrackSegments"],
    "SmoothOn": ["false"],
    "TPCHitCollection": ["TPCTrackerHits"],
    "TrackEndsOuterCentralDist": ["25"],
    "TrackEndsOuterForwardDist": ["40"],
    "TrackIsCurlerOmega": ["0.001"],
    "TrackStartsInnerDist": ["25"],
    "TrackSystemName": ["DDKalTest"],
    #"VXDHitCollection": VertexBarrelHitCollectionNames,
    #"VXDDetectorName": ["VertexBarrel"],
    "pickUpSiHits": ["true"],
}

MyConformalTracking = MarlinProcessorWrapper("MyConformalTracking")
MyConformalTracking.ProcessorType = "ConformalTrackingV2"
conformal_tracking_steps_config = {
    # Based on CLD's Reconstruction in CLDConfig
    "Vertex": {
        "collections": ["VertexBarrelTrackerHits"],
        "params": {
            "MaxCellAngle": 0.01,
            "MaxCellAngleRZ": 0.01,
            "Chi2Cut": 100,
            "MinClustersOnTrack": 4,
            "MaxDistance": CT_MAX_DIST,
            "SlopeZRange": 10.0,
            "HighPTCut": 10.0,
        },
        "flags": ["HighPTFit", "VertexToTracker"],
        "functions": ["CombineCollections", "BuildNewTracks"],
    },
    "Vertex": {
        "collections": ["VertexEndcapTrackerHits"],
        "params": {
            "MaxCellAngle": 0.01,
            "MaxCellAngleRZ": 0.01,
            "Chi2Cut": 100,
            "MinClustersOnTrack": 4,
            "MaxDistance": CT_MAX_DIST,
            "SlopeZRange": 10.0,
            "HighPTCut": 10.0,
        },
        "flags": ["HighPTFit", "VertexToTracker"],
        "functions": ["CombineCollections", "ExtendTracks"],
    },
    # Second pass (likely "inclusive seeding"): Based on the looser MaxCellAngle (0.05)
    # and combined collections, this step presumably aims to recover lower-pT
    # or transition-region tracks from hits not consumed in previous steps.
    # Note: This logic is inferred from parameters and has not been verified in the source code.
    "LowerCellAngle1": {
        "collections": VertexBarrelHitCollectionNames + VertexEndcapHitCollectionNames,
        "params": {
            "MaxCellAngle": 0.05,
            "MaxCellAngleRZ": 0.05,
            "Chi2Cut": 100,
            "MinClustersOnTrack": 4,
            "MaxDistance": CT_MAX_DIST,
            "SlopeZRange": 10.0,
            "HighPTCut": 10.0,
        },
        "flags": ["HighPTFit", "VertexToTracker", "RadialSearch"],
        "functions": ["CombineCollections", "BuildNewTracks"],
    },
    "LowerCellAngle2": {
        "collections": [""],
        "params": {
            "MaxCellAngle": 0.1,
            "MaxCellAngleRZ": 0.1,
            "Chi2Cut": 2000,
            "MinClustersOnTrack": 4,
            "MaxDistance": CT_MAX_DIST,
            "SlopeZRange": 10.0,
            "HighPTCut": 10.0,
        },
        "flags": ["HighPTFit", "VertexToTracker", "RadialSearch"],
        "functions": ["BuildNewTracks", "SortTracks"],
    },
    "Tracker": {
        "collections": ["InnerTrackerBarrelHits", "InnerTrackerEndcapHits"],
        "params": {
            "MaxCellAngle": 0.1,
            "MaxCellAngleRZ": 0.1,
            "Chi2Cut": 2000,
            "MinClustersOnTrack": 4,
            "MaxDistance": CT_MAX_DIST,
            "SlopeZRange": 10.0,
            "HighPTCut": 1.0,
        },
        "flags": ["HighPTFit", "VertexToTracker", "RadialSearch"],
        "functions": ["CombineCollections", "ExtendTracks"],
    },
}
MyConformalTracking.Parameters = {
    "DebugHits": ["DebugHits"],
    "DebugPlots": ["false"],
    "DebugTiming": ["false"],
    "MCParticleCollectionName": MCPartColName,
    "MaxHitInvertedFit": ["0"],
    "MinClustersOnTrackAfterFit": ["3"],
    "RelationsNames": [
        "VertexBarrelTrackerHitRelations",
        "VertexEndcapTrackerHitRelations",
        "InnerTrackerBarrelHitRelations",
        "InnerTrackerEndcapHitRelations",
    ],
    "RetryTooManyTracks": ["false"],
    "SiTrackCollectionName": ["SiTracksCT"],
    "SortTreeResults": ["true"],
    "Steps": encode_CT_steps_dict_to_legacy_list(conformal_tracking_steps_config),
    "ThetaRange": ["0.05"],
    "TooManyTracks": ["100000"],
    "TrackerHitCollectionNames": [
        "InnerTrackerBarrelHits",
        "InnerTrackerEndcapHits",
    ]
    + VertexBarrelHitCollectionNames
    + VertexEndcapHitCollectionNames,
    "trackPurity": ["0.7"],
    "VertexBarrelHitCollectionNames": VertexBarrelHitCollectionNames,
    "VertexEndcapHitCollectionNames": VertexEndcapHitCollectionNames,
}

MatchingThresholds = {
    "D0Tolerance": -1.0, # 0.5
    "Z0Tolerance": -1.0, # 2.5
    "PhiTolerance": -1.0,
    "OmegaTolerance": -1.0,
    "TanLambdaTolerance": -1.0,
    "D0Significance": 10.0, # 3.0
    "Z0Significance": 15.0, # 3.0
    "PhiSignificance": 100.0,
    "PtSignificance": -1.0,
    "TanLambdaSignificance": 100.0,
}
MyTrackMerger = TrackMerger("TrackMerger",
    InputInnerTracks="SiTracksCT",
    InputOuterTracks="ClupatraSETTracks",
    OutTracks="MergedTracks",
    **MatchingThresholds,
    UseSignificance = True,
    maxChi2PerHit = 100,
)

MyRefitter = MarlinProcessorWrapper("Refitter")
MyRefitter.ProcessorType = "RefitProcessor"
MyRefitter.Parameters = {
    "EnergyLossOn": ["true"],
    "FitDirection": ["-1"],
    "InitialTrackErrorD0": ["1e+06"],
    "InitialTrackErrorOmega": ["0.00001"],
    "InitialTrackErrorPhi0": ["100"],
    "InitialTrackErrorTanL": ["100"],
    "InitialTrackErrorZ0": ["1e+06"],
    "InitialTrackState": ["3"],
    "TrackSystemName": ["DDKalTest"],
    "InputTrackCollectionName": ["MergedTracks"],
    "InputTrackRelCollection": [],
    "OutputTrackCollectionName": ["MarlinTrkTracks"],
    "OutputTrackRelCollection": ["MarlinTrkTrackRelation"],
    "SkipFailedFits": ["true"],
    #"Verbosity": ["DEBUG"],
}

MyCompute_dEdxProcessor = MarlinProcessorWrapper("MyCompute_dEdxProcessor")
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
    "smearingFactor": [CONSTANTS["dEdXSmearingFactor"]],
}

MyV0Finder = MarlinProcessorWrapper("MyV0Finder")
MyV0Finder.ProcessorType = "V0Finder"
MyV0Finder.Parameters = {
    "MassRangeGamma": ["0.01"],
    "MassRangeK0S": ["0.02"],
    "MassRangeL0": ["0.02"],
    "TrackCollection": ["MarlinTrkTracks"],
}

MyKinkFinder = MarlinProcessorWrapper("MyKinkFinder")
MyKinkFinder.ProcessorType = "KinkFinder"
MyKinkFinder.Parameters = {
    "DebugPrinting": ["0"],
    "TrackCollection": ["MarlinTrkTracks"],
    "VXDName" : ["VertexBarrel"],
    "SITName" : ["InnerTrackerBarrel"],
}

MyRefitProcessorKaon = MarlinProcessorWrapper("MyRefitProcessorKaon")
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
    "SkipFailedFits": [
        "false"
    ],  # keep failed fits so that the output stays index-aligned with MarlinTrkTracks
    "ParticleMass": ["0.493677"],
    "TrackSystemName": ["DDKalTest"],
    #"Verbosity": ["DEBUG"],
}

MyRefitProcessorProton = MarlinProcessorWrapper("MyRefitProcessorProton")
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
    "SkipFailedFits": [
        "false"
    ],  # keep failed fits so that the output stays index-aligned with MarlinTrkTracks
    "ParticleMass": ["0.93828"],
    "TrackSystemName": ["DDKalTest"],
}


TrackingReco_FCCeeMDISequence = [
    MyClupatraProcessor,
    MyConformalTracking,
    MyTrackMerger,
    MyRefitter,
    MyCompute_dEdxProcessor,
    MyV0Finder,
    MyKinkFinder,
    MyRefitProcessorKaon,
    MyRefitProcessorProton,
]
