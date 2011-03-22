#!/usr/bin/env python

""" 
MSSE 12 : Software Testing
Lab   2 : Test Harness
"""

import sys              # command line parameters
import pexpect          # pExpect library
import getopt           # access to program parameters

VERSION_MAJOR   = 0
VERSION_MINOR   = 2

PROGRAM_TITLE   = "Software Testing: Test Harness"
PROGRAM_AUTHORS = "MSSE 12: Snowmen"
PROGRAM_VERSION = "version " + str(VERSION_MAJOR) + "." + str(VERSION_MINOR)
ENDL = "\r\n"

"""
Usage: python TestHarness.py <testCaseFile.xml> <logFile>
"""
def main():
    print PROGRAM_TITLE + " " + PROGRAM_AUTHORS
    print PROGRAM_VERSION 
    
    ###################################################################################
    # parse command line (must be exactly 3 parameters)
    if len(sys.argv) != 3:
        print "Usage: python TestHarness.py <testCaseFile.xml> <logFile> \n"
        return -1

    testCaseFileName = sys.argv[1]
    logFileName      = sys.argv[2]

    print "        Input File: " + testCaseFileName
    print "          Log File: " + logFileName
    print ""

    
    ###################################################################################
    # Generate output log file
    logWriter = open(logFileName, "a")
    logWriter.writelines(" " + ENDL)
    logWriter.writelines(PROGRAM_AUTHORS + ENDL)
    logWriter.writelines(PROGRAM_TITLE + ENDL)
    logWriter.writelines(PROGRAM_VERSION + ENDL)


    ###################################################################################
    # read in XML test case file
    # extract program to run, length of timeout, all the test cases
#    program, timeout, testCaseList = parseXMLTestCases(testCaseFileName)       ## TODO

    program = "a.out"
    timeout = 60
    testCaseList = [("a","b"), ("c","d")]

    write(logWriter, "Program Under Test: " + program)
    write(logWriter, " Timeout (seconds): " + str(timeout))
    write(logWriter, "   Test Case Count: " + str(len(testCaseList)))
    write(logWriter, "")


    ###################################################################################
    # Perform testing
    successCount = 0
    failureCount = 0

#    for case in testCaseList:
#        result, message = PerformTest.test(case)
#        
#        if result == True:
#            successCount += 1
#        else:
#            failureCount += 1
            


    ###################################################################################    
    # Print results
    write(logWriter, "Total test cases: " + str(len(testCaseList)))
    write(logWriter, "         PASSING: " + str(successCount))
    write(logWriter, "         FAILING: " + str(failureCount))
    

    ###################################################################################    
    # Close files
    logWriter.close()
    
#   main()

def write(log, msg):
    print msg
    log.writelines(msg + ENDL)
#   write




if __name__ == "__main__":
        main()




