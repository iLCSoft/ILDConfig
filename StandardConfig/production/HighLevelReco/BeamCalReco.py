#!/usr/bin/env python3

from Gaudi.Configuration import INFO
from Configurables import MarlinProcessorWrapper

MyBeamCalClusterReco = MarlinProcessorWrapper("MyBeamCalClusterReco")
MyBeamCalClusterReco.OutputLevel = INFO
MyBeamCalClusterReco.ProcessorType = "BeamCalClusterReco"
MyBeamCalClusterReco.Parameters = {
    "BackgroundMethod": ["Gaussian"],
    "BeamCalCollectionName": ["BCAL"],
    "CreateEfficiencyFile": ["false"],
    "DetectorName": ["BeamCal"],
    "DetectorStartingLayerID": ["1"],
    "ETCluster": ["0.06"],
    "ETPad": ["5e-5"],
    "EfficiencyFilename": ["TaggingEfficiency.root"],
    "InputFileBackgrounds": [CONSTANTS["BeamCalBackgroundFile"]],
    "LinearCalibrationFactor": [CONSTANTS["BeamCalCalibrationFactor"]],
    "LogWeightingConstant": ["-1."],
    "MCParticleCollectionName": ["MCParticle"],
    "MaxPadDistance": ["1e10"],
    "MinimumTowerSize": ["6"],
    "NShowerCountingLayers": ["3"],
    "NumberOfBX": ["1"],
    "PrintThisEvent": ["1"],
    "ReadoutName": ["BeamCalCollection"],
    "RecoClusterCollectionname": ["BCalClusters"],
    "RecoParticleCollectionname": ["BCalRecoParticle"],
    "SigmaCut": ["2"],
    "StartLookingInLayer": ["2"],
    "StartingRing": ["0"],
    "SubClusterEnergyID": ["5"],
    "TowerChi2ndfLimit": ["2."],
    "UseChi2Selection": ["false"],
    "UseConstPadCuts": ["false"],
}

BeamCalRecoSequence = [MyBeamCalClusterReco]
