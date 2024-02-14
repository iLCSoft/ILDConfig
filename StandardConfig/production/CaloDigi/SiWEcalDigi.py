#!/usr/bin/env python3

from Gaudi.Configuration import INFO
from Configurables import MarlinProcessorWrapper

MergeCollectionsEcalBarrelHits = MarlinProcessorWrapper(
    "MergeCollectionsEcalBarrelHits"
)
MergeCollectionsEcalBarrelHits.OutputLevel = INFO
MergeCollectionsEcalBarrelHits.ProcessorType = "MergeCollections"
MergeCollectionsEcalBarrelHits.Parameters = {
    "InputCollections": ["ECalBarrelSiHitsEven", "ECalBarrelSiHitsOdd"],
    "OutputCollection": ["EcalBarrelCollection"],
}

MergeCollectionsEcalEndcapHits = MarlinProcessorWrapper(
    "MergeCollectionsEcalEndcapHits"
)
MergeCollectionsEcalEndcapHits.OutputLevel = INFO
MergeCollectionsEcalEndcapHits.ProcessorType = "MergeCollections"
MergeCollectionsEcalEndcapHits.Parameters = {
    "InputCollections": ["ECalEndcapSiHitsEven", "ECalEndcapSiHitsOdd"],
    "OutputCollection": ["EcalEndcapsCollection"],
}

MyEcalBarrelDigi = MarlinProcessorWrapper("MyEcalBarrelDigi")
MyEcalBarrelDigi.OutputLevel = INFO
MyEcalBarrelDigi.ProcessorType = "RealisticCaloDigiSilicon"
MyEcalBarrelDigi.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_mip": ["%(EcalBarrelMip)s" % CONSTANTS],
    "inputHitCollections": ["EcalBarrelCollection"],
    "outputHitCollections": ["EcalBarrelCollectionDigi"],
    "outputRelationCollections": ["EcalBarrelRelationsSimDigi"],
    "threshold": ["0.5"],
    "timingCut": ["1"],
}

MyEcalBarrelReco = MarlinProcessorWrapper("MyEcalBarrelReco")
MyEcalBarrelReco.OutputLevel = INFO
MyEcalBarrelReco.ProcessorType = "RealisticCaloRecoSilicon"
MyEcalBarrelReco.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_factorsMipGev": ["%(EcalBarrelEnergyFactors)s" % CONSTANTS],
    "calibration_layergroups": ["20", "11"],
    "inputHitCollections": ["EcalBarrelCollectionDigi"],
    "inputRelationCollections": ["EcalBarrelRelationsSimDigi"],
    "outputHitCollections": ["EcalBarrelCollectionRec"],
    "outputRelationCollections": ["EcalBarrelRelationsSimRec"],
}

MyEcalBarrelGapFiller = MarlinProcessorWrapper("MyEcalBarrelGapFiller")
MyEcalBarrelGapFiller.OutputLevel = INFO
MyEcalBarrelGapFiller.ProcessorType = "BruteForceEcalGapFiller"
MyEcalBarrelGapFiller.Parameters = {
    "CellIDLayerString": ["layer"],
    "CellIDModuleString": ["module"],
    "CellIDStaveString": ["stave"],
    "applyInterModuleCorrection": ["false"],
    "expectedInterModuleDistance": ["7.0"],
    "inputHitCollection": ["EcalBarrelCollectionRec"],
    "outputHitCollection": ["EcalBarrelCollectionGapHits"],
}

MyEcalEndcapDigi = MarlinProcessorWrapper("MyEcalEndcapDigi")
MyEcalEndcapDigi.OutputLevel = INFO
MyEcalEndcapDigi.ProcessorType = "RealisticCaloDigiSilicon"
MyEcalEndcapDigi.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_mip": ["%(EcalEndcapMip)s" % CONSTANTS],
    "inputHitCollections": ["EcalEndcapsCollection"],
    "outputHitCollections": ["EcalEndcapsCollectionDigi"],
    "outputRelationCollections": ["EcalEndcapsRelationsSimDigi"],
    "threshold": ["0.5"],
    "timingCut": ["1"],
}

MyEcalEndcapReco = MarlinProcessorWrapper("MyEcalEndcapReco")
MyEcalEndcapReco.OutputLevel = INFO
MyEcalEndcapReco.ProcessorType = "RealisticCaloRecoSilicon"
MyEcalEndcapReco.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_factorsMipGev": ["%(EcalEndcapEnergyFactors)s" % CONSTANTS],
    "calibration_layergroups": ["20", "11"],
    "inputHitCollections": ["EcalEndcapsCollectionDigi"],
    "inputRelationCollections": ["EcalEndcapsRelationsSimDigi"],
    "outputHitCollections": ["EcalEndcapsCollectionRec"],
    "outputRelationCollections": ["EcalEndcapsRelationsSimRec"],
}

MyEcalEndcapGapFiller = MarlinProcessorWrapper("MyEcalEndcapGapFiller")
MyEcalEndcapGapFiller.OutputLevel = INFO
MyEcalEndcapGapFiller.ProcessorType = "BruteForceEcalGapFiller"
MyEcalEndcapGapFiller.Parameters = {
    "CellIDLayerString": ["layer"],
    "CellIDModuleString": ["module"],
    "CellIDStaveString": ["stave"],
    "applyInterModuleCorrection": ["false"],
    "expectedInterModuleDistance": ["7.0"],
    "inputHitCollection": ["EcalEndcapsCollectionRec"],
    "outputHitCollection": ["EcalEndcapsCollectionGapHits"],
}

MyEcalRingDigi = MarlinProcessorWrapper("MyEcalRingDigi")
MyEcalRingDigi.OutputLevel = INFO
MyEcalRingDigi.ProcessorType = "RealisticCaloDigiSilicon"
MyEcalRingDigi.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_mip": ["%(EcalRingMip)s" % CONSTANTS],
    "inputHitCollections": ["EcalEndcapRingCollection"],
    "outputHitCollections": ["EcalEndcapRingCollectionDigi"],
    "outputRelationCollections": ["EcalEndcapRingRelationsSimDigi"],
    "threshold": ["0.5"],
    "timingCut": ["1"],
}

MyEcalRingReco = MarlinProcessorWrapper("MyEcalRingReco")
MyEcalRingReco.OutputLevel = INFO
MyEcalRingReco.ProcessorType = "RealisticCaloRecoSilicon"
MyEcalRingReco.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_factorsMipGev": ["%(EcalRingEnergyFactors)s" % CONSTANTS],
    "calibration_layergroups": ["20", "11"],
    "inputHitCollections": ["EcalEndcapRingCollectionDigi"],
    "inputRelationCollections": ["EcalEndcapRingRelationsSimDigi"],
    "outputHitCollections": ["EcalEndcapRingCollectionRec"],
    "outputRelationCollections": ["EcalEndcapRingRelationsSimRec"],
}


EcalDigiSequence = [
    MergeCollectionsEcalBarrelHits,
    MergeCollectionsEcalEndcapHits,
    MyEcalBarrelDigi,
    MyEcalBarrelReco,
    MyEcalBarrelGapFiller,
    MyEcalEndcapDigi,
    MyEcalEndcapReco,
    MyEcalEndcapGapFiller,
    MyEcalRingDigi,
    MyEcalRingReco,
]
