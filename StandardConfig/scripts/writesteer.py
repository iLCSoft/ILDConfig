#! /usr/bin/python
#################################################################################
#
# Simple python script to facilitate creation of steering files for Marlin
#
# usage:
#   edit/create stdreco.cfg
#   writesteer.py stdreco_IN.xml stdreco.cfg
#
#  F.Gaede, DESY
#
#################################################################################

import sys

#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
def sar(inf, outf, **wdict):
    """ search and replace everything from dict in file inf to file outf"""
    for line in inf:
        nLine = line 
        for k in wdict.keys():
            v = wdict[ k ]
            nLine = nLine.replace( k , v  )  
	outf.write( nLine )
#--------------------------------------------------------------------------

if len( sys.argv ) < 3:
    print " usage: writesteer.py stdreco_IN.xml stdreco.cfg"
    sys.exit(0) 


execfile( sys.argv[2] )


#################################################################################


run_file= steer_base + 'run.sh'

runf = open( run_file , 'w' )



for fNum in fNums:
    
    theDict = dict( )
    theDict[ '$LCIOINFILE' ]  =  inPath  + fn_base + fNum + '.slcio'
    theDict[ '$LCIOOUTFILE' ] =  outPath + fn_base + fNum + '_REC.slcio'
    theDict[ '$LCIODSTFILE' ] =  outPath + fn_base + fNum + '_DST.slcio'
    theDict[ '$GEARFILE' ]    =  gearfile
    theDict[ '$RAIDAFILE' ]   =  steer_base + fNum
    theDict[ '$PANDORAFILE' ] =  steer_base + fNum + '_pandora.root'
    theDict[ '$PFOID_PDF_NEUTRALFILES' ] =  pfoidPDFneutralfiles
    theDict[ '$PFOID_PDF_CHARGEDFILES' ] =  pfoidPDFchargedfiles
    
    outfName = steer_base + fNum + '.xml'

    inf = open( sys.argv[1] , 'r' )

    outf = open( outfName , 'w' )

    sar( inf , outf , **theDict ) 

    inf.close()
    outf.close()


    logf =  steer_base + fNum +  ".out"
    errf =  steer_base + fNum +  ".err"
    
    outfline=" $MARLIN/bin/Marlin " + outfName + " > " + logf + " 2> " + errf + " & \n" 

    runf.write(outfline)


runf.close()
#--------------------------------------------------------------------------

