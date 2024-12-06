#!/usr/bin/env python3

from Configurables import MarlinProcessorWrapper

BgOverlayWW = MarlinProcessorWrapper("BgOverlayWW")
BgOverlayWW.ProcessorType = "Overlay"
BgOverlayWW.Parameters = {
    "InputFileNames": ["undefined.slcio"],
    "NumberOverlayEvents": ["0"],
    "expBG": [cms_energy_config["ExpectedBgWW"]],
}

BgOverlayWB = MarlinProcessorWrapper("BgOverlayWB")
BgOverlayWB.ProcessorType = "Overlay"
BgOverlayWB.Parameters = {
    "InputFileNames": ["undefined.slcio"],
    "NumberOverlayEvents": ["0"],
    "expBG": [cms_energy_config["ExpectedBgWB"]],
}

BgOverlayBW = MarlinProcessorWrapper("BgOverlayBW")
BgOverlayBW.ProcessorType = "Overlay"
BgOverlayBW.Parameters = {
    "InputFileNames": ["undefined.slcio"],
    "NumberOverlayEvents": ["0"],
    "expBG": [cms_energy_config["ExpectedBgBW"]],
}

BgOverlayBB = MarlinProcessorWrapper("BgOverlayBB")
BgOverlayBB.ProcessorType = "Overlay"
BgOverlayBB.Parameters = {
    "InputFileNames": ["undefined.slcio"],
    "NumberOverlayEvents": ["0"],
    "expBG": [cms_energy_config["ExpectedBgBB"]],
}

PairBgOverlay = MarlinProcessorWrapper("PairBgOverlay")
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
