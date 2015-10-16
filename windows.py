__author__ = 'eeamesX'

import sys
import os
import subprocess
import metaDataCreator
import glob
from collections import defaultdict
from shutil import copyfile

from PyQt4 import QtGui, QtCore

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s







class gameWindow(QtGui.QMainWindow):
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




class dataRelease(QtGui.QMainWindow):
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


        AboutMenu.addAction(popupmsgAction)


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








#________________________

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


# button move  (over, down)

        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("SSH Made Easy")
        self.lbl.resize(145, 125)
        self.lbl.move(600,20)


        #self.pixmap = QtGui.QPixmap("dotgreen.png")

        #self.lbl2 = QtGui.QLabel(self)
        #self.lbl2.setPixmap(self.pixmap)
        #self.lbl2.move(1000,40)
        #self.lbl2.resize(300,200)

# button move  (over, down)

        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Test SSH Connection")
        self.lbl.resize(145, 205)
        self.lbl.move(550,60)

        self.userl = QtGui.QLabel("Username: ",self)
        self.userl.move(350,200)
        self.user = QtGui.QLineEdit(self)
        self.user.move(430,200)

        self.sshaddl= QtGui.QLabel("SSH Address:",self)
        self.sshaddl.move(550,200)

        self.sshadd= QtGui.QLineEdit(self)
        self.sshadd.setEchoMode(self.sshadd.Password)
        self.sshadd.move(650,200)
        self.sshadd.setText('10.127.235.151')


        self.button7 = QtGui.QPushButton('Login', self)
        self.button7.clicked.connect(self.sshTest)
        self.button7.setIconSize(QtCore.QSize(24,24))
        self.button7.move(550, 250)


        self.echo = QtGui.QCheckBox("Show/Hide Adress",self)
        self.echo.stateChanged.connect(self.Echo)
        self.echo.move(550,300)
        self.echo.resize(140,145)

        self.pixmap = QtGui.QPixmap("dotred.png")

        self.lbl2 = QtGui.QLabel(self)
        self.lbl2.setPixmap(self.pixmap)
        self.lbl2.move(775,170)
        self.lbl2.resize(75,75)

        self.show()



