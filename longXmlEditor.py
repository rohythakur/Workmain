__author__ = 'eeamesX'
""" longXmlEditor """

# the folder(s), csv file(s), and xml file(s) should all have the same name.
# for example:  ./data/longXmlEditor.py
#               ./data/22CyclingOut/22CyclingOut.csv
#               ./data/22CyclingOut/22CyclingOut.xml

from collections import Counter
from lxml import etree
import csv
import os, os.path, shutil, argparse
from prettytable import PrettyTable
import UnicodeCSV
import sys
import shutil

try:
    __import__('prettytable')
    niceTable = True
except ImportError:
    niceTable = False
    pass


directory = sys.argv[1]



"""time format converter """
def timeFormatConverter(time):
    seconds = time
    microseconds = seconds % 1
    microString = ""
    if microseconds != 0:
        microString = str(microseconds)[1:5]
    minutes = seconds // 60
    hours = minutes // 60
    getTime =  ("%02d:%02d:%02d" % (hours, minutes % 60, seconds % 60)) + microString
    return getTime





def Main():
    allTranscriptionsFromCsv = []
    timeTranscriptionNoise = {}
    sameLineTimeStampingError = []

    print "Hello again"

    for root, dirs, files in os.walk(directory):
        if len(files) >= 3:
            for f in files:
                print(os.path.join(root, f))

                if f.endswith(".csv"):
                    print f + " made it this far"
                    with open(os.path.join(root, f), "r") as f:


                        reader = UnicodeCSV.UnicodeReader(f, encoding='utf-8')
                        next(reader, None)  # skip the headers
                        for num, row in enumerate(reader):
                            startTime = float(row[0].strip())
                            endTime = float(row[1].strip())
                            transcription = row[2].strip()
                            signalQuality = row[3].strip()
                            speechDuration = timeFormatConverter(endTime-startTime)

                            #when start and end times have been inverted
                            if startTime >= endTime:
                                sameLineTimeStampingError.append("between values at row %s:\n\t(%s, %s) %s"  % (num+2, row[0], row[1],row[2]))

                            timeSpan = (startTime, endTime)
                            postProcData = {'speechDuration' : speechDuration,  'transcription' : transcription, 'signalQuality' : signalQuality, 'csvIndex' : num}
                            timeTranscriptionNoise[timeSpan] = postProcData
                            allTranscriptionsFromCsv.append(transcription)

                            #closestMatch = min(promptTimeStamps, key=lambda x:abs(x-startTime))
                            #print closestMatch, startTime

                                                        #time mismatch between csv lines
                        previousErrors = []
                        for eachLine in timeTranscriptionNoise:
                            currentLine = eachLine
                            currentLineIndex = timeTranscriptionNoise[eachLine]['csvIndex']
                            for previousLine in timeTranscriptionNoise:
                                if timeTranscriptionNoise[previousLine]['csvIndex'] == currentLineIndex - 1:
                                    #print "previous", currentLineIndex, currentLine, previousLine
                                    if previousLine[1] >= currentLine[0]:
                                        #print "previous", previousLine[1], currentLine[0]
                                        previousErrors.append("between values of rows %s and %s:\n\trow %s: %s %s \n\trow %s: %s %s" %
                                                (currentLineIndex + 2, timeTranscriptionNoise[previousLine]['csvIndex'] + 2,
                                                currentLineIndex + 2, currentLine, timeTranscriptionNoise[currentLine]['transcription'],
                                                timeTranscriptionNoise[previousLine]['csvIndex'] + 2, previousLine, timeTranscriptionNoise[previousLine]['transcription']))




    for root, dirs, files in os.walk(directory):
            if len(files) >= 3:
                for f in files:
                    print(os.path.join(root, f))

                    if f.endswith(".xml"):
                        print f + ' THIS WILL BE DATA FILE'


                        output_file = directory + '/' + os.path.splitext(os.path.basename(f))[0] + "_edited.xml"
                        if os.path.exists(output_file):
                            os.remove(output_file)
                            print output_file + "  DELETED!!"

                        print " starting to copy info in"
                        print f + " this is f"
                        print directory + " this is directory"
                        fname, fext = os.path.splitext(f)
                        print fname
                        print files

                        xmltoParse = directory + '/' + fname + '/' + f
                        output_file = open(output_file, 'w')




                        parser = etree.XMLParser(remove_blank_text=True)

                        tree = etree.parse(xmltoParse, parser)

                        root = tree.getroot()

                        multipleTranscriptionPrompts = []
                        noTranscriptionPrompts = []
                        extraPrompts = 0

                        print "\n", str.upper(f)

                        if niceTable:
                            report = PrettyTable(["start/end", "Start Rec", "Start TS", "abs diff", "transcription"])
                            report.padding_width = 1 # One space between column edges and contents (default)
                            report.align["transcription"] = "l"
                        else:
                            print "stamped start/end time(s) not within recording window"
                            print "start/end \t Start Rec\t Start TS\t abs diff\t transcription\n-------------------------------------------------------------------------------"

                        "To handle duplicates and overflowing recordings"
                        listOfPromptStartMillis = []
                        for fprompt in root.findall("./Prompt/timeKeeping/promptStartMillis"):
                            listOfPromptStartMillis.append(float(fprompt.text))
                        listOfPromptStartMillis = sorted(listOfPromptStartMillis)

                        maxStart =  max(listOfPromptStartMillis)
                        minStart = min(listOfPromptStartMillis)
                        minStart = round(minStart/1000, 3)

                        timeType2Counter = 0
                        tetherCounter = 0
                        calorieCounter = 0
                        languageCounter = 0

                        totalExtraPrompts = 0
                        xmlElementCounter = 0
                        foundCsvMatchCounter = 0
                        listOfUsedTranscriptions = []
                        addedTranscriptions = []
                        reportInfo = {}
                        misaligned = 0

                        for xmlElement in root.findall("Prompt"):
                            xmlElementCounter += 1
                            literalPrompt = xmlElement.find("./literalPrompt")
                            literalPrompt = literalPrompt.text
                            startSpanOriginal = xmlElement.find("./timeKeeping/promptStartMillis")
                            endSpan = xmlElement.find("./timeKeeping/recordingEndMillis")
                            startRecord = xmlElement.find("./timeKeeping/recordingStartMillis")



                            startSpan = round(float(startSpanOriginal.text)/1000,3)
                            endSpan = round(float(endSpan.text)/1000,3)
                            startRecord = round(float(startRecord.text)/1000,3)

                            #if minStart > 0:
                            #    startSpanNewVal = startSpan - minStart
                            #    endSpan = endSpan - minStart
                            #    startRecord = startRecord - minStart
                            #    print startSpan, endSpan, startRecord
                            #else:
                            #    pass

                            #check for time stamping errors/overlap with IVR

                            Sample = etree.Element('Sample')
                            Sample.append(xmlElement)

                            if listOfPromptStartMillis.index(int(startSpanOriginal.text))+1 < len(listOfPromptStartMillis):
                                #print listOfPromptStartMillis.index(int(startSpanOriginal.text))+1, len(listOfPromptStartMillis), listOfPromptStartMillis[listOfPromptStartMillis.index(int(startSpanOriginal.text))+1]
                                extendedSpan = round(float(listOfPromptStartMillis[listOfPromptStartMillis.index(int(startSpanOriginal.text))+1]/1000))
                            else:
                                extendedSpan = endSpan

                            numberOfTranscriptionPerPrompt = 0
                            matchingTranscriptions = []
                            for k in (timeTranscriptionNoise):
                                if (float(k[0]) >= startSpan and float(k[1]) <= extendedSpan): # or (int(startSpanOriginal.text) == maxStart):
                                    #print int(startSpanOriginal.text), maxStart
                                    truncatedTranscription = timeTranscriptionNoise[k]['transcription']
                                    if len(truncatedTranscription) > 75:
                                        truncatedTranscription = (truncatedTranscription[:70] + '...')
                                    else:
                                        pass
                                    foundCsvMatchCounter +=1
                                    listOfUsedTranscriptions.append(timeTranscriptionNoise[k]['transcription'])
                                    if float(k[0]) <= startRecord:
                                        misaligned += 1
                                        if niceTable:
                                            report.add_row(["start", startRecord, float(k[0]), round(abs(startRecord-float(k[0])),3), truncatedTranscription])
                                        else:
                                            print "start\t\t", startRecord, "\t", float(k[0]), "\t", round(abs(startRecord-float(k[0])),3), "\t\t", truncatedTranscription
                                    if float(k[1]) >= endSpan:
                                        misaligned += 1
                                        if niceTable:
                                            report.add_row(["end", endSpan, float(k[1]), round(abs(endSpan-float(k[1])),3), truncatedTranscription])
                                        else:
                                            "end\t", endSpan, "\t\t", float(k[1]), "\t", round(abs(endSpan-float(k[1])),3), "\t\t", truncatedTranscription

                                    postProc = etree.Element('postProc')

                                    startOfSpeech = etree.Element('startOfSpeech')
                                    startOfSpeech.text = timeFormatConverter(k[0])
                                    postProc.append(startOfSpeech)

                                    endOfSpeech = etree.Element('endOfSpeech')
                                    endOfSpeech.text = timeFormatConverter(k[1])
                                    postProc.append(endOfSpeech)

                                    speechDuration = etree.Element('speechDuration')
                                    speechDuration.text = timeTranscriptionNoise[k]['speechDuration']
                                    postProc.append(speechDuration)

                                    utteranceTranscript = etree.Element('utteranceTranscript')
                                    utteranceTranscript.text = timeTranscriptionNoise[k]['transcription']
                                    postProc.append(utteranceTranscript)

                                    if timeTranscriptionNoise[k]['signalQuality'] != '':
                                        signalQuality = etree.Element('signalQuality')
                                        signalQuality.text = timeTranscriptionNoise[k]['signalQuality']
                                        postProc.append(signalQuality)

                                    Sample.append(postProc)

                                    tree = etree.ElementTree(Sample)
                                    numberOfTranscriptionPerPrompt += 1

                                    matchingTranscriptions.append(utteranceTranscript.text)

                                    #xmlReportedTime = {'startingTime' : startOfSpeech.text,'endingTime' : endOfSpeech.text}
                                    #reportInfo[utteranceTranscript.text] = xmlReportedTime
                                    addedTranscriptions.append(utteranceTranscript.text)



                            """ add language tag if missing """
                            lan =  str(directory)
                            LANGUAGE = xmlElement.find('language')
                            if LANGUAGE is None:




                                if "FR" in lan:
                                    languageTag = etree.Element('language')
                                    languageTag.text = 'French'
                                    xmlElement.append(languageTag)
                                    languageCounter += 1
                                    print "French!!!!!!"


                                elif "DE" in lan:
                                    languageTag = etree.Element('language')
                                    languageTag.text = 'German'
                                    xmlElement.append(languageTag)
                                    languageCounter += 1
                                    print "german!!!!!!"

                                elif "IT" in lan:
                                    languageTag = etree.Element('language')
                                    languageTag.text = 'Italian'
                                    xmlElement.append(languageTag)
                                    languageCounter += 1
                                    print "Italian!!!!!!"



                                elif "ES" in lan:

                                    languageTag = etree.Element('language')
                                    languageTag.text = 'Spanish'
                                    xmlElement.append(languageTag)
                                    languageCounter += 1
                                    print "Spanish!!!!!!"



                                else:
                                    languageTag = etree.Element('language')
                                    languageTag.text = 'None'
                                    xmlElement.append(languageTag)
                                    languageCounter += 1
                            """ DYNAMIC GENDER FINDING """

                            GENDER = root.find(".//gender")



                            if GENDER is None:
                                print "Gender was None"

                            elif GENDER.text == 'None':
                                GENDER.text == 'None'



                            #Italian
                            elif GENDER.text == 'Donna':
                                GENDER.text == 'Female'

                            elif GENDER.text == 'Uomo':
                                GENDER.text == 'Male'


                            #France
                            elif GENDER.text == 'Femme':
                                GENDER.text == 'Female'

                            elif GENDER.text == 'Homme':
                                GENDER.text == 'Male'


                            #Spanish
                            elif GENDER.text == 'Donna':
                                GENDER.text == 'Female'

                            elif GENDER.text == 'Donna':
                                GENDER.text == 'Male'


                            #Germian
                            elif GENDER.text == 'Donna':
                                GENDER.text == 'Female'

                            elif GENDER.text == 'Donna':
                                GENDER.text == 'Male'

                            else:
                                GENDER.text == "None"




                            """correct TetherStatus tag to tetherStatus if necessary"""
                            TETHER = xmlElement.find('TetherStatus')
                            if TETHER is None:
                                pass
                            else:
                                TETHER.tag = 'tetherStatus'
                                tetherCounter += 1

                            """correct calorie value in metrics to calories"""
                            METRICS = xmlElement.find('metrics')
                            if METRICS is None:
                                pass
                            else:
                                if METRICS.text == 'calorie':
                                    METRICS.text == 'calories'
                                    calorieCounter += 1
                                else:
                                    pass

                            """correct tommorow value in timeType2 to tomorrow"""
                            TIMETYPE2 = xmlElement.find('timeType2')
                            if TIMETYPE2 is None:
                                pass
                            else:
                                if TIMETYPE2.text == 'tommorow':
                                    TIMETYPE2.text == 'tomorrow'
                                    timeType2Counter += 1
                                else:
                                    pass




                            root.append(Sample)
                            if numberOfTranscriptionPerPrompt > 1:
                                multipleTranscriptionPrompts.append("<%s> has %s transcriptions: %s" %(literalPrompt, numberOfTranscriptionPerPrompt, matchingTranscriptions))
                                extraPrompts += (numberOfTranscriptionPerPrompt-1)
                                totalExtraPrompts += numberOfTranscriptionPerPrompt
                            elif numberOfTranscriptionPerPrompt < 1:
                                noTranscriptionPrompts.append("<%s> has no transcription" %(literalPrompt))

                        tree = etree.ElementTree(root)
                        tree.write(output_file, pretty_print=True, encoding="utf-8")


                        output_file.close()
                        print directory + "   go up one!!!"
                        aEdit = directory + '/Edited'
                        source = directory + '/' + f







                        if niceTable:
                            print "stamped start/end time(s) not within recording window"
                            print report
                        else:
                            pass

                        print "\n"

                        if len(multipleTranscriptionPrompts) > 0:
                            print "Prompt(s) with multiple transcriptions:"
                            countX = 0
                            for x in  multipleTranscriptionPrompts:
                                countX += 1
                                print countX, x

                        if len(noTranscriptionPrompts) > 0:
                            print "\nPrompt(s) with no transcription:"
                            countY = 0
                            for y in  noTranscriptionPrompts:
                                countY += 1
                                print countY, y

                        #print len(addedTranscriptions)
                        #print len(allTranscriptionsFromCsv)

                        print "\nTranscriptions duplicates:"
                        for k,v in Counter(allTranscriptionsFromCsv).items():
                            if v > 1:
                                print k, ":", v, "times"

                        csvTranscriptions = set(allTranscriptionsFromCsv)
                        usedTranscriptions = set(addedTranscriptions)
                        difference = [x for x in csvTranscriptions if x not in usedTranscriptions]
                        listOfDifferences = []

                        for d in difference:
                            for k in timeTranscriptionNoise:
                                if d == timeTranscriptionNoise[k]['transcription']:
                                    listOfDifferences.append("%s, %s, <%s>" % (k[0], k[1], d))

                        countR = 0
                        if len(listOfDifferences) > 0:
                            print "\n[!!!] ATTENTION transcriptions not used were found:"
                            for x in listOfDifferences:
                                countR += 1
                                print countR, x

                        countPR = 0
                        if len(previousErrors) > 0:
                            print "\nTime stamping inconsitencies were found in the csv file:"
                            for x in previousErrors:
                                countPR += 1
                                print countPR, x
                        if len(sameLineTimeStampingError) > 0:
                            print "\nTime stamping inconsitencies were found in the csv file:"
                            for x in sameLineTimeStampingError:
                                countPR += 1
                                print countPR, x


                        print "\nNumber of 'Prompt' element(s) found in the xml file:", xmlElementCounter
                        print "Number of transcriptions in the csv file:", len(timeTranscriptionNoise)
                        print "Number of transcription(s) matching a 'Prompt' element:",foundCsvMatchCounter
                        print "Number of extra transcriptions:", extraPrompts, "(over the number of non-empty 'Prompt' elements)"
                        print "Number of 'Prompt' element(s) with multiple transcriptions:", len(multipleTranscriptionPrompts)
                        print "Number of 'Prompt' element(s) with no transcription:", len(noTranscriptionPrompts)

                        print "Prompt to transcription mapping is correct:", xmlElementCounter - len(noTranscriptionPrompts) - len(multipleTranscriptionPrompts) + totalExtraPrompts == len(timeTranscriptionNoise)

                        if tetherCounter + calorieCounter + timeType2Counter + languageCounter> 0:
                            print "\nAd hoc fixes:"
                        if tetherCounter > 0:
                            print tetherCounter, "TetherCounter > tetherCounter"
                        if calorieCounter > 0:
                            print calorieCounter, "calorie > calories"
                        if timeType2Counter > 0:
                            print timeType2Counter, "tommorow > tomorrow"
                        if languageCounter > 0:
                            print languageCounter, "language tags added with the value 'English'"

                        #for x in listOfUsedTranscriptions:
                        #    print x
                        #leftOutTranscription = [x for x in csvTranscriptions if x not in listOfUsedTranscriptions]










                        print "\n"
                        if not niceTable:
                            print "(For better table formatting, download the prettytable module.)"

                        return output_file


Main()