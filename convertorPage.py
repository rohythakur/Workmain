__author__ = 'ed'
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon Sep 28 20:16:46 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class mainWindow(object):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.initUI()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1280, 800)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 70, 331, 671))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.calendarWidget = QtGui.QCalendarWidget(self.frame)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 10, 311, 201))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(0, 610, 331, 61))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 550, 331, 61))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.SciencePage = QtGui.QPushButton(self.frame)
        self.SciencePage.setGeometry(QtCore.QRect(0, 490, 331, 61))
        self.SciencePage.setObjectName(_fromUtf8("SciencePage"))
        self.pushButton_4 = QtGui.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 430, 331, 61))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 370, 331, 61))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(360, 70, 911, 671))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pushButton_3 = QtGui.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 140, 211, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.listWidget = QtGui.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(80, 230, 301, 291))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.pushButton_6 = QtGui.QPushButton(self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(410, 360, 141, 61))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.listWidget_2 = QtGui.QListWidget(self.tab)
        self.listWidget_2.setGeometry(QtCore.QRect(570, 230, 301, 291))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(300, 40, 231, 61))
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Game Page", None))
        self.pushButton_2.setText(_translate("MainWindow", "Upload / download DATA", None))
        self.SciencePage.setText(_translate("MainWindow", "Science Page", None))
        self.pushButton_4.setText(_translate("MainWindow", "Convertor", None))
        self.pushButton_5.setText(_translate("MainWindow", "Home", None))
        self.pushButton_3.setText(_translate("MainWindow", "Browse Directory", None))
        self.pushButton_6.setText(_translate("MainWindow", "Convert", None))
        self.label.setText(_translate("MainWindow", "Convert Directory CSV to XML", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
def main():

    app = QtGui.QApplication(sys.argv)
    main = mainWindow()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()