__author__ = 'eeamesX'
import sys, os, time
from PyQt4 import QtGui, QtCore
import shutil



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s




class csvWindow(QtGui.QWidget):

    def __init__(self):
        super(csvWindow, self).__init__()

        self.initUI()





    def initUI(self):
        self.setGeometry(300,300,800,600)
        self.setWindowTitle("Intel")

        #self.setStyleSheet("background-color: rgb(255, 255, 255);\n")
                           #"border:1px solid rgb(0, 131, 195);")



        self.listWidget = QtGui.QListWidget(self)

        self.listWidget.move(160,100)
        self.listWidget.resize(100,100)

        self.listWidgetcomplete = QtGui.QListWidget(self)

        self.listWidgetcomplete.move(580,100)
        self.listWidgetcomplete.resize(100,100)



    # Open a FILE and append to screen
        self.selectFileButton = QtGui.QPushButton('Select Files', self)
        self.selectFileButton.move(255, 250)
        self.selectFileButton.clicked.connect(self.selectFilecsvtoxml)




    # Open a FILE and append to screen
        self.convertButton = QtGui.QPushButton('Convert!', self)
        self.convertButton.move(370,200)
        self.convertButton.clicked.connect(self.osconvertfilecsvtoxml)





        self.quitButton = QtGui.QPushButton('Quit', self)
        self.quitButton.move(570,200)
        self.quitButton.clicked.connect(self.close_application)

        self.show()



#_________________________________________________________________________









    def close_application(self):
        print("whooaaaa so custom!!!")
        self.exit(1)





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





def main():
    app = QtGui.QApplication(sys.argv)
    main = csvWindow()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
