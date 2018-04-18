# ILDConfig
This package contains ilcsoft configuration files for running simulation and reconstruction for the ILD detector in iLCSoft with lcio, Marlin and DD4hep.

ILDConfig is distributed under the [GPLv3 License](http://www.gnu.org/licenses/gpl-3.0.en.html)

[![License](https://www.gnu.org/graphics/gplv3-127x51.png)](https://www.gnu.org/licenses/gpl-3.0.en.html)


## StandardConfig

- ./production
	- current example/standard configuration files for running simulation (ddsim) and reconstruction (Marlin) for ILD
	
See [./StandardConfig/production/README.md](./StandardConfig/production/README.md) for details.
Following the examples in this file is the quickest way to get started with running iLCSoft for ILD.

## LCFIPlusConfig

Input files for flavor tagging:

- ./steer
	- example steering files

- ./vtxprob
	- input histograms used for flavor tagging

- ./lcfiweights
	- TMVA weight files

## License and Copyright
Copyright (C), ILDConfig Authors

ILDConfig is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License long with this program.  If not, see <http://www.gnu.org/licenses/>.
