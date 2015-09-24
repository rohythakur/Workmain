__author__ = 'eeamesX'

import sys, time
import os


import subprocess
from os.path import abspath


from scipy.io.wavfile import read,write
from pylab import plot,show,subplot,specgram
from matplotlib.backends import qt4_compat
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


use_pyside = qt4_compat.QT_API == qt4_compat.QT_API_PYSIDE

from PyQt4 import QtGui, QtCore

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s




#_________________________________________________________________________
#_________________________________________________________________________
#_________________________________________________________________________
#_________________________________________________________________________
#_________________________________________________________________________


class pageTwo(QtGui.QDialog):
    def __init__(self,parent = None):
        QtGui.QDialog.__init__(self, parent)

        self.initUI()

    def initUI(self):
# button move  (over, down)
        self.setGeometry(300,300,800,600)
        self.setWindowTitle("PyMail")
        self.setWindowIcon(QtGui.QIcon("PyMail"))
        self.setStyleSheet("font-size:15px")

        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Page Two")
        self.lbl.move(20,20)

        self.button = QtGui.QPushButton('Home', self)
        self.button.clicked.connect(self.startPage)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(20, 30)
        self.button.setFixedSize(100,75)


        self.button = QtGui.QPushButton('Page Two', self)
        self.button.clicked.connect(self.pageTwo)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(220, 30)
        self.button.setFixedSize(100,75)



        self.button2 = QtGui.QPushButton('Page Three', self)
        self.button2.clicked.connect(self.pageThree)
        self.button2.setIconSize(QtCore.QSize(24,24))
        self.button2.move(420, 30)
        self.button2.setFixedSize(100,75)



        self.button4 = QtGui.QPushButton('Quit', self)
        self.button4.clicked.connect(self.close_application)
        self.button4.setIconSize(QtCore.QSize(24,24))
        self.button4.move(620, 500)
        self.button4.setFixedSize(100,75)

        self.listWidget = QtGui.QListWidget(self)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget.move(75,250)

        self.listWidgetcomplete = QtGui.QListWidget(self)
        self.listWidgetcomplete.setObjectName(_fromUtf8("listWidget"))
        self.listWidgetcomplete.move(475,250)



    # Open a FILE and append to screen
        self.selectFileButton = QtGui.QPushButton('Select Files', self)
        self.selectFileButton.move(135, 200)
        self.selectFileButton.clicked.connect(self.selectFile)




    # Open a FILE and append to screen
        self.convertButton = QtGui.QPushButton('Convert!', self)
        self.convertButton.move(350,350)
        self.convertButton.clicked.connect(self.osconvertfile)






    def close_application(self):

        print("whooaaaa so custom!!!")
        sys.exit()


    def startPage(self):

        self.hide()
        startpage = mainWindow(self)
        startpage.show()


    def pageTwo(self):

        self.hide()
        pagetwo = pageTwo(self)
        pagetwo.show()

    def pageThree(self):
        self.hide()
        pagethree = pageThree(self)
        pagethree.show()


# **************
#Functions
        #directory = ' directory'
        #convertorString = "python /Users/eeamesX/work/data-scripts/longFileScripts/createXMLFromCSVSept.py"

        #os.system('python createXMLFromCS.py' +directory)
