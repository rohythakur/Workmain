import sys, os, time
from PyQt4 import QtGui, QtCore
import shutil



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s





class moveWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.initUI()





    def initUI(self):
        self.setGeometry(300,300,800,600)
        self.setWindowTitle("Intel")

        #self.setStyleSheet("background-color: rgb(255, 255, 255);\n")
                           #"border:1px solid rgb(0, 131, 195);")




        self.button = QtGui.QPushButton('Source', self)
        self.button.clicked.connect(self.directorySource)

        self.button.move(150, 120)



        self.source = QtGui.QLineEdit(self)
        self.source.resize(250, 30)
        self.source.move(260,120)


        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Ex: FR_042")
        self.lbl.resize(145, 25)
        self.lbl.move(560,120)




        self.button = QtGui.QPushButton('Destination', self)
        self.button.clicked.connect(self.directoryMaker)

        self.button.move(150, 220)


        self.dest = QtGui.QLineEdit(self)
        self.dest.resize(250, 30)
        self.dest.move(260,220)
        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Ex: releaseNov12")
        self.lbl.resize(145, 25)
        self.lbl.move(560,220)



        self.button = QtGui.QPushButton('Move!', self)
        self.button.clicked.connect(self.quickMove)
        self.button.clicked.connect(self.removeEnd)
        self.button.clicked.connect(self.showFinished)

        self.button.move(350, 280)



        self.buttonclose = QtGui.QPushButton('Quit', self)
        self.buttonclose.clicked.connect(self.close_application)
        self.buttonclose.move(670, 550)


        self.lbl = QtGui.QLabel(self)
        self.lbl.setText("Quick Move")
        self.lbl.resize(145, 25)
        self.lbl.move(360,40)


        self.listWidgetcomplete = QtGui.QListWidget(self)

        self.listWidgetcomplete.move(220,330)
        self.listWidgetcomplete.resize(390,250)






        self.show()



#_________________________________________________________________________









    def close_application(self):
        print("whooaaaa so custom!!!")
        sys.exit()

    def directorySource(self):
        directoryS = QtGui.QFileDialog.getExistingDirectory(self, caption="Pick a folder", directory=QtCore.QDir.currentPath())



        x = str(directoryS)
        print x + " this is string of directory"
        self.source.setText(directoryS)



        return directoryS

    def directoryMaker(self):
        directoryMake = QtGui.QFileDialog.getExistingDirectory(self, caption="Pick a folder", directory=QtCore.QDir.currentPath())

        self.dest.setText(directoryMake)

        x = str(directoryMake)
        print x + " this is string of directory"




        return directoryMake

    def quickMove(self):
        directory = str(self.source.text())
        directoryEnd = str(self.dest.text())
        #print directoryEnd
        print directory
        for root, dirs, files in os.walk(directory):
            if len(files) >= 5:
                for f in files:
                    #print(os.path.join(root, f))

                    if f.endswith("_Edited.xml"):



                        print f + ' THIS WILL BE DATA FILE'
                        fname, fext = os.path.splitext(f)
                        print fname[:-7]

                        try:
                            ftoMove = directory + '/' + fname[:-7] + '/' + f
                            print ftoMove + 'this is file xml to move'
                            shutil.copy2(ftoMove, directoryEnd)

                        except Exception as e:
                            print str(e)

                    elif f.endswith(".wav"):
                        print f + ' This is wav file'
                        fname, fext = os.path.splitext(f)

                        try:
                            ftoMove = directory + '/' + fname + '/' + f
                            print ftoMove + 'this is file xml to move'
                            shutil.copy2(ftoMove, directoryEnd)




                        except Exception as e:
                            print str(e)



    def removeEnd(self):
        directoryEnd = str(self.dest.text())

        print directoryEnd + "this is directory in removeend"

        for f in os.listdir(directoryEnd):
            filepath = os.path.join(directoryEnd, f)
            if f.endswith("_Edited.xml"):
                print f + " this needs to be renamed!!!!"
                os.rename(filepath, filepath[:-11] + '.xml')





    def showFinished(self):
        directoryEnd = str(self.dest.text())

        print directoryEnd + "this is directory in removeend"

        for f in os.listdir(directoryEnd):
            if f.endswith(".xml"):

                self.listWidgetcomplete.addItem(f)





def main():
    app = QtGui.QApplication(sys.argv)
    main = moveWindow()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()



