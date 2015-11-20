__author__ = 'eeamesX'

import sys
import os
import subprocess
import metaDataCreator
import glob
import time
from collections import defaultdict
from shutil import copyfile
import shutil
from PyQt4 import QtGui, QtCore

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s





abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)

class gameWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.initUI()





    def initUI(self):
        self.setGeometry(300,300,1280,800)
        self.setWindowTitle("Intel")
        #self.setWindowIcon(QtGui.QIcon("images/Intelmed.png"))
        #self.setStyleSheet("background-color: rgb(255, 255, 255);\n")
                           #"border:1px solid rgb(0, 131, 195);")



#_________________________________________________________________________
#(Menubah)

        extractActionHome = QtGui.QAction(QtGui.QIcon('images/homelogo.png'), 'Home Page', self)
        extractActionHome.triggered.connect(self.startPage)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActionHome)




        extractActionConvert = QtGui.QAction(QtGui.QIcon('images/convertlogo.png'), 'Convert Page', self)
        extractActionConvert.triggered.connect(self.pageTwo)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActionConvert)




        extractActiondataScience = QtGui.QAction(QtGui.QIcon('images/graphlogo.png'), 'Data Page', self)
        extractActiondataScience.triggered.connect(self.pageThree)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiondataScience)

        extractActiondataRelease = QtGui.QAction(QtGui.QIcon('images/dataRelease.png'), 'Data Release', self)
        extractActiondataRelease.triggered.connect(self.pageFour)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiondataRelease)

        extractActiongameWindow = QtGui.QAction(QtGui.QIcon('images/gamelogo.png'), 'Tools', self)
        extractActiongameWindow.triggered.connect(self.pageFive)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiongameWindow)
##Calnder







        self.button = QtGui.QPushButton('Home', self)
        self.button.clicked.connect(self.startPage)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(20, 480)
        self.button.setFixedSize(200,75)
# button move  (over, down)

        self.button2 = QtGui.QPushButton('Data Processing', self)
        self.button2.clicked.connect(self.pageTwo)
        self.button2.setIconSize(QtCore.QSize(24,24))
        self.button2.move(20, 535)
        self.button2.setFixedSize(200,75)


        self.button3 = QtGui.QPushButton('Data Release ', self)
        self.button3.clicked.connect(self.pageThree)
        self.button3.setIconSize(QtCore.QSize(24,24))
        self.button3.move(20, 590)
        self.button3.setFixedSize(200,75)



        self.button5 = QtGui.QPushButton('Remote File Upload', self)
        self.button5.clicked.connect(self.pageFour)
        self.button5.setIconSize(QtCore.QSize(24,24))
        self.button5.move(20, 645)
        self.button5.setFixedSize(200,75)

        self.button6 = QtGui.QPushButton('Tools', self)
        self.button6.clicked.connect(self.pageFive)
        self.button6.setIconSize(QtCore.QSize(24,24))
        self.button6.move(20, 700)
        self.button6.setFixedSize(200,75)





        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Data Team Program")
        self.lbl.resize(145, 25)
        self.lbl.move(580,40)


        self.pixmap = QtGui.QPixmap("images/intelmed.png")

        self.lbl2 = QtGui.QLabel(self)
        self.lbl2.setPixmap(self.pixmap)
        self.lbl2.move(10,50)
        self.lbl2.resize(300,200)




        self.buttonMove = QtGui.QPushButton('Group Files', self)
        self.buttonMove.clicked.connect(self.moveFiles)
        self.buttonMove.setIconSize(QtCore.QSize(24,24))
        self.buttonMove.move(250, 250)
        self.buttonMove.setFixedSize(200,75)

        self.buttonMove = QtGui.QPushButton('CSV to XML', self)
        self.buttonMove.clicked.connect(self.csvtoXml)
        self.buttonMove.setIconSize(QtCore.QSize(24,24))
        self.buttonMove.move(250, 350)
        self.buttonMove.setFixedSize(200,75)



        self.buttonMove = QtGui.QPushButton('Future Tool', self)
        self.buttonMove.clicked.connect(self.moveFiles)
        self.buttonMove.setIconSize(QtCore.QSize(24,24))
        self.buttonMove.move(250, 450)
        self.buttonMove.setFixedSize(200,75)



        self.buttonMove = QtGui.QPushButton('Future Tool', self)
        self.buttonMove.clicked.connect(self.moveFiles)
        self.buttonMove.setIconSize(QtCore.QSize(24,24))
        self.buttonMove.move(250, 550)
        self.buttonMove.setFixedSize(200,75)





        self.show()
#_________________________________________________________________________



    def moveFiles(self):
        from tools.moveFiles import moveWindow
        movePage = moveWindow()
        movePage.show()
        print cmd
        QtGui.qApp.processEvents()
        #os.system(cmd)
        QtGui.qApp.processEvents()

        #Improve this section


    def csvtoXml(self):
        from tools.csvmaker import csvWindow
        csvPage = csvWindow()
        csvPage.show()
        print cmd
        QtGui.qApp.processEvents()
        #os.system(cmd)
        QtGui.qApp.processEvents()

        #Improve this section


    def close_application(self):
        print("whooaaaa so custom!!!")
        sys.exit()


    def startPage(self):

        self.close()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed********************** on self.close")
        startpage = mainWindow(self)
        startpage.show()

        print ("Now Entering Start Page")


    def pageTwo(self):

        self.close()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed********************** on self.close")

        pagetwo = convertorPage(self)
        pagetwo.show()
        print ("Now Entering Page Two")

    def pageThree(self):
        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pagethree = dataScience(self)
        pagethree.show()
        print ("Now Entering Page Three")


    def pageFour(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFour = dataRelease(self)
        pageFour.show()
        print ("Now Entering Page 4")

    def pageFive(self):


        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFive = gameWindow(self)
        pageFive.show()
        print ("Now Entering Page 5")



class dataRelease(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.initUI()





    def initUI(self):
        self.setGeometry(300,300,1280,800)
        self.setWindowTitle("Intel")
        self.setWindowIcon(QtGui.QIcon("images/Intel.png"))
        #self.setStyleSheet("background-color: rgb(255, 255, 255);\n")
                           #"border:1px solid rgb(0, 131, 195);")



#_________________________________________________________________________
#(Menubah)



###Icon bar

        extractActionHome = QtGui.QAction(QtGui.QIcon('images/homelogo.png'), 'Home Page', self)
        extractActionHome.triggered.connect(self.startPage)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActionHome)



        extractActionConvert = QtGui.QAction(QtGui.QIcon('images/convertlogo.png'), 'Convert Page', self)
        extractActionConvert.triggered.connect(self.pageTwo)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActionConvert)




        extractActiondataScience = QtGui.QAction(QtGui.QIcon('images/graphlogo.png'), 'Data Page', self)
        extractActiondataScience.triggered.connect(self.pageThree)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiondataScience)

        extractActiondataRelease = QtGui.QAction(QtGui.QIcon('images/dataRelease.png'), 'Data Release', self)
        extractActiondataRelease.triggered.connect(self.pageFour)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiondataRelease)

        extractActiongameWindow = QtGui.QAction(QtGui.QIcon('images/gamelogo.png'), 'Game Page', self)
        extractActiongameWindow.triggered.connect(self.pageFive)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiongameWindow)

##Calnder
        self.pixmap = QtGui.QPixmap("images/intelmed.png")

        self.lbl2 = QtGui.QLabel(self)
        self.lbl2.setPixmap(self.pixmap)
        self.lbl2.move(10,50)
        self.lbl2.resize(300,200)









        self.button = QtGui.QPushButton('Home', self)
        self.button.clicked.connect(self.startPage)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(20, 480)
        self.button.setFixedSize(200,75)
# button move  (over, down)

        self.button2 = QtGui.QPushButton('Data Processing', self)
        self.button2.clicked.connect(self.pageTwo)
        self.button2.setIconSize(QtCore.QSize(24,24))
        self.button2.move(20, 535)
        self.button2.setFixedSize(200,75)


        self.button3 = QtGui.QPushButton('Data Release', self)
        self.button3.clicked.connect(self.pageThree)
        self.button3.setIconSize(QtCore.QSize(24,24))
        self.button3.move(20, 590)
        self.button3.setFixedSize(200,75)



        self.button5 = QtGui.QPushButton('Remote File Upload', self)
        self.button5.clicked.connect(self.pageFour)
        self.button5.setIconSize(QtCore.QSize(24,24))
        self.button5.move(20, 645)
        self.button5.setFixedSize(200,75)

        self.button6 = QtGui.QPushButton('Tools', self)
        self.button6.clicked.connect(self.pageFive)
        self.button6.setIconSize(QtCore.QSize(24,24))
        self.button6.move(20, 700)
        self.button6.setFixedSize(200,75)


# button move  (over, down)

        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Uploading/ Downloading Made Easy")
        self.lbl.resize(245, 125)
        self.lbl.move(600,20)






        self.button = QtGui.QPushButton('Upload', self)
        self.button.clicked.connect(self.uploadPage)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(450, 120)

# button move  (over, down)

        self.button2 = QtGui.QPushButton('Download', self)
        self.button2.clicked.connect(self.downloadPage)
        self.button2.setIconSize(QtCore.QSize(24,24))
        self.button2.move(850, 120)




#_--------





        self.show()



#_________________________________________________________________________





    def close_application(self):
        print("whooaaaa so custom!!!")
        sys.exit()




    def directoryChoice(self):
        self.listWidget.clear()

        directoryChoice = QtGui.QFileDialog.getExistingDirectory(self, "Pick a folder")

        self.listWidget.addItem(directoryChoice)
        print directoryChoice
        return directoryChoice

    def fileChoice(self):
        self.listWidget.clear()
        fileChoice = QtGui.QFileDialog.getOpenFileName(self, "Pick a folder")
        self.listWidget.addItem(fileChoice)

        print fileChoice
        return fileChoice






    def upload_button(self):
        directoryUser = self.directoryChoice()

        username = self.userName.text()
        filepath = self.listWidgetdest.text()




        cmdIvr = ('rsync  -av --progress ' +                                                                                                                                                                                                                                                 str(directoryUser)+ ' ' + str(username) +
                '@10.127.235.151:' + str(filepath))




        print cmdIvr
        print "button 1"

        os.system(cmdIvr)







    def downloadPage(self):
        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        startpage = downloadWindow(self)
        startpage.show()
        print ("Now Entering download Page")

    def uploadPage(self):
        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        startpage = uploadWindow(self)
        startpage.show()
        print ("Now Entering upload Page")


    def startPage(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        startpage = mainWindow(self)
        startpage.show()

        print ("Now Entering Start Page")


    def pageTwo(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")

        pagetwo = convertorPage(self)
        pagetwo.show()
        print ("Now Entering Page Two")

    def pageThree(self):
        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pagethree = dataScience(self)
        pagethree.show()
        print ("Now Entering Page Three")


    def pageFour(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFour = dataRelease(self)
        pageFour.show()
        print ("Now Entering Page 4")

    def pageFive(self):


        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFive = gameWindow(self)
        pageFive.show()
        print ("Now Entering Page 5")




class uploadWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.initUI()





    def initUI(self):
        self.setGeometry(300,300,1280,800)
        self.setWindowTitle("Intel")
        self.setWindowIcon(QtGui.QIcon("images/Intel.png"))
        #self.setStyleSheet("background-color: rgb(255, 255, 255);\n")
                           #"border:1px solid rgb(0, 131, 195);")



#_________________________________________________________________________
#(Menubah)



###Icon bar

        extractActionHome = QtGui.QAction(QtGui.QIcon('images/homelogo.png'), 'Home Page', self)
        extractActionHome.triggered.connect(self.startPage)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActionHome)



        extractActionConvert = QtGui.QAction(QtGui.QIcon('images/convertlogo.png'), 'Convert Page', self)
        extractActionConvert.triggered.connect(self.pageTwo)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActionConvert)




        extractActiondataScience = QtGui.QAction(QtGui.QIcon('images/graphlogo.png'), 'Data Page', self)
        extractActiondataScience.triggered.connect(self.pageThree)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiondataScience)

        extractActiondataRelease = QtGui.QAction(QtGui.QIcon('images/dataRelease.png'), 'Data Release', self)
        extractActiondataRelease.triggered.connect(self.pageFour)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiondataRelease)

        extractActiongameWindow = QtGui.QAction(QtGui.QIcon('images/gamelogo.png'), 'Game Page', self)
        extractActiongameWindow.triggered.connect(self.pageFive)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiongameWindow)

