from PyQt4 import QtGui, QtCore

import sys, os

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import style
style.use('dark_background')


from lxml import etree
import scikits.audiolab
import re

import wave



f = Figure()
a = f.add_subplot(111)

class Sample():

    def __init__(self, startSample, endSample, data, transcription, prompt=""):
        self.startSample = startSample
        self.endSample = endSample
        self.data = data
        self.transcription = transcription
        if prompt != "":
            self.prompt=prompt
a

class PlayWavePage(QtGui.QDialog):

    def __init__self(self,parent=None):
        super(PlayWavePage, self).__init__(parent)

        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)

        self.textBrowser = QtGui.QTextBrowser(self)
        self.textBrowser.append("This is a QTextBrowser!")

        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout.addWidget(self.buttonBox)

        self.createSamples()
        self.refreshSample()
        # on page raise, create the samples and draw the graph and text




class Window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.setGeometry(500, 300, 1200, 900)

        self.setWindowTitle("Visualize waves! Transcription Checker 1.0")
#_________________________________________________________________________
#(Menubah)


        self.myQMenuBar = QtGui.QMenuBar(self)

        FileMenu = self.myQMenuBar.addMenu('File')

        AboutMenu = self.myQMenuBar.addMenu('About')

#______________


        exitAction = QtGui.QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Quit Program')
        exitAction.triggered.connect(QtGui.qApp.quit)

        newAction = QtGui.QAction('New', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('Create new file')
        newAction.triggered.connect(self.newFile)

        saveAction = QtGui.QAction('Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save current file')
        saveAction.triggered.connect(self.saveFile)

        openAction = QtGui.QAction('Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open a file')
        openAction.triggered.connect(self.openFile)


        popupmsgAction = QtGui.QAction('Open', self)
        popupmsgAction.setStatusTip('Popup')
        popupmsgAction.triggered.connect(self.popupmsg)


        FileMenu.addAction(newAction)
        FileMenu.addAction(saveAction)
        FileMenu.addAction(openAction)
        FileMenu.addAction(exitAction)

        AboutMenu.addAction(popupmsgAction)

        extractAction = QtGui.QAction(QtGui.QIcon('min1.png'), 'Flee the Scene', self)
        extractAction.triggered.connect(self.close_application)




#_________________________________________________________________________
#

#Canvas------------------





        #menu = QtGui.QMenu()
        #menu.addAction(deselect_others)
        #menu.exec_(self.sender().mapToGlobal(position))

        self.wavEntryInput = QtGui.QLineEdit(self)

        self.browsebutton11 = QtGui.QPushButton('Browse WAV')
        self.browsebutton11.clicked.connect(self.browsebutton1)












        self.canvas = FigureCanvas(f)
        self.canvas.show()

        self.show()



#_________________________________________________________________________
#(down starting from top, from left, continuing, how many rows it spas across)
        grid = QtGui.QGridLayout()


        grid.addWidget(self.wavEntryInput, 1, 1, 1, 3)
        grid.addWidget(self.browsebutton11, 2, 2, 1, 1)







        grid.addWidget(self.canvas, 1, 5, 6, 5)






        self.setLayout(grid)
#_________________________________________________________________________





#_________________________________________________________________________
    #Functions--------------------------------------------------------------



    def browsebutton1(self, xmlEntry):
        browsebutton = QtGui.QPushButton("Browse WAV", self)
        browsebutton.triggered.connect(lambda: self.askForFile(xmlEntry))

    def close_application(self):
        print("Exiting")
        sys.exit()
    def openFile(self):
        pass
    def saveFile(self):
        pass
    def newFile(self):
        pass


    def popupmsg(self):
        msg = QtGui.QMessageBox.question(self, "Error!",
                                         "If you have any questions feel free to ask.  Email me at EdwinX.Eames@intel.com",
                                         QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if msg == QtGui.QMessageBox.Yes:
            print("Exiting!!!!")
            sys.exit()
        else:
            pass



    def xmlEntry(self):
        openfile, ok = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
        print ('path file: ', openfile)

        if ok:
            return openfile


    def askForFile(self, target): # get path to file and enter it into the target field
        dirname = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
        self.wavEntryInput.addItem(dirname)
        return dirname





    def playAudio(self):
        try: # try playing from numpy array
            scikits.audiolab.play(self.listOfSamples[self.index].data, fs=self.sampleRate)
        except RuntimeError: # if it doesn't work, make a wav file and play it with pyaudio
            import pyaudio
            scikits.audiolab.wavwrite(self.listOfSamples[self.index].data, 'test.wav', fs=self.sampleRate, enc=self.enc)
            wf = wave.open('test.wav', 'rb')
            chunk = 1024

            # open stream based on the wave object which has been input.
            p = pyaudio.PyAudio()
            stream = p.open(format =
                            p.get_format_from_width(wf.getsampwidth()),
                            channels = wf.getnchannels(),
                            rate = wf.getframerate(),
                            output = True)

            # read data (based on the chunk size)
            data = wf.readframes(chunk)

            os.remove('test.wav')

    # play stream (looping from beginning of file to the end)
            while data != '':
            # writing to the stream is what *actually* plays the sound.
                stream.write(data)
                data = wf.readframes(chunk)

    # redraw graph, reset text
    def refreshSample(self):
        self.a.clear()
        currSample = self.listOfSamples[self.index]
        secondsAxis = [i/float(self.sampleRate) for i in range(currSample.startSample, currSample.endSample)]
        self.a.plot(secondsAxis, currSample.data)
        self.transcriptionLabel.config(text=currSample.transcription)
        self.promptLabel.config(text=currSample.prompt)
        #self.a.set_title(currSample.transcription + "\n" + str(self.index + 1) + '/' + str(len(self.listOfSamples)))
        self.canvas.draw()

    # scroll forward
    def nextClip(self):
        self.index += 1
        if self.index >= len(self.listOfSamples):
            self.index = 0
        self.refreshSample()

    # scroll backwards
    def prevClip(self):
        self.index -= 1
        if self.index < 0:
            self.index = len(self.listOfSamples)-1
        self.refreshSample()

    # find all samples in XML and build sample list


    def timestampToMS(ts):
        tsRE = re.compile(r'(?P<hours>[0-9]{2}):(?P<minutes>[0-9]{2}):(?P<seconds>[0-9]{2})(?:(?P<milliseconds>\.[0-9]{0,3}))?')
        groups = tsRE.search(ts)
        if groups.group('milliseconds'):
            ms = (3600000 * int(groups.group('hours'))) + (60000 * int(groups.group('minutes'))) + (1000 * int(groups.group('seconds'))) + int(float(groups.group('milliseconds')) * 1000)
        else:
            ms = (3600000 * int(groups.group('hours'))) + (60000 * int(groups.group('minutes'))) + (1000 * int(groups.group('seconds')))
        return ms# gives sample index given a rate and millisecond index





     # validation function, checks both text entry fields for valid files
    def validFiles(self, *args):
        if os.path.isfile(self.wavPath.get()) and os.path.isfile(self.xmlPath.get()):
            self.examineButton.config()
        else:
            self.examineButton.config()
        return True



    # callback for loading PlayWavePage, passes file paths
    def loadWavPage(self):
        self.frames[PlayWavePage].setSources(self.xmlPath.get(), self.wavPath.get())
        self.show_frame(PlayWavePage)
        return True


    def msToSampleIndex(ms, sampleRate):

        return int(ms * (sampleRate/1000.0))


    def createSamples(self, msToSampleIndex, timestampToMS):
        # get wav data
        data, self.sampleRate, self.enc = scikits.audiolab.wavread(self.wavFilename)

        # get XML data
        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(self.xmlFilename, parser)
        sampleNodes = tree.findall('.//postProc')
        self.listOfSamples = []
        for node in sampleNodes:
            startOfSpeech = timestampToMS(node.find(".//startOfSpeech").text)
            endOfSpeech = timestampToMS(node.find(".//endOfSpeech").text)
            transcription = node.find(".//utteranceTranscript").text
            prompt = None
            try: # if there's a prompt, get it
                prompt = node.getparent().find(".//literalPrompt").text
            except:
                pass
            startSample = msToSampleIndex(startOfSpeech, self.sampleRate)
            endSample = msToSampleIndex(endOfSpeech, self.sampleRate)
            sample = Sample(startSample, endSample, data[startSample:endSample], transcription, prompt)
            self.listOfSamples.append(sample)
        self.index = 0


#______________________
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())
