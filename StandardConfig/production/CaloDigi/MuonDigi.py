#!/usr/bin/env python3

from Configurables import MarlinProcessorWrapper

MyDDSimpleMuonDigi = MarlinProcessorWrapper("MyDDSimpleMuonDigi")
MyDDSimpleMuonDigi.ProcessorType = "DDSimpleMuonDigi"
MyDDSimpleMuonDigi.Parameters = {
    "CalibrMUON": [CONSTANTS["MuonCalibration"]],
    "CellIDLayerString": ["layer"],
    "DetectorNameBarrel": ["YokeBarrel"],
    "DetectorNameEndcap": ["YokeEndcap"],
    "MUONCollections": ["YokeBarrelCollection", "YokeEndcapsCollection"],
    "MUONOutputCollection": ["MUON"],
    "MaxHitEnergyMUON": ["2.0"],
    "MuonThreshold": ["0.025"],
    "MuonTimeThreshold": ["0.025"],
    "RelationOutputCollection": ["RelationMuonHit"],
}

MuonDigiSequence = [MyDDSimpleMuonDigi]
