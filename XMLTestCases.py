#!/usr/bin/env python

""" 
MSSE 12 : Software Testing
Lab   2 : Test Harness
"""

from xml.dom import minidom     # simple xml parser


def parseXMLTestCases(inFile):
    """
    This routine reads in an XML formatted file containing all of the 
    test case details. Each test cases is parsed into a TestStruct
    object. The program name and timeout values are extracted from
    the 'parameters' tag, and all three items are returned together.

    Return
        program under test - string
        timeout - int
        test cases - array of tuples
    """
    xmldoc = minidom.parse(inFile)
    cNode = xmldoc.childNodes
    #printNode(cNode, 1)
    
    # get root node
    rootNode = xmldoc.getElementsByTagName("TEST")
#    rootNode = cNode.getElementsByTagName("TEST")
    print "<TEST> count: " + str(len(rootNode))

    # extract all test cases
    testCaseNodes = rootNode[0].getElementsByTagName("CASE")
    print "    <CASE> count: " + str(len(testCaseNodes))

    # create list of test cases
    testCaseObjects = []
    for testNode in testCaseNodes:
        testCaseObjects.append(parseTestCase(testNode))

    # return parsed test cases
    print testCaseObjects

#   parseXMLTestCases

#### PARSE TEST CASE ####
# <CASE id="test case ID">
#     <ARGUMENTS>options</ARGUMENTS>
#     <INPUT>filename</INPUT>
#     <OUTPUTDIR>directoryname</OUTPUTDIR>
#     <ARGUMENTSEXTRA>extra_options</ARGUMENTSEXTRA>
#     <OUTPUTFILE fileName="" expectedPath="" />
#     <OUTPUTCMD>fileName</OUTPUTCMD>
# </CASE>
def parseTestCase(tNode):
    print "  "
    print "        => Parsing Test Case: "

    # extract arguements
    cNode = tNode.getElementsByTagName("ARGUMENTS")
    if cNode is not None and len(cNode) > 0 and len(cNode[0].childNodes) > 0:
        print "      { " + cNode[0].nodeName + " => " + str(cNode[0].childNodes[0].nodeValue) + " }"

    # extract inputFile
    cNode = tNode.getElementsByTagName("INPUT")
    if cNode is not None and len(cNode) > 0 and len(cNode[0].childNodes) > 0:
        print "      { " + cNode[0].nodeName + " => " + str(cNode[0].childNodes[0].nodeValue) + " }"
    
    
    # extract output directory
    cNode = tNode.getElementsByTagName("OUTPUTDIR")
    if cNode is not None and len(cNode) > 0 and len(cNode[0].childNodes) > 0:
        print "      { " + cNode[0].nodeName + " => " + str(cNode[0].childNodes[0].nodeValue) + " }"


    # extract extra-arguements
    cNode = tNode.getElementsByTagName("ARGUMENTSEXTRA")
    if cNode is not None and len(cNode) > 0 and len(cNode[0].childNodes) > 0:
        print "      { " + cNode[0].nodeName + " => " + str(cNode[0].childNodes[0].nodeValue) + " }"

    # extract output file(s)
    cNode = tNode.getElementsByTagName("OUTPUTFILE")
    for node in cNode:
        print "      { " + node.nodeName + " => "
        print "           { path => " + xml_attributeValue(node, "expectedPath") + " } "
        print "           { name => " + xml_attributeValue(node, "fileName")     + " } "
        print "      } "
    
    # extract output command line text
    cNode = tNode.getElementsByTagName("OUTPUTCMD")
    if cNode is not None and len(cNode) > 0 and len(cNode[0].childNodes) > 0:
        print "      { " + cNode[0].nodeName + " => " + str(cNode[0].childNodes[0].nodeValue) + " }"


    return 1

#   parseTestCase



def xml_attributeValue(node, attribute):
    if node.hasAttribute(attribute):
        return node.getAttribute(attribute)
    else:
        return None
#   xml_attributeValue



## Test entry point
def main():
    fileName = "test_cases.xml"
    parseXMLTestCases(fileName)
#   main



if __name__ == "__main__":
        main()




