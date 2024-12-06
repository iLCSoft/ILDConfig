#!/usr/bin/env python3

from Configurables import MarlinProcessorWrapper

MergeCollectionsEcalBarrelHits = MarlinProcessorWrapper(
    "MergeCollectionsEcalBarrelHits"
)
MergeCollectionsEcalBarrelHits.ProcessorType = "MergeCollections"
MergeCollectionsEcalBarrelHits.Parameters = {
    "InputCollections": ["ECalBarrelSiHitsEven", "ECalBarrelSiHitsOdd"],
    "OutputCollection": ["EcalBarrelCollection"],
}

MergeCollectionsEcalEndcapHits = MarlinProcessorWrapper(
    "MergeCollectionsEcalEndcapHits"
)
MergeCollectionsEcalEndcapHits.ProcessorType = "MergeCollections"
MergeCollectionsEcalEndcapHits.Parameters = {
    "InputCollections": ["ECalEndcapSiHitsEven", "ECalEndcapSiHitsOdd"],
    "OutputCollection": ["EcalEndcapsCollection"],
}

MyEcalBarrelDigi = MarlinProcessorWrapper("MyEcalBarrelDigi")
MyEcalBarrelDigi.ProcessorType = "RealisticCaloDigiSilicon"
MyEcalBarrelDigi.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_mip": [CONSTANTS["EcalBarrelMip"]],
    "inputHitCollections": ["EcalBarrelCollection"],
    "outputHitCollections": ["EcalBarrelCollectionDigi"],
    "outputRelationCollections": ["EcalBarrelRelationsSimDigi"],
    "threshold": ["0.5"],
    "timingCut": ["1"],
}

MyEcalBarrelReco = MarlinProcessorWrapper("MyEcalBarrelReco")
MyEcalBarrelReco.ProcessorType = "RealisticCaloRecoSilicon"
MyEcalBarrelReco.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_factorsMipGev": [CONSTANTS["EcalBarrelEnergyFactors"]],
    "calibration_layergroups": ["20", "11"],
    "inputHitCollections": ["EcalBarrelCollectionDigi"],
    "inputRelationCollections": ["EcalBarrelRelationsSimDigi"],
    "outputHitCollections": ["EcalBarrelCollectionRec"],
    "outputRelationCollections": ["EcalBarrelRelationsSimRec"],
}

MyEcalBarrelGapFiller = MarlinProcessorWrapper("MyEcalBarrelGapFiller")
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
MyEcalEndcapDigi.ProcessorType = "RealisticCaloDigiSilicon"
MyEcalEndcapDigi.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_mip": [CONSTANTS["EcalEndcapMip"]],
    "inputHitCollections": ["EcalEndcapsCollection"],
    "outputHitCollections": ["EcalEndcapsCollectionDigi"],
    "outputRelationCollections": ["EcalEndcapsRelationsSimDigi"],
    "threshold": ["0.5"],
    "timingCut": ["1"],
}

MyEcalEndcapReco = MarlinProcessorWrapper("MyEcalEndcapReco")
MyEcalEndcapReco.ProcessorType = "RealisticCaloRecoSilicon"
MyEcalEndcapReco.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_factorsMipGev": [CONSTANTS["EcalEndcapEnergyFactors"]],
    "calibration_layergroups": ["20", "11"],
    "inputHitCollections": ["EcalEndcapsCollectionDigi"],
    "inputRelationCollections": ["EcalEndcapsRelationsSimDigi"],
    "outputHitCollections": ["EcalEndcapsCollectionRec"],
    "outputRelationCollections": ["EcalEndcapsRelationsSimRec"],
}

MyEcalEndcapGapFiller = MarlinProcessorWrapper("MyEcalEndcapGapFiller")
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
MyEcalRingDigi.ProcessorType = "RealisticCaloDigiSilicon"
MyEcalRingDigi.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_mip": [CONSTANTS["EcalRingMip"]],
    "inputHitCollections": ["EcalEndcapRingCollection"],
    "outputHitCollections": ["EcalEndcapRingCollectionDigi"],
    "outputRelationCollections": ["EcalEndcapRingRelationsSimDigi"],
    "threshold": ["0.5"],
    "timingCut": ["1"],
}

MyEcalRingReco = MarlinProcessorWrapper("MyEcalRingReco")
MyEcalRingReco.ProcessorType = "RealisticCaloRecoSilicon"
MyEcalRingReco.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_factorsMipGev": [CONSTANTS["EcalRingEnergyFactors"]],
    "calibration_layergroups": ["20", "11"],
    "inputHitCollections": ["EcalEndcapRingCollectionDigi"],
    "inputRelationCollections": ["EcalEndcapRingRelationsSimDigi"],
    "outputHitCollections": ["EcalEndcapRingCollectionRec"],
    "outputRelationCollections": ["EcalEndcapRingRelationsSimRec"],
}


SiWEcalDigiSequence = [
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
