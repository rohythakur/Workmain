__author__ = 'ed'
import sys
import os
import subprocess


import windows
import csvtoxmlPage
import windowConvertor

import windowRemoteupload
import windowGame




from PyQt4 import QtGui, QtCore

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s





class dataScience(QtGui.QMainWindow):
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




        self.button = QtGui.QPushButton('Home', self)
        self.button.clicked.connect(self.startPage)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(20, 480)
        self.button.setFixedSize(200,75)
# button move  (over, down)

        self.button2 = QtGui.QPushButton('Convertor Page', self)
        self.button2.clicked.connect(self.pageTwo)
        self.button2.setIconSize(QtCore.QSize(24,24))
        self.button2.move(20, 535)
        self.button2.setFixedSize(200,75)


        self.button3 = QtGui.QPushButton('Data Science', self)
        self.button3.clicked.connect(self.pageThree)
        self.button3.setIconSize(QtCore.QSize(24,24))
        self.button3.move(20, 590)
        self.button3.setFixedSize(200,75)



        self.button5 = QtGui.QPushButton('Remote File Upload', self)
        self.button5.clicked.connect(self.pageFour)
        self.button5.setIconSize(QtCore.QSize(24,24))
        self.button5.move(20, 645)
        self.button5.setFixedSize(200,75)

        self.button6 = QtGui.QPushButton('Game Page', self)
        self.button6.clicked.connect(self.pageFive)
        self.button6.setIconSize(QtCore.QSize(24,24))
        self.button6.move(20, 700)
        self.button6.setFixedSize(200,75)





        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Data Science")
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
    childwindow = dataScience()
    childwindow.show()

    sys.exit(app.exec_())






