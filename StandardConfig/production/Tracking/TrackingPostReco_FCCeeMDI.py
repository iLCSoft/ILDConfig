#!/usr/bin/env python3

# Processors that need the final, refitted tracks (MarlinTrkTracks),
# so they run after TrackMerging_FCCee.py, where MarlinTrkTracks is created

from Configurables import MarlinProcessorWrapper

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
    "SkipFailedFits": ["false"],  # keep failed fits so that the output stays index-aligned with MarlinTrkTracks
    "ParticleMass": ["0.493677"],
    "TrackSystemName": ["DDKalTest"],
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
    "SkipFailedFits": ["false"],  # keep failed fits so that the output stays index-aligned with MarlinTrkTracks
    "ParticleMass": ["0.93828"],
    "TrackSystemName": ["DDKalTest"],
}


TrackingPostReco_FCCeeMDISequence = [
    MyCompute_dEdxProcessor,
    MyV0Finder,
    # MyKinkFinder,
    MyRefitProcessorKaon,
    MyRefitProcessorProton,
]
