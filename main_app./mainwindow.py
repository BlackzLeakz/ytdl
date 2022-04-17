import os
import sys
import platform
import youtube_dl
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets


now = datetime.now()
current_time = now.strftime("%H:%M:%S")




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 472)
        MainWindow.setStyleSheet("background-color:    rgb(0, 0, 0);\n"
"color: rgb(0, 255, 106);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.inpuri = QtWidgets.QLineEdit(self.centralwidget)
        self.inpuri.setGeometry(QtCore.QRect(10, 350, 681, 21))
        self.inpuri.setObjectName("inpuri")

        self.dlbtn = QtWidgets.QPushButton(self.centralwidget)
        self.dlbtn.setGeometry(QtCore.QRect(710, 350, 80, 21))
        self.dlbtn.setObjectName("dlbtn")
        self.dlbtn.clicked.connect(self.load)

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 781, 281))
        self.groupBox.setObjectName("groupBox")

        self.console = QtWidgets.QTextBrowser(self.groupBox)
        self.console.setGeometry(QtCore.QRect(0, 20, 781, 261))
        self.console.setObjectName("console")
        self.console.append("\n================================================\n")
        self.console.append("\n== Youtube-Downloader |by BlackLeakz 16042022 ==\n")
        self.console.append("\n================================================\n")
        self.console.append("\n== This is the console log - verbose = True   ==\n")
        self.console.append("\n================================================\n")
        self.console.append("\n~~~ https://github.com/BlackLeakz96/youtubedl ~~\n")
        self.console.append("\nConsoleLog@" + current_time + " oClock")
        self.console.append("\n\n\n")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 330, 251, 16))
        self.label.setObjectName("label")

        self.groupBox.raise_()
        self.inpuri.raise_()
        self.dlbtn.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menuBar.setObjectName("menuBar")

        self.menuMain = QtWidgets.QMenu(self.menuBar)
        self.menuMain.setObjectName("menuMain")
        MainWindow.setMenuBar(self.menuBar)

        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")

        self.actionAbout_2 = QtWidgets.QAction(MainWindow)
        self.actionAbout_2.setObjectName("actionAbout_2")

        self.actionUpdate_2 = QtWidgets.QAction(MainWindow)
        self.actionUpdate_2.setObjectName("actionUpdate_2")

        self.actionWebsite = QtWidgets.QAction(MainWindow)
        self.actionWebsite.setObjectName("actionWebsite")

        self.menuMain.addAction(self.actionAbout_2)
        self.menuMain.addAction(self.actionUpdate_2)
        self.menuMain.addAction(self.actionWebsite)
        self.menuBar.addAction(self.menuMain.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube-Downloader"))
        self.dlbtn.setText(_translate("MainWindow", "Download"))
        self.groupBox.setTitle(_translate("MainWindow", "Console"))
        self.label.setText(_translate("MainWindow", "Enter download- url: "))
        self.menuMain.setTitle(_translate("MainWindow", "Main"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.actionAbout_2.setText(_translate("MainWindow", "About"))
        self.actionUpdate_2.setText(_translate("MainWindow", "Update"))
        self.actionWebsite.setText(_translate("MainWindow", "Website"))


#def my_hook(d):
    #if d['status'] == 'finished':
        #print('Done downloading, now converting ...')
#
#ydl_opts = {
    #'format': 'bestaudio/best',
    #'outtmpl': '%(id)s',
    #'noplaylist' : True,
    #'progress_hooks': [my_hook],
#}
