# mini-DST production

This page will explain how to create mini-DST file. The detailed documentation is available at [arXiv](https://arxiv.org/abs/2105.08622).

# How to create mini-DST
First, you have to initailize your iLCSoft environment, and prepare input files (MC samples of fully-simulated, SGV, ...).
The steering file takes a few configuration parameters, the default settings require at least the an input file to run.
A more fine grained control is possible, please check the steering file for them and a brief description below
In the end, type the following command to create mini-DST file
```
Marlin MarlinStdRecoMiniDST.xml \
  --global.LCIOInputFiles=/path/to/your/input_DST.slcio
```
Note that the job might take hours (or even a day), depending on the number of events of input file and/or multiplicity of the physics process.

# Configuring the mini-DST creation process
The mini-DST creation process runs a few high level reconstruction algorithms that need additional inputs in the form of weights or configuration, e.g. to `LCFIPlus` or also to run isolated lepton taggers.
In order to make an example easy to run `ILDConfig` comes with some default inputs for these in the `production` folder.
The following sections describe how to change these settings in a bit more detail.
For the default values and some more configuration parameters please have a look at the `MarlinStdRecoMiniDST.xml` steering file.

## LCFIPlus weights
The creation of mini-DST files uses `LCFIPlus` which needs input weigths. These weights are shipped in `ILDConfig/LCFIPlusConfig` but are partially compressed. To unpack these weights you can use the following commands

```bash
cd /path/to/ILDConfig/LCFIPlusConfig/lcfiweights
tar xf 4q250_ZZ_v4_p00_ildl5.tar.gz
```

This will result in a a new folder with a few files. To use these weights you an override the following parameters
- `--constant.LCFIPlusWeightsDir` point this to the directory that was created by unpacking the tarball
- `--constant.LCFIPlusWeightsPrefix` this is the common prefix of the files in the directory. In the case of the tarball above it is `4q250_v04_p00_ildl5`

There are additional input weights for the `LCFIPlus` flavor tagging that live in the `LCFIPlusConfig/vtxprob` directory. These can be configured via
- `--constant.LCFIPlusD0ProbFile` the value that will be passed to the `LCFIPlus.FlavorTag.D0ProbFileName` parameter
- `--constant.LCFIPlusZ0ProbFile` the value that will be passed to the `LCFIPlus.FlavorTag.Z0ProbFileName` parameter

## Isolated lepton tagger weights
The isolated lepton tagging weights are shipped in `ILDConfig/IsolatedLeptonTagging`.
Here different weight folders are present and these folders are the input parameters for the `IsolatedLeptonTaggingProcessor`.
The following configuration parameters can be used to change the default values
- `--constant.ElectronIsolationWeightsDir` point this to the direction containing the electron isolation weights
- `--constant.MuonIsolationWeightsDir` point this to the direction containing the muon isolation weights

## dEdx corrections
The miniDST also runs a recalculation of the dEdx calculations taking into account an angular dependency (see [here](https://github.com/iLCSoft/MarlinReco/pull/91) for a few more details).
After that it re-runs the LikelihoodPID processor to use the corrected dEdx to calculate the PID likelihoods.
This requires a few more weights which are by default in `ILDConfig/StandardConfig/production/`.
- `--constant.RundEdxCorrections=false` can be used to completely disable this
- `--constant.ProductionDir` can be used to change this directory.
