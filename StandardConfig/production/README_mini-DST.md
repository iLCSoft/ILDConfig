# mini-DST production

This page will explain how to create mini-DST file. The detailed documentation is available at [arXiv](https://arxiv.org/abs/2105.08622).

# How to create mini-DST
First, you have to initailize your iLCSoft environment, and prepare input files (MC samples of fully-simulated, SGV, ...).
Then specify the place of your input file as INPUTNAME, and output filename as OUTPUTNAME.
The place of weight files for IsolatedLeptonTagging and/or Lcfiplus must be specified properly.
The weight files of Lcfiplus might be packed in tar.gz, thus these are should be unpacked to use.
In the end, type the following command to create mini-DST file.
```
Marlin mini-DST-maker.xml
```
Note that the job might take hours (or even a day), depending on the number of events of input file and/or multiplicity of the physics process.
