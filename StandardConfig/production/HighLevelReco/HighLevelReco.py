#!/usr/bin/env python3

from Configurables import MarlinProcessorWrapper
from Gaudi.Configuration import INFO

MyAdd4MomCovMatrixCharged = MarlinProcessorWrapper("MyAdd4MomCovMatrixCharged")
MyAdd4MomCovMatrixCharged.OutputLevel = INFO
MyAdd4MomCovMatrixCharged.ProcessorType = "Add4MomCovMatrixCharged"
MyAdd4MomCovMatrixCharged.Parameters = {"InputPandoraPFOsCollection": ["PandoraPFOs"]}

MyAddClusterProperties = MarlinProcessorWrapper("MyAddClusterProperties")
MyAddClusterProperties.OutputLevel = INFO
MyAddClusterProperties.ProcessorType = "AddClusterProperties"
MyAddClusterProperties.Parameters = {
    "ClusterCollection": ["PandoraClusters"],
    "PFOCollectionName": ["PandoraPFOs"],
}

MyComputeShowerShapesProcessor = MarlinProcessorWrapper(
    "MyComputeShowerShapesProcessor"
)
MyComputeShowerShapesProcessor.OutputLevel = INFO
MyComputeShowerShapesProcessor.ProcessorType = "ComputeShowerShapesProcessor"
MyComputeShowerShapesProcessor.Parameters = {
    "ClusterCollectionName": ["PandoraClusters"],
    "Debug": ["0"],
    "MoliereRadius_Ecal": ["9.00"],
    "MoliereRadius_Hcal": ["17.19"],
    "PFOCollection": ["PandoraPFOs"],
    "RadiationLength_Ecal": ["3.50"],
    "RadiationLength_Hcal": ["17.57"],
}

MyphotonCorrectionProcessor = MarlinProcessorWrapper("MyphotonCorrectionProcessor")
MyphotonCorrectionProcessor.OutputLevel = INFO
MyphotonCorrectionProcessor.ProcessorType = "photonCorrectionProcessor"
MyphotonCorrectionProcessor.Parameters = {
    "energyCor_Linearise": ["0.987", "0.01426"],
    "energyCorr_barrelPhi": [
        "0.412249",
        "0.0142289",
        "-0.0933687",
        "0.01345",
        "0.0408156",
    ],
    "energyCorr_costh": [
        "-0.09",
        "0.",
        "0.235",
        "0.007256",
        "-0.0369648",
        "0.",
        "0.588",
        "0.0121604",
        "-0.0422968",
        "0.774",
        "0.009",
        "1.002",
    ],
    "energyCorr_endcap": ["-0.025", "855.", "23.", "-0.07", "1489.", "18."],
    "inputCollection": ["PandoraPFOs"],
    "modifyPFOdirection": [CONSTANTS["ApplyPhotonPFOCorrections"]],
    "modifyPFOenergies": [CONSTANTS["ApplyPhotonPFOCorrections"]],
    "nominalEnergy": ["200"],
    "phiCorr_barrel": [
        "2.36517e-05",
        "1.32090e-04",
        "-3.86883e+00",
        "-1.67809e-01",
        "2.28614e-05",
        "6.03495e-05",
        "0.419",
        "0.00728",
        "0.025",
        "0.00",
        "2.86667e-05",
        "2.49371e-05",
        "-7.71684e-06",
        "-1.48118e-05",
        "-5.63786e-06",
        "-9.38376e-06",
        "-4.96296e-06",
        "2.91262e-06",
    ],
    "thetaCorr_barrel": ["-0.000166568", "-7.119e-05", "0.000223618", "-3.95915e-05"],
    "thetaCorr_endcap": [
        "0.000129478",
        "-3.73863e-05",
        "-0.000847783",
        "0.000153646",
        "0.000806605",
        "-0.000132608",
    ],
    "validationPlots": ["false"],
}

MyPi0Finder = MarlinProcessorWrapper("MyPi0Finder")
MyPi0Finder.OutputLevel = INFO
MyPi0Finder.ProcessorType = "GammaGammaCandidateFinder"
MyPi0Finder.Parameters = {
    "GammaGammaResonanceMass": ["0.1349766"],
    "GammaGammaResonanceName": ["Pi0"],
    "GammaMomentumCut": ["0.5"],
    "InputParticleCollectionName": ["PandoraPFOs"],
    "MaxDeltaMgg": ["0.04"],
    "OutputParticleCollectionName": ["GammaGammaCandidatePi0s"],
    "Printing": ["0"],
}

