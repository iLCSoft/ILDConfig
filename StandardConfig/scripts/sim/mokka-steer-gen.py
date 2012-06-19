#! /usr/bin/python -Wignore::FutureWarning
# optparse.py:668: FutureWarning: %u/%o/%x/%X of negative int will return a signed string in Python 2.4 and up


###############################################################################
# generate mokka steering file + g4macro from templates
#
# ARGUMENTS AND REQUIREMENTS:
#
#   - run with option --help
#
#
# LIST OF CHANGES:
#
#   - 2009/03/20:   Initial version 1.0 (J. Engels)
#
#
# author: Jan Engels, DESY - IT
###############################################################################

#------------------- configuration ---------------------------

# current version
_version='1.0'

# this dictionary will contain all the values to be replaced
# in the mokka input template file
# it now already contains a set of default values
mokka_options = {
#    'db_host'   : 'pollin1.in2p3.fr',
    'db_host'   : 'polui01.in2p3.fr',
    'db_user'   : 'consult'         ,
    'db_pass'   : 'consult'         ,
    'start_event'   : 0             ,
    'total_events'  : 1             ,
    'detector_model': 'ILD_00'      ,
    'physics_list'  : 'QGSP_BERT'   ,
    'lcio_filename' : 'mokka-out.slcio'
}

# default mokka g4macro template
default_g4macro_template = """
/run/verbose 0
/event/verbose 0
/tracking/verbose 0
/generator/generator %(input_file)s
/run/beamOn %(total_events)s
"""

#------------------- end configuration ------------------------

import os, sys

usage_msg = """%prog [options] MOKKA_STEER_TEMPLATE [MOKKA_G4MACRO_TEMPLATE]

Description: small python script to generate mokka steering file + g4macro from templates"""

if __name__=="__main__":

    from optparse import OptionParser

    parser = OptionParser( usage=usage_msg, version="%prog " + _version )

    parser.add_option('--log-level', help='set the level of verbosity DEFAULT: %default', default='INFO')
    parser.add_option('-v', '--verbose', '--debug', action='store_true', dest='verbose', help='run in debug mode')

    parser.add_option('--output-dir', help='choose a directory for the output of the script. DEFAULT: %default', default='.')
    parser.add_option('--old-db-id', help='get all parameters from the old mc database for the given job id (e.g. 351272)', type="int")
    #parser.add_option('--new-db-id', help='get all parameters from the new mc database for the given job id (e.g. 351272)', type="int")

    parser.add_option('--mokka-input-file', help='the input filename for mokka')
    parser.add_option('--mokka-start-event', help='start event', type='int')
    parser.add_option('--mokka-total-events', help='total number of events to process', type='int')
    parser.add_option('--mokka-detector-model', help='the detector model used for the simulation')
    parser.add_option('--mokka-physics-list', help='the physics list used for the simulation')
    parser.add_option('--mokka-run-number', help='the run number', type='int')
    parser.add_option('--mokka-random-seed', help='the random seed', type='int')
    parser.add_option('--mokka-lcio-filename', help='the output lcio filename')
    parser.add_option('--mokka-process', help='the process string')
    parser.add_option('--mokka-energy', help='the energy')
    parser.add_option('--mokka-pol-ep', help='the polarisation ep')
    parser.add_option('--mokka-pol-em', help='the polarisation em')
    parser.add_option('--mokka-cross-section', help='the cross section')

    (options, args) = parser.parse_args()


    # --------------------------- process command line options -----------------------------------


    if len(args) < 1 or len(args) > 2:
        parser.error('incorrect number of arguments (-h for help)')

    # ----- old mc database -----
    if options.old_db_id:

        import MySQLdb

        db=MySQLdb.connect( host="flcweb01.desy.de", user="MCRead", db="MC" )
        c=db.cursor(MySQLdb.cursors.DictCursor)
        c.execute("select * from Grid_jobs where ID = %d" % options.old_db_id )
        mokka_opts=c.fetchall()[0]

        #if options.verbose:
        #    print 'mokka opts:'
        #    for k,v in mokka_opts.iteritems():
        #        print '%s:   %s' % (k,v)

        # old database keys
        mokka_options['input_file'] = mokka_opts['Input_File']
        mokka_options['start_event'] = mokka_opts['Start_Number']
        mokka_options['total_events'] = mokka_opts['Number_of_Events']
        mokka_options['detector_model'] = mokka_opts['Detector_Model']
        mokka_options['physics_list'] = mokka_opts['Physics_List']
        mokka_options['random_seed'] = mokka_opts['Random_Seed']
        mokka_options['mc_run_number'] = mokka_opts['Run_Number']
        # FIXME energy, pol_ep, pol_em, cross_section, process

        c.close()

    # read the --mokka-options from the cmd line and set them in the mokka_options dictionary
    for k in options.__dict__.keys():
        if k[:6] == 'mokka_':
            val = getattr(options,k)
            if val != None:
                mokka_options[ k[6:] ] = val

    if options.verbose:
        print 'mokka options: %s' % mokka_options

    # --------------------------- end process command line options --------------------------------

    mokka_steer_template_file=args[0]

    if not os.path.exists( mokka_steer_template_file ):
        parser.error('MOKKA_STEER_TEMPLATE not valid')

    mokka_steer_template = open( mokka_steer_template_file, 'r' ).read()

    # substitute values in template
    mokka_steer = mokka_steer_template % mokka_options

    if len(args) == 2:
        mokka_g4macro_template_file = args[1]
        mokka_g4macro_template = open( mokka_g4macro_template_file, 'r' ).read()
    else:
        mokka_g4macro_template = default_g4macro_template

    # substitute values in template
    mokka_g4macro = mokka_g4macro_template % mokka_options

    if options.verbose:
        print 'mokka steer:'
        print mokka_steer
        print
        print 'mokka g4macro'
        print mokka_g4macro

    # ----- output directory -----
    if not os.path.exists( options.output_dir ):
        os.makedirs( options.output_dir )
    if not os.path.isdir( options.output_dir ):
        parser.error('failed to createoutput-dir')

    print 'writing mokka.steer'
    f = open( options.output_dir+'/mokka.steer', 'w' )
    f.write( mokka_steer )
    f.close()

    print 'writing mokka.g4macro'
    f = open( options.output_dir+'/mokka.g4macro', 'w' )
    f.write( mokka_g4macro )
    f.close()

# EOF

