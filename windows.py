__author__ = 'eeamesX'

import sys
import os



from matplotlib.backends import qt4_compat

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


class pageTwo(QtGui.QMainWindow):
    def __init__(self,parent = None):
        QtGui.QMainWindow.__init__(self, parent)

        self.initUI()

    def initUI(self):
# button move  (over, down)
        self.setGeometry(300,300,1280,800)
        self.setWindowTitle("Intel")
        self.setWindowIcon(QtGui.QIcon("Intel Converter"))
        self.setStyleSheet("font-size:15px")


#_________________________________________________________________________
#(Menubah)


        self.myQMenuBar = QtGui.QMenuBar(self)
        self.toolBar = QtGui.QToolBar(self)
        FileMenu = self.myQMenuBar.addMenu('File')
        AboutMenu = self.myQMenuBar.addMenu('Help')

#______________
###Actions

        exitAction = QtGui.QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Quit Program')
        exitAction.triggered.connect(QtGui.qApp.quit)

        popupmsgAction = QtGui.QAction('ReportErrors', self)
        popupmsgAction.setStatusTip('Popup')
        popupmsgAction.triggered.connect(self.popupmsg)


###Icon bar

        extractAction = QtGui.QAction(QtGui.QIcon('homologo.png'), 'Home Page', self)
        extractAction.triggered.connect(self.close_application)
        FileMenu.addAction(exitAction)

        extractAction = QtGui.QAction(QtGui.QIcon('convertogo.png'), 'Convert Page', self)
        extractAction.triggered.connect(self.close_application)
        FileMenu.addAction(exitAction)

        extractAction = QtGui.QAction(QtGui.QIcon('graphlogo.png'), 'Data Page', self)
        extractAction.triggered.connect(self.close_application)
        FileMenu.addAction(exitAction)

        AboutMenu.addAction(popupmsgAction)
##Calnder
        cal = QtGui.QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 100)
        cal.resize(200,200)
        cal.clicked[QtCore.QDate].connect(self.showDate)
####








#Split Frames

##

#_________________________________________________________________________
#

#Canvas------------------
# button move  (over, down)



        self.lbl = QtGui.QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(70, 300)


        extractAction = QtGui.QAction(QtGui.QIcon('homelogo.png'), 'Home Page', self)
        extractAction.triggered.connect(self.startPage)

        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        extractAction = QtGui.QAction(QtGui.QIcon('convertlogo.png'), 'Convert Page', self)
        extractAction.triggered.connect(self.pageTwo)

        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)


        extractAction = QtGui.QAction(QtGui.QIcon('graphlogo.png'), 'Data Page', self)
        extractAction.triggered.connect(self.pageThree)

        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Page Two")
        self.lbl.move(20,100)

        self.button = QtGui.QPushButton('Home', self)
        self.button.clicked.connect(self.startPage)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(20, 590)
        self.button.setFixedSize(200,75)
# button move  (over, down)

        self.button2 = QtGui.QPushButton('Page Two', self)
        self.button2.clicked.connect(self.pageTwo)
        self.button2.setIconSize(QtCore.QSize(24,24))
        self.button2.move(20, 645)
        self.button2.setFixedSize(200,75)


        self.button3 = QtGui.QPushButton('Page Three', self)
        self.button3.clicked.connect(self.pageThree)
        self.button3.setIconSize(QtCore.QSize(24,24))
        self.button3.move(20, 700)
        self.button3.setFixedSize(200,75)