MyEtaFinder = MarlinProcessorWrapper("MyEtaFinder")
MyEtaFinder.OutputLevel = INFO
MyEtaFinder.ProcessorType = "GammaGammaCandidateFinder"
MyEtaFinder.Parameters = {
    "GammaGammaResonanceMass": ["0.547862"],
    "GammaGammaResonanceName": ["Eta"],
    "GammaMomentumCut": ["1.0"],
    "InputParticleCollectionName": ["PandoraPFOs"],
    "MaxDeltaMgg": ["0.14"],
    "OutputParticleCollectionName": ["GammaGammaCandidateEtas"],
    "Printing": ["0"],
}

MyEtaPrimeFinder = MarlinProcessorWrapper("MyEtaPrimeFinder")
MyEtaPrimeFinder.OutputLevel = INFO
MyEtaPrimeFinder.ProcessorType = "GammaGammaCandidateFinder"
MyEtaPrimeFinder.Parameters = {
    "GammaGammaResonanceMass": ["0.95778"],
    "GammaGammaResonanceName": ["EtaPrime"],
    "GammaMomentumCut": ["2.0"],
    "InputParticleCollectionName": ["PandoraPFOs"],
    "MaxDeltaMgg": ["0.19"],
    "OutputParticleCollectionName": ["GammaGammaCandidateEtaPrimes"],
    "Printing": ["0"],
}

MyGammaGammaSolutionFinder = MarlinProcessorWrapper("MyGammaGammaSolutionFinder")
MyGammaGammaSolutionFinder.OutputLevel = INFO
MyGammaGammaSolutionFinder.ProcessorType = "GammaGammaSolutionFinder"
MyGammaGammaSolutionFinder.Parameters = {
    "InputParticleCollectionName1": ["GammaGammaCandidatePi0s"],
    "InputParticleCollectionName2": ["GammaGammaCandidateEtas"],
    "InputParticleCollectionName3": ["GammaGammaCandidateEtaPrimes"],
    "OutputParticleCollectionName": ["GammaGammaParticles"],
    "Printing": ["0"],
}

MyDistilledPFOCreator = MarlinProcessorWrapper("MyDistilledPFOCreator")
MyDistilledPFOCreator.OutputLevel = INFO
MyDistilledPFOCreator.ProcessorType = "DistilledPFOCreator"
MyDistilledPFOCreator.Parameters = {
    "InputParticleCollectionName1": ["PandoraPFOs"],
    "InputParticleCollectionName2": ["GammaGammaParticles"],
    "OutputParticleCollectionName": ["DistilledPFOs"],
    "Printing": ["0"],
}

MyLikelihoodPID = MarlinProcessorWrapper("MyLikelihoodPID")
MyLikelihoodPID.OutputLevel = INFO
MyLikelihoodPID.ProcessorType = "LikelihoodPIDProcessor"
MyLikelihoodPID.Parameters = {
    # fmt: off
    "CostMatrix": [
        "1.0e-50", "1.0", "1.5", "1.0", "1.5",
        "1.0", "1.0e-50", "3.0", "1.0", "1.0",
        "1.0", "1.0", "1.0e-50", "1.0", "3.0",
        "1.0", "1.0", "4.0", "1.0e-50", "2.0",
        "1.0", "1.0", "5.0", "1.0", "1.0e-50",
    ],
    # fmt: on
    "Debug": ["0"],
    "EnergyBoundaries": ["0", "1.0e+07"],
    "FilePDFName": [CONSTANTS["PidPDFFile"]],
    "FileWeightFormupiSeparationName": [CONSTANTS["PidWeightFiles"]],
    "RecoParticleCollection": ["PandoraPFOs"],
    "UseBayesian": ["2"],
    "UseLowMomentumMuPiSeparation": ["true"],
    "dEdxErrorFactor": [CONSTANTS["dEdXErrorFactor"]],
    "dEdxNormalization": ["1.350e-7"],
    "dEdxParameter_electron": [
        "-1.28883368e-02",
        "2.72959919e+01",
        "1.10560871e+01",
        "-1.74534200e+00",
        "-9.84887586e-07",
    ],
    "dEdxParameter_kaon": [
        "7.52235689e-02",
        "1.59710415e+04",
        "1.79625604e+06",
        "3.15315795e-01",
        "2.30414997e-04",
    ],
    "dEdxParameter_muon": [
        "6.49143971e-02",
        "1.55775592e+03",
        "9.31848047e+08",
        "2.32201725e-01",
        "2.50492066e-04",
    ],
    "dEdxParameter_pion": [
        "6.54955215e-02",
        "8.26239081e+06",
        "1.92933904e+05",
        "2.52743206e-01",
        "2.26657525e-04",
    ],
    "dEdxParameter_proton": [
        "7.92251260e-02",
        "6.38129720e+04",
        "3.82995071e+04",
        "2.80793601e-01",
        "7.14371743e-04",
    ],
}