#____________
#



    def sshTest(self):

        HOST="10.127.235.151"
        # Ports are handled in ~/.ssh/config since we use OpenSSH
        COMMAND="uname -a"

        USERNAME= self.sshadd.text()

        ssh = subprocess.Popen(["ssh", USERNAME % HOST, COMMAND],
                               shell=False,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        print ssh
        result = ssh.stdout.readlines()
        print result
        if result == []:
            error = ssh.stderr.readlines()
            print >>sys.stderr, "ERROR: %s" % error

        else:
            print result


    def Echo(self,state):
        if state == QtCore.Qt.Checked:
            self.sshadd.setEchoMode(self.sshadd.Normal)
        else:
            self.sshadd.setEchoMode(self.sshadd.Password)


    def showDate(self, date):

        self.lbl.setText(date.toString())


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





        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Data Release Made Easy")
        self.lbl.move(550,20)
        self.lbl.resize(250,70)


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

# button move  (over, down)







        self.convertpageOne = QtGui.QPushButton('CSV -> XML', self)
        self.convertpageOne.clicked.connect(self.csvtoXmlconvertor)
        self.convertpageOne.setIconSize(QtCore.QSize(24,24))
        self.convertpageOne.move(200,70)
        self.convertpageOne.setFixedSize(250,50)

        self.convertpageTwo = QtGui.QPushButton('IVR DATA DOWNLOAD', self)
        self.convertpageTwo.clicked.connect(self.filesdownloaderconvertor)
        self.convertpageTwo.setIconSize(QtCore.QSize(24,24))
        self.convertpageTwo.move(450,70)
        self.convertpageTwo.setFixedSize(250,50)

        self.convertpageThree = QtGui.QPushButton('IVR CLEANUP', self)
        self.convertpageThree.clicked.connect(self.filescleanupconvertor)
        self.convertpageThree.setIconSize(QtCore.QSize(24,24))
        self.convertpageThree.move(700,70)
        self.convertpageThree.setFixedSize(250,50)

        self.convertpageFour = QtGui.QPushButton('IVR CONVERSION', self)
        self.convertpageFour.clicked.connect(self.createedditconvertor)
        self.convertpageFour.setIconSize(QtCore.QSize(24,24))
        self.convertpageFour.move(950,70)
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
        self.btn.clicked.connect(self.download_button)


        self.lblWorked = QtGui.QLabel(self)
        self.lblWorked.setText("Download was Successful! ")
        self.lblWorked.resize(340, 50)
        self.lblWorked.move(750,670)
        self.lblWorked.hide()

        self.lblFailed = QtGui.QLabel(self)
        self.lblFailed.setText("Download Failed :( ")
        self.lblFailed.resize(340, 50)
        self.lblFailed.move(770,670)
        self.lblFailed.hide()



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



        self.show()


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



    def download_button(self, text):
        directoryUser = self.directory
        ivrNum = self.lblNumber.text()
        username = self.userName.text()

        ivrLang = self.languageLbl.text()


        print username
        print directoryUser
        print ivrNum
        print ivrLang
        try:

            if ivrLang == '':
                self.lblFailed.show()


            if ivrLang == 'IVR_Italy':


                cmdIvrtranscripts = ('rsync  -avp ' + str(username) +
                        '@10.127.235.151:/media/sdidrive/proj/Localization/DataCollection/'
                        +str(ivrLang) + '/Transcripts/'+str(ivrNum) + ' ' + str(directoryUser))

                cmdIvr = ('rsync  -avp ' + str(username) +
                        '@10.127.235.151:/media/sdidrive/proj/Localization/DataCollection/'
                        +str(ivrLang) + '/' + str(ivrNum) + ' ' + str(directoryUser))


                print cmdIvr
                print cmdIvrtranscripts
                os.system(cmdIvrtranscripts)
                os.system(cmdIvr)

                self.lblWorked.show()



            if ivrLang == 'IVR_France':




                cmdIvr = ('rsync  -avp ' + str(username) +
                        '@10.127.235.151:/media/sdidrive/proj/Localization/DataCollection/'
                        +str(ivrLang) + '/' + str(ivrNum) + ' ' + str(directoryUser))



                cmdIvrtranscripts = ('rsync  -avp ' + str(username) +
                        '@10.127.235.151:/media/sdidrive/proj/Localization/DataCollection/Transcripts/FR_Transcripts'
                        + '/' +str(ivrNum)  + ' ' + str(directoryUser))


                print cmdIvr
                print cmdIvrtranscripts
                os.system(cmdIvr)
                os.system(cmdIvrtranscripts)

                self.lblWorked.show()

            if ivrLang == 'IVR_Spain':

                cmdIvr = ('rsync  -avp ' + str(username) +
                        '@10.127.235.151:/media/sdidrive/proj/Localization/DataCollection/'
                        +str(ivrLang) + '/' + str(ivrNum) + ' ' + str(directoryUser))


                cmdIvrtranscripts = ('rsync  -avp ' + str(username) +
                        '@10.127.235.151:/media/sdidrive/proj/Localization/DataCollection/Transcripts/ES_Transcripts'
                        + '/' +str(ivrNum)  + ' ' + str(directoryUser))





                print cmdIvr
                print cmdIvrtranscripts
                os.system(cmdIvr)
                os.system(cmdIvrtranscripts)

                self.lblWorked.show()

            if ivrLang == 'IVR_Germany':


                cmdIvr = ('rsync  -avp ' + str(username) +
                        '@10.127.235.151:/media/sdidrive/proj/Localization/DataCollection/'
                        +str(ivrLang) + '/' + str(ivrNum) + ' ' + str(directoryUser))

                cmdIvrtranscripts = ('rsync  -avp ' + str(username) +
                        '@10.127.235.151:/media/sdidrive/proj/Localization/DataCollection/Transcripts/DE_Transcripts'
                        + '/' +str(ivrNum)  + ' ' + str(directoryUser))




                print cmdIvr
                print cmdIvrtranscripts
                os.system(cmdIvr)
                os.system(cmdIvrtranscripts)

                self.lblWorked.show()


        except Exception as e:
            print str(e)
            self.lblFailed.show()






    def csvtoXmlconvertor(self):
        self.hide()
        convert1 = convertcsvtoXml(self)
        convert1.show()
        print 'Button Pressed'


    def filesdownloaderconvertor(self):
        self.hide()
        convert1 = filesdownloadConvertorpage(self)
        convert1.show()
        print 'Button Pressed'

    def filescleanupconvertor(self):
        self.hide()
        convert1 = filescleanupConvertorpage(self)
        convert1.show()
        print 'Button Pressed'

    def createedditconvertor(self):
        self.hide()
        convert1 = createedditConvertorpage(self)
        convert1.show()
        print 'Button Pressed'



    def startPage(self):

        self.hide()
        startpage = mainWindow()
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





        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Data Release Made Easy")
        self.lbl.move(550,20)
        self.lbl.resize(250,70)


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

# button move  (over, down)





        self.convertpageOne = QtGui.QPushButton('CSV -> XML', self)
        self.convertpageOne.clicked.connect(self.csvtoXmlconvertor)
        self.convertpageOne.setIconSize(QtCore.QSize(24,24))
        self.convertpageOne.move(200,70)
        self.convertpageOne.setFixedSize(250,50)

        self.convertpageTwo = QtGui.QPushButton('IVR DATA DOWNLOAD', self)
        self.convertpageTwo.clicked.connect(self.filesdownloaderconvertor)
        self.convertpageTwo.setIconSize(QtCore.QSize(24,24))
        self.convertpageTwo.move(450,70)
        self.convertpageTwo.setFixedSize(250,50)

        self.convertpageThree = QtGui.QPushButton('IVR CLEANUP', self)
        self.convertpageThree.clicked.connect(self.filescleanupconvertor)
        self.convertpageThree.setIconSize(QtCore.QSize(24,24))
        self.convertpageThree.move(700,70)
        self.convertpageThree.setFixedSize(250,50)

        self.convertpageFour = QtGui.QPushButton('IVR CONVERSION', self)
        self.convertpageFour.clicked.connect(self.createedditconvertor)
        self.convertpageFour.setIconSize(QtCore.QSize(24,24))
        self.convertpageFour.move(950,70)
        self.convertpageFour.setFixedSize(250,50)



        self.listWidget = QtGui.QListWidget(self)

        self.listWidget.move(660,200)
        self.listWidget.resize(450,150)

        self.selectFileButton = QtGui.QPushButton('Clean files in a directory', self)
        self.selectFileButton.move(355, 250)
        self.selectFileButton.setFixedSize(250,50)
        self.selectFileButton.clicked.connect(self.cleanFiles)


        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Most likely the /continious folder")
        self.lbl.move(365,280)
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


        self.show()




    def directoryChoice(self):

        self.listWidget.clear() # In case there are any existing elements in the list
        directory = QtGui.QFileDialog.getExistingDirectory(self, "    Pick a folder")
        print directory + "     In directory Choice"
        for file_name in os.listdir(directory):
            if not file_name.startswith('.'):

                self.listWidget.addItem(file_name)
                print (file_name)
        return directory


    def cleanFiles(self):

        directoryChosen = self.directoryChoice()
        print directoryChosen + "     you made it to files selected \n \n \n \n"


        try:
            cmdDollartohash = ('python replaceDollartohash.py '
                   +str(directoryChosen) + '/')
            print cmdDollartohash
            os.system(cmdDollartohash)
            self.lblNamechange.show()


            print " change dollar to hash over boss \n \n \n \n"

        except Exception:
            print "Changeing dollar to hash failed**************"
            self.Namechange2.show()



        try:
            cmdGroupfiles = ('python groupFiles.py '
                   +str(directoryChosen) + '/')

            print cmdGroupfiles
            os.system(cmdGroupfiles)
            self.lblGroupfiles.show()

            print " grouped the files boss  \n \n \n \n"
        except Exception:
            print "Grouping Files Failed"
            self.lblGroupfiles2.show()

        try:
            cmdRmfiles = ('python rmFiles.py '
                   +str(directoryChosen))

            print cmdRmfiles
            os.system(cmdRmfiles)
            self.lblRemovejunk.show()


            print " removed junk files boss  \n \n \n \n"
        except Exception:
            print "Removing Files Failed"
            self.lblRemovejunk2.show()



    def csvtoXmlconvertor(self):
        self.hide()
        convert1 = convertcsvtoXml(self)
        convert1.show()
        print 'Button Pressed'


    def filesdownloaderconvertor(self):
        self.hide()
        convert1 = filesdownloadConvertorpage(self)
        convert1.show()
        print 'Button Pressed'

    def filescleanupconvertor(self):
        self.hide()
        convert1 = filescleanupConvertorpage(self)
        convert1.show()
        print 'Button Pressed'

    def createedditconvertor(self):
        self.hide()
        convert1 = createedditConvertorpage(self)
        convert1.show()
        print 'Button Pressed'



    def startPage(self):

        self.hide()
        startpage = mainWindow()
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

    def showDate(self, date):

        self.lbl.setText(date.toString())



    def close_application(self):
        print("whooaaaa you quit!!")
        sys.exit()

class convertcsvtoXml(QtGui.QMainWindow):
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





        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Data Release Made Easy")
        self.lbl.move(550,20)
        self.lbl.resize(250,70)


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

# button move  (over, down)





        self.listWidget = QtGui.QListWidget(self)

        self.listWidget.move(360,300)
        self.listWidget.resize(300,300)

        self.listWidgetcomplete = QtGui.QListWidget(self)

        self.listWidgetcomplete.move(780,300)
        self.listWidgetcomplete.resize(300,300)



    # Open a FILE and append to screen
        self.selectFileButton = QtGui.QPushButton('Select Files', self)
        self.selectFileButton.move(455, 250)
        self.selectFileButton.clicked.connect(self.selectFilecsvtoxml)




    # Open a FILE and append to screen
        self.convertButton = QtGui.QPushButton('Convert!', self)
        self.convertButton.move(670,400)
        self.convertButton.clicked.connect(self.osconvertfilecsvtoxml)







        self.convertpageOne = QtGui.QPushButton('CSV -> XML', self)
        self.convertpageOne.clicked.connect(self.csvtoXmlconvertor)
        self.convertpageOne.setIconSize(QtCore.QSize(24,24))
        self.convertpageOne.move(200,70)
        self.convertpageOne.setFixedSize(250,50)

        self.convertpageTwo = QtGui.QPushButton('IVR DATA DOWNLOAD', self)
        self.convertpageTwo.clicked.connect(self.filesdownloaderconvertor)
        self.convertpageTwo.setIconSize(QtCore.QSize(24,24))
        self.convertpageTwo.move(450,70)
        self.convertpageTwo.setFixedSize(250,50)

        self.convertpageThree = QtGui.QPushButton('IVR CLEANUP', self)
        self.convertpageThree.clicked.connect(self.filescleanupconvertor)
        self.convertpageThree.setIconSize(QtCore.QSize(24,24))
        self.convertpageThree.move(700,70)
        self.convertpageThree.setFixedSize(250,50)

        self.convertpageFour = QtGui.QPushButton('IVR CONVERSION', self)
        self.convertpageFour.clicked.connect(self.createedditconvertor)
        self.convertpageFour.setIconSize(QtCore.QSize(24,24))
        self.convertpageFour.move(950,70)
        self.convertpageFour.setFixedSize(250,50)





        self.show()

    def csvtoXmlconvertor(self):
        self.hide()
        convert1 = convertcsvtoXml(self)
        convert1.show()
        print 'Button Pressed'


    def filesdownloaderconvertor(self):
        self.hide()
        convert1 = filesdownloadConvertorpage(self)
        convert1.show()
        print 'Button Pressed'

    def filescleanupconvertor(self):
        self.hide()
        convert1 = filescleanupConvertorpage(self)
        convert1.show()
        print 'Button Pressed'

    def createedditconvertor(self):
        self.hide()
        convert1 = createedditConvertorpage(self)
        convert1.show()
        print 'Button Pressed'



    def startPage(self):

        self.hide()
        startpage = mainWindow()
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

    def showDate(self, date):

        self.lbl.setText(date.toString())



    def close_application(self):
        print("whooaaaa you quit!!")
        sys.exit()



    def selectFilecsvtoxml(self):


        self.listWidget.clear() # In case there are any existing elements in the list
        directory = QtGui.QFileDialog.getExistingDirectory(self, "Pick a folder")
        print directory


        for file_name in os.listdir(directory):
            if file_name.endswith(".csv"):
                self.listWidget.addItem(file_name)
                print (file_name)
        self.directory = directory
        return directory





    def osconvertfilecsvtoxml(self):


        directoryPath = self.directory
        print directoryPath

        cmd = ('python createxmlFromcsv.py '
               +str(directoryPath))
        print cmd
        os.system(cmd)
        for file_name in directoryPath:
            if file_name.endswith(".xml"):
                self.listWidgetcomplete.addItem(file_name)
                print (file_name)



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
        fileOpen = createedditConvertorpage()
        #fileOpen.openFile()
        #self.textEdit.setText(fileOpen.openFile)




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





        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Data Release Made Easy")
        self.lbl.move(550,20)
        self.lbl.resize(250,70)


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

# button move  (over, down)










        self.convertpageOne = QtGui.QPushButton('CSV -> XML', self)
        self.convertpageOne.clicked.connect(self.csvtoXmlconvertor)
        self.convertpageOne.setIconSize(QtCore.QSize(24,24))
        self.convertpageOne.move(200,70)
        self.convertpageOne.setFixedSize(250,50)

        self.convertpageTwo = QtGui.QPushButton('IVR DATA DOWNLOAD', self)
        self.convertpageTwo.clicked.connect(self.filesdownloaderconvertor)
        self.convertpageTwo.setIconSize(QtCore.QSize(24,24))
        self.convertpageTwo.move(450,70)
        self.convertpageTwo.setFixedSize(250,50)

        self.convertpageThree = QtGui.QPushButton('IVR CLEANUP', self)
        self.convertpageThree.clicked.connect(self.filescleanupconvertor)
        self.convertpageThree.setIconSize(QtCore.QSize(24,24))
        self.convertpageThree.move(700,70)
        self.convertpageThree.setFixedSize(250,50)

        self.convertpageFour = QtGui.QPushButton('IVR CONVERSION', self)
        self.convertpageFour.clicked.connect(self.createedditconvertor)
        self.convertpageFour.setIconSize(QtCore.QSize(24,24))
        self.convertpageFour.move(950,70)
        self.convertpageFour.setFixedSize(250,50)



        self.listDirPath = QtGui.QLineEdit(self)
        self.listDirPath.resize(500,50)
        self.listDirPath.move(650,250)


        self.selectFileButton = QtGui.QPushButton('Create merged directory', self)
        self.selectFileButton.move(355, 250)
        self.selectFileButton.setFixedSize(250,50)
        self.selectFileButton.clicked.connect(self.convertDirectory)
        self.selectFileButton.clicked.connect(self.openReadout)







        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Folder contains .csv, .xml, .wav")
        self.lbl.move(365,280)
        self.lbl.resize(250,70)


        self.show()






    def selectFilecsvtoxml(self):



        directory = QtGui.QFileDialog.getExistingDirectory(self, "Pick a folder")
        print directory
        self.listDirPath.setText(directory)

        for file_name in os.listdir(directory):
            if not file_name.startswith("."):

                print (file_name) +  "   this is selectFilcestoxml"
        self.directory = directory
        return directory





    def convertDirectory(self):


        directoryPath = self.selectFilecsvtoxml()
        print directoryPath


        cmd = ('python longXmlEditor.py '
               +str(directoryPath))
        print cmd + "   this is executable command"
        os.system(cmd)

        print "opening popup now .."



    def openFile(self):
        directoryPath = self.selectFilecsvtoxml()
        print " this is openfile"
        print directoryPath + " this is directory in openFile"
        for fileTxt in os.listdir(directoryPath):
            if fileTxt.endswith(".txt"):
                print fileTxt + " this is the file to be opened"
                text = fileTxt.read()
                self.textEdit.setText(text)




















    def openReadout(self):

        readOut = readoutWindow(self)
        readOut.show()
        print ("Opening Readout")


    def csvtoXmlconvertor(self):
        self.hide()
        convert1 = convertcsvtoXml(self)
        convert1.show()
        print 'Button Pressed'


    def filesdownloaderconvertor(self):
        self.hide()
        convert1 = filesdownloadConvertorpage(self)
        convert1.show()
        print 'Button Pressed'

    def filescleanupconvertor(self):
        self.hide()
        convert1 = filescleanupConvertorpage(self)
        convert1.show()
        print 'Button Pressed'

    def createedditconvertor(self):
        self.hide()
        convert1 = createedditConvertorpage(self)
        convert1.show()
        print 'Button Pressed'



    def startPage(self):

        self.hide()
        startpage = mainWindow()
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


        self.myQMenuBar = QtGui.QMenuBar(self)
        self.toolBar = QtGui.QToolBar(self)


#______________
###Actions



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


#Canvas------------------
# button move  (over, down)









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

# button move  (over, down)



        self.convertpageOne = QtGui.QPushButton('CSV -> XML', self)
        self.convertpageOne.clicked.connect(self.csvtoXmlconvertor)
        self.convertpageOne.setIconSize(QtCore.QSize(24,24))
        self.convertpageOne.move(200,70)
        self.convertpageOne.setFixedSize(250,50)

        self.convertpageTwo = QtGui.QPushButton('IVR DATA DOWNLOAD', self)
        self.convertpageTwo.clicked.connect(self.filesdownloaderconvertor)
        self.convertpageTwo.setIconSize(QtCore.QSize(24,24))
        self.convertpageTwo.move(450,70)
        self.convertpageTwo.setFixedSize(250,50)

        self.convertpageThree = QtGui.QPushButton('IVR CLEANUP', self)
        self.convertpageThree.clicked.connect(self.filescleanupconvertor)
        self.convertpageThree.setIconSize(QtCore.QSize(24,24))
        self.convertpageThree.move(700,70)
        self.convertpageThree.setFixedSize(250,50)

        self.convertpageFour = QtGui.QPushButton('IVR CONVERSION', self)
        self.convertpageFour.clicked.connect(self.createedditconvertor)
        self.convertpageFour.setIconSize(QtCore.QSize(24,24))
        self.convertpageFour.move(950,70)
        self.convertpageFour.setFixedSize(250,50)


        self.show()






    def csvtoXmlconvertor(self):
        self.hide()
        convert1 = convertcsvtoXml(self)
        convert1.show()
        print 'Button Pressed'


    def filesdownloaderconvertor(self):
        self.hide()
        convert1 = filesdownloadConvertorpage(self)
        convert1.show()
        print 'Button Pressed'

    def filescleanupconvertor(self):
        self.hide()
        convert1 = filescleanupConvertorpage(self)
        convert1.show()
        print 'Button Pressed'

    def createedditconvertor(self):
        self.hide()
        convert1 = createedditConvertorpage(self)
        convert1.show()
        print 'Button Pressed'










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



#______________
###Actions










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
        self.lbl.setText("Data Team Program")
        self.lbl.resize(145, 25)
        self.lbl.move(580,40)


        self.pixmap = QtGui.QPixmap("intelmed.png")

        self.lbl2 = QtGui.QLabel(self)
        self.lbl2.setPixmap(self.pixmap)
        self.lbl2.move(1000,40)
        self.lbl2.resize(300,200)


        self.pixmap = QtGui.QPixmap("DataScience.png")

        self.lbl2 = QtGui.QLabel(self)
        self.lbl2.setPixmap(self.pixmap)
        self.lbl2.move(300,200)
        self.lbl2.resize(600,600)





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
#
    def popupmsg(self):
        msg = QtGui.QMessageBox.question(self, "Error!",
                                         "If you have any questions feel free to ask.  Email me at EdwinX.Eames@intel.com",
                                         QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if msg == QtGui.QMessageBox.Yes:

            sys.exit()
        else:
            pass



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






def main():
    app = QtGui.QApplication(sys.argv)
    main = mainWindow()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()