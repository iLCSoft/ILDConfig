#!/usr/bin/env python3

from Gaudi.Configuration import INFO
from Configurables import MarlinProcessorWrapper

MySimDigital = MarlinProcessorWrapper("MySimDigital")
MySimDigital.OutputLevel = INFO
MySimDigital.ProcessorType = "SimDigital"
MySimDigital.Parameters = {
    "AngleCorrectionPower": ["0.65"],
    "CellIDEncodingStringType": ["LCGEO"],
    "ChargeSplitterOption": ["Exact"],
    "ChargeSplitterd": ["0.221368"],
    "EffMapConstantValue": ["0.95"],
    "HCALCellSize": ["10"],
    "HCALThreshold": ["0.114", "6.12", "16.83"],
    "KeepAtLeastOneStep": ["true"],
    "LinkSteps": ["true"],
    "PolyaAverageCharge": ["5.55942"],
    "PolyaWidthParameter": ["2.42211"],
    "RPC_PadSeparation": ["0.408"],
    "StepCellCenterMaxDistanceLayerDirection": ["0.0005"],
    "StepLengthCut": ["0.001"],
    "StepsMinDistanceRPCplaneDirection": ["0.5"],
    "doThresholds": ["true"],
    "functionRange": ["61"],
    "inputHitCollections": [
        "HCalBarrelRPCHits",
        "HCalEndcapRPCHits",
        "HCalECRingRPCHits",
    ],
    "outputHitCollections": [
        "HcalBarrelCollectionDigi",
        "HcalEndcapsCollectionDigi",
        "HcalEndcapRingCollectionDigi",
    ],
    "outputRelationCollections": [
        "HcalBarrelRelationsSimDigi",
        "HcalEndcapsRelationsSimDigi",
        "HcalEndcapRingRelationsSimDigi",
    ],
}

MySimDigitalToEnergy = MarlinProcessorWrapper("MySimDigitalToEnergy")
MySimDigitalToEnergy.OutputLevel = INFO
MySimDigitalToEnergy.ProcessorType = "SimDigitalToEnergy"
MySimDigitalToEnergy.Parameters = {
    "EnergyCalibration": [CONSTANTS["SDHcalEnergyFactors"]],
    "inputHitCollections": [
        "HcalBarrelCollectionDigi",
        "HcalEndcapsCollectionDigi",
        "HcalEndcapRingCollectionDigi",
    ],
    "inputRelationCollections": [
        "HcalBarrelRelationsSimDigi",
        "HcalEndcapsRelationsSimDigi",
        "HcalEndcapRingRelationsSimDigi",
    ],
    "outputHitCollections": [
        "HcalBarrelCollectionRec",
        "HcalEndcapsCollectionRec",
        "HcalEndcapRingCollectionRec",
    ],
    "outputRelationCollections": [
        "HcalBarrelRelationsSimRec",
        "HcalEndcapsRelationsSimRec",
        "HcalEndcapRingRelationsSimRec",
    ],
}

SDHcalDigiSequence = [
    MySimDigital,
    MySimDigitalToEnergy,
]
