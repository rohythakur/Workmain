import csv, argparse, sys, metaDataCreator
from lxml import etree


csvFilename = sys.argv[1]

csvFile = open(csvFilename, 'rU')

csvReader = csv.DictReader(csvFile, delimiter=',', quotechar='"')

postProcTags = ["startTime", "endTime", "transcription"]

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

metaDataObj.createSpeakerNode(speakerId='80', gender="Female", ageGroupMin="40", ageGroupMax="49", nativeSpeaker="True")
#metaDataObj.createAudioNode(mic="AT-3030", environment="clean", sampleRate="48000", bitDepth="32", channels="2", encoding="PCM Wave", filePath="./Bucket1-128.wav", duration="500")
metaDataObj.createAudioNode(mic="AT-3030", environment="clean", encoding="PCM Wave", filePath="./Bucket1-128.wav")

tree = etree.ElementTree(metaDataObj.root)
outputFilename = csvFilename.replace(".csv", ".xml")

tree.write(outputFilename, pretty_print=True)