MyRecoMCTruthLinker = MarlinProcessorWrapper("MyRecoMCTruthLinker")
MyRecoMCTruthLinker.OutputLevel = INFO
MyRecoMCTruthLinker.ProcessorType = "RecoMCTruthLinker"
MyRecoMCTruthLinker.Parameters = {
    "ClusterCollection": ["PandoraClusters"],
    "ClusterMCTruthLinkName": ["ClusterMCTruthLink"],
    "FullRecoRelation": ["true"],
    "KeepDaughtersPDG": ["22", "111", "310", "13", "211", "321"],
    "MCParticleCollection": ["MCParticle"],
    "MCParticlesSkimmedName": ["MCParticlesSkimmed"],
    "MCTruthClusterLinkName": ["MCTruthClusterLink"],
    "MCTruthRecoLinkName": ["MCTruthRecoLink"],
    "MCTruthTrackLinkName": ["MCTruthMarlinTrkTracksLink"],
    "RecoMCTruthLinkName": ["RecoMCTruthLink"],
    "RecoParticleCollection": ["PandoraPFOs"],
    "SimCaloHitCollections": [
        "BeamCalCollection",
        "LHCalCollection",
        "LumiCalCollection",
        CONSTANTS["ECalSimHitCollections"],
        CONSTANTS["HCalSimHitCollections"],
        "YokeBarrelCollection",
        "YokeEndcapsCollection",
    ],
    "SimCalorimeterHitRelationNames": [
        "EcalBarrelRelationsSimRec",
        "EcalEndcapRingRelationsSimRec",
        "EcalEndcapsRelationsSimRec",
        "HcalBarrelRelationsSimRec",
        "HcalEndcapRingRelationsSimRec",
        "HcalEndcapsRelationsSimRec",
        "RelationLHcalHit",
        "RelationMuonHit",
        "RelationLcalHit",
        "RelationBCalHit",
    ],
    "SimTrackerHitCollections": [
        "VXDCollection",
        "SITCollection",
        "FTD_PIXELCollection",
        "FTD_STRIPCollection",
        "TPCCollection",
        "SETCollection",
    ],
    "TrackCollection": ["MarlinTrkTracks"],
    "TrackMCTruthLinkName": ["MarlinTrkTracksMCTruthLink"],
    "TrackerHitsRelInputCollections": [
        "VXDTrackerHitRelations",
        "SITTrackerHitRelations",
        "FTDPixelTrackerHitRelations",
        "FTDSpacePointRelations",
        "TPCTrackerHitRelations",
        "SETSpacePointRelations",
    ],
    "UseTrackerHitRelations": ["true"],
    "UsingParticleGun": ["false"],
}