##########################################

    def selectFile(self):


        self.listWidget.clear() # In case there are any existing elements in the list
        directory = QtGui.QFileDialog.getExistingDirectory(self, "Pick a folder")


        for file_name in os.listdir(directory):
            if file_name.endswith(".csv"):
                self.listWidget.addItem(file_name)
                print (file_name)
        self.directory = directory





    def osconvertfile(self):


        directoryPath = self.directory
        print directoryPath

        cmd = ('python /Users/eeamesX/PycharmProjects/Workmain/Createxmlfromcsv.py ' +str(directoryPath))
        print cmd
        os.system(cmd)





    def convertfile(self, directory):

        import csv, argparse, sys, metaDataCreator
        from lxml import etree
        from datetime import date
        import os
        import re

        genderMap = {"M": "Male", "F" : "Female"}
        nativeMap = {"N": "True", "NN": "False"}




        directoryPath = directory

        #directoryPath = "./" + directoryPath + "/"

        print directoryPath, ':'

        # process all non-master CSVs
        for fileLocated in directoryPath:
            if fileLocated.endswith(".csv") and 'master' not in fileLocated.lower():

                csvFilename = fileLocated
                strippedFileName =  os.path.splitext(csvFilename)[0]
                wavFileName =  directoryPath  + strippedFileName + ".wav"

                print strippedFileName
                filenameRE = re.compile(r"(?P<PTL>PTL{2}[0-9][a-z]?)-(?P<UID>UID_[^-]*)-(?P<GENDER>[MF])-(?P<NATIVITY>N{1,2})-(?P<SERIALNUMBER>[0-9a-z]{6})-.*")
                filenameGroups = filenameRE.search(strippedFileName)

                ptlPortion = filenameGroups.group("PTL")
                uidPortion = filenameGroups.group("UID")
                genderPortion = filenameGroups.group("GENDER")
                nativityPortion = filenameGroups.group("NATIVITY")
                serialNumberPortion = filenameGroups.group("SERIALNUMBER")
                #cutOff = re.compile(r"(([0-9]{8})?.*_[Tt]r-[0-9]+)_?(?:([0-9]+)mph)?.*")
                #allGroups = cutOff.search(strippedFileName).groups()
                #result = cutOff.search(strippedFileName)
                xmlBaseFileName = filenameGroups.group(0)
                #if result.group(2) is not None: # try to get date of delivery from filename
                    #dateDelivery = "%s/%s/%s" % (result.group(2)[0:2], result.group(2)[2:4], result.group(2)[4:8])
                #else:
                    #dateDelivery = 'n/a'
                    #print 'Could not parse date received from filename'
                #if result.group(3) is not None: # try to get mph from filename
                    #mph = result.group(3)
                #else:
                    #mph = 'n/a/'
                    #print 'Could not parse mph from filename'

                csvFilename = directoryPath + csvFilename
                csvFile = open(csvFilename, 'rU')


                csvReader = csv.DictReader(csvFile, delimiter=',', quotechar='"')
                csvReader.fieldnames = map(csvReader.fieldnames)

                postProcTags = ["startTime", "endTime", "transcription", "signalQuality"]

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
                        promptNode = metaDataCreator.createPromptNode(fileName="prototype_testing_list_3b.csv")
                        sampleNode.append(postProcNode)
                        sampleNode.append(promptNode)

                    metaDataObj.addSamplePair(sampleNode)

                        #print etree.tostring(sampleNode, pretty_print=True)

                metaDataObj.createSpeakerNode(gender=genderMap[genderPortion], speakerId=uidPortion.replace("UID_", ""), nativeSpeaker=nativeMap[nativityPortion]) # (speakerId='80', gender="Female", ageGroupMin="40", ageGroupMax="49", nativeSpeaker="True")
                metaDataObj.createAudioNode(filePath=wavFileName)
                metaDataObj.createDeviceNode(serialNumber=serialNumberPortion)
                #metaDataObj.createSessionNode(subDomain='biking')
                metaDataObj.createGeneralNode(originalFileName=xmlBaseFileName, dateOfProcessing='%s/%s/%s' % (date.today().month, date.today().day, date.today().year))
                #metaDataObj.createHardwareSetupNode(micType='n/a', bikeUnit='311', micAngle='n/a')






                tree = etree.ElementTree(metaDataObj.root)
                outputFilename = csvFilename.replace(".csv", ".xml")

                tree.write(outputFilename, pretty_print=True)










#_________________________________________________________________________
#_________________________________________________________________________
#_________________________________________________________________________
#_________________________________________________________________________
#_________________________________________________________________________
#_________________________________________________________________________
#_________________________________________________________________________





class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)

        self.compute_initial_figure()

        #
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass

class MyStaticMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""

    def compute_initial_figure(self):
        #file = str(QtGui.QFileDialog.getOpenFileName(self, "Select File", "", "*.wav *.mp3"))

        rate,data = read('test.wav') # reading
        subplot(411)
        plot(range(len(data)),data)
        subplot(412)
        # NFFT is the number of data points used in each block for the FFT
        # and noverlap is the number of points of overlap between blocks
        specgram(data, NFFT=128, noverlap=0) # small window
        subplot(413)
        specgram(data, NFFT=512, noverlap=0)
        subplot(414)
        specgram(data, NFFT=1024, noverlap=0) # big window

        self.show()



class pageThree(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)

        self.initUI()





    def initUI(self):