##Calnder
        self.pixmap = QtGui.QPixmap("images/intelmed.png")

        self.lbl2 = QtGui.QLabel(self)
        self.lbl2.setPixmap(self.pixmap)
        self.lbl2.move(10,50)
        self.lbl2.resize(300,200)









        self.button = QtGui.QPushButton('Home', self)
        self.button.clicked.connect(self.startPage)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(20, 480)
        self.button.setFixedSize(200,75)
# button move  (over, down)

        self.button2 = QtGui.QPushButton('Data Processing', self)
        self.button2.clicked.connect(self.pageTwo)
        self.button2.setIconSize(QtCore.QSize(24,24))
        self.button2.move(20, 535)
        self.button2.setFixedSize(200,75)


        self.button3 = QtGui.QPushButton('Data Release', self)
        self.button3.clicked.connect(self.pageThree)
        self.button3.setIconSize(QtCore.QSize(24,24))
        self.button3.move(20, 590)
        self.button3.setFixedSize(200,75)



        self.button5 = QtGui.QPushButton('Remote File Upload', self)
        self.button5.clicked.connect(self.pageFour)
        self.button5.setIconSize(QtCore.QSize(24,24))
        self.button5.move(20, 645)
        self.button5.setFixedSize(200,75)

        self.button6 = QtGui.QPushButton('Tools', self)
        self.button6.clicked.connect(self.pageFive)
        self.button6.setIconSize(QtCore.QSize(24,24))
        self.button6.move(20, 700)
        self.button6.setFixedSize(200,75)


# button move  (over, down)

        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Uploading/ Downloading Made Easy")
        self.lbl.resize(245, 125)
        self.lbl.move(600,20)





        self.button = QtGui.QPushButton('Upload', self)
        self.button.clicked.connect(self.uploadPage)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(450, 120)

# button move  (over, down)

        self.button2 = QtGui.QPushButton('Download', self)
        self.button2.clicked.connect(self.downloadPage)
        self.button2.setIconSize(QtCore.QSize(24,24))
        self.button2.move(850, 120)






        self.btnFolder = QtGui.QPushButton('Select Folder', self)
        self.btnFolder.move(320, 390)
        self.btnFolder.clicked.connect(self.directoryChoice)


        self.btnFile = QtGui.QPushButton('Select File', self)
        self.btnFile.move(420, 390)
        self.btnFile.clicked.connect(self.fileChoice)

        self.listWidget = QtGui.QListWidget(self)
        self.listWidget.move(550,390)
        self.listWidget.resize(300,30)






        self.btnDest = QtGui.QPushButton('Destination', self)
        self.btnDest.move(420, 500)
        self.btnDest.clicked.connect(self.fileChoice)

        self.listWidgetdest = QtGui.QListWidget(self)
        self.listWidgetdest.move(550,500)
        self.listWidgetdest.resize(300,30)





        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("ssh username")
        self.lbl.resize(345, 25)
        self.lbl.move(410,280)


        self.userName = QtGui.QLineEdit(self)
        self.userName.setPlaceholderText('Username')
        self.userName.move(550,280)


        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("IP Address")
        self.lbl.resize(145, 25)
        self.lbl.move(700,280)


        self.address = QtGui.QLineEdit(self)
        self.address.setPlaceholderText('10.127.235.151')
        self.address.move(800,280)






        self.btnFolder = QtGui.QPushButton('Upload', self)
        self.btnFolder.move(650, 620)
        self.btnFolder.clicked.connect(self.upload_button)






#_--------





        self.show()



#_________________________________________________________________________




    def downloadPage(self):
        self.hide()
        startpage = downloadWindow(self)
        startpage.show()
        print ("Now Entering download Page")

    def uploadPage(self):
        self.hide()
        startpage = uploadWindow(self)
        startpage.show()
        print ("Now Entering upload Page")

    def close_application(self):
        print("whooaaaa so custom!!!")
        sys.exit()




    def directoryChoice(self):
        self.listWidget.clear()

        directoryChoice = QtGui.QFileDialog.getExistingDirectory(self, "Pick a folder")

        self.listWidget.addItem(directoryChoice)
        print directoryChoice
        return directoryChoice

    def fileChoice(self):
        self.listWidget.clear()
        fileChoice = QtGui.QFileDialog.getOpenFileName(self, "Pick a folder")
        self.listWidget.addItem(fileChoice)

        print fileChoice
        return fileChoice






    def upload_button(self):
        directoryUser = self.directoryChoice()

        username = self.userName.text()
        filepath = self.listWidgetdest.text()




        cmdIvr = ('rsync  -av --progress ' +                                                                                                                                                                                                                                                 str(directoryUser)+ ' ' + str(username) +
                '@10.127.235.151:' + str(filepath))




        print cmdIvr
        print "button 1"

        os.system(cmdIvr)




    def close_application(self):
        print("whooaaaa so custom!!!")
        sys.exit()



    def startPage(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        startpage = mainWindow(self)
        startpage.show()

        print ("Now Entering Start Page")


    def pageTwo(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")

        pagetwo = convertorPage(self)
        pagetwo.show()
        print ("Now Entering Page Two")

    def pageThree(self):
        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pagethree = dataScience(self)
        pagethree.show()
        print ("Now Entering Page Three")


    def pageFour(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFour = dataRelease(self)
        pageFour.show()
        print ("Now Entering Page 4")

    def pageFive(self):


        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFive = gameWindow(self)
        pageFive.show()
        print ("Now Entering Page 5")



class downloadWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.initUI()





    def initUI(self):
        self.setGeometry(300,300,1280,800)
        self.setWindowTitle("Intel")
        self.setWindowIcon(QtGui.QIcon("images/Intel.png"))
        #self.setStyleSheet("background-color: rgb(255, 255, 255);\n")
                           #"border:1px solid rgb(0, 131, 195);")



#_________________________________________________________________________
#(Menubah)



###Icon bar

        extractActionHome = QtGui.QAction(QtGui.QIcon('images/homelogo.png'), 'Home Page', self)
        extractActionHome.triggered.connect(self.startPage)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActionHome)



        extractActionConvert = QtGui.QAction(QtGui.QIcon('images/convertlogo.png'), 'Convert Page', self)
        extractActionConvert.triggered.connect(self.pageTwo)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActionConvert)




        extractActiondataScience = QtGui.QAction(QtGui.QIcon('images/graphlogo.png'), 'Data Page', self)
        extractActiondataScience.triggered.connect(self.pageThree)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiondataScience)

        extractActiondataRelease = QtGui.QAction(QtGui.QIcon('images/dataRelease.png'), 'Data Release', self)
        extractActiondataRelease.triggered.connect(self.pageFour)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiondataRelease)

        extractActiongameWindow = QtGui.QAction(QtGui.QIcon('images/gamelogo.png'), 'Game Page', self)
        extractActiongameWindow.triggered.connect(self.pageFive)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiongameWindow)

##Calnder
        self.pixmap = QtGui.QPixmap("images/intelmed.png")

        self.lbl2 = QtGui.QLabel(self)
        self.lbl2.setPixmap(self.pixmap)
        self.lbl2.move(10,50)
        self.lbl2.resize(300,200)









        self.button = QtGui.QPushButton('Home', self)
        self.button.clicked.connect(self.startPage)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(20, 480)
        self.button.setFixedSize(200,75)
# button move  (over, down)

        self.button2 = QtGui.QPushButton('Data Processing', self)
        self.button2.clicked.connect(self.pageTwo)
        self.button2.setIconSize(QtCore.QSize(24,24))
        self.button2.move(20, 535)
        self.button2.setFixedSize(200,75)


        self.button3 = QtGui.QPushButton('Data Release', self)
        self.button3.clicked.connect(self.pageThree)
        self.button3.setIconSize(QtCore.QSize(24,24))
        self.button3.move(20, 590)
        self.button3.setFixedSize(200,75)



        self.button5 = QtGui.QPushButton('Remote File Upload', self)
        self.button5.clicked.connect(self.pageFour)
        self.button5.setIconSize(QtCore.QSize(24,24))
        self.button5.move(20, 645)
        self.button5.setFixedSize(200,75)

        self.button6 = QtGui.QPushButton('Tools', self)
        self.button6.clicked.connect(self.pageFive)
        self.button6.setIconSize(QtCore.QSize(24,24))
        self.button6.move(20, 700)
        self.button6.setFixedSize(200,75)


# button move  (over, down)

        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Uploading/ Downloading Made Easy")
        self.lbl.resize(245, 125)
        self.lbl.move(600,20)





        self.button = QtGui.QPushButton('Upload', self)
        self.button.clicked.connect(self.uploadPage)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(450, 120)

# button move  (over, down)

        self.button2 = QtGui.QPushButton('Download', self)
        self.button2.clicked.connect(self.downloadPage)
        self.button2.setIconSize(QtCore.QSize(24,24))
        self.button2.move(850, 120)








#_--------





        self.show()



