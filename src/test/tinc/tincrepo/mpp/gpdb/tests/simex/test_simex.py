#!/usr/bin/env python

############################################################################
# Set up some globals, and import gptest 
#    [YOU DO NOT NEED TO CHANGE THESE]
#
import sys, os, inspect, traceback, shutil, socket, re
from mpp.lib.PSQL import PSQL

from mpp.models import SQLConcurrencyTestCase

class simex( SQLConcurrencyTestCase):

###########Utility methods############
        
    def _parseOutFileForPattern( self, pattern, outFile ):
        """cmdStr is an awk command to be run on outFile"""
        cmdStr = "awk '/" + pattern + "/'" + " " + outFile    
        ( result, output ) = shell.run( cmdStr + " " + outFile )
        if ( ( result ) & ( len( output ) > 0 ) ):
            return True
        else:
            return False
        
    def _collectOffendingStackTraces( self, sqlFile, iteration ):
        print "Collecting stack traces from master and segments"
        #Find the name of the input file to form the outputFile pattern
        listOfSubstitutions = [( "%iteration%", str( iteration ) )]
        self.generateFileFromEachTemplate( MYD, ["collect_stack_traces.sql.t"], listOfSubstitutions )
        psql.runfile( mkpath( 'collect_stack_traces.sql' ) )
        
    def runTest( self, sqlFile ):
        continueLoop = True
        count = 0
        
        #Find the name of the input file to form the outputFile pattern
        iFile = sqlFile[sqlFile.rfind( "/" ) + 1:]
        pattern = iFile[0:iFile.rfind( "." )]
        ansfile = pattern + ".ans"
        print "Pattern is " + pattern
        
        while continueLoop:
            print "Executing iteration " + str( count )
            ofile = pattern + str( count ) + '.out'            
            psql.runfile( sqlFile, flag = '-a', outputFile = mkpath( ofile ) )
            filediff = isFileEqual( mkpath( ofile ), mkpath( ansfile ) )
            if not filediff:
                if self._parseOutFileForPattern( _EXPECTED_ERROR_STRING, mkpath( ofile ) ):
                    count = count + 1
                    continue
                else:
                    print "Failed validation for iteration " + str( count )
                    print "Check out file" + ofile
                    self._collectOffendingStackTraces( iFile, count )
            else:
                break
            count = count + 1
    
    @classmethod
    def setUpClass(cls):
        print "Setting up class"

    @classmethod
    def tearDownClass(cls):
        print "Tearing down class"
    
    def setUp(self):
        print "setting up test"

    def test1_tpch_q1( self ):
        #self.runTest( mkpath( 'query01.sql' ) )
        print "running test...."

    def test2_tpch_q2(self):
        print "running simex for tpch q2"
        
                
###########################################################################
#  Try to run if user launched this script directly
#     [YOU SHOULD NOT CHANGE THIS]
if __name__ == '__main__':
    gptest.main()