# button move  (over, down)


        self.listWidget = QtGui.QListWidget(self)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget.move(360,300)
        self.listWidget.resize(300,300)

        self.listWidgetcomplete = QtGui.QListWidget(self)
        self.listWidgetcomplete.setObjectName(_fromUtf8("listWidget"))
        self.listWidgetcomplete.move(780,300)
        self.listWidgetcomplete.resize(300,300)



    # Open a FILE and append to screen
        self.selectFileButton = QtGui.QPushButton('Select Files', self)
        self.selectFileButton.move(455, 250)
        self.selectFileButton.clicked.connect(self.selectFile)




    # Open a FILE and append to screen
        self.convertButton = QtGui.QPushButton('Convert!', self)
        self.convertButton.move(670,400)
        self.convertButton.clicked.connect(self.osconvertfile)




    def popupmsg(self):
        msg = QtGui.QMessageBox.question(self, "Error!",
                                         "If you have any questions feel free to ask.  Email me at EdwinX.Eames@intel.com",
                                         QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if msg == QtGui.QMessageBox.Yes:

            sys.exit()
        else:
            pass



    def showDate(self, date):

        self.lbl.setText(date.toString())



    def close_application(self):
        print("whooaaaa you quit!!")
        sys.exit()




    def startPage(self):

        self.hide()
        startpage = mainWindow(self)
        startpage.show()
        print ("Now Entering Start Page")


    def pageTwo(self):

        self.hide()
        pagetwo = pageTwo(self)
        pagetwo.show()
        print ("Now Entering Page Two")

    def pageThree(self):
        self.hide()
        pagethree = pageThree(self)
        pagethree.show()
        print ("Now Entering Page Three")


# **************
#Functions


    def selectFile(self):


        self.listWidget.clear() # In case there are any existing elements in the list
        directory = QtGui.QFileDialog.getExistingDirectory(self, "Pick a folder")
        print directory


        for file_name in os.listdir(directory):
            if file_name.endswith(".csv"):
                self.listWidget.addItem(file_name)
                print (file_name)
        self.directory = directory
        return directory





    def osconvertfile(self):


        directoryPath = self.directory
        print directoryPath

        cmd = ('python createXMLFromCSV.py '
               +str(directoryPath))
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







class pageThree(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.initUI()





    def initUI(self):
        self.setGeometry(300,300,1280,800)
        self.setWindowTitle("Intel")
        self.setWindowIcon(QtGui.QIcon("Intel.png"))
        #self.setStyleSheet("background-color: rgb(255, 255, 255);\n")
                           #"border:1px solid rgb(0, 131, 195);")



#_________________________________________________________________________
#(Menubah)


        self.myQMenuBar = QtGui.QMenuBar(self)

        FileMenu = self.myQMenuBar.addMenu('File')
        AboutMenu = self.myQMenuBar.addMenu('Help')

#______________
###Actions

        exitAction = QtGui.QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Quit Program')
        exitAction.triggered.connect(QtGui.qApp.quit)

        popupmsgAction = QtGui.QAction('ReportErrors', self)
        popupmsgAction.setStatusTip('Popup')
        popupmsgAction.triggered.connect(self.popupmsg)










###Icon bar

        extractAction = QtGui.QAction(QtGui.QIcon('homologo.png'), 'Home Page', self)
        extractAction.triggered.connect(self.close_application)
        FileMenu.addAction(exitAction)

        extractAction = QtGui.QAction(QtGui.QIcon('convertogo.png'), 'Convert Page', self)
        extractAction.triggered.connect(self.close_application)
        FileMenu.addAction(exitAction)

        extractAction = QtGui.QAction(QtGui.QIcon('graphlogo.png'), 'Data Page', self)
        extractAction.triggered.connect(self.close_application)
        FileMenu.addAction(exitAction)

        AboutMenu.addAction(popupmsgAction)
##Calnder
        cal = QtGui.QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 100)
        cal.resize(200,200)
        cal.clicked[QtCore.QDate].connect(self.showDate)
####








#Split Frames

##

#_________________________________________________________________________
#

#Canvas------------------
# button move  (over, down)




        self.lbl = QtGui.QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(70, 300)


        extractAction = QtGui.QAction(QtGui.QIcon('homelogo.png'), 'Home Page', self)
        extractAction.triggered.connect(self.startPage)

        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        extractAction = QtGui.QAction(QtGui.QIcon('convertlogo.png'), 'Convert Page', self)
        extractAction.triggered.connect(self.pageTwo)

        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)


        extractAction = QtGui.QAction(QtGui.QIcon('graphlogo.png'), 'Data Page', self)
        extractAction.triggered.connect(self.pageThree)

        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)





        self.button = QtGui.QPushButton('Home', self)
        self.button.clicked.connect(self.startPage)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(20, 590)
        self.button.setFixedSize(200,75)


        self.button2 = QtGui.QPushButton('Page Two', self)
        self.button2.clicked.connect(self.pageTwo)
        self.button2.setIconSize(QtCore.QSize(24,24))
        self.button2.move(20, 645)
        self.button2.setFixedSize(200,75)


        self.button3 = QtGui.QPushButton('Page Three', self)
        self.button3.clicked.connect(self.pageThree)
        self.button3.setIconSize(QtCore.QSize(24,24))
        self.button3.move(20, 700)
        self.button3.setFixedSize(200,75)






        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Data Team Program")
        self.lbl.resize(145, 25)
        self.lbl.move(580,40)


        self.pixmap = QtGui.QPixmap("intelmed.png")

        self.lbl2 = QtGui.QLabel(self)
        self.lbl2.setPixmap(self.pixmap)
        self.lbl2.move(1000,40)
        self.lbl2.resize(300,200)



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




    def showDate(self, date):

        self.lbl.setText(date.toString())
    def close_application(self):
        print("whooaaaa so custom!!!")
        sys.exit()


    def startPage(self):

        self.hide()
        startpage = mainWindow(self)
        startpage.show()
        print ("Now Entering Start Page")


    def pageTwo(self):

        self.hide()
        pagetwo = pageTwo(self)
        pagetwo.show()
        print ("Now Entering Page Two")

    def pageThree(self):
        self.hide()
        pagethree = pageThree(self)
        pagethree.show()
        print ("Now Entering Page Three")










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
        self.setGeometry(300,300,1280,800)
        self.setWindowTitle("Intel")
        self.setWindowIcon(QtGui.QIcon("Intel.png"))
        #self.setStyleSheet("background-color: rgb(255, 255, 255);\n")
                           #"border:1px solid rgb(0, 131, 195);")



