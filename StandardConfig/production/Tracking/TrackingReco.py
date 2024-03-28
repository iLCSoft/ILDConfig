#!/usr/bin/env python3

from Configurables import MarlinProcessorWrapper
from Gaudi.Configuration import INFO

MyClupatraProcessor = MarlinProcessorWrapper("MyClupatraProcessor")
MyClupatraProcessor.OutputLevel = INFO
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
    "OutputCollection": ["ClupatraTracks"],
    "PadRowRange": ["15"],
    "SITHitCollection": ["SITTrackerHits"],
    "SegmentCollectionName": ["ClupatraTrackSegments"],
    "SmoothOn": ["false"],
    "TPCHitCollection": ["TPCTrackerHits"],
    "TrackEndsOuterCentralDist": ["25"],
    "TrackEndsOuterForwardDist": ["40"],
    "TrackIsCurlerOmega": ["0.001"],
    "TrackStartsInnerDist": ["25"],
    "TrackSystemName": ["DDKalTest"],
    "VXDHitCollection": ["VXDTrackerHits"],
    "pickUpSiHits": ["false"],
}

MySiliconTracking_MarlinTrk = MarlinProcessorWrapper("MySiliconTracking_MarlinTrk")
MySiliconTracking_MarlinTrk.OutputLevel = INFO
MySiliconTracking_MarlinTrk.ProcessorType = "SiliconTracking_MarlinTrk"
MySiliconTracking_MarlinTrk.Parameters = {
    "AngleCutForMerging": ["0.1"],
    "AplySimpleUpdatedCoreBin": ["true"],
    "CheckForDelta": ["1"],
    "Chi2FitCut": ["120"],
    "Chi2PrefitCut": ["1e+10"],
    "Chi2WRphiQuartet": ["1"],
    "Chi2WRphiSeptet": ["1"],
    "Chi2WRphiTriplet": ["1"],
    "Chi2WZQuartet": ["0.5"],
    "Chi2WZSeptet": ["0.5"],
    "Chi2WZTriplet": ["0.5"],
    "CutOnD0": ["100"],
    "CutOnPt": ["0.05"],
    "CutOnZ0": ["100"],
    "EnergyLossOn": ["true"],
    "FTDPixelHitCollectionName": ["FTDPixelTrackerHits"],
    "FTDSpacePointCollection": ["FTDSpacePoints"],
    "FastAttachment": ["0"],
    "InitialTrackErrorD0": ["1e+06"],
    "InitialTrackErrorOmega": ["0.0001"],
    "InitialTrackErrorPhi0": ["100"],
    "InitialTrackErrorTanL": ["100"],
    "InitialTrackErrorZ0": ["1e+06"],
    # fmt: off
    "LayerCombinations": [
        "8","6","5",  "8","6","4",  "8","6","3",  "8","6","2",
        "8","5","3",  "8","5","2",  "8","4","3",  "8","4","2",
        "6","5","3",  "6","5","2",  "6","4","3",  "6","4","2",
        "6","3","1",  "6","3","0",  "6","2","1",  "6","2","0",
        "5","3","1",  "5","3","0",  "5","2","1",  "5","2","0",
        "4","3","1",  "4","3","0",  "4","2","1",  "4","2","0",
        "3","2","1",  "3","2","0",  "2","1","0",
    ],
    "LayerCombinationsFTD": [
        "13","11","9",  "13","11","8",  "13","10","9",  "13","10","8",
        "12","11","9",  "12","11","8",  "12","10","9",  "12","10","8",
        "11","9","7",   "11","9","6",   "11","8","7",   "11","8","6",
        "10","9","7",   "10","9","6",   "10","8","7",   "10","8","6",
        "9","7","5",    "9","7","4",    "9","6","5",    "9","6","4",
        "8","7","5",    "8","7","4",    "8","6","5",    "8","6","4",
        "7","5","3",    "7","5","2",    "7","4","3",    "7","4","2",
        "6","5","3",    "6","5","2",    "6","4","3",    "6","4","2",
        "5","3","1",    "5","3","0",    "5","2","1",    "5","2","0",
        "4","3","1",    "4","3","0",    "4","2","1",    "4","2","0",
    ],
    # fmt: on
    "MaxChi2PerHit": ["100"],
    "MaxHitsPerSector": ["100"],
    "MinDistCutAttach": ["2.5"],
    "MinDistToDelta": ["0.25"],
    "MinLayerToAttach": ["-1"],
    "MinimalHits": ["3"],
    "MultipleScatteringOn": ["true"],
    "NDivisionsInPhi": ["80"],
    "NDivisionsInPhiFTD": ["30"],
    "NDivisionsInTheta": ["80"],
    "NHitsChi2": ["5"],
    "RunMarlinTrkDiagnostics": ["false"],
    "SITHitCollectionName": ["SITTrackerHits"],
    "SiTrackCollectionName": ["SiTracks"],
    "SmoothOn": ["false"],
    "TrackSystemName": ["DDKalTest"],
    "UseEventDisplay": ["false"],
    "UseSIT": ["1"],
    "UseSimpleAttachHitToTrack": ["true"],
    "VTXHitCollectionName": ["VXDTrackerHits"],
}

