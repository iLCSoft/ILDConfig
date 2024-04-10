#!/usr/bin/env python3

from Configurables import MarlinProcessorWrapper
from Gaudi.Configuration import INFO

MySplitCollectionByLayer = MarlinProcessorWrapper("MySplitCollectionByLayer")
MySplitCollectionByLayer.OutputLevel = INFO
MySplitCollectionByLayer.ProcessorType = "SplitCollectionByLayer"
MySplitCollectionByLayer.Parameters = {
    "InputCollection": ["FTDCollection"],
    "OutputCollections": [
        "FTD_PIXELCollection",
        "0",
        "1",
        "FTD_STRIPCollection",
        "2",
        "6",
    ],
}

VXDPlanarDigiProcessor_CMOSVXD5 = MarlinProcessorWrapper(
    "VXDPlanarDigiProcessor_CMOSVXD5"
)
VXDPlanarDigiProcessor_CMOSVXD5.OutputLevel = INFO
VXDPlanarDigiProcessor_CMOSVXD5.ProcessorType = "DDPlanarDigiProcessor"
VXDPlanarDigiProcessor_CMOSVXD5.Parameters = {
    "ForceHitsOntoSurface": ["true"],
    "IsStrip": ["false"],
    "ResolutionU": ["0.003", "0.003", "0.003", "0.003", "0.003", "0.003"],
    "ResolutionV": ["0.003", "0.003", "0.003", "0.003", "0.003", "0.003"],
    "SimTrackHitCollectionName": ["VXDCollection"],
    "SimTrkHitRelCollection": ["VXDTrackerHitRelations"],
    "SubDetectorName": ["VXD"],
    "TrackerHitCollectionName": ["VXDTrackerHits"],
}

SITPlanarDigiProcessor = MarlinProcessorWrapper("SITPlanarDigiProcessor")
SITPlanarDigiProcessor.OutputLevel = INFO
SITPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
SITPlanarDigiProcessor.Parameters = {
    "ForceHitsOntoSurface": ["true"],
    "IsStrip": ["false"],
    "ResolutionU": ["0.005"],
    "ResolutionV": ["0.005"],
    "SimTrackHitCollectionName": ["SITCollection"],
    "SimTrkHitRelCollection": ["SITTrackerHitRelations"],
    "SubDetectorName": ["SIT"],
    "TrackerHitCollectionName": ["SITTrackerHits"],
}

FTDPixelPlanarDigiProcessor = MarlinProcessorWrapper("FTDPixelPlanarDigiProcessor")
FTDPixelPlanarDigiProcessor.OutputLevel = INFO
FTDPixelPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
FTDPixelPlanarDigiProcessor.Parameters = {
    "ForceHitsOntoSurface": ["true"],
    "IsStrip": ["false"],
    "ResolutionU": ["0.003"],
    "ResolutionV": ["0.003"],
    "SimTrackHitCollectionName": ["FTD_PIXELCollection"],
    "SimTrkHitRelCollection": ["FTDPixelTrackerHitRelations"],
    "SubDetectorName": ["FTD"],
    "TrackerHitCollectionName": ["FTDPixelTrackerHits"],
}

FTDStripPlanarDigiProcessor = MarlinProcessorWrapper("FTDStripPlanarDigiProcessor")
FTDStripPlanarDigiProcessor.OutputLevel = INFO
FTDStripPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
FTDStripPlanarDigiProcessor.Parameters = {
    "ForceHitsOntoSurface": ["true"],
    "IsStrip": ["true"],
    "ResolutionU": ["0.007"],
    "ResolutionV": ["0.0"],
    "SimTrackHitCollectionName": ["FTD_STRIPCollection"],
    "SimTrkHitRelCollection": ["FTDStripTrackerHitRelations"],
    "SubDetectorName": ["FTD"],
    "TrackerHitCollectionName": ["FTDStripTrackerHits"],
}

