#!/usr/bin/env python3
#
# Native Gaudi replacement for ParticleFlow/PandoraPFA.py, using the
# DDPandoraPFANewAlgorithm from k4GaudiPandora instead of the
# MarlinProcessorWrapper around DDPandoraPFANewProcessor. Kept as a separate
# sequence for now so it can be tested independently; the parameter names and
# values are ported 1:1 from PandoraPFA.py. Parameters that configured
# detector names for DDMarlinPandora (e.g. ECalBarrelDetectorName, CoilName,
# TrackerBarrelDetectorNames, ...) have no equivalent here since
# DDPandoraPFANewAlgorithm resolves the relevant subdetectors via DD4hep
# detector-type flags instead. NEventsToSkip and UseOldTrackStateCalculation
# are likewise gone (the latter is now a compile-time option in
# k4GaudiPandora).

from Configurables import DDPandoraPFANewAlgorithm
from Gaudi.Configuration import ERROR

MyDDGaudiPandoraParameters = {
    # Inputs
    "MCParticleCollections": ["MCParticle"],
    "TrackCollections": ["MarlinTrkTracks"],
    "RelTrackCollections": ["MarlinTrkTracksMCTruthLink"],
    "KinkVertexCollections": ["KinkVertices"],
    "ProngVertexCollections": ["ProngVertices"],
    "SplitVertexCollections": ["SplitVertices"],
    "V0VertexCollections": ["V0Vertices"],
    "ECalCaloHitCollections": [
        "EcalBarrelCollectionRec",
        "EcalBarrelCollectionGapHits",
        "EcalEndcapsCollectionRec",
        "EcalEndcapsCollectionGapHits",
        "EcalEndcapRingCollectionRec",
    ],
    "HCalCaloHitCollections": [
        "HcalBarrelCollectionRec",
        "HcalEndcapsCollectionRec",
        "HcalEndcapRingCollectionRec",
    ],
    "MuonCaloHitCollections": ["MUON"],
    "LCalCaloHitCollections": ["LCAL"],
    "LHCalCaloHitCollections": ["LHCAL"],
    "RelCaloHitCollections": [
        "EcalBarrelRelationsSimRec",
        "EcalEndcapsRelationsSimRec",
        "EcalEndcapRingRelationsSimRec",
        "HcalBarrelRelationsSimRec",
        "HcalEndcapsRelationsSimRec",
        "HcalEndcapRingRelationsSimRec",
        "RelationMuonHit",
        "RelationLHcalHit",
        "RelationLcalHit",
    ],
    # Outputs
    "ClusterCollectionName": ["PandoraClusters"],
    "PFOCollectionName": ["PandoraPFOs"],
    "StartVertexCollectionName": ["PandoraPFANewStartVertices"],
    "StartVertexAlgorithmName": "PandoraPFANew",
    # Settings
    "TrackCreatorName": "DDTrackCreatorILD",
    "PandoraSettingsXmlFile": CONSTANTS["PandoraSettingsFile"],
    "CreateGaps": False,
    "UseDD4hepField": False,
    "DigitalMuonHits": 0,
    "MaxBarrelTrackerInnerRDistance": 105.0,
    "ECalMipThreshold": 0.5,
    "HCalMipThreshold": 0.3,
    "ECalToEMGeVCalibration": float(CONSTANTS["PandoraEcalToEMScale"]),
    "HCalToEMGeVCalibration": float(CONSTANTS["PandoraHcalToEMScale"]),
    "ECalToHadGeVCalibrationBarrel": float(CONSTANTS["PandoraEcalToHadBarrelScale"]),
    "ECalToHadGeVCalibrationEndCap": float(CONSTANTS["PandoraEcalToHadEndcapScale"]),
    "HCalToHadGeVCalibration": float(CONSTANTS["PandoraHcalToHadScale"]),
    "ECalToMipCalibration": float(CONSTANTS["PandoraEcalToMip"]),
    "HCalToMipCalibration": float(CONSTANTS["PandoraHcalToMip"]),
    "MuonToMipCalibration": float(CONSTANTS["PandoraMuonToMip"]),
    "FinalEnergyDensityBin": 30.0,
    "MaxClusterEnergyToApplySoftComp": 1000.0,
    "MaxHCalHitHadronicEnergy": 1000000.0,
    "MinCleanHitEnergy": 0.5,
    "MinCleanHitEnergyFraction": 0.01,
    "MinCleanCorrectedHitEnergy": 0.1,
    "SoftwareCompensationEnergyDensityBins": [
        0.0,
        2.0,
        5.0,
        7.5,
        9.5,
        13.0,
        16.0,
        20.0,
        23.5,
        28.0,
    ],
    "SoftwareCompensationWeights": [
        float(w) for w in CONSTANTS["PandoraSoftwareCompensationWeights"].split()
    ],
    "YokeBarrelNormalVector": [0.0, 1.0, 0.0],
}

MyDDGaudiPandora = DDPandoraPFANewAlgorithm("MyDDGaudiPandora", **MyDDGaudiPandoraParameters)
MyDDGaudiPandora.OutputLevel = ERROR

PandoraPFA_GaudiSequence = [MyDDGaudiPandora]
