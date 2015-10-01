__author__ = 'ed'
import sys
import os
import subprocess


import windows
import csvtoxmlPage
import windowConvertor
import windowDatascience

import windowGame


from PyQt4 import QtGui, QtCore

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


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

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    childwindow = dataRelease()
    childwindow.show()

    sys.exit(app.exec_())

