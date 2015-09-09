#! /usr/bin/python
import sys, os
from PyQt4 import QtGui, QtCore
import subprocess





class Window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)



        self.setWindowTitle("Intel!")

        self.setMinimumHeight(600)
        self.setMaximumHeight(600)
        self.setMinimumWidth(800)
        self.setMaximumWidth(800)
        self.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)

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



        self.button = QtGui.QPushButton('', self)
        self.button.clicked.connect(self.handleButton)
        self.button.setIcon(QtGui.QIcon('min1.png'))
        self.button.setIconSize(QtCore.QSize(24,24))
        self.button.move(20, 150)
        self.button.setFixedSize(100,75)


        self.button2 = QtGui.QPushButton('', self)
        self.button2.clicked.connect(lambda: self.run('visWaves.py'))
        self.button2.setIcon(QtGui.QIcon('min2.jpeg'))
        self.button2.setIconSize(QtCore.QSize(24,24))
        self.button2.move(20, 330)
        self.button2.setFixedSize(100,75)


        self.button4 = QtGui.QPushButton('', self)
        self.button4.clicked.connect(self.handleButton)
        self.button4.setIcon(QtGui.QIcon('min3.jpeg'))
        self.button4.setIconSize(QtCore.QSize(24,24))
        self.button4.move(20, 500)
        self.button4.setFixedSize(100,75)

        self.text = QtGui.QLabel('')

        self.text2 = QtGui.QLabel('Hello welcome to version 1.0')
        self.text2.move(500,500)

        cal = QtGui.QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(500, 450)
        cal.clicked[QtCore.QDate].connect(self.showDate)

        self.lbl = QtGui.QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130, 260)


        self.show()






#_________________________________________________________________________
    #Functions--------------------------------------------------------------




    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()
    def drawLines(self, qp):

        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)

        qp.setPen(pen)
        qp.drawLine(20, 100, 750, 100)


    def button1(self):
        pass

    def button2(self):
        pass

    def button2(self):
        pass

    def button2(self):
        pass


    def handleButton(self):
        sys.exit()

    def close_application(self):
        print("whooaaaa so custom!!!")
        sys.exit()


    def popupmsg(self):
        msg = QtGui.QMessageBox.question(self, "Error!",
                                         "If you have any questions feel free to ask.  Email me at EdwinX.Eames@intel.com",
                                         QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if msg == QtGui.QMessageBox.Yes:

            sys.exit()
        else:
            pass


    def run(self, path):
        subprocess.call([sys.executable,path])

    def showDate(self, date):

        self.lbl.setText(date.toString())



#_____________________
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())