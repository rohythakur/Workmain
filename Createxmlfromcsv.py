import csv, argparse, sys, metaDataCreator
from lxml import etree
from datetime import date
import os
import re



def convert():
    #directoryPath = sys.argv[1]

    directoryPath = "/"

    print directoryPath, ':'

    # process all non-master CSVs
    for fileLocated in os.listdir(directoryPath):
        if fileLocated.endswith(".csv") and 'master' not in fileLocated.lower():

            csvFilename = fileLocated
            strippedFileName =  os.path.splitext(csvFilename)[0]
            wavFileName =  directoryPath  + strippedFileName + ".wav"

            print strippedFileName
            cutOff = re.compile(r"(([0-9]{8})?.*_[Tt]r-[0-9]+)_?(?:([0-9]+)mph)?.*")
            allGroups = cutOff.search(strippedFileName).groups()
            result = cutOff.search(strippedFileName)
            xmlBaseFileName = result.group(1)
            if result.group(2) is not None: # try to get date of delivery from filename
                dateDelivery = "%s/%s/%s" % (result.group(2)[0:2], result.group(2)[2:4], result.group(2)[4:8])
            else:
                dateDelivery = 'n/a'
                print 'Could not parse date received from filename'
            if result.group(3) is not None: # try to get mph from filename
                mph = result.group(3)
            else:
                mph = 'n/a/'
                print 'Could not parse mph from filename'

            csvFilename = directoryPath + csvFilename
            csvFile = open(csvFilename, 'rU')

            csvReader = csv.DictReader(csvFile, delimiter=',', quotechar='"')

            postProcTags = ["startTime", "endTime", "transcription", "signalQuality", "startSession", "endSession"]

            metaDataObj = metaDataCreator.MetaData()

            for row in csvReader:
                sampleNode = etree.Element("Sample")
                if "literalPrompt" in row and row["literalPrompt"].strip() != '':
                    promptNode = etree.Element("Prompt")
                    promptNode = metaDataCreator.createPromptNode(*[(tagName, row[tagName]) for tagName in row.keys() if tagName not in postProcTags and tagName != 'order'])
                    sampleNode.append(promptNode)
                if "transcription" in row and row["transcription"].strip() != '':

                    postProcNode = etree.Element("postProc")
                    postProcNode = metaDataCreator.createPostProcNode(*[row[postProcTag] for postProcTag in postProcTags])
                    sampleNode.append(postProcNode)

                metaDataObj.addSamplePair(sampleNode)

                    #print etree.tostring(sampleNode, pretty_print=True)

            metaDataObj.createSpeakerNode(gender="Male") # (speakerId='80', gender="Female", ageGroupMin="40", ageGroupMax="49", nativeSpeaker="True")
            metaDataObj.createAudioNode(filePath=wavFileName)
            metaDataObj.createSessionNode(speed=mph, subDomain='biking')
            metaDataObj.createGeneralNode(originalFileName=xmlBaseFileName, dateOfDelivery=dateDelivery, dateOfProcessing='%s/%s/%s' % (date.today().month, date.today().day, date.today().year))
            metaDataObj.createHardwareSetupNode(micType='n/a', bikeUnit='311', micAngle='n/a')






            tree = etree.ElementTree(metaDataObj.root)
            outputFilename = csvFilename.replace(".csv", ".xml")

            tree.write(outputFilename, pretty_print=True)


