# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets # UI libraries
from PyQt5.QtGui import QPixmap
from glob import glob #The glob module finds all the pathnames matching a specified pattern
import random as rd # we use that to generate rundom numbers
#import cv2 as cv 
import sys #

images = glob('images/*.png') + glob('images/*.jpg') #finds all images and shoves them to a list
memes = glob('memes/*.png')+glob('memes/*.jpg')

print(len(images))
print(images)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):# Creates thw UI window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1373, 860)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.randomButton = QtWidgets.QPushButton(self.centralwidget)
        self.randomButton.setGeometry(QtCore.QRect(50, 60, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.randomButton.setFont(font)
        self.randomButton.setObjectName("randomButton")
        self.randomButton.clicked.connect(self.showImage)
        self.customButton = QtWidgets.QPushButton(self.centralwidget)
        self.customButton.setGeometry(QtCore.QRect(90, 160, 131, 41))
        self.customButton.setObjectName("customButton")
        self.customSettingsButton = QtWidgets.QToolButton(self.centralwidget)
        self.customSettingsButton.setGeometry(QtCore.QRect(220, 160, 41, 41))
        self.customSettingsButton.setObjectName("customSettingsButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(330, 20, 1011, 721))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.imageViewer = QtWidgets.QLabel(self.frame)
        self.imageViewer.setGeometry(QtCore.QRect(0, 0, 1011, 721))
        self.imageViewer.setObjectName("imageViewer")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1373, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow): # Sets text to Buttons
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.randomButton.setText(_translate("MainWindow", "Random"))
        self.customButton.setText(_translate("MainWindow", "custom"))
        self.customSettingsButton.setText(_translate("MainWindow", "..."))
        self.imageViewer.setText(_translate("MainWindow", ""))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSave.setText(_translate("MainWindow", "Save..."))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))

    def showImage(self): #shows the image
        self.image = QPixmap(self.loadRandomImage())
        self.resizeImage = self.image.scaled(800, 600, QtCore.Qt.KeepAspectRatio)
        self.imageViewer.setPixmap(self.resizeImage)

    def loadRandomImage(self): # this in the end will influence the probability of different types of images from a template
        self.i = rd.randint(1, 10)  # we set i as a random number so we can then influence the frequency of the images that will appear
        self.j = rd.randint(0,11) 
        if self.i <= 5:
            self.n = rd.randint(0, 7)
        elif self.i > 5 and self.i <= 8:
            self.n = rd.randint(8, 14)
        elif self.i > 8 and self.i <= 10:
            self.n = rd.randint(15, 19)
        print(self.n)
        if j<=1:
            self.selectedImagePath = images[self.n]
        elif j>=2:
            self.selectedImagePath=memes[self.n] 
        return self.selectedImagePath

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
