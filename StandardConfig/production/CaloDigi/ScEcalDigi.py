#!/usr/bin/env python3

from Configurables import MarlinProcessorWrapper

MyEcalBarrelDigiEven = MarlinProcessorWrapper("MyEcalBarrelDigiEven")
MyEcalBarrelDigiEven.ProcessorType = "RealisticCaloDigiScinPpd"
MyEcalBarrelDigiEven.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_mip": [CONSTANTS["EcalBarrelMip"]],
    "inputHitCollections": ["ECalBarrelScHitsEven"],
    "outputHitCollections": ["ECalBarrelScHitsEvenDigi"],
    "outputRelationCollections": ["ECalBarrelScHitsEvenDigiRelations"],
    "ppd_mipPe": ["10"],
    "ppd_npix": ["10000"],
    "ppd_npix_uncert": ["0"],
    "ppd_pix_spread": ["0"],
    "threshold": ["0.5"],
    "thresholdUnit": ["MIP"],
    "timingCut": ["1"],
}

MyEcalBarrelDigiOdd = MarlinProcessorWrapper("MyEcalBarrelDigiOdd")
MyEcalBarrelDigiOdd.ProcessorType = "RealisticCaloDigiScinPpd"
MyEcalBarrelDigiOdd.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_mip": [CONSTANTS["EcalBarrelMip"]],
    "inputHitCollections": ["ECalBarrelScHitsOdd"],
    "outputHitCollections": ["ECalBarrelScHitsOddDigi"],
    "outputRelationCollections": ["ECalBarrelScHitsOddDigiRelations"],
    "ppd_mipPe": ["10"],
    "ppd_npix": ["10000"],
    "ppd_npix_uncert": ["0"],
    "ppd_pix_spread": ["0"],
    "threshold": ["0.5"],
    "thresholdUnit": ["MIP"],
    "timingCut": ["1"],
}

MyEcalBarrelRecoEven = MarlinProcessorWrapper("MyEcalBarrelRecoEven")
MyEcalBarrelRecoEven.ProcessorType = "RealisticCaloRecoScinPpd"
MyEcalBarrelRecoEven.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_factorsMipGev": [CONSTANTS["EcalBarrelEnergyFactors"]],
    "calibration_layergroups": ["20", "11"],
    "inputHitCollections": ["ECalBarrelScHitsEvenDigi"],
    "inputRelationCollections": ["ECalBarrelScHitsEvenDigiRelations"],
    "outputHitCollections": ["ECalBarrelScHitsEvenRec"],
    "outputRelationCollections": ["ECalBarrelScHitsEvenRecRelations"],
    "ppd_mipPe": ["10"],
    "ppd_npix": ["10000"],
}

MyEcalBarrelRecoOdd = MarlinProcessorWrapper("MyEcalBarrelRecoOdd")
MyEcalBarrelRecoOdd.ProcessorType = "RealisticCaloRecoScinPpd"
MyEcalBarrelRecoOdd.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_factorsMipGev": [CONSTANTS["EcalBarrelEnergyFactors"]],
    "calibration_layergroups": ["20", "11"],
    "inputHitCollections": ["ECalBarrelScHitsOddDigi"],
    "inputRelationCollections": ["ECalBarrelScHitsOddDigiRelations"],
    "outputHitCollections": ["ECalBarrelScHitsOddRec"],
    "outputRelationCollections": ["ECalBarrelScHitsOddRecRelations"],
    "ppd_mipPe": ["10"],
    "ppd_npix": ["10000"],
}

MyEcalEndcapDigiEven = MarlinProcessorWrapper("MyEcalEndcapDigiEven")
MyEcalEndcapDigiEven.ProcessorType = "RealisticCaloDigiScinPpd"
MyEcalEndcapDigiEven.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_mip": [CONSTANTS["EcalEndcapMip"]],
    "inputHitCollections": ["ECalEndcapScHitsEven"],
    "outputHitCollections": ["ECalEndcapScHitsEvenDigi"],
    "outputRelationCollections": ["ECalEndcapScHitsEvenDigiRelations"],
    "ppd_mipPe": ["10"],
    "ppd_npix": ["10000"],
    "ppd_npix_uncert": ["0"],
    "ppd_pix_spread": ["0"],
    "threshold": ["0.5"],
    "thresholdUnit": ["MIP"],
    "timingCut": ["1"],
}