MyForwardTracking = MarlinProcessorWrapper("MyForwardTracking")
MyForwardTracking.OutputLevel = INFO
MyForwardTracking.ProcessorType = "ForwardTracking"
MyForwardTracking.Parameters = {
    "BestSubsetFinder": ["SubsetSimple"],
    "Chi2ProbCut": ["0.0"],
    "Crit2_DeltaPhi_max": ["30", "0.8"],
    "Crit2_DeltaPhi_min": ["0", "0"],
    "Crit2_DeltaRho_max": ["150"],
    "Crit2_DeltaRho_min": ["20"],
    "Crit2_RZRatio_max": ["1.08"],
    "Crit2_RZRatio_min": ["1.002"],
    "Crit2_StraightTrackRatio_max": ["1.02", "1.01"],
    "Crit2_StraightTrackRatio_min": ["0.9", "0.99"],
    "Crit3_3DAngle_max": ["10", "0.35"],
    "Crit3_3DAngle_min": ["0", "0"],
    "Crit3_ChangeRZRatio_max": ["1.015", "1.001"],
    "Crit3_ChangeRZRatio_min": ["0.995", "0.999"],
    "Crit3_IPCircleDist_max": ["20", "1.5"],
    "Crit3_IPCircleDist_min": ["0", "0"],
    "Crit3_PT_max": ["99999999"],
    "Crit3_PT_min": ["0.1"],
    "Crit4_3DAngleChange_max": ["1.3", "1.01"],
    "Crit4_3DAngleChange_min": ["0.8", "0.99"],
    "Crit4_DistToExtrapolation_max": ["1.0", "0.05"],
    "Crit4_DistToExtrapolation_min": ["0", "0"],
    "Criteria": [
        "Crit2_DeltaPhi",
        "Crit2_DeltaRho",
        "Crit2_RZRatio",
        "Crit2_StraightTrackRatio",
        "Crit3_3DAngle",
        "Crit3_ChangeRZRatio",
        "Crit3_IPCircleDist",
        "Crit3_PT",
        "Crit4_DistToExtrapolation",
        "Crit4_3DAngleChange",
    ],
    "EnergyLossOn": ["true"],
    "FTDHitCollections": ["FTDPixelTrackerHits", "FTDSpacePoints"],
    "ForwardTrackCollection": ["ForwardTracks"],
    "HelixFitMax": ["500"],
    "HitsPerTrackMin": ["3"],
    "MaxConnectionsAutomaton": ["100000"],
    "MaxHitsPerSector": ["1000"],
    "MultipleScatteringOn": ["true"],
    "OverlappingHitsDistMax": ["3.5"],
    "SmoothOn": ["false"],
    "TakeBestVersionOfTrack": ["true"],
    "TrackSystemName": ["DDKalTest"],
}

MyTrackSubsetProcessor = MarlinProcessorWrapper("MyTrackSubsetProcessor")
MyTrackSubsetProcessor.OutputLevel = INFO
MyTrackSubsetProcessor.ProcessorType = "TrackSubsetProcessor"
MyTrackSubsetProcessor.Parameters = {
    "EnergyLossOn": ["true"],
    "MultipleScatteringOn": ["true"],
    "Omega": ["0.75"],
    "RemoveShortTracks": ["true"],
    "SmoothOn": ["false"],
    "TrackInputCollections": ["ForwardTracks", "SiTracks"],
    "TrackOutputCollection": ["SubsetTracks"],
    "TrackSystemName": ["DDKalTest"],
}