VertexFinder = MarlinProcessorWrapper("VertexFinder")
VertexFinder.OutputLevel = INFO
VertexFinder.ProcessorType = "LcfiplusProcessor"
VertexFinder.Parameters = {
    "Algorithms": ["PrimaryVertexFinder", "BuildUpVertex"],
    "BeamSizeX": [cms_energy_config["BeamSizeX"]],
    "BeamSizeY": [cms_energy_config["BeamSizeY"]],
    "BeamSizeZ": [cms_energy_config["BeamSizeZ"]],
    "BuildUpVertex.AssocIPTracks": ["1"],
    "BuildUpVertex.AssocIPTracksChi2RatioSecToPri": ["2.0"],
    "BuildUpVertex.AssocIPTracksMinDist": ["0."],
    "BuildUpVertex.MassThreshold": ["10."],
    "BuildUpVertex.MaxChi2ForDistOrder": ["1.0"],
    "BuildUpVertex.MinDistFromIP": ["0.3"],
    "BuildUpVertex.PrimaryChi2Threshold": ["25."],
    "BuildUpVertex.SecondaryChi2Threshold": ["9."],
    "BuildUpVertex.TrackMaxD0": ["10."],
    "BuildUpVertex.TrackMaxD0Err": ["0.1"],
    "BuildUpVertex.TrackMaxZ0": ["20."],
    "BuildUpVertex.TrackMaxZ0Err": ["0.1"],
    "BuildUpVertex.TrackMinFtdHits": ["10000"],
    "BuildUpVertex.TrackMinPt": ["0.1"],
    "BuildUpVertex.TrackMinTpcHits": ["10000"],
    "BuildUpVertex.TrackMinVxdFtdHits": ["0"],
    "BuildUpVertex.TrackMinVxdHits": ["10000"],
    "BuildUpVertex.UseAVF": ["0"],
    "BuildUpVertex.UseV0Selection": ["1"],
    "BuildUpVertex.V0VertexCollectionName": ["BuildUpVertex_V0"],
    "BuildUpVertexCollectionName": ["BuildUpVertex"],
    "PFOCollection": ["PandoraPFOs"],
    "PrimaryVertexCollectionName": ["PrimaryVertex"],
    "PrimaryVertexFinder.BeamspotConstraint": [
        cms_energy_config["LCFIPlusBeamspotConstraint"]
    ],
    "PrimaryVertexFinder.BeamspotSmearing": ["0"],
    "PrimaryVertexFinder.Chi2Threshold": ["25."],
    "PrimaryVertexFinder.TrackMaxD0": ["20."],
    "PrimaryVertexFinder.TrackMaxZ0": ["20."],
    "PrimaryVertexFinder.TrackMinVtxFtdHits": ["1"],
    "PrintEventNumber": ["0"],
    "ReadSubdetectorEnergies": ["1"],
    "TrackHitOrdering": ["1"],
    "UpdateVertexRPDaughters": ["1"],
}

TrackLengthProcessor = MarlinProcessorWrapper("TrackLengthProcessor")
TrackLengthProcessor.OutputLevel = INFO
TrackLengthProcessor.ProcessorType = "TrackLengthProcessor"
TrackLengthProcessor.Parameters = {"ReconstructedParticleCollection": ["PandoraPFOs"]}

TOFEstimators0ps = MarlinProcessorWrapper("TOFEstimators0ps")
TOFEstimators0ps.OutputLevel = INFO
TOFEstimators0ps.ProcessorType = "TOFEstimators"
TOFEstimators0ps.Parameters = {
    "ExtrapolateToEcal": ["true"],
    "MaxEcalLayer": ["10"],
    "ReconstructedParticleCollection": ["PandoraPFOs"],
    "TimeResolution": ["0"],
    "TofMethod": ["closest"],
}

TOFEstimators10ps = MarlinProcessorWrapper("TOFEstimators10ps")
TOFEstimators10ps.OutputLevel = INFO
TOFEstimators10ps.ProcessorType = "TOFEstimators"
TOFEstimators10ps.Parameters = {
    "ExtrapolateToEcal": ["true"],
    "MaxEcalLayer": ["10"],
    "ReconstructedParticleCollection": ["PandoraPFOs"],
    "TimeResolution": ["10."],
    "TofMethod": ["closest"],
}

TOFEstimators50ps = MarlinProcessorWrapper("TOFEstimators50ps")
TOFEstimators50ps.OutputLevel = INFO
TOFEstimators50ps.ProcessorType = "TOFEstimators"
TOFEstimators50ps.Parameters = {
    "ExtrapolateToEcal": ["true"],
    "MaxEcalLayer": ["10"],
    "ReconstructedParticleCollection": ["PandoraPFOs"],
    "TimeResolution": ["50"],
    "TofMethod": ["closest"],
}

TOFEstimators100ps = MarlinProcessorWrapper("TOFEstimators100ps")
TOFEstimators100ps.OutputLevel = INFO
TOFEstimators100ps.ProcessorType = "TOFEstimators"
TOFEstimators100ps.Parameters = {
    "ExtrapolateToEcal": ["true"],
    "MaxEcalLayer": ["10"],
    "ReconstructedParticleCollection": ["PandoraPFOs"],
    "TimeResolution": ["100"],
    "TofMethod": ["closest"],
}

HighLevelRecoSequence = [
    MyAdd4MomCovMatrixCharged,
    MyAddClusterProperties,
    MyComputeShowerShapesProcessor,
    MyphotonCorrectionProcessor,
    MyPi0Finder,
    MyEtaFinder,
    MyEtaPrimeFinder,
    MyGammaGammaSolutionFinder,
    MyDistilledPFOCreator,
    MyLikelihoodPID,
    MyRecoMCTruthLinker,
    VertexFinder,
    TrackLengthProcessor,
    TOFEstimators0ps,
    TOFEstimators10ps,
    TOFEstimators50ps,
    TOFEstimators100ps,
]
