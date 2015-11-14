import os, sys, re, collections
from lxml import etree


import shutil




#oldContinuousRE = re.compile(r".*ivr_continuous.*\.xml")
oldContinuousRE = re.compile(r".*\.xml")
parser = etree.XMLParser()

def getContinuousXMLs(rootDir):
    continuousXMLs = []
    for root, dirs, files in os.walk(rootDir):
        continuous = filter(lambda f : oldContinuousRE.search(f), files)
        continuous = map(lambda f : root + '/' + f, continuous)
        continuousXMLs.extend(continuous)
    return continuousXMLs

def getUniqueNodeText(root, nodeName):
    node = root.find(".//" + nodeName)
    if node is not None:
        return node.text
    else:
        return None

def getListOfNodesText(root, nodeName):
    foundNodes = root.findall(".//" + nodeName)
    nodeTexts = map(lambda n : n.text, [node for node in foundNodes if node is not None])
    return nodeTexts



if __name__ == "__main__":
    d = sys.argv[1]
    continuousXMLs = getContinuousXMLs(d)

    UIDDict = collections.defaultdict(lambda : {})

    for xmlFile in continuousXMLs:
        try:
            root = etree.parse(xmlFile, parser)
        except etree.XMLSyntaxError:
            continue
        UID = getUniqueNodeText(root, "speakerId")
        gender = getUniqueNodeText(root, "gender")
        ageMin = getUniqueNodeText(root, "ageGroupMin")
        ageMax = getUniqueNodeText(root, "ageGroupMax")
        native = getUniqueNodeText(root, "nativeSpeaker")
        fileName = getUniqueNodeText(root, "fileName")
        numPostProcs = len(getListOfNodesText(root, "postProc"))
        UIDDict[UID]["Gender"] = gender
        UIDDict[UID]["Age Group"] = ageMin + "-" + ageMax
        UIDDict[UID]["Native Speaker"] = native

        if "Files" not in UIDDict[UID]:
            UIDDict[UID]["Files"] = []
        UIDDict[UID]["Files"].append((os.path.basename(xmlFile), fileName, numPostProcs))





    textFile = 'UUIDreadout.txt'
    print textFile
    textFileSource = os.getcwd() + '/' + textFile
    print textFileSource + " this is text file source"
    textFileDest = d
    print str(textFileDest) + " this is text file destination"

    print "stamped start/end time(s) not within recording window"


    print " ...  Writing to txt file :  " + textFile

    f = open(textFile, 'w')
    sys.stdout = f
    shutil.move(textFileSource, textFileDest)
    print "Happy data release day! "
    print ""
    print ""
    print "We have <number> <language> data files."
    print "All files have been directly added to <LANGUAGEFightClub> dataset in LDS."
    print ""
    print ""

    for UID in UIDDict:
        print "UID:", UID, "Gender:", UIDDict[UID]["Gender"], "Age Group:",\
            UIDDict[UID]["Age Group"], "Native Speaker", UIDDict[UID]["Native Speaker"]
        for fileTuple in UIDDict[UID]["Files"]:
            print "\t", ' '.join(map(str,list(fileTuple)))

    print ""
    print ""
    print ""
    print ""

    print "Thanks,"
    print "Data Team"


