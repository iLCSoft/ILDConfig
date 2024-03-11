#!/usr/bin/env python3

from Gaudi.Configuration import INFO
from Configurables import MarlinProcessorWrapper


MySimpleBCalDigi = MarlinProcessorWrapper("MySimpleBCalDigi")
MySimpleBCalDigi.OutputLevel = INFO
MySimpleBCalDigi.ProcessorType = "SimpleFCalDigi"
MySimpleBCalDigi.Parameters = {
    "CalibrFCAL": [CONSTANTS["BeamCalCalibrationFactor"]],
    "CaloID": ["bcal"],
    "CellIDLayerString": ["layer"],
    "FCALCollections": ["BeamCalCollection"],
    "FCALOutputCollection": ["BCAL"],
    "FcalThreshold": ["5e-05"],
    "RelationOutputCollection": ["RelationBCalHit"],
}

MySimpleLCalDigi = MarlinProcessorWrapper("MySimpleLCalDigi")
MySimpleLCalDigi.OutputLevel = INFO
MySimpleLCalDigi.ProcessorType = "SimpleFCalDigi"
MySimpleLCalDigi.Parameters = {
    "CalibrFCAL": ["89.0"],
    "CaloID": ["lcal"],
    "CellIDLayerString": ["layer"],
    "FCALCollections": ["LumiCalCollection"],
    "FCALOutputCollection": ["LCAL"],
    "FcalThreshold": ["0.4e-04"],
    "RelationOutputCollection": ["RelationLcalHit"],
}

MySimpleLHCalDigi = MarlinProcessorWrapper("MySimpleLHCalDigi")
MySimpleLHCalDigi.OutputLevel = INFO
MySimpleLHCalDigi.ProcessorType = "SimpleFCalDigi"
MySimpleLHCalDigi.Parameters = {
    "CalibrFCAL": ["150"],
    "CaloID": ["lhcal"],
    "CellIDLayerString": ["layer"],
    "FCALCollections": ["LHCalCollection"],
    "FCALOutputCollection": ["LHCAL"],
    "FcalThreshold": ["1.7e-04"],
    "RelationOutputCollection": ["RelationLHcalHit"],
}

FcalDigiSequence = [
    MySimpleBCalDigi,
    MySimpleLCalDigi,
    MySimpleLHCalDigi,
]