FTDDDSpacePointBuilder = MarlinProcessorWrapper("FTDDDSpacePointBuilder")
FTDDDSpacePointBuilder.OutputLevel = INFO
FTDDDSpacePointBuilder.ProcessorType = "DDSpacePointBuilder"
FTDDDSpacePointBuilder.Parameters = {
    "SimHitSpacePointRelCollection": ["FTDSpacePointRelations"],
    "SpacePointsCollection": ["FTDSpacePoints"],
    "StripLength": ["2.500000000e+02"],
    "SubDetectorName": ["FTD"],
    "TrackerHitCollection": ["FTDStripTrackerHits"],
    "TrackerHitSimHitRelCollection": ["FTDStripTrackerHitRelations"],
}

SETPlanarDigiProcessor = MarlinProcessorWrapper("SETPlanarDigiProcessor")
SETPlanarDigiProcessor.OutputLevel = INFO
SETPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
SETPlanarDigiProcessor.Parameters = {
    "ForceHitsOntoSurface": ["true"],
    "IsStrip": ["true"],
    "ResolutionU": ["0.007"],
    "ResolutionV": ["0"],
    "SimTrackHitCollectionName": ["SETCollection"],
    "SimTrkHitRelCollection": ["SETTrackerHitRelations"],
    "SubDetectorName": ["SET"],
    "TrackerHitCollectionName": ["SETTrackerHits"],
}

SETDDSpacePointBuilder = MarlinProcessorWrapper("SETDDSpacePointBuilder")
SETDDSpacePointBuilder.OutputLevel = INFO
SETDDSpacePointBuilder.ProcessorType = "DDSpacePointBuilder"
SETDDSpacePointBuilder.Parameters = {
    "SimHitSpacePointRelCollection": ["SETSpacePointRelations"],
    "SpacePointsCollection": ["SETSpacePoints"],
    "StripLength": ["9.200000000e+01"],
    "SubDetectorName": ["SET"],
    "TrackerHitCollection": ["SETTrackerHits"],
    "TrackerHitSimHitRelCollection": ["SETTrackerHitRelations"],
}

MyTPCDigiProcessor = MarlinProcessorWrapper("MyTPCDigiProcessor")
MyTPCDigiProcessor.OutputLevel = INFO
MyTPCDigiProcessor.ProcessorType = "DDTPCDigiProcessor"
MyTPCDigiProcessor.Parameters = {
    "DiffusionCoeffRPhi": ["0.025"],
    "DiffusionCoeffZ": ["0.08"],
    "DoubleHitResolutionRPhi": ["2"],
    "DoubleHitResolutionZ": ["5"],
    "HitSortingBinningRPhi": ["2"],
    "HitSortingBinningZ": ["5"],
    "MaxClusterSizeForMerge": ["3"],
    "N_eff": ["22"],
    "PointResolutionPadPhi": ["0.9"],
    "PointResolutionRPhi": ["0.05"],
    "PointResolutionZ": ["0.4"],
    "RejectCellID0": ["1"],
    "SimTrkHitRelCollection": ["TPCTrackerHitRelations"],
    "TPCEndPlateModuleGapPhi": ["1."],
    "TPCEndPlateModuleGapR": ["1."],
    "TPCEndPlateModuleNumbers": ["14", "18", "23", "28", "32", "37", "42", "46"],
    "TPCEndPlateModulePhi0s": [
        "0",
        "0.17453292519943298",
        "0.030350516853376176",
        "0.2108457469509264",
        "0.11998920441304516",
        "0.1600004647682326",
        "0.02051011203843622",
        "0.062176216344090166",
    ],
    "TPCLowPtCollectionName": ["TPCLowPtCollection"],
    "TPCPadRowHitCollectionName": ["TPCCollection"],
    "TPCSpacePointCollectionName": ["TPCSpacePointCollection"],
    "TPCTrackerHitsCol": ["TPCTrackerHits"],
}

TrackingDigiSequence = [
    MySplitCollectionByLayer,
    VXDPlanarDigiProcessor_CMOSVXD5,
    SITPlanarDigiProcessor,
    FTDPixelPlanarDigiProcessor,
    FTDStripPlanarDigiProcessor,
    FTDDDSpacePointBuilder,
    SETPlanarDigiProcessor,
    SETDDSpacePointBuilder,
    MyTPCDigiProcessor,
]