# button move  (over, down)
        self.setGeometry(300,300,800,600)
        self.setWindowTitle("PyMail")
        self.setWindowIcon(QtGui.QIcon("PyMail"))
        self.setStyleSheet("font-size:15px")



        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Page Three")
        self.lbl.move(20,20)

        self.button = QtGui.QPushButton('Home', self)
        self.button.clicked.connect(self.startPage)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(20, 30)
        self.button.setFixedSize(100,75)


        self.button = QtGui.QPushButton('Page Two', self)
        self.button.clicked.connect(self.pageTwo)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(220, 30)
        self.button.setFixedSize(100,75)


        self.button2 = QtGui.QPushButton('Page Three', self)
        self.button2.clicked.connect(self.pageThree)
        self.button2.setIconSize(QtCore.QSize(24,24))
        self.button2.move(420, 30)
        self.button2.setFixedSize(100,75)



        self.button4 = QtGui.QPushButton('Quit', self)
        self.button4.clicked.connect(self.close_application)
        self.button4.setIconSize(QtCore.QSize(24,24))
        self.button4.move(620, 500)
        self.button4.setFixedSize(100,75)


        # Open a FILE and append to screen
        self.buttonSelect = QtGui.QPushButton('Select Wav', self)
        self.buttonSelect.move(135, 200)
        #self.buttonSelect.clicked.connect(self.computeInitialFigure)


        self.main_widget = QtGui.QWidget(self)

        l = QtGui.QVBoxLayout(self.main_widget)
        sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)

        l.addWidget(sc)
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.statusBar().showMessage("All hail matplotlib!", 2000)




    def close_application(self):
        print("whooaaaa so custom!!!")
        sys.exit()


    def startPage(self):

        self.hide()
        startpage = mainWindow(self)
        startpage.show()


    def pageTwo(self):

        self.hide()
        pagetwo = pageTwo(self)
        pagetwo.show()

    def pageThree(self):
        self.hide()
        pagethree = pageThree(self)
        pagethree.show()







#_________________________________________________________________________
#_________________________________________________________________________
#_________________________________________________________________________
#_________________________________________________________________________
#_________________________________________________________________________
#_________________________________________________________________________

class mainWindow(QtGui.QMainWindow):

    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,800,600)
        self.setWindowTitle("Intel")
        self.setWindowIcon(QtGui.QIcon("Intel.png"))
        self.setStyleSheet("font-size:15px")




#_________________________________________________________________________
#(Menubah)


        self.myQMenuBar = QtGui.QMenuBar(self)

        FileMenu = self.myQMenuBar.addMenu('File')
        AboutMenu = self.myQMenuBar.addMenu('Help')

#______________


        exitAction = QtGui.QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Quit Program')
        exitAction.triggered.connect(QtGui.qApp.quit)



        popupmsgAction = QtGui.QAction('ReportErrors', self)
        popupmsgAction.setStatusTip('Popup')
        popupmsgAction.triggered.connect(self.popupmsg)


        FileMenu.addAction(exitAction)

        AboutMenu.addAction(popupmsgAction)



#_________________________________________________________________________
#

#Canvas------------------
# button move  (over, down)

        self.button = QtGui.QPushButton('Home', self)
        self.button.clicked.connect(self.startPage)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(20, 30)
        self.button.setFixedSize(100,75)


        self.button = QtGui.QPushButton('Page Two', self)
        self.button.clicked.connect(self.pageTwo)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(220, 30)
        self.button.setFixedSize(100,75)


        self.button2 = QtGui.QPushButton('Page Three', self)
        self.button2.clicked.connect(self.pageThree)
        self.button2.setIconSize(QtCore.QSize(24,24))
        self.button2.move(420, 30)
        self.button2.setFixedSize(100,75)



        self.button4 = QtGui.QPushButton('Quit', self)
        self.button4.clicked.connect(self.close_application)
        self.button4.setIconSize(QtCore.QSize(24,24))
        self.button4.move(620, 500)
        self.button4.setFixedSize(100,75)



        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Home")
        self.lbl.move(390,100)

        self.show()



#_________________________________________________________________________
#
    def popupmsg(self):
        msg = QtGui.QMessageBox.question(self, "Error!",
                                         "If you have any questions feel free to ask.  Email me at EdwinX.Eames@intel.com",
                                         QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if msg == QtGui.QMessageBox.Yes:

            sys.exit()
        else:
            pass





    def close_application(self):
        print("whooaaaa so custom!!!")
        sys.exit()


    def startPage(self):

        self.hide()
        startpage = mainWindow(self)
        startpage.show()


    def pageTwo(self):

        self.hide()
        pagetwo = pageTwo(self)
        pagetwo.show()

    def pageThree(self):
        self.hide()
        pagethree = pageThree(self)
        pagethree.show()




def main():
    app = QtGui.QApplication(sys.argv)
    main = mainWindow()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()