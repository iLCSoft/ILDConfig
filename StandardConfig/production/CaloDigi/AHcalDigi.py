#!/usr/bin/env python3

from Configurables import MarlinProcessorWrapper

MyHcalBarrelDigi = MarlinProcessorWrapper("MyHcalBarrelDigi")
MyHcalBarrelDigi.ProcessorType = "RealisticCaloDigiScinPpd"
MyHcalBarrelDigi.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_mip": [CONSTANTS["HcalBarrelMip"]],
    "inputHitCollections": ["HcalBarrelRegCollection"],
    "outputHitCollections": ["HcalBarrelCollectionDigi"],
    "outputRelationCollections": ["HcalBarrelRelationsSimDigi"],
    "ppd_mipPe": ["15"],
    "ppd_npix": ["2000"],
    "ppd_npix_uncert": ["0"],
    "ppd_pix_spread": ["0"],
    "threshold": ["0.5"],
    "thresholdUnit": ["MIP"],
    "timingCut": ["1"],
}

MyHcalBarrelReco = MarlinProcessorWrapper("MyHcalBarrelReco")
MyHcalBarrelReco.ProcessorType = "RealisticCaloRecoScinPpd"
MyHcalBarrelReco.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_factorsMipGev": [CONSTANTS["HcalBarrelEnergyFactors"]],
    "calibration_layergroups": ["100"],
    "inputHitCollections": ["HcalBarrelCollectionDigi"],
    "inputRelationCollections": ["HcalBarrelRelationsSimDigi"],
    "outputHitCollections": ["HcalBarrelCollectionRec"],
    "outputRelationCollections": ["HcalBarrelRelationsSimRec"],
    "ppd_mipPe": ["15"],
    "ppd_npix": ["2000"],
}

MyHcalEndcapDigi = MarlinProcessorWrapper("MyHcalEndcapDigi")
MyHcalEndcapDigi.ProcessorType = "RealisticCaloDigiScinPpd"
MyHcalEndcapDigi.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_mip": [CONSTANTS["HcalEndcapMip"]],
    "inputHitCollections": ["HcalEndcapsCollection"],
    "outputHitCollections": ["HcalEndcapsCollectionDigi"],
    "outputRelationCollections": ["HcalEndcapsRelationsSimDigi"],
    "ppd_mipPe": ["15"],
    "ppd_npix": ["2000"],
    "ppd_npix_uncert": ["0"],
    "ppd_pix_spread": ["0"],
    "threshold": ["0.5"],
    "thresholdUnit": ["MIP"],
    "timingCut": ["1"],
}

MyHcalEndcapReco = MarlinProcessorWrapper("MyHcalEndcapReco")
MyHcalEndcapReco.ProcessorType = "RealisticCaloRecoScinPpd"
MyHcalEndcapReco.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_factorsMipGev": [CONSTANTS["HcalEndcapEnergyFactors"]],
    "calibration_layergroups": ["100"],
    "inputHitCollections": ["HcalEndcapsCollectionDigi"],
    "inputRelationCollections": ["HcalEndcapsRelationsSimDigi"],
    "outputHitCollections": ["HcalEndcapsCollectionRec"],
    "outputRelationCollections": ["HcalEndcapsRelationsSimRec"],
    "ppd_mipPe": ["15"],
    "ppd_npix": ["2000"],
}

MyHcalRingDigi = MarlinProcessorWrapper("MyHcalRingDigi")
MyHcalRingDigi.ProcessorType = "RealisticCaloDigiScinPpd"
MyHcalRingDigi.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_mip": [CONSTANTS["HcalRingMip"]],
    "inputHitCollections": ["HcalEndcapRingCollection"],
    "outputHitCollections": ["HcalEndcapRingCollectionDigi"],
    "outputRelationCollections": ["HcalEndcapRingRelationsSimDigi"],
    "ppd_mipPe": ["15"],
    "ppd_npix": ["2000"],
    "ppd_npix_uncert": ["0"],
    "ppd_pix_spread": ["0"],
    "threshold": ["0.5"],
    "thresholdUnit": ["MIP"],
    "timingCut": ["1"],
}

MyHcalRingReco = MarlinProcessorWrapper("MyHcalRingReco")
MyHcalRingReco.ProcessorType = "RealisticCaloRecoScinPpd"
MyHcalRingReco.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_factorsMipGev": [CONSTANTS["HcalRingEnergyFactors"]],
    "calibration_layergroups": ["100"],
    "inputHitCollections": ["HcalEndcapRingCollectionDigi"],
    "inputRelationCollections": ["HcalEndcapRingRelationsSimDigi"],
    "outputHitCollections": ["HcalEndcapRingCollectionRec"],
    "outputRelationCollections": ["HcalEndcapRingRelationsSimRec"],
    "ppd_mipPe": ["15"],
    "ppd_npix": ["2000"],
}

AHcalDigiSequence = [
    MyHcalBarrelDigi,
    MyHcalBarrelReco,
    MyHcalEndcapDigi,
    MyHcalEndcapReco,
    MyHcalRingDigi,
    MyHcalRingReco,
]