#_________________________________________________________________________




    def downloadPage(self):
        self.hide()
        startpage = downloadWindow(self)
        startpage.show()
        print ("Now Entering download Page")

    def uploadPage(self):
        self.hide()
        startpage = uploadWindow(self)
        startpage.show()
        print ("Now Entering upload Page")

    def close_application(self):
        print("whooaaaa so custom!!!")
        sys.exit()




    def directoryChoice(self):
        self.listWidget.clear()

        directoryChoice = QtGui.QFileDialog.getExistingDirectory(self, "Pick a folder")

        self.listWidget.addItem(directoryChoice)
        print directoryChoice
        return directoryChoice

    def fileChoice(self):
        self.listWidget.clear()
        fileChoice = QtGui.QFileDialog.getOpenFileName(self, "Pick a folder")
        self.listWidget.addItem(fileChoice)

        print fileChoice
        return fileChoice






    def upload_button(self):
        directoryUser = self.directoryChoice()

        username = self.userName.text()
        filepath = self.listWidgetdest.text()




        cmdIvr = ('rsync  -av --progress ' +                                                                                                                                                                                                                                                 str(directoryUser)+ ' ' + str(username) +
                '@10.127.235.151:' + str(filepath))




        print cmdIvr
        print "button 1"

        os.system(cmdIvr)






    def startPage(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        startpage = mainWindow(self)
        startpage.show()

        print ("Now Entering Start Page")


    def pageTwo(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")

        pagetwo = convertorPage(self)
        pagetwo.show()
        print ("Now Entering Page Two")

    def pageThree(self):
        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pagethree = dataScience(self)
        pagethree.show()
        print ("Now Entering Page Three")


    def pageFour(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFour = dataRelease(self)
        pageFour.show()
        print ("Now Entering Page 4")

    def pageFive(self):


        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFive = gameWindow(self)
        pageFive.show()
        print ("Now Entering Page 5")




class filesdownloadConvertorpage(QtGui.QMainWindow):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.initUI()

    def initUI(self):
# button move  (over, down)
        self.setGeometry(300,300,1280,800)
        self.setWindowTitle("Intel")
        self.setWindowIcon(QtGui.QIcon("Intel Converter"))
        self.setStyleSheet("font-size:15px")


#_________________________________________________________________________
#(Menubah)



        self.pixmap = QtGui.QPixmap("images/intelmed.png")

        self.lbl2 = QtGui.QLabel(self)
        self.lbl2.setPixmap(self.pixmap)
        self.lbl2.move(10,50)
        self.lbl2.resize(300,200)




        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Data Release Made Easy")
        self.lbl.move(630,20)
        self.lbl.resize(250,70)


        self.button = QtGui.QPushButton('Home', self)
        self.button.clicked.connect(self.startPage)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(20, 480)
        self.button.setFixedSize(200,75)
# button move  (over, down)

        self.button2 = QtGui.QPushButton('Data Processing', self)
        self.button2.clicked.connect(self.pageTwo)
        self.button2.setIconSize(QtCore.QSize(24,24))
        self.button2.move(20, 535)
        self.button2.setFixedSize(200,75)


        self.button3 = QtGui.QPushButton('Data Release ', self)
        self.button3.clicked.connect(self.pageThree)
        self.button3.setIconSize(QtCore.QSize(24,24))
        self.button3.move(20, 590)
        self.button3.setFixedSize(200,75)



        self.button5 = QtGui.QPushButton('Remote File Upload', self)
        self.button5.clicked.connect(self.pageFour)
        self.button5.setIconSize(QtCore.QSize(24,24))
        self.button5.move(20, 645)
        self.button5.setFixedSize(200,75)

        self.button6 = QtGui.QPushButton('Tools', self)
        self.button6.clicked.connect(self.pageFive)
        self.button6.setIconSize(QtCore.QSize(24,24))
        self.button6.move(20, 700)
        self.button6.setFixedSize(200,75)

# button move  (over, down)







        self.convertpageTwo = QtGui.QPushButton('IVR DATA DOWNLOAD', self)
        self.convertpageTwo.clicked.connect(self.filesdownloaderconvertor)
        self.convertpageTwo.setIconSize(QtCore.QSize(24,24))
        self.convertpageTwo.move(300,75)
        self.convertpageTwo.setFixedSize(250,50)

        self.convertpageThree = QtGui.QPushButton('IVR CLEANUP', self)
        self.convertpageThree.clicked.connect(self.filescleanupconvertor)
        self.convertpageThree.setIconSize(QtCore.QSize(24,24))
        self.convertpageThree.move(600,75)
        self.convertpageThree.setFixedSize(250,50)

        self.convertpageFour = QtGui.QPushButton('IVR CONVERSION', self)
        self.convertpageFour.clicked.connect(self.createedditconvertor)
        self.convertpageFour.setIconSize(QtCore.QSize(24,24))
        self.convertpageFour.move(900,75)
        self.convertpageFour.setFixedSize(250,50)





        self.lblNum = QtGui.QLabel(self)
        self.lblNum.setText("Select Which Language IVR Number")
        self.lblNum.resize(340, 50)
        self.lblNum.move(300,340)

        self.lblNum = QtGui.QLabel(self)
        self.lblNum.setText("(EX: ES_002, FR_002, DE_002, IT_002)")
        self.lblNum.resize(340, 50)
        self.lblNum.move(800,340)




        self.lblNumber = QtGui.QLineEdit(self)
        #self.lblNumber.setText("Select Number you want to process:")
        self.lblNumber.resize(100, 50)
        self.lblNumber.move(650,340)



        self.lblName = QtGui.QLabel(self)
        self.lblName.setText("Enter your SSH username")
        self.lblName.resize(340, 50)
        self.lblName.move(300,440)

        self.lblNum = QtGui.QLabel(self)
        self.lblNum.setText("(Assigned by Tim or Edwin)")
        self.lblNum.resize(340, 50)
        self.lblNum.move(800,440)


        self.userName = QtGui.QLineEdit(self)

        self.userName.resize(100, 50)
        self.userName.move(650,440)



        self.lblLanguage = QtGui.QLabel(self)
        self.lblLanguage.setText("Select Which Language You want to download")
        self.lblLanguage.resize(340, 50)
        self.lblLanguage.move(300,240)




        self.btnFolder = QtGui.QPushButton('Download Destination', self)
        self.btnFolder.move(300, 540)
        self.btnFolder.resize(250,80)
        self.btnFolder.clicked.connect(self.directoryChoice)


        self.listUserPath = QtGui.QLineEdit(self)
        self.listUserPath.resize(500,50)
        self.listUserPath.move(650,550)






        self.btn = QtGui.QPushButton('Download', self)
        self.btn.move(550, 670)
        self.btn.resize(140,80)
        #self.btn.clicked.connect(self.download)
        self.btn.clicked.connect(self.download_button)


        self.lblWorked = QtGui.QLabel(self)
        self.lblWorked.setText("Download was Successful! ")
        self.lblWorked.resize(340, 50)
        self.lblWorked.move(770,670)
        self.lblWorked.hide()

        self.lblFailed = QtGui.QLabel(self)
        self.lblFailed.setText("Download Failed :( ")
        self.lblFailed.resize(340, 50)
        self.lblFailed.move(770,670)
        self.lblFailed.hide()

        self.lblconnecting = QtGui.QLabel(self)
        self.lblconnecting.setText("Connecting ")
        self.lblconnecting.resize(340, 50)
        self.lblconnecting.move(770,670)
        self.lblconnecting.hide()

        self.lbldata = QtGui.QLabel(self)
        self.lbldata.setText("downloading giant wav.. ")
        self.lbldata.resize(340, 50)
        self.lbldata.move(770,670)
        self.lbldata.hide()

        self.lblwav = QtGui.QLabel(self)
        self.lblwav.setText("downloading data files.. ")
        self.lblwav.resize(340, 50)
        self.lblwav.move(770,670)
        self.lblwav.hide()



        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.addItem("")
        self.comboBox.addItem("IVR_Italy")
        self.comboBox.addItem("IVR_France")
        self.comboBox.addItem("IVR_Spain")
        self.comboBox.addItem("IVR_Germany")
        self.comboBox.move(650, 250)
        self.comboBox.resize(150,40)

        self.languageLbl = QtGui.QLabel("Download_IVR", self)
        self.languageLbl.move(650,150)
        self.comboBox.activated[str].connect(self.languageChoice)

        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(770, 670, 250, 80)




        self.show()


    def download(self):
        self.completed = 0

        while self.completed < 100:
            QtGui.qApp.processEvents()
            self.completed += 0.0001
            self.progress.setValue(self.completed)





    def checkFile(self):
        self.hide()
        convert1 = finalCheck(self)
        convert1.show()
        print 'Button Pressed'

    def languageChoice(self, text):

        self.languageLbl.setText(text)
        ivrLang = text
        return ivrLang



    def directoryChoice(self):
        self.listUserPath.clear() # In case there are any existing elements in the list
        directory = QtGui.QFileDialog.getExistingDirectory(self, "Pick a folder")
        self.listUserPath.setText(directory)
        self.directory = directory
        print directory
        return directory



    def download_button(self):

        directoryUser = self.directory
        ivrNum = self.lblNumber.text()
        username = self.userName.text()
        self.completed = 0
        ivrLang = self.languageLbl.text()


        print username
        print directoryUser
        print ivrNum
        print ivrLang
        try:

            if ivrLang == '':
                self.lblFailed.show()


            if ivrLang == 'IVR_Italy':
                self.lblWorked.hide()
                self.lblwav.hide()
                self.lblFailed.hide()
                self.lblconnecting.hide()

                while self.completed < 10:
                    QtGui.qApp.processEvents()
                    self.completed += 0.0001
                    self.progress.setValue(self.completed)
                    self.lblconnecting.show()


                cmdIvrtranscripts = ('rsync  -avp ' + str(username) +
                        '@10.127.235.151:/media/sdidrive/proj/Localization/DataCollection/'
                        +str(ivrLang) + '/Transcripts/'+str(ivrNum) + ' ' + str(directoryUser))
                self.lblconnecting.hide()
                os.system(cmdIvrtranscripts)
                while self.completed < 50:
                    QtGui.qApp.processEvents()
                    self.lbldata.show()

                    self.completed += 0.01
                    self.progress.setValue(self.completed)

                cmdIvr = ('rsync  -avp ' + str(username) +
                        '@10.127.235.151:/media/sdidrive/proj/Localization/DataCollection/'
                        +str(ivrLang) + '/' + str(ivrNum) + ' ' + str(directoryUser))



                print cmdIvr
                print cmdIvrtranscripts


                self.lbldata.hide()
                self.lblwav.show()
                os.system(cmdIvr)





                while self.completed < 100:

                    QtGui.qApp.processEvents()
                    self.completed += 0.01
                    self.progress.setValue(self.completed)
                self.lblwav.hide()
                self.lblWorked.show()

                time.sleep(2)
                self.lblWorked.hide()
                self.lblwav.hide()
                self.lblFailed.hide()
                self.lblconnecting.hide()


            if ivrLang == 'IVR_France':
                self.lblWorked.hide()
                self.lblwav.hide()
                self.lblFailed.hide()
                self.lblconnecting.hide()

                while self.completed < 10:
                    QtGui.qApp.processEvents()
                    self.completed += 0.0001
                    self.progress.setValue(self.completed)
                    self.lblconnecting.show()


                cmdIvr = ('rsync  -avp ' + str(username) +
                        '@10.127.235.151:/media/sdidrive/proj/Localization/DataCollection/'
                        +str(ivrLang) + '/' + str(ivrNum) + ' ' + str(directoryUser))



                cmdIvrtranscripts = ('rsync  -avp ' + str(username) +
                        '@10.127.235.151:/media/sdidrive/proj/Localization/DataCollection/Transcripts/FR_Transcripts'
                        + '/' +str(ivrNum)  + ' ' + str(directoryUser))


                print cmdIvr
                print cmdIvrtranscripts

                self.lblconnecting.hide()
                os.system(cmdIvrtranscripts)
                while self.completed < 50:
                    QtGui.qApp.processEvents()
                    self.lbldata.show()

                    self.completed += 0.01
                    self.progress.setValue(self.completed)
                self.lbldata.hide()
                self.lblwav.show()
                os.system(cmdIvr)


                while self.completed < 100:

                    QtGui.qApp.processEvents()
                    self.completed += 0.01
                    self.progress.setValue(self.completed)
                self.lblwav.hide()


                self.lblWorked.show()

            if ivrLang == 'IVR_Spain':
                self.lblWorked.hide()
                self.lblwav.hide()
                self.lblFailed.hide()
                self.lblconnecting.hide()

                cmdIvr = ('rsync  -avp ' + str(username) +
                        '@10.127.235.151:/media/sdidrive/proj/Localization/DataCollection/'
                        +str(ivrLang) + '/' + str(ivrNum) + ' ' + str(directoryUser))


                cmdIvrtranscripts = ('rsync  -avp ' + str(username) +
                        '@10.127.235.151:/media/sdidrive/proj/Localization/DataCollection/Transcripts/ES_Transcripts'
                        + '/' +str(ivrNum)  + ' ' + str(directoryUser))





                print cmdIvr
                print cmdIvrtranscripts

                self.lblconnecting.hide()
                os.system(cmdIvrtranscripts)
                while self.completed < 50:
                    QtGui.qApp.processEvents()
                    self.lbldata.show()

                    self.completed += 0.01
                    self.progress.setValue(self.completed)
                self.lbldata.hide()
                self.lblwav.show()
                os.system(cmdIvr)



                while self.completed < 100:

                    QtGui.qApp.processEvents()
                    self.completed += 0.01
                    self.progress.setValue(self.completed)
                self.lblwav.hide()


                self.lblWorked.show()

                time.sleep(2)
                self.lblWorked.hide()
                self.lblwav.hide()
                self.lblFailed.hide()
                self.lblconnecting.hide()



            if ivrLang == 'IVR_Germany':
                self.lblWorked.hide()
                self.lblwav.hide()
                self.lblFailed.hide()
                self.lblconnecting.hide()

                while self.completed < 10:
                    QtGui.qApp.processEvents()
                    self.completed += 0.0001
                    self.progress.setValue(self.completed)
                    self.lblconnecting.show()

                cmdIvr = ('rsync  -avp ' + str(username) +
                        '@10.127.235.151:/media/sdidrive/proj/Localization/DataCollection/'
                        +str(ivrLang) + '/' + str(ivrNum) + ' ' + str(directoryUser))

                cmdIvrtranscripts = ('rsync  -avp ' + str(username) +
                        '@10.127.235.151:/media/sdidrive/proj/Localization/DataCollection/Transcripts/DE_Transcripts'
                        + '/' +str(ivrNum)  + ' ' + str(directoryUser))


                print cmdIvr
                print cmdIvrtranscripts

                self.lblconnecting.hide()
                os.system(cmdIvrtranscripts)
                while self.completed < 50:
                    QtGui.qApp.processEvents()
                    self.lbldata.show()

                    self.completed += 0.01
                    self.progress.setValue(self.completed)
                self.lbldata.hide()
                self.lblwav.show()
                os.system(cmdIvr)


                while self.completed < 100:

                    QtGui.qApp.processEvents()
                    self.completed += 0.01
                    self.progress.setValue(self.completed)
                self.lblwav.hide()


                self.lblWorked.show()

                time.sleep(2)
                self.lblWorked.hide()
                self.lblwav.hide()
                self.lblFailed.hide()
                self.lblconnecting.hide()


        except Exception as e:
            print str(e)
            self.lblFailed.show()








    def csvtoXmlconvertor(self):
        self.hide()

        self.filescleanupconvertor = None
        self.filesdownloaderconvertor = None
        self.createedditconvertor = None

        convert1 = convertcsvtoXml(self)
        convert1.show()
        print 'Button Pressed'


    def filesdownloaderconvertor(self):
        self.hide()

        self.filescleanupconvertor = None
        #self.filesdownloaderconvertor = None
        self.createedditconvertor = None
        convert1 = filesdownloadConvertorpage(self)
        convert1.show()
        print 'Button Pressed'

    def filescleanupconvertor(self):
        self.hide()

        #self.filescleanupconvertor = None
        self.filesdownloaderconvertor = None
        self.createedditconvertor = None
        convert1 = filescleanupConvertorpage(self)
        convert1.show()
        print 'Button Pressed'

    def createedditconvertor(self):
        self.hide()

        self.filescleanupconvertor = None
        self.filesdownloaderconvertor = None
        #self.createedditconvertor = None
        convert1 = createedditConvertorpage(self)
        convert1.show()
        print 'Button Pressed'




    def startPage(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        startpage = mainWindow(self)
        startpage.show()

        print ("Now Entering Start Page")


    def pageTwo(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")

        pagetwo = convertorPage(self)
        pagetwo.show()
        print ("Now Entering Page Two")

    def pageThree(self):
        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pagethree = dataScience(self)
        pagethree.show()
        print ("Now Entering Page Three")


    def pageFour(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFour = dataRelease(self)
        pageFour.show()
        print ("Now Entering Page 4")

    def pageFive(self):


        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFive = gameWindow(self)
        pageFive.show()
        print ("Now Entering Page 5")
    def showDate(self, date):

        self.lbl.setText(date.toString())



    def close_application(self):
        print("whooaaaa you quit!!")
        sys.exit()

class filescleanupConvertorpage(QtGui.QMainWindow):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.initUI()

    def initUI(self):
# button move  (over, down)
        self.setGeometry(300,300,1280,800)
        self.setWindowTitle("Intel")
        self.setWindowIcon(QtGui.QIcon("Intel Converter"))
        self.setStyleSheet("font-size:15px")


#_________________________________________________________________________
#(Menubah)


        self.pixmap = QtGui.QPixmap("images/intelmed.png")

        self.lbl2 = QtGui.QLabel(self)
        self.lbl2.setPixmap(self.pixmap)
        self.lbl2.move(10,50)
        self.lbl2.resize(300,200)




        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Data Release Made Easy")
        self.lbl.move(630,20)
        self.lbl.resize(250,70)


        self.button = QtGui.QPushButton('Home', self)
        self.button.clicked.connect(self.startPage)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(20, 480)
        self.button.setFixedSize(200,75)
# button move  (over, down)

        self.button2 = QtGui.QPushButton('Data Processing', self)
        self.button2.clicked.connect(self.pageTwo)
        self.button2.setIconSize(QtCore.QSize(24,24))
        self.button2.move(20, 535)
        self.button2.setFixedSize(200,75)


        self.button3 = QtGui.QPushButton('Data Release ', self)
        self.button3.clicked.connect(self.pageThree)
        self.button3.setIconSize(QtCore.QSize(24,24))
        self.button3.move(20, 590)
        self.button3.setFixedSize(200,75)



        self.button5 = QtGui.QPushButton('Remote File Upload', self)
        self.button5.clicked.connect(self.pageFour)
        self.button5.setIconSize(QtCore.QSize(24,24))
        self.button5.move(20, 645)
        self.button5.setFixedSize(200,75)

        self.button6 = QtGui.QPushButton('Tools', self)
        self.button6.clicked.connect(self.pageFive)
        self.button6.setIconSize(QtCore.QSize(24,24))
        self.button6.move(20, 700)
        self.button6.setFixedSize(200,75)

# button move  (over, down)






        self.convertpageTwo = QtGui.QPushButton('IVR DATA DOWNLOAD', self)
        self.convertpageTwo.clicked.connect(self.filesdownloaderconvertor)
        self.convertpageTwo.setIconSize(QtCore.QSize(24,24))
        self.convertpageTwo.move(300,75)
        self.convertpageTwo.setFixedSize(250,50)

        self.convertpageThree = QtGui.QPushButton('IVR CLEANUP', self)
        self.convertpageThree.clicked.connect(self.filescleanupconvertor)
        self.convertpageThree.setIconSize(QtCore.QSize(24,24))
        self.convertpageThree.move(600,75)
        self.convertpageThree.setFixedSize(250,50)

        self.convertpageFour = QtGui.QPushButton('IVR CONVERSION', self)
        self.convertpageFour.clicked.connect(self.createedditconvertor)
        self.convertpageFour.setIconSize(QtCore.QSize(24,24))
        self.convertpageFour.move(900,75)
        self.convertpageFour.setFixedSize(250,50)






        self.listWidget = QtGui.QListWidget(self)

        self.listWidget.move(660,200)
        self.listWidget.resize(450,150)

        self.selectFileButton = QtGui.QPushButton('Clean files in a directory', self)
        self.selectFileButton.move(355, 250)
        self.selectFileButton.setFixedSize(250,50)
        self.selectFileButton.clicked.connect(self.cleanFiles)


        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Select Folder")
        self.lbl.move(435,280)
        self.lbl.resize(250,70)


        self.lblNamechange= QtGui.QLabel(self)
        self.lblNamechange.setText("Successfully changed names ")
        self.lblNamechange.resize(340, 50)
        self.lblNamechange.move(300,500)
        self.lblNamechange.hide()

        self.lblGroupfiles = QtGui.QLabel(self)
        self.lblGroupfiles.setText("Successfully Grouped Files ")
        self.lblGroupfiles.resize(340, 50)
        self.lblGroupfiles.move(550,500)
        self.lblGroupfiles.hide()

        self.lblRemovejunk = QtGui.QLabel(self)
        self.lblRemovejunk.setText("Successfully Removed junk ")
        self.lblRemovejunk.resize(340, 50)
        self.lblRemovejunk.move(800,500)
        self.lblRemovejunk.hide()

        self.lblSucess = QtGui.QLabel(self)
        self.lblSucess.setText("Ready to convert! ")
        self.lblSucess.resize(340, 50)
        self.lblSucess.move(600,600)
        self.lblSucess.hide()


        self.Namechange2 = QtGui.QLabel(self)
        self.Namechange2.setText("Failed to change names ")
        self.Namechange2.resize(340, 50)
        self.Namechange2.move(300,500)
        self.Namechange2.hide()

        self.lblGroupfiles2 = QtGui.QLabel(self)
        self.lblGroupfiles2.setText("Failed to Group Files ")
        self.lblGroupfiles2.resize(340, 50)
        self.lblGroupfiles2.move(550,500)
        self.lblGroupfiles2.hide()

        self.lblRemovejunk2 = QtGui.QLabel(self)
        self.lblRemovejunk2.setText("Failed to Remove junk ")
        self.lblRemovejunk2.resize(340, 50)
        self.lblRemovejunk2.move(800,500)
        self.lblRemovejunk2.hide()

        self.lblFailed = QtGui.QLabel(self)
        self.lblFailed.setText("You Broke it :( ")
        self.lblFailed.resize(340, 50)
        self.lblFailed.move(600,600)
        self.lblFailed.hide()








        self.lblPage = QtGui.QLabel(self)
        self.lblPage.setText("Select the data folder you downloaded ex: IT_044")

        self.lblPage.resize(640, 50)
        self.lblPage.move(400,130)



        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("***  Folder created appears above ***")
        self.lbl.move(755,350)
        self.lbl.resize(850,70)
        self.show()




    def directoryChoice(self):

        self.listWidget.clear() # In case there are any existing elements in the list
        directory = QtGui.QFileDialog.getExistingDirectory(self, "    Pick a folder")
        print directory + "     In directory Choice"


        return directory


    def cleanFiles(self):

        directoryChosen = self.directoryChoice()
        print directoryChosen + "     you made it to files selected \n \n \n \n"
        findFolder = directoryChosen + '/continuous'
        print findFolder






        try:
            os.chdir(directoryChosen)
            os.getcwd()
            print (os.getcwd()) + " this is the current directory"
            cmdremoveJunk = ('rm *')
            print cmdremoveJunk
            os.system(cmdremoveJunk)



            print " removed excess files \n \n \n \n"

        except Exception:
            print "failed tp remove files**************"


        try:
            os.chdir(dname)
            os.getcwd()
            print (os.getcwd()) + " this is the current directory"
            cmdDollartohash = ('python fixFiles/replaceDollartohash.py '
                   +str(findFolder) + '/')
            print cmdDollartohash
            os.system(cmdDollartohash)
            self.lblNamechange.show()


            print " change dollar to hash over boss \n \n \n \n"

        except Exception:
            print "Changeing dollar to hash failed**************"
            self.Namechange2.show()



        try:
            os.chdir(dname)
            cmdGroupfiles = ('python fixFiles/groupFiles.py '
                   +str(findFolder) + '/')

            print cmdGroupfiles
            os.system(cmdGroupfiles)
            self.lblGroupfiles.show()

            print " grouped the files boss  \n \n \n \n"
        except Exception:
            print "Grouping Files Failed"
            self.lblGroupfiles2.show()

        try:
            os.chdir(dname)
            cmdRmfiles = ('python fixFiles/rmFiles.py '
                   +str(findFolder))

            print cmdRmfiles
            os.system(cmdRmfiles)
            self.lblRemovejunk.show()


            print " removed junk files boss  \n \n \n \n"
        except Exception:
            print "Removing Files Failed"
            self.lblRemovejunk2.show()

        for file_names in os.listdir(findFolder):
            if not file_names.startswith('.'):
                print file_names
                self.listWidget.addItem(file_names)

                print (findFolder)
        try:
            os.chdir(findFolder)
            moveSource = '-v ' + str(findFolder) + str('/*')

            print str(os.getcwd())
            print moveSource
            moveDest = str(directoryChosen)
            print directoryChosen
            cmdMove = ('mv -v ' + str(moveSource) + ' ' + str(moveDest))
            cmdremoveC = ('rm -r continuous')
            os.system(cmdMove)
            os.chdir(directoryChosen)
            os.system(cmdremoveC)
        except Exception as e:
            print str(e)

    def csvtoXmlconvertor(self):
        self.hide()
        self.filescleanupConvertorpage = None
        self.createedditConvertorpage = None

        self.finalCheck = None
        convert1 = convertcsvtoXml(self)
        convert1.show()
        print 'Button Pressed'

    def checkFile(self):
        self.hide()
        self.createedditconvertor = None
        self.filescleanupconvertor = None
        self.filesdownloaderconvertor = None
        self.convercsvtoXml = None
        convert1 = finalCheck(self)
        convert1.show()
        print 'Button Pressed'

    def filesdownloaderconvertor(self):
        self.hide()
        self.filescleanupConvertorpage = None
        self.createedditConvertorpage = None
        self.convertcsvtoXml = None
        self.convertcsvtoXml = None
        self.finalCheck = None

        convert1 = filesdownloadConvertorpage(self)
        convert1.show()
        print 'Button Pressed'

    def filescleanupconvertor(self):
        self.hide()

        self.createedditConvertorpage = None
        self.convertcsvtoXml = None
        self.convertcsvtoXml = None
        self.finalCheck = None
        convert1 = filescleanupConvertorpage(self)
        convert1.show()
        print 'Button Pressed'

    def createedditconvertor(self):
        self.hide()
        self.filescleanupConvertorpage = None

        self.convertcsvtoXml = None
        self.convertcsvtoXml = None
        self.finalCheck = None
        convert1 = createedditConvertorpage(self)
        convert1.show()
        print 'Button Pressed'




    def startPage(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        startpage = mainWindow(self)
        startpage.show()

        print ("Now Entering Start Page")


    def pageTwo(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")

        pagetwo = convertorPage(self)
        pagetwo.show()
        print ("Now Entering Page Two")

    def pageThree(self):
        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pagethree = dataScience(self)
        pagethree.show()
        print ("Now Entering Page Three")


    def pageFour(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFour = dataRelease(self)
        pageFour.show()
        print ("Now Entering Page 4")

    def pageFive(self):


        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFive = gameWindow(self)
        pageFive.show()
        print ("Now Entering Page 5")

    def showDate(self, date):

        self.lbl.setText(date.toString())



    def close_application(self):
        print("whooaaaa you quit!!")
        sys.exit()




class readoutWindow(QtGui.QDialog):

    def __init__(self, parent=None):
        super(readoutWindow, self).__init__(parent)

        self.home()
    def home(self):

        self.setGeometry(50, 50, 750, 700)
        self.setWindowTitle("Edited XML Summary")

        self.textEdit = QtGui.QTextEdit(self)
        self.textEdit.resize(650,500)
        self.textEdit.move(20,20)

        self.textEdit.setReadOnly(1)






        self.btn = QtGui.QPushButton("Quit", self)
        self.btn.clicked.connect(self.close_application)
        self.btn.move(600,600)
        self.openTxt()
        self.show()

    def close_application(self):
        print("Closes popup window!")
        self.close()






    def openTxt(self):
        directoryFile = createedditConvertorpage()
        dir1=directoryFile.selectFilecsvtoxml()
        print "this s open text"
        print str(dir1) + "   this is directory of opentxt"
        os.chdir(dir1)
        print os.getcwd()+ "    this is directory before looking for txt"
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for file_name in files:

            if file_name.endswith(".txt"):
                print dir1 + "/" + (file_name)  + "   this is txt file"
                readMe = open(file_name,'r').read()
                self.textEdit.setText(readMe)




class createedditConvertorpage(QtGui.QMainWindow):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.initUI()

    def initUI(self):
# button move  (over, down)
        self.setGeometry(300,300,1280,800)
        self.setWindowTitle("Intel")
        self.setWindowIcon(QtGui.QIcon("Intel Converter"))
        self.setStyleSheet("font-size:15px")


#_________________________________________________________________________
#(Menubah)


        self.pixmap = QtGui.QPixmap("images/intelmed.png")

        self.lbl2 = QtGui.QLabel(self)
        self.lbl2.setPixmap(self.pixmap)
        self.lbl2.move(10,50)
        self.lbl2.resize(300,200)



        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Data Release Made Easy")
        self.lbl.move(630,20)
        self.lbl.resize(250,70)



        self.button = QtGui.QPushButton('Home', self)
        self.button.clicked.connect(self.startPage)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(20, 480)
        self.button.setFixedSize(200,75)
# button move  (over, down)

        self.button2 = QtGui.QPushButton('Data Processing', self)
        self.button2.clicked.connect(self.pageTwo)
        self.button2.setIconSize(QtCore.QSize(24,24))
        self.button2.move(20, 535)
        self.button2.setFixedSize(200,75)


        self.button3 = QtGui.QPushButton('Data Release ', self)
        self.button3.clicked.connect(self.pageThree)
        self.button3.setIconSize(QtCore.QSize(24,24))
        self.button3.move(20, 590)
        self.button3.setFixedSize(200,75)



        self.button5 = QtGui.QPushButton('Remote File Upload', self)
        self.button5.clicked.connect(self.pageFour)
        self.button5.setIconSize(QtCore.QSize(24,24))
        self.button5.move(20, 645)
        self.button5.setFixedSize(200,75)

        self.button6 = QtGui.QPushButton('Tools', self)
        self.button6.clicked.connect(self.pageFive)
        self.button6.setIconSize(QtCore.QSize(24,24))
        self.button6.move(20, 700)
        self.button6.setFixedSize(200,75)

# button move  (over, down)








        self.convertpageTwo = QtGui.QPushButton('IVR DATA DOWNLOAD', self)
        self.convertpageTwo.clicked.connect(self.filesdownloaderconvertor)
        self.convertpageTwo.setIconSize(QtCore.QSize(24,24))
        self.convertpageTwo.move(300,75)
        self.convertpageTwo.setFixedSize(250,50)

        self.convertpageThree = QtGui.QPushButton('IVR CLEANUP', self)
        self.convertpageThree.clicked.connect(self.filescleanupconvertor)
        self.convertpageThree.setIconSize(QtCore.QSize(24,24))
        self.convertpageThree.move(600,75)
        self.convertpageThree.setFixedSize(250,50)

        self.convertpageFour = QtGui.QPushButton('IVR CONVERSION', self)
        self.convertpageFour.clicked.connect(self.createedditconvertor)
        self.convertpageFour.setIconSize(QtCore.QSize(24,24))
        self.convertpageFour.move(900,75)
        self.convertpageFour.setFixedSize(250,50)




        self.listDirPath = QtGui.QLineEdit(self)
        self.listDirPath.resize(500,50)
        self.listDirPath.move(650,300)


        self.selectFileButton = QtGui.QPushButton('Select File', self)
        self.selectFileButton.move(355, 300)
        self.selectFileButton.setFixedSize(250,50)
        self.selectFileButton.clicked.connect(self.convertDirectorybefore)
        #self.selectFileButton.clicked.connect(self.openTxt)




        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Folder contains .csv, .xml, .wav")
        self.lbl.move(365,330)
        self.lbl.resize(250,70)

        self.pixmap = QtGui.QPixmap("images/xmlLogo.png")

        self.lblxml = QtGui.QLabel(self)
        self.lblxml.setPixmap(self.pixmap)
        self.lblxml.move(450,130)
        self.lblxml.resize(150,150)

        self.pixmap = QtGui.QPixmap("images/addIcon.png")

        self.lblplus = QtGui.QLabel(self)
        self.lblplus.setPixmap(self.pixmap)
        self.lblplus.move(650,130)
        self.lblplus.resize(150,150)

        self.pixmap = QtGui.QPixmap("images/csvLogo.png")

        self.lblcsv = QtGui.QLabel(self)
        self.lblcsv.setPixmap(self.pixmap)
        self.lblcsv.move(850,130)
        self.lblcsv.resize(150,150)










        self.textEdit = QtGui.QTextEdit(self)
        self.textEdit.resize(500,350)
        self.textEdit.move(500,400)

        self.textEdit.setReadOnly(1)




        self.directory =None
        self.show()



    def checkFile(self):
        self.hide()
        convert1 = finalCheck(self)
        convert1.show()
        print 'Button Pressed'


    def selectFilecsvtoxml(self):


        directory = QtGui.QFileDialog.getExistingDirectory(self, caption="Pick a folder", directory=QtCore.QDir.currentPath())


        print directory + " this si dirrrrectory"
        self.listDirPath.setText(directory)

        for file_name in os.listdir(directory):
            if not file_name.startswith("."):

                print (file_name) +  "   this is selectFilcestoxml"

        return directory



    def convertDirectory(self):

        import longXmlEditor
        longXmlEditor.Main()







    def convertDirectorybefore(self):

        os.chdir(dname)
        os.getcwd()
        print (os.getcwd()) + " this is the current directory"
        directoryPath = self.selectFilecsvtoxml()
        print directoryPath



        cmd = ('python longXmlEditor.py '
               +str(directoryPath))
        print cmd + "   this is executable command"
        os.system(cmd)
        os.chdir(directoryPath)
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        print str(files) + '********'
        for file_name in files:

            if file_name.endswith(".txt"):
                print file_name + " this is txt"
                readMe = open(file_name,'r').read()
                self.textEdit.setText(readMe)









    def csvtoXmlconvertor(self):
        self.hide()
        self.createedditconvertor = None
        self.filescleanupconvertor = None
        self.filesdownloaderconvertor = None
        self.convercsvtoXml = None
        convert1 = convertcsvtoXml(self)
        convert1.show()
        print 'Button Pressed'


    def filesdownloaderconvertor(self):
        self.hide()
        self.createedditconvertor = None
        self.filescleanupconvertor = None
        self.filesdownloaderconvertor = None
        self.convercsvtoXml = None
        convert1 = filesdownloadConvertorpage(self)
        convert1.show()
        print 'Button Pressed'

    def filescleanupconvertor(self):
        self.hide()
        self.createedditconvertor = None
        self.filescleanupconvertor = None
        self.filesdownloaderconvertor = None
        self.convercsvtoXml = None
        convert1 = filescleanupConvertorpage(self)
        convert1.show()
        print 'Button Pressed'

    def createedditconvertor(self):
        self.hide()
        self.createedditconvertor = None
        self.filescleanupconvertor = None
        self.filesdownloaderconvertor = None
        self.convercsvtoXml = None
        convert1 = createedditConvertorpage(self)
        convert1.show()
        print 'Button Pressed'




    def startPage(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        startpage = mainWindow(self)
        startpage.show()

        print ("Now Entering Start Page")


    def pageTwo(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")

        pagetwo = convertorPage(self)
        pagetwo.show()
        print ("Now Entering Page Two")

    def pageThree(self):
        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pagethree = dataScience(self)
        pagethree.show()
        print ("Now Entering Page Three")


    def pageFour(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFour = dataRelease(self)
        pageFour.show()
        print ("Now Entering Page 4")

    def pageFive(self):


        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFive = gameWindow(self)
        pageFive.show()
        print ("Now Entering Page 5")

    def showDate(self, date):

        self.lbl.setText(date.toString())



    def close_application(self):
        print("whooaaaa you quit!!")
        sys.exit()





class convertorPage(QtGui.QMainWindow):
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


        self.pixmap = QtGui.QPixmap("images/intelmed.png")

        self.lbl2 = QtGui.QLabel(self)
        self.lbl2.setPixmap(self.pixmap)
        self.lbl2.move(10,50)
        self.lbl2.resize(300,200)


#______________
###Actions



###Icon bar

        extractActionHome = QtGui.QAction(QtGui.QIcon('images/homelogo.png'), 'Home Page', self)
        extractActionHome.triggered.connect(self.startPage)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActionHome)



        extractActionConvert = QtGui.QAction(QtGui.QIcon('images/convertlogo.png'), 'Convert Page', self)
        extractActionConvert.triggered.connect(self.pageTwo)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActionConvert)




        extractActiondataScience = QtGui.QAction(QtGui.QIcon('images/graphlogo.png'), 'Data Page', self)
        extractActiondataScience.triggered.connect(self.pageThree)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiondataScience)

        extractActiondataRelease = QtGui.QAction(QtGui.QIcon('images/dataRelease.png'), 'Data Release', self)
        extractActiondataRelease.triggered.connect(self.pageFour)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiondataRelease)

        extractActiongameWindow = QtGui.QAction(QtGui.QIcon('images/gamelogo.png'), 'Tools', self)
        extractActiongameWindow.triggered.connect(self.pageFive)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiongameWindow)


#Canvas------------------
# button move  (over, down)









        self.button = QtGui.QPushButton('Home', self)
        self.button.clicked.connect(self.startPage)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(20, 480)
        self.button.setFixedSize(200,75)
# button move  (over, down)

        self.button2 = QtGui.QPushButton('Data Processing', self)
        self.button2.clicked.connect(self.pageTwo)
        self.button2.setIconSize(QtCore.QSize(24,24))
        self.button2.move(20, 535)
        self.button2.setFixedSize(200,75)


        self.button3 = QtGui.QPushButton('Data Release ', self)
        self.button3.clicked.connect(self.pageThree)
        self.button3.setIconSize(QtCore.QSize(24,24))
        self.button3.move(20, 590)
        self.button3.setFixedSize(200,75)



        self.button5 = QtGui.QPushButton('Remote File Upload', self)
        self.button5.clicked.connect(self.pageFour)
        self.button5.setIconSize(QtCore.QSize(24,24))
        self.button5.move(20, 645)
        self.button5.setFixedSize(200,75)

        self.button6 = QtGui.QPushButton('Tools', self)
        self.button6.clicked.connect(self.pageFive)
        self.button6.setIconSize(QtCore.QSize(24,24))
        self.button6.move(20, 700)
        self.button6.setFixedSize(200,75)

# button move  (over, down)




        self.convertpageTwo = QtGui.QPushButton('IVR DATA DOWNLOAD', self)
        self.convertpageTwo.clicked.connect(self.filesdownloaderconvertor)
        self.convertpageTwo.setIconSize(QtCore.QSize(24,24))
        self.convertpageTwo.move(300,75)
        self.convertpageTwo.setFixedSize(250,50)

        self.convertpageThree = QtGui.QPushButton('IVR CLEANUP', self)
        self.convertpageThree.clicked.connect(self.filescleanupconvertor)
        self.convertpageThree.setIconSize(QtCore.QSize(24,24))
        self.convertpageThree.move(600,75)
        self.convertpageThree.setFixedSize(250,50)

        self.convertpageFour = QtGui.QPushButton('IVR CONVERSION', self)
        self.convertpageFour.clicked.connect(self.createedditconvertor)
        self.convertpageFour.setIconSize(QtCore.QSize(24,24))
        self.convertpageFour.move(900,75)
        self.convertpageFour.setFixedSize(250,50)



        self.lblPage = QtGui.QLabel(self)
        self.lblPage.setText("Data Processing Center ")
        self.lblPage.resize(360, 50)
        self.lblPage.move(650,150)



        self.lbl1Page = QtGui.QLabel(self)
        self.lbl1Page.setText("This page will download Foreign Language Data and convert it to clean XML Files. ")
        self.lbl1Page.resize(640, 50)
        self.lbl1Page.move(300,200)

        self.lblPage = QtGui.QLabel(self)
        self.lblPage.setText("1.  Download the language folder and this will include all necessary files automatically.")
        self.lblPage.resize(640, 50)
        self.lblPage.move(300,250)


        self.lblPage = QtGui.QLabel(self)
        self.lblPage.setText("2.  The file cleaner will properly format names, remove wrong punctuation in files, and group files in folders by name")
        self.lblPage.resize(640, 50)
        self.lblPage.move(300,300)


        self.lblPage = QtGui.QLabel(self)
        self.lblPage.setText("3.  IVR will merge the csv transcript and xml data into one long file.  If successful a text file be made and display any errors.")
        self.lblPage.resize(680, 50)
        self.lblPage.move(300,350)



        self.lblPage = QtGui.QLabel(self)
        self.lblPage.setText("4.  The last step is to check the file for any errors, and ensure the timestamps match the wav file..")
        self.lblPage.resize(640, 50)
        self.lblPage.move(300,400)

        self.show()



    def checkFile(self):
        self.hide()
        self.createedditconvertor = None
        self.filescleanupconvertor = None
        self.filesdownloaderconvertor = None
        self.convercsvtoXml = None
        convert1 = finalCheck(self)
        convert1.show()
        print 'Button Pressed'


    def csvtoXmlconvertor(self):
        self.hide()
        self.createedditconvertor = None
        self.filescleanupconvertor = None
        self.filesdownloaderconvertor = None
        self.convercsvtoXml = None
        convert1 = convertcsvtoXml(self)
        convert1.show()
        print 'Button Pressed'


    def filesdownloaderconvertor(self):
        self.hide()
        self.createedditconvertor = None
        self.filescleanupconvertor = None
        self.filesdownloaderconvertor = None
        self.convercsvtoXml = None
        convert1 = filesdownloadConvertorpage(self)
        convert1.show()
        print 'Button Pressed'

    def filescleanupconvertor(self):
        self.hide()
        self.createedditconvertor = None
        self.filescleanupconvertor = None
        self.filesdownloaderconvertor = None
        self.convercsvtoXml = None
        convert1 = filescleanupConvertorpage(self)
        convert1.show()
        print 'Button Pressed'

    def createedditconvertor(self):
        self.hide()
        self.createedditconvertor = None
        self.filescleanupconvertor = None
        self.filesdownloaderconvertor = None
        self.convercsvtoXml = None
        convert1 = createedditConvertorpage(self)
        convert1.show()
        print 'Button Pressed'



    def startPage(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        startpage = mainWindow(self)
        startpage.show()

        print ("Now Entering Start Page")


    def pageTwo(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")

        pagetwo = convertorPage(self)
        pagetwo.show()
        print ("Now Entering Page Two")

    def pageThree(self):
        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pagethree = dataScience(self)
        pagethree.show()
        print ("Now Entering Page Three")


    def pageFour(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFour = dataRelease(self)
        pageFour.show()
        print ("Now Entering Page 4")

    def pageFive(self):


        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFive = gameWindow(self)
        pageFive.show()
        print ("Now Entering Page 5")




    def showDate(self, date):

        self.lbl.setText(date.toString())



    def close_application(self):
        print("whooaaaa you quit!!")
        sys.exit()






class finalCheck(QtGui.QMainWindow):
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


        self.pixmap = QtGui.QPixmap("images/intelmed.png")

        self.lbl2 = QtGui.QLabel(self)
        self.lbl2.setPixmap(self.pixmap)
        self.lbl2.move(10,50)
        self.lbl2.resize(300,200)




#______________
###Actions



###Icon bar

        extractActionHome = QtGui.QAction(QtGui.QIcon('images/homelogo.png'), 'Home Page', self)
        extractActionHome.triggered.connect(self.startPage)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActionHome)



        extractActionConvert = QtGui.QAction(QtGui.QIcon('images/convertlogo.png'), 'Convert Page', self)
        extractActionConvert.triggered.connect(self.pageTwo)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActionConvert)




        extractActiondataScience = QtGui.QAction(QtGui.QIcon('images/graphlogo.png'), 'Data Page', self)
        extractActiondataScience.triggered.connect(self.pageThree)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiondataScience)

        extractActiondataRelease = QtGui.QAction(QtGui.QIcon('images/dataRelease.png'), 'Data Release', self)
        extractActiondataRelease.triggered.connect(self.pageFour)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiondataRelease)

        extractActiongameWindow = QtGui.QAction(QtGui.QIcon('images/gamelogo.png'), 'Tools', self)
        extractActiongameWindow.triggered.connect(self.pageFive)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiongameWindow)


#Canvas------------------
# button move  (over, down)









        self.button = QtGui.QPushButton('Home', self)
        self.button.clicked.connect(self.startPage)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(20, 480)
        self.button.setFixedSize(200,75)
# button move  (over, down)

        self.button2 = QtGui.QPushButton('Data Processing', self)
        self.button2.clicked.connect(self.pageTwo)
        self.button2.setIconSize(QtCore.QSize(24,24))
        self.button2.move(20, 535)
        self.button2.setFixedSize(200,75)


        self.button3 = QtGui.QPushButton('Data Release ', self)
        self.button3.clicked.connect(self.pageThree)
        self.button3.setIconSize(QtCore.QSize(24,24))
        self.button3.move(20, 590)
        self.button3.setFixedSize(200,75)



        self.button5 = QtGui.QPushButton('Remote File Upload', self)
        self.button5.clicked.connect(self.pageFour)
        self.button5.setIconSize(QtCore.QSize(24,24))
        self.button5.move(20, 645)
        self.button5.setFixedSize(200,75)

        self.button6 = QtGui.QPushButton('Tools', self)
        self.button6.clicked.connect(self.pageFive)
        self.button6.setIconSize(QtCore.QSize(24,24))
        self.button6.move(20, 700)
        self.button6.setFixedSize(200,75)

# button move  (over, down)




        self.convertpageTwo = QtGui.QPushButton('IVR DATA DOWNLOAD', self)
        self.convertpageTwo.clicked.connect(self.filesdownloaderconvertor)
        self.convertpageTwo.setIconSize(QtCore.QSize(24,24))
        self.convertpageTwo.move(300,75)
        self.convertpageTwo.setFixedSize(250,50)

        self.convertpageThree = QtGui.QPushButton('IVR CLEANUP', self)
        self.convertpageThree.clicked.connect(self.filescleanupconvertor)
        self.convertpageThree.setIconSize(QtCore.QSize(24,24))
        self.convertpageThree.move(600,75)
        self.convertpageThree.setFixedSize(250,50)

        self.convertpageFour = QtGui.QPushButton('IVR CONVERSION', self)
        self.convertpageFour.clicked.connect(self.createedditconvertor)
        self.convertpageFour.setIconSize(QtCore.QSize(24,24))
        self.convertpageFour.move(900,75)
        self.convertpageFour.setFixedSize(250,50)

        self.fileButton = QtGui.QPushButton('Select Txt', self)
        self.fileButton.clicked.connect(self.selectTxt)
        self.fileButton.setIconSize(QtCore.QSize(24,24))
        self.fileButton.move(400, 250)




# button move  (over, down)
        self.textEdit = QtGui.QTextEdit(self)
        self.textEdit.resize(450,400)
        self.textEdit.move(250,300)

        self.textEdit.setReadOnly(1)

        self.lblPage = QtGui.QLabel(self)
        self.lblPage.setText("Select the txt in the /continous folder")

        self.lblPage.resize(440, 50)
        self.lblPage.move(320,130)


        self.lblPage = QtGui.QLabel(self)
        self.lblPage.setText("Open the .wav using media player")

        self.lblPage.resize(440, 50)
        self.lblPage.move(320,150)








        self.lblPage2 = QtGui.QLabel(self)
        self.lblPage2.setText("What the text file says:")

        self.lblPage2.resize(440, 50)
        self.lblPage2.move(750,140)


        self.lblPage3 = QtGui.QLabel(self)
        self.lblPage3.setText("-No Txt File:  The data doesnt contain a csv and xml file.")
        self.lblPage3.resize(440, 50)
        self.lblPage3.move(750,180)
        self.lblPage4 = QtGui.QLabel(self)
        self.lblPage4.setText("                      Incorrect conversion during cleanup.")
        self.lblPage4.resize(440, 50)
        self.lblPage4.move(750,200)




        self.lblPage5 = QtGui.QLabel(self)
        self.lblPage5.setText("-Blank Txt File:  There was an error in the xml or csv conversion.")
        self.lblPage5.resize(440, 50)
        self.lblPage5.move(750,250)




        self.lblPage6 = QtGui.QLabel(self)
        self.lblPage6.setText("-Txt file didnt complete processing:  Most likely conversion worked.  Usually caused by weird characters in data.")
        self.lblPage6.resize(440, 50)
        self.lblPage6.move(750,300)
        self.lblPage7 = QtGui.QLabel(self)
        self.lblPage7.setText("                       Usually caused by weird characters in data.")
        self.lblPage7.resize(440, 50)
        self.lblPage7.move(750,320)



        self.lblPage7 = QtGui.QLabel(self)
        self.lblPage7.setText("Last check:  Open audacity and .wav file under /continous.")
        self.lblPage7.resize(440, 50)
        self.lblPage7.move(750,420)
        self.lblPage8 = QtGui.QLabel(self)
        self.lblPage8.setText("                     * Check timestamps match the .xml")
        self.lblPage8.resize(440, 50)
        self.lblPage8.move(750,440)

        self.lblPage8 = QtGui.QLabel(self)
        self.lblPage8.setText("                     * Ensure Male / Female Labels in .xml")
        self.lblPage8.resize(440, 50)
        self.lblPage8.move(750,460)


        self.lblPage9 = QtGui.QLabel(self)
        self.lblPage9.setText("                     ** Often times blank/none transcript lines are caused ")
        self.lblPage9.resize(440, 50)
        self.lblPage9.move(750,480)
        self.lblPage10 = QtGui.QLabel(self)
        self.lblPage10.setText("                       by the person not saying anything.  Double check,   ")
        self.lblPage10.resize(440, 50)
        self.lblPage10.move(750,500)
        self.lblPage11 = QtGui.QLabel(self)
        self.lblPage11.setText("                       using .wav player.  Usually ignore this... ")
        self.lblPage11.resize(440, 50)
        self.lblPage11.move(750,520)




        self.show()

    def selectTxt(self):

        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name,'r')



        with file:
            text = file.read()

            self.textEdit.setText(text)




    def checkFile(self):
        self.hide()
        self.filescleanupconvertor = None
        self.filesdownloaderconvertor = None
        self.createedditconvertor = None
        convert1 = finalCheck(self)
        convert1.show()
        print 'Button Pressed'


    def csvtoXmlconvertor(self):
        self.hide()
        self.filescleanupconvertor = None
        self.filesdownloaderconvertor = None
        self.createedditconvertor = None
        self.finalCheck = None

        convert1 = convertcsvtoXml(self)
        convert1.show()
        print 'Button Pressed'


    def filesdownloaderconvertor(self):
        self.hide()
        self.filescleanupconvertor = None
        #self.filesdownloaderconvertor = None
        self.createedditconvertor = None
        self.finalCheck = None

        convert1 = filesdownloadConvertorpage(self)
        convert1.show()
        print 'Button Pressed'

    def filescleanupconvertor(self):
        self.hide()
        #self.filescleanupconvertor = None
        self.filesdownloaderconvertor = None
        self.createedditconvertor = None
        self.finalCheck = None

        convert1 = filescleanupConvertorpage(self)
        convert1.show()
        print 'Button Pressed'

    def createedditconvertor(self):
        self.hide()
        self.filescleanupconvertor = None
        #self.filesdownloaderconvertor = None
        self.createedditconvertor = None
        convert1 = filesdownloadConvertorpage(self)
        convert1 = createedditConvertorpage(self)
        convert1.show()
        print 'Button Pressed'



    def startPage(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        startpage = mainWindow(self)
        startpage.show()

        print ("Now Entering Start Page")


    def pageTwo(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")

        pagetwo = convertorPage(self)
        pagetwo.show()
        print ("Now Entering Page Two")

    def pageThree(self):
        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pagethree = dataScience(self)
        pagethree.show()
        print ("Now Entering Page Three")


    def pageFour(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFour = dataRelease(self)
        pageFour.show()
        print ("Now Entering Page 4")

    def pageFive(self):


        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFive = gameWindow(self)
        pageFive.show()
        print ("Now Entering Page 5")



    def showDate(self, date):

        self.lbl.setText(date.toString())



    def close_application(self):
        print("whooaaaa you quit!!")
        sys.exit()






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












###Icon bar


        extractActionHome = QtGui.QAction(QtGui.QIcon('images/homelogo.png'), 'Home Page', self)
        extractActionHome.triggered.connect(self.startPage)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActionHome)



        extractActionConvert = QtGui.QAction(QtGui.QIcon('images/convertlogo.png'), 'Convert Page', self)
        extractActionConvert.triggered.connect(self.pageTwo)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActionConvert)




        extractActiondataScience = QtGui.QAction(QtGui.QIcon('images/graphlogo.png'), 'Data Page', self)
        extractActiondataScience.triggered.connect(self.pageThree)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiondataScience)

        extractActiondataRelease = QtGui.QAction(QtGui.QIcon('images/dataRelease.png'), 'Data Release', self)
        extractActiondataRelease.triggered.connect(self.pageFour)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiondataRelease)

        extractActiongameWindow = QtGui.QAction(QtGui.QIcon('images/gamelogo.png'), 'Tools', self)
        extractActiongameWindow.triggered.connect(self.pageFive)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiongameWindow)
##Calnder
        self.pixmap = QtGui.QPixmap("images/intelmed.png")

        self.lbl2 = QtGui.QLabel(self)
        self.lbl2.setPixmap(self.pixmap)
        self.lbl2.move(10,50)
        self.lbl2.resize(300,200)


####








#Split Frames

##

#_________________________________________________________________________
#

#Canvas------------------
# button move  (over, down)


        self.emailpage = QtGui.QPushButton('Email Formatter', self)
        self.emailpage.clicked.connect(self.emailformatPage)
        self.emailpage.setIconSize(QtCore.QSize(24,24))
        self.emailpage.move(350,100)
        self.emailpage.setFixedSize(250,50)

        self.ldsPage = QtGui.QPushButton('Upload LDS', self)
        self.ldsPage.clicked.connect(self.ldsformatPage)
        self.ldsPage.setIconSize(QtCore.QSize(24,24))
        self.ldsPage.move(700,100)
        self.ldsPage.setFixedSize(250,50)








        self.button = QtGui.QPushButton('Home', self)
        self.button.clicked.connect(self.startPage)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(20, 480)
        self.button.setFixedSize(200,75)
# button move  (over, down)

        self.button2 = QtGui.QPushButton('Data Processing', self)
        self.button2.clicked.connect(self.pageTwo)
        self.button2.setIconSize(QtCore.QSize(24,24))
        self.button2.move(20, 535)
        self.button2.setFixedSize(200,75)


        self.button3 = QtGui.QPushButton('Data Release ', self)
        self.button3.clicked.connect(self.pageThree)
        self.button3.setIconSize(QtCore.QSize(24,24))
        self.button3.move(20, 590)
        self.button3.setFixedSize(200,75)



        self.button5 = QtGui.QPushButton('Remote File Upload', self)
        self.button5.clicked.connect(self.pageFour)
        self.button5.setIconSize(QtCore.QSize(24,24))
        self.button5.move(20, 645)
        self.button5.setFixedSize(200,75)

        self.button6 = QtGui.QPushButton('Tools', self)
        self.button6.clicked.connect(self.pageFive)
        self.button6.setIconSize(QtCore.QSize(24,24))
        self.button6.move(20, 700)
        self.button6.setFixedSize(200,75)





        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Data Release ")
        self.lbl.resize(145, 25)
        self.lbl.move(580,40)






        self.lbl1Page = QtGui.QLabel(self)
        self.lbl1Page.setText("This page will generate an email for outlook, and directly release data to LDS. ")
        self.lbl1Page.resize(640, 50)
        self.lbl1Page.move(300,200)

        self.lblPage = QtGui.QLabel(self)
        self.lblPage.setText("1.  All .xml/.wav files are to be placed into one folder.")
        self.lblPage.resize(640, 50)
        self.lblPage.move(300,250)


        self.lblPage = QtGui.QLabel(self)
        self.lblPage.setText("2. Under email formatter, select that folder, and a template for outlook is generated.")
        self.lblPage.resize(640, 50)
        self.lblPage.move(300,300)


        self.lblPage = QtGui.QLabel(self)
        self.lblPage.setText("3.  Under LDS upload, select the folder with the .xml/.wav files.  Enter in information and upload! (takes ~30 mins)")
        self.lblPage.resize(690, 50)
        self.lblPage.move(300,350)





        self.show()



#_________________________________________________________________________
#



    def showDate(self, date):

        self.lbl.setText(date.toString())


    def close_application(self):
        print("whooaaaa so custom!!!")
        sys.exit()


    def ldsformatPage(self):
        self.hide()
        convert1 = ldsuploadformatPage(self)
        convert1.show()
        print 'Button Pressed'

    def emailformatPage (self):
        self.hide()
        convert1 = emaildataUpload(self)
        convert1.show()
        print 'Button Pressed'


    def startPage(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        startpage = mainWindow(self)
        startpage.show()

        print ("Now Entering Start Page")


    def pageTwo(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")

        pagetwo = convertorPage(self)
        pagetwo.show()
        print ("Now Entering Page Two")

    def pageThree(self):
        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pagethree = dataScience(self)
        pagethree.show()
        print ("Now Entering Page Three")


    def pageFour(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFour = dataRelease(self)
        pageFour.show()
        print ("Now Entering Page 4")

    def pageFive(self):


        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFive = gameWindow(self)
        pageFive.show()
        print ("Now Entering Page 5")






class ldsuploadformatPage(QtGui.QMainWindow):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.initUI()

    def initUI(self):
# button move  (over, down)
        self.setGeometry(300,300,1280,800)
        self.setWindowTitle("Intel")
        self.setWindowIcon(QtGui.QIcon("Intel Converter"))
        self.setStyleSheet("font-size:15px")


#_________________________________________________________________________
#(Menubah)
        self.pixmap = QtGui.QPixmap("images/intelmed.png")

        self.lbl2 = QtGui.QLabel(self)
        self.lbl2.setPixmap(self.pixmap)
        self.lbl2.move(10,50)
        self.lbl2.resize(300,200)





        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Data Release Made Easy")
        self.lbl.move(570,20)
        self.lbl.resize(250,70)


        self.button = QtGui.QPushButton('Home', self)
        self.button.clicked.connect(self.startPage)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(20, 480)
        self.button.setFixedSize(200,75)
# button move  (over, down)

        self.button2 = QtGui.QPushButton('Data Processing', self)
        self.button2.clicked.connect(self.pageTwo)
        self.button2.setIconSize(QtCore.QSize(24,24))
        self.button2.move(20, 535)
        self.button2.setFixedSize(200,75)


        self.button3 = QtGui.QPushButton('Data Release ', self)
        self.button3.clicked.connect(self.pageThree)
        self.button3.setIconSize(QtCore.QSize(24,24))
        self.button3.move(20, 590)
        self.button3.setFixedSize(200,75)



        self.button5 = QtGui.QPushButton('Remote File Upload', self)
        self.button5.clicked.connect(self.pageFour)
        self.button5.setIconSize(QtCore.QSize(24,24))
        self.button5.move(20, 645)
        self.button5.setFixedSize(200,75)

        self.button6 = QtGui.QPushButton('Tools', self)
        self.button6.clicked.connect(self.pageFive)
        self.button6.setIconSize(QtCore.QSize(24,24))
        self.button6.move(20, 700)
        self.button6.setFixedSize(200,75)

# button move  (over, down)











        self.emailpage = QtGui.QPushButton('Email Formatter', self)
        self.emailpage.clicked.connect(self.emailformatPage)
        self.emailpage.setIconSize(QtCore.QSize(24,24))
        self.emailpage.move(350,100)
        self.emailpage.setFixedSize(250,50)

        self.ldsPage = QtGui.QPushButton('Upload LDS', self)
        self.ldsPage.clicked.connect(self.ldsformatPage)
        self.ldsPage.setIconSize(QtCore.QSize(24,24))
        self.ldsPage.move(700,100)
        self.ldsPage.setFixedSize(250,50)








        self.selectFileButton = QtGui.QPushButton('Select Folder', self)
        self.selectFileButton.move(345, 250)
        self.selectFileButton.setFixedSize(250,50)
        self.selectFileButton.clicked.connect(self.selectFolder)


        self.listDirPath = QtGui.QLineEdit(self)
        self.listDirPath.resize(500,50)
        self.listDirPath.move(650,250)



        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Enter the log name")
        self.lbl.resize(250,70)
        self.lbl.move(350,350)



        self.logPath = QtGui.QLineEdit(self)
        self.logPath.resize(350,50)
        self.logPath.move(650,350)




        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Enter the transaction id")
        self.lbl.resize(250,70)
        self.lbl.move(350,450)

        self.transidPath = QtGui.QLineEdit(self)
        self.transidPath.resize(350,50)
        self.transidPath.move(650,450)











        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Remove Directory Path")
        self.lbl.resize(250,70)
        self.lbl.move(350,550)



        self.listremovePath = QtGui.QLineEdit(self)
        self.listremovePath.resize(350,50)
        self.listremovePath.move(650,550)













        self.selectFileButton = QtGui.QPushButton('Upload', self)
        self.selectFileButton.move(555, 650)
        self.selectFileButton.clicked.connect(self.uploadLds)






        self.directory =None
        self.show()


    def uploadLds(self):


        tranID = self.transidPath.text()
        logLocation = self.logPath.text()
        pathRemover = self.listremovePath.text()

        directoryPath = self.listDirPath.text()


        cmd = ('python ingest_audio.py -c -p ' + "'" + str(pathRemover) + "'" + ' -t' + "'" + str(tranID) + "'" + '-l' + "'" + str(logLocation)  + "'" + ' ingest --audio_files' + str(directoryPath)+ '*.wav'   '--xml_metadata' + str(directoryPath) + '*.xml'+ ' -d')
        print cmd + "   this is executable command"
        #os.system(cmd)




        print "Worked .."




    def selectFolder(self):


        directory = QtGui.QFileDialog.getExistingDirectory(self, caption="Pick a folder", directory=QtCore.QDir.currentPath())


        print directory + " this si dirrrrectory"
        self.listDirPath.setText(directory)

        for file_name in os.listdir(directory):
            if not file_name.startswith("."):

                print (file_name) +  "   this is selectFilcestoxml"

        return directory


    def checkFile(self):
        self.hide()
        convert1 = finalCheck(self)
        convert1.show()
        print 'Button Pressed'


    def ldsformatPage(self):
        self.hide()
        convert1 = ldsuploadformatPage(self)
        convert1.show()
        print 'Button Pressed'

    def emailformatPage (self):
        self.hide()
        convert1 = emaildataUpload(self)
        convert1.show()
        print 'Button Pressed'



    def startPage(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        startpage = mainWindow(self)
        startpage.show()

        print ("Now Entering Start Page")


    def pageTwo(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")

        pagetwo = convertorPage(self)
        pagetwo.show()
        print ("Now Entering Page Two")

    def pageThree(self):
        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pagethree = dataScience(self)
        pagethree.show()
        print ("Now Entering Page Three")


    def pageFour(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFour = dataRelease(self)
        pageFour.show()
        print ("Now Entering Page 4")

    def pageFive(self):


        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFive = gameWindow(self)
        pageFive.show()
        print ("Now Entering Page 5")

    def showDate(self, date):

        self.lbl.setText(date.toString())



    def close_application(self):
        print("whooaaaa you quit!!")
        sys.exit()






class emaildataUpload(QtGui.QMainWindow):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.initUI()

    def initUI(self):
# button move  (over, down)
        self.setGeometry(300,300,1280,800)
        self.setWindowTitle("Intel")
        self.setWindowIcon(QtGui.QIcon("Intel Converter"))
        self.setStyleSheet("font-size:15px")


#_________________________________________________________________________
#(Menubah)
        self.pixmap = QtGui.QPixmap("images/intelmed.png")

        self.lbl2 = QtGui.QLabel(self)
        self.lbl2.setPixmap(self.pixmap)
        self.lbl2.move(10,50)
        self.lbl2.resize(300,200)





        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Data Release Made Easy")
        self.lbl.move(570,20)
        self.lbl.resize(250,70)


        self.button = QtGui.QPushButton('Home', self)
        self.button.clicked.connect(self.startPage)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(20, 480)
        self.button.setFixedSize(200,75)
# button move  (over, down)

        self.button2 = QtGui.QPushButton('Data Processing', self)
        self.button2.clicked.connect(self.pageTwo)
        self.button2.setIconSize(QtCore.QSize(24,24))
        self.button2.move(20, 535)
        self.button2.setFixedSize(200,75)


        self.button3 = QtGui.QPushButton('Data Release ', self)
        self.button3.clicked.connect(self.pageThree)
        self.button3.setIconSize(QtCore.QSize(24,24))
        self.button3.move(20, 590)
        self.button3.setFixedSize(200,75)



        self.button5 = QtGui.QPushButton('Remote File Upload', self)
        self.button5.clicked.connect(self.pageFour)
        self.button5.setIconSize(QtCore.QSize(24,24))
        self.button5.move(20, 645)
        self.button5.setFixedSize(200,75)

        self.button6 = QtGui.QPushButton('Tools', self)
        self.button6.clicked.connect(self.pageFive)
        self.button6.setIconSize(QtCore.QSize(24,24))
        self.button6.move(20, 700)
        self.button6.setFixedSize(200,75)

# button move  (over, down)










        self.emailpage = QtGui.QPushButton('Email Formatter', self)
        self.emailpage.clicked.connect(self.emailformatPage)
        self.emailpage.setIconSize(QtCore.QSize(24,24))
        self.emailpage.move(350,100)
        self.emailpage.setFixedSize(250,50)

        self.ldsPage = QtGui.QPushButton('Upload LDS', self)
        self.ldsPage.clicked.connect(self.ldsformatPage)
        self.ldsPage.setIconSize(QtCore.QSize(24,24))
        self.ldsPage.move(700,100)
        self.ldsPage.setFixedSize(250,50)


        self.listDirPath = QtGui.QLineEdit(self)
        self.listDirPath.resize(500,50)
        self.listDirPath.move(650,210)


        self.selectFileButton = QtGui.QPushButton('Select Folder', self)
        self.selectFileButton.move(355, 210)
        self.selectFileButton.setFixedSize(250,50)
        self.selectFileButton.clicked.connect(self.convertDirectory)
        #self.selectFileButton.clicked.connect(self.openTxt)




        self.textEdit = QtGui.QTextEdit(self)
        self.textEdit.resize(600,400)
        self.textEdit.move(450,360)

        #self.textEdit.setReadOnly(1)


        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Folder contains .xml, .wav")
        self.lbl.move(385,235)
        self.lbl.resize(250,70)

        self.lblEmail = QtGui.QLabel(self)
        self.lblEmail.setText("Copy and paste this output into outlook.")
        self.lblEmail.move(600,305)
        self.lblEmail.resize(300,70)

        self.directory =None
        self.show()


    def directorySource(self):
        pass

    def directoryMaker(self):
        pass

    def quickMove(self):
        for root, dirs, files in os.walk(directory):
            if len(files) >= 5:
                for f in files:
                    #print(os.path.join(root, f))

                    if f.endswith("_Edited.xml"):
                        print f + ' THIS WILL BE DATA FILE'

    def checkFile(self):
        self.hide()
        convert1 = finalCheck(self)
        convert1.show()
        print 'Button Pressed'


    def selectFilecsvtoxml(self):


        directory = QtGui.QFileDialog.getExistingDirectory(self, caption="Pick a folder", directory=QtCore.QDir.currentPath())


        print directory + " this si dirrrrectory"
        x = str(directory)
        print x + " this is string of directory"
        self.listDirPath.setText(directory)



        return directory


    def convertDirectory(self):


        directoryPath = self.selectFilecsvtoxml()
        os.chdir(dname)
        os.getcwd()
        print (os.getcwd()) + " this is the current directory"

        cmd = ('python log.py '
               +str(directoryPath))
        print cmd + "   this is executable command"
        os.system(cmd)

        for file_name in os.listdir(directoryPath):
            print (directoryPath) + "XXXXXXXXXXXX" + file_name

            if file_name.endswith(".txt"):
                f = file_name
                print f + "  this needs to go in textedit"
                os.chdir(directoryPath)
                print os.getcwd()

                readMe = open(f,'r').read()
                self.textEdit.setText(readMe)




        print "opening popup now .."







    def ldsformatPage(self):
        self.hide()
        convert1 = ldsuploadformatPage(self)
        convert1.show()
        print 'Button Pressed'

    def emailformatPage (self):
        self.hide()
        convert1 = emaildataUpload(self)
        convert1.show()
        print 'Button Pressed'



    def startPage(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        startpage = mainWindow(self)
        startpage.show()

        print ("Now Entering Start Page")


    def pageTwo(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")

        pagetwo = convertorPage(self)
        pagetwo.show()
        print ("Now Entering Page Two")

    def pageThree(self):
        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pagethree = dataScience(self)
        pagethree.show()
        print ("Now Entering Page Three")


    def pageFour(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFour = dataRelease(self)
        pageFour.show()
        print ("Now Entering Page 4")

    def pageFive(self):


        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFive = gameWindow(self)
        pageFive.show()
        print ("Now Entering Page 5")
    def showDate(self, date):

        self.lbl.setText(date.toString())



    def close_application(self):
        print("whooaaaa you quit!!")
        sys.exit()







class mainWindow(QtGui.QMainWindow):

    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.initUI()



    def initUI(self):
        self.setGeometry(300,300,1280,800)
        self.setWindowTitle("Intel V1.01")
        self.setWindowIcon(QtGui.QIcon("Intel.png"))
        #self.setStyleSheet("background-color: rgb(255, 255, 255);\n")
                           #"border:1px solid rgb(0, 131, 195);")



#_________________________________________________________________________
#(Menubah)



#______________
###Actions










###Icon bar


        extractActionHome = QtGui.QAction(QtGui.QIcon('images/homelogo.png'), 'Home Page', self)
        extractActionHome.triggered.connect(self.startPage)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActionHome)



        extractActionConvert = QtGui.QAction(QtGui.QIcon('images/convertlogo.png'), 'Convert Page', self)
        extractActionConvert.triggered.connect(self.pageTwo)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActionConvert)




        extractActiondataScience = QtGui.QAction(QtGui.QIcon('images/graphlogo.png'), 'Data Page', self)
        extractActiondataScience.triggered.connect(self.pageThree)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiondataScience)

        extractActiondataRelease = QtGui.QAction(QtGui.QIcon('images/dataRelease.png'), 'Data Release', self)
        extractActiondataRelease.triggered.connect(self.pageFour)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiondataRelease)

        extractActiongameWindow = QtGui.QAction(QtGui.QIcon('images/gamelogo.png'), 'Tools', self)
        extractActiongameWindow.triggered.connect(self.pageFive)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractActiongameWindow)
##Calnder







        self.button = QtGui.QPushButton('Home', self)
        self.button.clicked.connect(self.startPage)
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(20, 480)
        self.button.setFixedSize(200,75)
# button move  (over, down)

        self.button2 = QtGui.QPushButton('Data Processing', self)
        self.button2.clicked.connect(self.pageTwo)
        self.button2.setIconSize(QtCore.QSize(24,24))
        self.button2.move(20, 535)
        self.button2.setFixedSize(200,75)


        self.button3 = QtGui.QPushButton('Data Release ', self)
        self.button3.clicked.connect(self.pageThree)
        self.button3.setIconSize(QtCore.QSize(24,24))
        self.button3.move(20, 590)
        self.button3.setFixedSize(200,75)



        self.button5 = QtGui.QPushButton('Remote File Upload', self)
        self.button5.clicked.connect(self.pageFour)
        self.button5.setIconSize(QtCore.QSize(24,24))
        self.button5.move(20, 645)
        self.button5.setFixedSize(200,75)

        self.button6 = QtGui.QPushButton('Tools', self)
        self.button6.clicked.connect(self.pageFive)
        self.button6.setIconSize(QtCore.QSize(24,24))
        self.button6.move(20, 700)
        self.button6.setFixedSize(200,75)





        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Data Team Program")
        self.lbl.resize(145, 25)
        self.lbl.move(580,40)


        self.pixmap = QtGui.QPixmap("images/intelmed.png")

        self.lbl2 = QtGui.QLabel(self)
        self.lbl2.setPixmap(self.pixmap)
        self.lbl2.move(10,50)
        self.lbl2.resize(300,200)


        self.pixmap = QtGui.QPixmap("images/DataScience.png")

        self.lbl2 = QtGui.QLabel(self)
        self.lbl2.setPixmap(self.pixmap)
        self.lbl2.move(500,100)
        self.lbl2.resize(600,700)





        print(self.style().objectName())
        self.styleChoice = QtGui.QLabel("Windows Vista", self)

        comboBox = QtGui.QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("windowsvista")
        comboBox.move(50, 350)

        self.styleChoice.move(50,400)
        comboBox.activated[str].connect(self.style_choice)

        self.show()
#_________________________________________________________________________




    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

    def showDate(self, date):

        self.lbl.setText(date.toString())

    def close_application(self):
        print("whooaaaa so custom!!!")
        sys.exit()



    def startPage(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        startpage = mainWindow(self)
        startpage.show()

        print ("Now Entering Start Page")


    def pageTwo(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")

        pagetwo = convertorPage(self)
        pagetwo.show()
        print ("Now Entering Page Two")

    def pageThree(self):
        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pagethree = dataScience(self)
        pagethree.show()
        print ("Now Entering Page Three")


    def pageFour(self):

        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFour = dataRelease(self)
        pageFour.show()
        print ("Now Entering Page 4")

    def pageFive(self):


        self.hide()
        self.gameWindow = None
        self.downloadWindow = None
        self.uploadWindow = None
        self.convertorPage = None
        self.dataRelease = None
        self.dataScience = None
        self.mainWindow = None
        print ("Closed**********************")
        pageFive = gameWindow(self)
        pageFive.show()
        print ("Now Entering Page 5")






def main():
    app = QtGui.QApplication(sys.argv)
    main = mainWindow()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()