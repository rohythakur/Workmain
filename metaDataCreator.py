__author__ = 'eeamesX'
import os.path
from lxml import etree

class MetaData:

    validSpeakerChildren = ['speakerId', 'gender', 'ageGroupMin', 'ageGroupMax', 'nativeSpeaker']
#    validAudioChildren = ['duration', 'mic', 'environment', 'sampleRate', 'bitDepth', 'channels', 'encoding', 'filePath']
    validAudioChildren = ['sampleRate', 'bitDepth', 'filePath']

    validSessionChildren = ['speed', 'subDomain', 'windCondition']
    validGeneralChildren = ['originalFileName', 'dateOfDelivery', 'dateOfProcessing']
    validHardwareSetupChildren = ['micType', 'bikeUnit', 'micAngle']


    def __init__(self):
        self.root = etree.Element("Meta")
        pass

    def addSamplePair(self, sampleNode):
        self.root.append(sampleNode)

    def createDeviceNode(self, manufacturer=None, os=None, cpu=None, model=None, osVersion=None):
        pass

    #def createSpeakerNode(self, speakerId=None, gender=None, ageGroupMin=None, ageGroupMax=None, nativeSpeaker=None):
    def createSpeakerNode(self, **kwargs):
        if not set(kwargs.keys()).issubset(set(MetaData.validSpeakerChildren)):
            raise KeyError("Speaker children passed in do not belong in list of valid speaker children tag names")
        speakerNode = etree.Element("Speaker")
        for key in kwargs:
            speakerChildNode = etree.Element(key)
            speakerChildNode.text = kwargs[key]
            speakerNode.append(speakerChildNode)
        self.root.append(speakerNode)

    def createAudioNode(self, **kwargs):
        if not set(kwargs.keys()).issubset(set(MetaData.validAudioChildren)):
            raise KeyError("Audio children passed in do not belong in list of valid audio children tag names")
        audioNode = etree.Element("Audio")
        if "filePath" in kwargs and os.path.exists(kwargs["filePath"]):
            overrideAudioParams(kwargs)
            del kwargs["filePath"]
        for key in kwargs:
            audioChildNode = etree.Element(key)
            audioChildNode.text = str(kwargs[key])
            audioNode.append(audioChildNode)
        self.root.append(audioNode)


    def createSessionNode(self, **kwargs):
        if not set(kwargs.keys()).issubset(set(MetaData.validSessionChildren)):
            raise KeyError("Speaker children passed in do not belong in list of valid session children tag names")
        sessionNode = etree.Element("Session")
        for key in kwargs:
            sessionChildNode = etree.Element(key)
            sessionChildNode.text = kwargs[key]
            sessionNode.append(sessionChildNode)
        self.root.append(sessionNode)

    def createGeneralNode(self, **kwargs):
        if not set(kwargs.keys()).issubset(set(MetaData.validGeneralChildren)):
            raise KeyError("Speaker children passed in do not belong in list of valid general children tag names")
        generalNode = etree.Element("General")
        for key in kwargs:
            generalChildNode = etree.Element(key)
            generalChildNode.text = kwargs[key]
            generalNode.append(generalChildNode)
        self.root.append(generalNode)

    def createHardwareSetupNode(self, **kwargs):
        if not set(kwargs.keys()).issubset(set(MetaData.validHardwareSetupChildren)):
            raise KeyError("Speaker children passed in do not belong in list of valid hardware setup children tag names")
        hardwareSetupNode = etree.Element("HardwareSetup")
        for key in kwargs:
            hardwareSetupChildNode = etree.Element(key)
            hardwareSetupChildNode.text = kwargs[key]
            hardwareSetupNode.append(hardwareSetupChildNode)
        self.root.append(hardwareSetupNode)



def createPromptNode(*args):
    promptNode = etree.Element("Prompt")
    for arg in args:
        if arg[1].strip() != '':
            promptChildNode = etree.Element(arg[0])
            promptChildNode.text = arg[1]
            promptNode.append(promptChildNode)
    return promptNode

def createPostProcNode(startOfSpeech=None, endOfSpeech=None, utteranceTranscript=None, signalQuality=None, startOfSession=None, endOfSession=None):
    startOfSpeechNode, endOfSpeechNode, speechDurationNode, utteranceTranscriptNode, signalQualityNode, startOfSessionNode, endOfSessionNode, startTimeNode, endTimeNode = None, None, None, None, None, None, None, None, None
    if startOfSpeech:
        startOfSpeechNode = etree.Element("startOfSpeech")
        startOfSpeechNode.text = timeFormatConverter(float(startOfSpeech))
    if endOfSpeech:
        endOfSpeechNode = etree.Element("endOfSpeech")
        endOfSpeechNode.text = timeFormatConverter(float(endOfSpeech))
    if startOfSpeech and endOfSpeech:
        speechDurationNode = etree.Element("speechDuration")
        speechDurationNode.text = timeFormatConverter(float(endOfSpeech)-float(startOfSpeech))
    if utteranceTranscript:
        utteranceTranscriptNode = etree.Element("utteranceTranscript")
        utteranceTranscriptNode.text = utteranceTranscript
    if signalQuality:
        signalQualityNode = etree.Element("signalQuality")
        signalQualityNode.text = signalQuality
    if startOfSession:
        startOfSessionNode = etree.Element("startSession")
        startOfSessionNode.text = startOfSession
    if endOfSession:
        endOfSessionNode = etree.Element("endSession")
        endOfSessionNode.text = endOfSession

#if SpeedOfWind:
#SpeedOfWindNode = etree.Element("windSpeed")
#SpeedOfWindNode.text = SpeedOfWind




    nodesToAdd = [startOfSpeechNode, endOfSpeechNode, speechDurationNode, utteranceTranscriptNode, signalQualityNode, startOfSessionNode, endOfSessionNode, endTimeNode, startTimeNode]
    nonNullNodes = [node for node in nodesToAdd if node is not None]
    postProcNode = etree.Element("postProc")
    for node in nonNullNodes:
        postProcNode.append(node)
    return postProcNode


def SpeedOfWind():
    pass


def overrideAudioParams(oldKwargs):
    filePath = oldKwargs["filePath"]
    import wave
    f = wave.open(filePath, 'rb')
    # get duration
    fframes = f.getnframes()
    frate = f.getframerate()
    fduration = float(fframes / float(frate))

    # get num channels
    fchannels = f.getnchannels()

    # get bitdepth
    fbitDepth = f.getsampwidth()*8

    oldKwargs["bitDepth"] = fbitDepth
    oldKwargs["channels"] = fchannels
    oldKwargs["sampleRate"] = frate
    oldKwargs["duration"] = timeFormatConverter(fduration)



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
