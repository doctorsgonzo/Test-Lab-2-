#!/usr/bin/env python

""" 
MSSE 12 : Software Testing
Lab   2 : Test Harness
"""

import os           # OS commands
import pexpect      # command line program tester
import shutil       # recusively delete directory
import filecmp      # file comparison module

import TestStruct   

def test(programName, case, timeout=-1, unitTest=False):
    """
    Execute a single test case, return PASS/FAIL and an option FAIL message

    case - TestStruct containing all the details needed to execute a single test case
    timeout - number of seconds to allow program to run before 'killing' it
    """
    tmpResult = case.testCaseID
    errorFree = True

    ###################################################################################
    # clear contents of destination directory
    # if directory exists -> delete it
    if not unitTest:
        if(os.path.isdir(case.destinationDirectory)):
            shutil.rmtree(case.destinationDirectory)
    
        # make new, empty directory
        os.mkdir(case.destinationDirectory)

    ###################################################################################
    # run program
    commandString = programName + " " + case.commandString()
    if not unitTest:
        (consoleResult, returnCode) = pexpect.run(commandString, "timeout=" + timeout, withexitstatus=True)
    print "command: " + commandString

    ###################################################################################
    # verify command line contents
    ## TODO


    ###################################################################################
    # verify files names generated 
    # 1) correct files appeared
    # 2) no extra files were generated
    # 3) if files were expected, conpair contents against expected results
    if(case.destinationDirectory is not None):
        resultFiles = os.listdir(case.destinationDirectory)
        print resultFiles
        print len(case.expectedFiles)

        if len(resultFiles) != len(case.expectedFiles):
            errorFree = False
            tmpResult += "\r\n\tOutput file count different from expected count" 

        #loop over all expected files
        for expected in case.expectedFiles:
            for actual in resultFiles:
                if expected[0] == actual:    # names match
                    if 0 == filecmp.cmp(expected[1], case.destinationDirectory + "/" + actual):
                        errorFree = False
                        tmpResult += "\r\n\tInvalid file contents: " + expected[0]


    ###################################################################################
    # generate pass/fail results, log them, return
    if(errorFree):
        return (True, "PASS")
    else:
        return (False, "FAIL " + tmpResult)


# test

def test_unitTest()

    test_values_1 = TestStruct.TestStruct("test_1", "-h")
    test_values_2 = TestStruct.TestStruct("test_2", "-o", "in.txt", "qwerty", None, [("a.txt", "expect/a.txt")])

    print test("program", test_values_1, 60, True)
    print test("program", test_values_2, 40, True)

#   test_unitTest






