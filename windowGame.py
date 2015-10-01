__author__ = 'ed'
import sys
import os
import subprocess
import windows
import csvtoxmlPage
import windowConvertor
import windowDatascience
import windowRemoteupload



from PyQt4 import QtGui, QtCore

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s



class gamerWindow(QtGui.QMainWindow):
    def __init__(self, parent):
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




#______________
###Actions

        centralwidget = QtGui.QWidget(gameWindow)
        centralwidget.setObjectName(_fromUtf8("centralwidget"))
        frame = QtGui.QFrame(self.centralwidget)
        frame.setGeometry(QtCore.QRect(10, 70, 331, 671))
        frame.setFrameShape(QtGui.QFrame.StyledPanel)
        frame.setFrameShadow(QtGui.QFrame.Raised)

#______________
###Icon bar

        extractActionHome = QtGui.QAction(QtGui.QIcon('homelogo.png'), 'Home Page', self)
        extractActionHome.triggered.connect(self.startPage)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActionHome)



        extractActionConvert = QtGui.QAction(QtGui.QIcon('convertlogo.png'), 'Convert Page', self)
        extractActionConvert.triggered.connect(self.pageTwo)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActionConvert)




        extractActiondataScience = QtGui.QAction(QtGui.QIcon('graphlogo.png'), 'Data Page', self)
        extractActiondataScience.triggered.connect(self.pageThree)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiondataScience)

        extractActiondataRelease = QtGui.QAction(QtGui.QIcon('dataRelease.png'), 'Data Release', self)
        extractActiondataRelease.triggered.connect(self.pageFour)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiondataRelease)

        extractActiongameWindow = QtGui.QAction(QtGui.QIcon('gamelogo.png'), 'Game Page', self)
        extractActiongameWindow.triggered.connect(self.pageFive)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiongameWindow)

















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
        pagetwo = convertorPage(self)
        pagetwo.show()
        print ("Now Entering Page Two")

    def pageThree(self):
        self.hide()
        pagethree = dataScience(self)
        pagethree.show()
        print ("Now Entering Page Three")


    def pageFour(self):

        self.hide()
        pageFour = dataRelease(self)
        pageFour.show()
        print ("Now Entering Page 4")

    def pageFive(self):
        self.hide()
        pageFive = gameWindow(self)
        pageFive.show()
        print ("Now Entering Page 5")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    childwindow = gamerWindow()
    childwindow.show()

    sys.exit(app.exec_())



