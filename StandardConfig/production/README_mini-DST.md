# mini-DST production

This page will explain how to create mini-DST file. The detailed documentation is available at [arXiv](https://arxiv.org/abs/2105.08622).

# How to create mini-DST
First, you have to initailize your iLCSoft environment, and prepare input files (MC samples of fully-simulated, SGV, ...).

## Preparing LCFIPlus weights
The creation of mini-DST files uses `LCFIPlus` which needs input weigths. These weights are shipped with `ILDConfig` but need to be unpacked partially. For the default settings of the steering file the following steps have to be taken

```bash
cd /path/to/ILDConfig/LCFIPlusConfig/lcfiweights
tar xf 4q250_ZZ_v4_p00_ildl5
```

## Running the mini-DST
The steering file takes a few configuration parameters, the default settings require at least the an input file as well as the path to the `ILDConfig` directory that you are currently using.
A more fine grained control is possible, please check the steering file for them.
In the end, type the following command to create mini-DST file
```
Marlin MarlinStdRecoMiniDST.xml \
  --global.LCIOInputFiles=/path/to/your/input_DST.slcio \
  --constant.ILDConfig_DIR=/path/to/ILDConfig
```
Note that the job might take hours (or even a day), depending on the number of events of input file and/or multiplicity of the physics process.
