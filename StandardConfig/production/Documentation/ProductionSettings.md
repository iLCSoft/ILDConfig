
# Production settings

This document describe the different parameters used for simulating and reconstructing events for the MC production.

## 1. Simulation parameters

Some specific parameters have to be set for collision events (physics and background). These do not apply for single particles or uds events usually used for calibration or detector performance studies.

### A. Interaction vertex position

There are 4 types of collision events, depending on the nature of the incoming particles.

- e- e+ or gamma-gamma background with two real photons (denoted *WW*),
- e- gamma or gamma-gamma background with one virtual and one real photon (denoted *WB*),
- gamma e+ or gamma-gamma background with one real and one virtual photon (denoted *BW*),
- gamma-gamma physics or gamma-gamma background with two virtual photons (denoted *BB*).

Additionally there is background from incoherent e+e- pairs coming from Beamstrahlung, simply denoted by *pair* in the following. In this special case, the vertex position of the individual pairs is computed by the generator (GuineaPig).

### 250 GeV vertex parameters for 250-SetA beam

<table>
  <tr> <th> Process </th><th> Vertex z offset (mm) </th><th> Vertex z sigma (mm) </th></tr>
  <tr> <td> e+e- / WW         </td><td> n.c                    </td><td> n.c             </td></tr>
  <tr> <td> e- gamma / WB     </td><td> n.c	                   </td><td> n.c             </td></tr>
  <tr> <td> e+ gamma / BW     </td><td> n.c                    </td><td> n.c             </td></tr>
  <tr> <td> gamma gamma / BB  </td><td> n.c                    </td><td> n.c             </td></tr>
  <tr> <td> pair              </td><td> n.c                    </td><td> n.c             </td></tr>
  <caption>Vertex parameters for the different processes at 250 GeV center of mass energy</caption>
</table>

### 350 GeV vertex parameters for 350-TDR_ws beam

<table>
  <tr> <th> Process </th><th> Vertex z offset (mm) </th><th> Vertex z sigma (mm) </th></tr>
  <tr> <td> e+e- / WW         </td><td> n.c                    </td><td> n.c             </td></tr>
  <tr> <td> e- gamma / WB     </td><td> n.c	                   </td><td> n.c             </td></tr>
  <tr> <td> e+ gamma / BW     </td><td> n.c                    </td><td> n.c             </td></tr>
  <tr> <td> gamma gamma / BB  </td><td> n.c                    </td><td> n.c             </td></tr>
  <tr> <td> pair              </td><td> n.c                    </td><td> n.c             </td></tr>
  <caption>Vertex parameters for the different processes at 350 GeV center of mass energy</caption>
</table>

### 500 GeV vertex parameters for 500-TDR_ws beam

<table>
  <tr> <th> Process </th><th> Vertex z offset (mm) </th><th> Vertex z sigma (mm) </th></tr>
  <tr> <td> e+e- / WW         </td><td> 0                    </td><td> 0.1968            </td></tr>
  <tr> <td> e- gamma / WB     </td><td> -0.04222	           </td><td> 0.186             </td></tr>
  <tr> <td> e+ gamma / BW     </td><td> +0.04222             </td><td> 0.186             </td></tr>
  <tr> <td> gamma gamma / BB  </td><td> 0                    </td><td> 0.16988           </td></tr>
  <tr> <td> pair              </td><td> 0                    </td><td> 0                 </td></tr>
  <caption>Vertex parameters for the different processes at 500 GeV center of mass energy</caption>
</table>

### 1000 GeV vertex parameters for 1000-B1b_ws beam

<table>
  <tr> <th> Process </th><th> Vertex z offset (mm) </th><th> Vertex z sigma (mm) </th></tr>
  <tr> <td> e+e- / WW         </td><td> 0                    </td><td> 0.1468          </td></tr>
  <tr> <td> e- gamma / WB     </td><td> -0.0352	             </td><td> 0.1389          </td></tr>
  <tr> <td> e+ gamma / BW     </td><td> +0.0357              </td><td> 0.1394          </td></tr>
  <tr> <td> gamma gamma / BB  </td><td> 0                    </td><td> 0.1260          </td></tr>
  <tr> <td> pair              </td><td> 0                    </td><td> 0               </td></tr>
  <caption>Vertex parameters for the different processes at 1 TeV center of mass energy</caption>
</table>

Examples on how to simulate background events with these parameters can be found in the document [HowToRunBgOverlay.md](HowToRunBgOverlay.md) in the same directory.

## 2. Reconstruction parameters

To reconstruct events we assume we have 1 source of physics event (e+e- collision) and a set of background (all backgrounds being WW, WB, BW, BB and pair).
The number of background events to be overlaid on the physics event is the only reconstruction parameter in this case. All these values can be found in the *Config* directory and depend on the CMS energy.

Examples on how to run the reconstruction with the background overlay can be found in the document [HowToRunBgOverlay.md](HowToRunBgOverlay.md) in the same directory.
