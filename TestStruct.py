#!/usr/bin/env python

""" 
MSSE 12 : Software Testing
Lab   2 : Test Harness
"""

class TestStruct():
    def __init__(self, TestCaseID, Parameters=None, InputFile=None, DestinationDirectory=None, ExtraParameters=None, ExpectedConsole=None, ExpectedFiles=None):
        """
        TestStruct - This class holds all the details for running a single test case.

        Other
          TestCaseID              - Identifier for this test case

        Inputs:
          InputFile               - Name of file to be used as input source
          DestinationDirectory    - Name of directory where output files will be stored
          ExtraParameters         - Any additional parameters

        Outputs:
          ExpectedConsole         - Expect output values on the command line
          ExpectedFiles           - Array of tuples (fileName, file to compare contents against)
        """
        self.testCaseID             = TestCaseID
        self.parameters             = Parameters
        self.inputFile              = InputFile                
        self.destinationDirectory   = DestinationDirectory
        self.extraParameters        = ExtraParameters
        self.expectedFiles          = ExpectedFiles
    # __init__

    def commandString(self):
        """
        Builds the arguement string which appears after the program name on the command line
        """
        result = ""

        if(self.parameters is not None):
            result += self.parameters + " "

        if(self.inputFile is not None):
            result += self.inputFile + " "

        if(self.destinationDirectory is not None):
            result += self.destinationDirectory + " "

        if(self.extraParameters is not None):
            result += self.extraParameters

        return result

    #   commandString