MyEcalEndcapDigiOdd = MarlinProcessorWrapper("MyEcalEndcapDigiOdd")
MyEcalEndcapDigiOdd.ProcessorType = "RealisticCaloDigiScinPpd"
MyEcalEndcapDigiOdd.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_mip": [CONSTANTS["EcalEndcapMip"]],
    "inputHitCollections": ["ECalEndcapScHitsOdd"],
    "outputHitCollections": ["ECalEndcapScHitsOddDigi"],
    "outputRelationCollections": ["ECalEndcapScHitsOddDigiRelations"],
    "ppd_mipPe": ["10"],
    "ppd_npix": ["10000"],
    "ppd_npix_uncert": ["0"],
    "ppd_pix_spread": ["0"],
    "threshold": ["0.5"],
    "thresholdUnit": ["MIP"],
    "timingCut": ["1"],
}

MyEcalEndcapRecoEven = MarlinProcessorWrapper("MyEcalEndcapRecoEven")
MyEcalEndcapRecoEven.ProcessorType = "RealisticCaloRecoScinPpd"
MyEcalEndcapRecoEven.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_factorsMipGev": [CONSTANTS["EcalEndcapEnergyFactors"]],
    "calibration_layergroups": ["20", "11"],
    "inputHitCollections": ["ECalEndcapScHitsEvenDigi"],
    "inputRelationCollections": ["ECalEndcapScHitsEvenDigiRelations"],
    "outputHitCollections": ["ECalEndcapScHitsEvenRec"],
    "outputRelationCollections": ["ECalEndcapScHitsEvenRecRelations"],
    "ppd_mipPe": ["10"],
    "ppd_npix": ["10000"],
}

MyEcalEndcapRecoOdd = MarlinProcessorWrapper("MyEcalEndcapRecoOdd")
MyEcalEndcapRecoOdd.ProcessorType = "RealisticCaloRecoScinPpd"
MyEcalEndcapRecoOdd.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_factorsMipGev": [CONSTANTS["EcalEndcapEnergyFactors"]],
    "calibration_layergroups": ["20", "11"],
    "inputHitCollections": ["ECalEndcapScHitsOddDigi"],
    "inputRelationCollections": ["ECalEndcapScHitsOddDigiRelations"],
    "outputHitCollections": ["ECalEndcapScHitsOddRec"],
    "outputRelationCollections": ["ECalEndcapScHitsOddRecRelations"],
    "ppd_mipPe": ["10"],
    "ppd_npix": ["10000"],
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

MyDDStripSplitterBarrel = MarlinProcessorWrapper("MyDDStripSplitterBarrel")
MyDDStripSplitterBarrel.ProcessorType = "DDStripSplitter"
MyDDStripSplitterBarrel.Parameters = {
    "ECALcollection_evenLayers": ["ECalBarrelScHitsEvenRec"],
    "ECALcollection_oddLayers": ["ECalBarrelScHitsOddRec"],
    "LCRelations_evenLayers": ["ECalBarrelScHitsEvenRecRelations"],
    "LCRelations_oddLayers": ["ECalBarrelScHitsOddRecRelations"],
    "isBarrelHits": ["true"],
    "splitEcalCollection": ["ECalBarrelScHitsSplit"],
    "splitEcalRelCol": ["EcalBarrelRelationsSimRec"],
    "unsplitEcalCollection": ["ECalBarrelScHitsUnSplit"],
}

MyDDStripSplitterEndcap = MarlinProcessorWrapper("MyDDStripSplitterEndcap")
MyDDStripSplitterEndcap.ProcessorType = "DDStripSplitter"
MyDDStripSplitterEndcap.Parameters = {
    "ECALcollection_evenLayers": ["ECalEndcapScHitsEvenRec"],
    "ECALcollection_oddLayers": ["ECalEndcapScHitsOddRec"],
    "LCRelations_evenLayers": ["ECalEndcapScHitsEvenRecRelations"],
    "LCRelations_oddLayers": ["ECalEndcapScHitsOddRecRelations"],
    "isBarrelHits": ["false"],
    "splitEcalCollection": ["ECalEndcapScHitsSplit"],
    "splitEcalRelCol": ["EcalEndcapsRelationsSimRec"],
    "unsplitEcalCollection": ["ECalEndcapScHitsUnSplit"],
}

