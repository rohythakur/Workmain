__author__ = 'eeamesX'
import sys, os


directoryChosen = (sys.argv[1])


print directoryChosen + "   thi is inside dollartohash"
if os.path.isdir(directoryChosen):
    for n in os.listdir(directoryChosen):
        if not n.startswith('.'):
            allPromptStartNodes = root.findall(".//promptStartMillis")
            allPromptStartValues = map((lambda x : int(x.text)), allPromptStartNodes)

            lowestPromptStart = min(allPromptStartValues)
            if lowestPromptStart != 0:
                for xmlElement in root.xpath("//*[contains(local-name(), 'Millis')]"):
                    nodeValue = int(xmlElement.text)
                    newValue = nodeValue - lowestPromptStart
                    xmlElement.text = str(int(newValue))

