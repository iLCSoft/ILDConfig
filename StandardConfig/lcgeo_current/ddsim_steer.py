from DDSim.DD4hepSimulation import DD4hepSimulation
from SystemOfUnits import mm, GeV, MeV, rad
import os

SIM = DD4hepSimulation()

SIM.printLevel="INFO"

SIM.runType = "batch"
SIM.numberOfEvents = 3
SIM.skipNEvents = 0

SIM.field.eps_min = 1*mm

SIM.part.minimalKineticEnergy = 1*MeV

SIM.crossingAngleBoost = 7.e-3*rad

SIM.action.tracker = ("Geant4TrackerWeightedAction", {"HitPositionCombination" : 2 , "CollectSingleDeposits" :  False } )

SIM.action.mapActions['tpc'] = "TPCSDAction"

SIM.filter.mapDetFilter['TPC'] = "edep0"

SIM.physics.list = "QGSP_BERT"
SIM.physics.rangecut = 0.1*mm

## Add parameters to the run header
## This will store the Parameter "MyNewParameter" in the runHeader of the slcio file
## all members are added to the runheader. Isn't Python beautiful?
#SIM.MyNewParameter = "Value"


SIM.enableDetailedShowerMode=True

SIM.physics.pdgfile = os.path.join( os.environ.get("DD4hepINSTALL"), 
                                    "examples/DDG4/examples/particle.tbl")


## --- set to True in order to run particle gun --------
SIM.enableGun = False

if( SIM.enableGun ):
#    SIM.gun.direction GUN.DIRECTION
    SIM.gun.particle = "pi-"
    SIM.gun.multiplicity=1 
    SIM.gun.energy = 5*GeV
#    SIM.gun.isotrop = True
    SIM.gun.position = (0., 0., 0. ) 
    SIM.gun.direction = (.5, .5 , .5 ) 



##optional arguments:
##  SIM.compactFile COMPACTFILE
##                        The compact XML file
##  SIM.runType {batch,vis,run,shell}
##                        The type of action to do in this invocation
##                        batch: just simulate some events, needs numberOfEvents, and input file or gun
##                        vis: enable visualisation
##                        run: enable run the macro
##                        shell: enable interactive session
##  SIM.inputFiles INPUTFILES [INPUTFILES ...], -I INPUTFILES [INPUTFILES ...]
##                        InputFiles for simulation, lcio, stdhep, HEPEvt, and hepevt files are supported
##  SIM.outputFile OUTPUTFILE, -O OUTPUTFILE
##                        Outputfile from the simulation,only lcio output is supported
##  -v {1,2,3,4,5,6,7,VERBOSE,DEBUG,INFO,WARNING,ERROR,FATAL,ALWAYS}, 
##  SIM.printLevel {1,2,3,4,5,6,7,VERBOSE,DEBUG,INFO,WARNING,ERROR,FATAL,ALWAYS}
##                        Verbosity use integers from 1(most) to 7(least) verbose
##                        or strings: VERBOSE, DEBUG, INFO, WARNING, ERROR, FATAL, ALWAYS
##  SIM.numberOfEvents NUMBEROFEVENTS, -N NUMBEROFEVENTS
##                        number of events to simulate, used in batch mode
##  SIM.skipNEvents SKIPNEVENTS
##                        Skip first N events when reading a file
##  SIM.physicsList PHYSICSLIST
##                        Physics list to use in simulation
##  SIM.crossingAngleBoost CROSSINGANGLEBOOST
##                        Lorentz boost for the crossing angle, in radian!
##  SIM.vertexSigma X Y Z T
##                        FourVector of the Sigma for the Smearing of the Vertex position: x y z t
##  SIM.vertexOffset X Y Z T
##                        FourVector of translation for the Smearing of the Vertex position: x y z t
##  SIM.macroFile MACROFILE, -M MACROFILE
##                        Macro file to execute for runType 'run' or 'vis'
##  SIM.enableGun, -G       enable the DDG4 particle gun
##  SIM.dumpParameter, SIM.dump
##                        Print all configuration Parameters and exit
##  SIM.enableDetailedShowerMode
##                        use detailed shower mode
##  SIM.random.type RANDOM.TYPE
##  SIM.random.seed RANDOM.SEED
##  SIM.random.replace_gRandom RANDOM.REPLACE_GRANDOM
##  SIM.random.luxury RANDOM.LUXURY
##  SIM.random.file RANDOM.FILE
##  SIM.field.delta_intersection FIELD.DELTA_INTERSECTION
##  SIM.field.min_chord_step FIELD.MIN_CHORD_STEP
##  SIM.field.equation FIELD.EQUATION
##  SIM.field.stepper FIELD.STEPPER
##  SIM.field.delta_chord FIELD.DELTA_CHORD
##  SIM.field.eps_min FIELD.EPS_MIN
##  SIM.field.eps_max FIELD.EPS_MAX
##  SIM.field.delta_one_step FIELD.DELTA_ONE_STEP
##  SIM.part.keepAllParticles PART.KEEPALLPARTICLES
##                         Keep all created particles 
##  SIM.part.minimalKineticEnergy PART.MINIMALKINETICENERGY
##                        MinimalKineticEnergy to store particles created in the tracking region
##  SIM.part.saveProcesses PART.SAVEPROCESSES
##                        List of processes to save, give as whitespace separated string in quotation marks
##  SIM.part.printStartTracking PART.PRINTSTARTTRACKING
##                         Printout at Start of Tracking 
##  SIM.part.printEndTracking PART.PRINTENDTRACKING
##                         Printout at End of Tracking 
##  SIM.gun.direction GUN.DIRECTION
##                         direction of the particle gun, 3 vector 
##  SIM.gun.particle GUN.PARTICLE
##  SIM.gun.multiplicity GUN.MULTIPLICITY
##  SIM.gun.energy GUN.ENERGY
##  SIM.gun.isotrop GUN.ISOTROP
##                         isotropic distribution for the particle gun 
##  SIM.gun.position GUN.POSITION
##                         position of the particle gun, 3 vector 
##  SIM.action.tracker ACTION.TRACKER
##                         set the default tracker action 
##  SIM.action.mapActions ACTION.MAPACTIONS
##                         create a map of patterns and actions to be applied to sensitive detectors
##                            e.g. tpc SIM.> TPCSDAction 
##  SIM.action.calo ACTION.CALO
##                         set the default calorimeter action 
##  SIM.output.random OUTPUT.RANDOM
##                        Output level for Random Number Generator setup
##  SIM.output.kernel OUTPUT.KERNEL
##                        Output level for Geant4 kernel
##  SIM.output.part OUTPUT.PART
##                        Output level for ParticleHandler
##  SIM.output.inputStage OUTPUT.INPUTSTAGE
##                        Output level for input sources