MergeEcalBarrelHits = MarlinProcessorWrapper("MergeEcalBarrelHits")
MergeEcalBarrelHits.ProcessorType = "MergeCollections"
MergeEcalBarrelHits.Parameters = {
    "InputCollections": ["ECalBarrelScHitsEven", "ECalBarrelScHitsOdd"],
    "OutputCollection": ["EcalBarrelCollection"],
}

MergeEcalEndcapHits = MarlinProcessorWrapper("MergeEcalEndcapHits")
MergeEcalEndcapHits.ProcessorType = "MergeCollections"
MergeEcalEndcapHits.Parameters = {
    "InputCollections": ["ECalEndcapScHitsEven", "ECalEndcapScHitsOdd"],
    "OutputCollection": ["EcalEndcapsCollection"],
}

MergeEcalBarrelDigiHits = MarlinProcessorWrapper("MergeEcalBarrelDigiHits")
MergeEcalBarrelDigiHits.ProcessorType = "MergeCollections"
MergeEcalBarrelDigiHits.Parameters = {
    "InputCollections": ["ECalBarrelScHitsEvenDigi", "ECalBarrelScHitsOddDigi"],
    "OutputCollection": ["EcalBarrelCollectionDigi"],
}

MergeEcalEndcapDigiHits = MarlinProcessorWrapper("MergeEcalEndcapDigiHits")
MergeEcalEndcapDigiHits.ProcessorType = "MergeCollections"
MergeEcalEndcapDigiHits.Parameters = {
    "InputCollections": ["ECalEndcapScHitsEvenDigi", "ECalEndcapScHitsOddDigi"],
    "OutputCollection": ["EcalEndcapsCollectionDigi"],
}

MergeEcalBarrelRecStripHits = MarlinProcessorWrapper("MergeEcalBarrelRecStripHits")
MergeEcalBarrelRecStripHits.ProcessorType = "MergeCollections"
MergeEcalBarrelRecStripHits.Parameters = {
    "InputCollections": ["ECalBarrelScHitsEvenRec", "ECalBarrelScHitsOddRec"],
    "OutputCollection": ["EcalBarrelStripCollectionRec"],
}

MergeEcalEndcapRecStripHits = MarlinProcessorWrapper("MergeEcalEndcapRecStripHits")
MergeEcalEndcapRecStripHits.ProcessorType = "MergeCollections"
MergeEcalEndcapRecStripHits.Parameters = {
    "InputCollections": ["ECalEndcapScHitsEvenRec", "ECalEndcapScHitsOddRec"],
    "OutputCollection": ["EcalEndcapStripCollectionRec"],
}

MergeEcalBarrelRecHits = MarlinProcessorWrapper("MergeEcalBarrelRecHits")
MergeEcalBarrelRecHits.ProcessorType = "MergeCollections"
MergeEcalBarrelRecHits.Parameters = {
    "InputCollections": ["ECalBarrelScHitsSplit", "ECalBarrelScHitsUnSplit"],
    "OutputCollection": ["EcalBarrelCollectionRec"],
}

MergeEcalEndcapRecHits = MarlinProcessorWrapper("MergeEcalEndcapRecHits")
MergeEcalEndcapRecHits.ProcessorType = "MergeCollections"
MergeEcalEndcapRecHits.Parameters = {
    "InputCollections": ["ECalEndcapScHitsSplit", "ECalEndcapScHitsUnSplit"],
    "OutputCollection": ["EcalEndcapsCollectionRec"],
}

ScEcalSequence = [
    MyEcalBarrelDigiEven,
    MyEcalBarrelDigiOdd,
    MyEcalBarrelRecoEven,
    MyEcalBarrelRecoOdd,
    MyEcalEndcapDigiEven,
    MyEcalEndcapDigiOdd,
    MyEcalEndcapRecoEven,
    MyEcalEndcapRecoOdd,
    MyEcalRingDigi,
    MyEcalRingReco,
    MyDDStripSplitterBarrel,
    MyDDStripSplitterEndcap,
    MergeEcalBarrelHits,
    MergeEcalEndcapHits,
    MergeEcalBarrelDigiHits,
    MergeEcalEndcapDigiHits,
    MergeEcalBarrelRecStripHits,
    MergeEcalEndcapRecStripHits,
    MergeEcalBarrelRecHits,
    MergeEcalEndcapRecHits,
]
