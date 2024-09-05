#!/usr/bin/env python3

from Gaudi.Configuration import INFO
from Configurables import MarlinProcessorWrapper

BgOverlayWW = MarlinProcessorWrapper("BgOverlayWW")
BgOverlayWW.OutputLevel = INFO
BgOverlayWW.ProcessorType = "Overlay"
BgOverlayWW.Parameters = {
    "InputFileNames": ["undefined.slcio"],
    "NumberOverlayEvents": ["0"],
    "expBG": [cms_energy_config["ExpectedBgWW"]],
}

BgOverlayWB = MarlinProcessorWrapper("BgOverlayWB")
BgOverlayWB.OutputLevel = INFO
BgOverlayWB.ProcessorType = "Overlay"
BgOverlayWB.Parameters = {
    "InputFileNames": ["undefined.slcio"],
    "NumberOverlayEvents": ["0"],
    "expBG": [cms_energy_config["ExpectedBgWB"]],
}

BgOverlayBW = MarlinProcessorWrapper("BgOverlayBW")
BgOverlayBW.OutputLevel = INFO
BgOverlayBW.ProcessorType = "Overlay"
BgOverlayBW.Parameters = {
    "InputFileNames": ["undefined.slcio"],
    "NumberOverlayEvents": ["0"],
    "expBG": [cms_energy_config["ExpectedBgBW"]],
}

BgOverlayBB = MarlinProcessorWrapper("BgOverlayBB")
BgOverlayBB.OutputLevel = INFO
BgOverlayBB.ProcessorType = "Overlay"
BgOverlayBB.Parameters = {
    "InputFileNames": ["undefined.slcio"],
    "NumberOverlayEvents": ["0"],
    "expBG": [cms_energy_config["ExpectedBgBB"]],
}

PairBgOverlay = MarlinProcessorWrapper("PairBgOverlay")
PairBgOverlay.OutputLevel = INFO
PairBgOverlay.ProcessorType = "Overlay"
PairBgOverlay.Parameters = {
    "ExcludeCollections": ["BeamCalCollection"],
    "InputFileNames": ["undefined.slcio"],
    "NumberOverlayEvents": ["0"],
}

BgOverlaySequence = [
    BgOverlayWW,
    BgOverlayWB,
    BgOverlayBW,
    BgOverlayBB,
    PairBgOverlay,
]