#_________________________________________________________________________
#(Menubah)


        self.myQMenuBar = QtGui.QMenuBar(self)

        FileMenu = self.myQMenuBar.addMenu('File')
        AboutMenu = self.myQMenuBar.addMenu('Help')

#______________
###Actions

        exitAction = QtGui.QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Quit Program')
        exitAction.triggered.connect(QtGui.qApp.quit)

        popupmsgAction = QtGui.QAction('ReportErrors', self)
        popupmsgAction.setStatusTip('Popup')
        popupmsgAction.triggered.connect(self.popupmsg)










###Icon bar

        extractAction = QtGui.QAction(QtGui.QIcon('homologo.png'), 'Home Page', self)
        extractAction.triggered.connect(self.close_application)
        FileMenu.addAction(exitAction)

        extractAction = QtGui.QAction(QtGui.QIcon('convertogo.png'), 'Convert Page', self)
        extractAction.triggered.connect(self.close_application)
        FileMenu.addAction(exitAction)

        extractAction = QtGui.QAction(QtGui.QIcon('graphlogo.png'), 'Data Page', self)
        extractAction.triggered.connect(self.close_application)
        FileMenu.addAction(exitAction)

        AboutMenu.addAction(popupmsgAction)
##Calnder
        cal = QtGui.QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 100)
        cal.resize(200,200)
        cal.clicked[QtCore.QDate].connect(self.showDate)
####








#Split Frames

##

#_________________________________________________________________________
#

#Canvas------------------
# button move  (over, down)




        self.lbl = QtGui.QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(70, 300)


        extractAction = QtGui.QAction(QtGui.QIcon('homelogo.png'), 'Home Page', self)
        extractAction.triggered.connect(self.startPage)

        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        extractAction = QtGui.QAction(QtGui.QIcon('convertlogo.png'), 'Convert Page', self)
        extractAction.triggered.connect(self.pageTwo)

        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)


        extractAction = QtGui.QAction(QtGui.QIcon('graphlogo.png'), 'Data Page', self)
        extractAction.triggered.connect(self.pageThree)

        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)





        self.button = QtGui.QPushButton('Home', self)
        self.button.clicked.connect(self.startPage)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(20, 590)
        self.button.setFixedSize(200,75)


        self.button = QtGui.QPushButton('Page Two', self)
        self.button.clicked.connect(self.pageTwo)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(20, 645)
        self.button.setFixedSize(200,75)


        self.button2 = QtGui.QPushButton('Page Three', self)
        self.button2.clicked.connect(self.pageThree)
        self.button2.setIconSize(QtCore.QSize(24,24))
        self.button2.move(20, 700)
        self.button2.setFixedSize(200,75)






        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Data Team Program")
        self.lbl.resize(145, 25)
        self.lbl.move(580,40)


        self.pixmap = QtGui.QPixmap("intelmed.png")

        self.lbl2 = QtGui.QLabel(self)
        self.lbl2.setPixmap(self.pixmap)
        self.lbl2.move(1000,40)
        self.lbl2.resize(300,200)



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




    def showDate(self, date):

        self.lbl.setText(date.toString())
    def close_application(self):
        print("whooaaaa so custom!!!")
        sys.exit()


    def startPage(self):

        self.hide()
        startpage = mainWindow(self)
        startpage.show()
        print ("Now Entering Start Page")


    def pageTwo(self):

        self.hide()
        pagetwo = pageTwo(self)
        pagetwo.show()
        print ("Now Entering Page Two")

    def pageThree(self):
        self.hide()
        pagethree = pageThree(self)
        pagethree.show()
        print ("Now Entering Page Three")




def main():
    app = QtGui.QApplication(sys.argv)
    main = mainWindow()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()