MyFullLDCTracking_MarlinTrk = MarlinProcessorWrapper("MyFullLDCTracking_MarlinTrk")
MyFullLDCTracking_MarlinTrk.OutputLevel = INFO
MyFullLDCTracking_MarlinTrk.ProcessorType = "FullLDCTracking_MarlinTrk"
MyFullLDCTracking_MarlinTrk.Parameters = {
    "AngleCutForForcedMerging": ["0.05"],
    "AngleCutForMerging": ["0.1"],
    "AssignETDHits": ["0"],
    "AssignFTDHits": ["1"],
    "AssignSETHits": ["1"],
    "AssignSITHits": ["1"],
    "AssignTPCHits": ["0"],
    "AssignVTXHits": ["1"],
    "Chi2FitCut": ["100"],
    "CutOnSiHits": ["4"],
    "CutOnTPCHits": ["10"],
    "CutOnTrackD0": ["500"],
    "CutOnTrackZ0": ["500"],
    "D0CutForForcedMerging": ["50"],
    "D0CutForMerging": ["500"],
    "D0CutToMergeTPCSegments": ["100"],
    "Debug": ["0"],
    "DeltaPCutToMergeTPCSegments": ["0.1"],
    "EnergyLossOn": ["true"],
    "FTDHitToTrackDistance": ["2"],
    "FTDPixelHitCollectionName": ["FTDPixelTrackerHits"],
    "FTDSpacePointCollection": ["FTDSpacePoints"],
    "ForbidOverlapInZComb": ["0"],
    "ForbidOverlapInZTPC": ["0"],
    "ForceSiTPCMerging": ["1"],
    "ForceTPCSegmentsMerging": ["0"],
    "InitialTrackErrorD0": ["1e+06"],
    "InitialTrackErrorOmega": ["0.00001"],
    "InitialTrackErrorPhi0": ["100"],
    "InitialTrackErrorTanL": ["100"],
    "InitialTrackErrorZ0": ["1e+06"],
    "LDCTrackCollection": ["MarlinTrkTracks"],
    "MaxChi2PerHit": ["200"],
    "MinChi2ProbForSiliconTracks": ["0.00001"],
    "MultipleScatteringOn": ["true"],
    "NHitsExtrapolation": ["35"],
    "OmegaCutForForcedMerging": ["0.15"],
    "OmegaCutForMerging": ["0.25"],
    "PtCutToMergeTPCSegments": ["1.2"],
    "RunMarlinTrkDiagnostics": ["false"],
    "SETHitCollection": ["SETSpacePoints"],
    "SETHitToTrackDistance": ["50"],
    "SITHitCollection": ["SITTrackerHits"],
    "SITHitToTrackDistance": ["2"],
    "SiTracks": ["SubsetTracks"],
    "SiTracksMCPRelColl": ["SubsetTracksMCTruthLink"],
    "SmoothOn": ["true"],
    "TPCHitCollection": ["TPCTrackerHits"],
    "TPCHitToTrackDistance": ["15"],
    "TPCTracks": ["ClupatraTracks"],
    "TPCTracksMCPRelColl": ["TPCTracksMCTruthLink"],
    "TrackSystemName": ["DDKalTest"],
    "VTXHitCollection": ["VXDTrackerHits"],
    "VTXHitToTrackDistance": ["1.5"],
    "Z0CutForForcedMerging": ["200"],
    "Z0CutForMerging": ["1000"],
    "Z0CutToMergeTPCSegments": ["5000"],
    "cosThetaCutHighPtMerge": ["0.99"],
    "cosThetaCutSoftHighPtMerge": ["0.998"],
    "hitDistanceCutHighPtMerge": ["25"],
    "maxFractionOfOutliersCutHighPtMerge": ["0.95"],
    "maxHitDistanceCutHighPtMerge": ["50"],
    "momDiffCutHighPtMerge": ["0.01"],
    "momDiffCutSoftHighPtMerge": ["0.25"],
}

MyCompute_dEdxProcessor = MarlinProcessorWrapper("MyCompute_dEdxProcessor")
MyCompute_dEdxProcessor.OutputLevel = INFO
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
MyV0Finder.OutputLevel = INFO
MyV0Finder.ProcessorType = "V0Finder"
MyV0Finder.Parameters = {
    "MassRangeGamma": ["0.01"],
    "MassRangeK0S": ["0.02"],
    "MassRangeL0": ["0.02"],
    "TrackCollection": ["MarlinTrkTracks"],
}

MyKinkFinder = MarlinProcessorWrapper("MyKinkFinder")
MyKinkFinder.OutputLevel = INFO
MyKinkFinder.ProcessorType = "KinkFinder"
MyKinkFinder.Parameters = {
    "DebugPrinting": ["0"],
    "TrackCollection": ["MarlinTrkTracks"],
}

MyRefitProcessorKaon = MarlinProcessorWrapper("MyRefitProcessorKaon")
MyRefitProcessorKaon.OutputLevel = INFO
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
    "ParticleMass": ["0.493677"],
    "TrackSystemName": ["DDKalTest"],
}

MyRefitProcessorProton = MarlinProcessorWrapper("MyRefitProcessorProton")
MyRefitProcessorProton.OutputLevel = INFO
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
    "ParticleMass": ["0.93828"],
    "TrackSystemName": ["DDKalTest"],
}

TrackingRecoSequence = [
    MyClupatraProcessor,
    MySiliconTracking_MarlinTrk,
    # MyForwardTracking,
    MyTrackSubsetProcessor,
    MyFullLDCTracking_MarlinTrk,
    MyCompute_dEdxProcessor,
    MyV0Finder,
    # MyKinkFinder,
    MyRefitProcessorKaon,
    MyRefitProcessorProton,
]
