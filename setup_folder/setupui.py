import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("appicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color:    rgb(17, 17, 17);\n"
"color:    rgb(0, 255, 225);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 20, 301, 31))
        self.label.setObjectName("label")

        self.progBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progBar.setGeometry(QtCore.QRect(0, 550, 791, 23))
        self.progBar.setProperty("value", 24)
        self.progBar.setObjectName("progBar")

        self.accept = QtWidgets.QCheckBox(self.centralwidget)
        self.accept.setGeometry(QtCore.QRect(20, 320, 381, 19))
        self.accept.setObjectName("accept")
        self.accept.setChecked(False)
        self.accept.stateChanged.connect(self.acceptbox)

        self.instbtn = QtWidgets.QPushButton(self.centralwidget)
        self.instbtn.setGeometry(QtCore.QRect(700, 350, 80, 21))
        self.instbtn.setObjectName("instbtn")
        self.instbtn.clicked.connect(self.install)

        self.log = QtWidgets.QTextBrowser(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(20, 60, 761, 251))
        self.log.setObjectName("log")
        self.log.append("\nInstallationManager-LOG:~$ " + current_time + "\n")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 390, 271, 16))
        self.label_2.setObjectName("label_2")

        self.inpdir = QtWidgets.QLineEdit(self.centralwidget)
        self.inpdir.setGeometry(QtCore.QRect(20, 410, 601, 21))
        self.inpdir.setObjectName("inpdir")
    #    detdir = self.inpdir.text()
    #    self.log.append("\nYou selected: " + detdir + " as your installation-folder.")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube-Downloader Installmanager (c) by BlackLeakz@blackspace.cf | v0.1a  || ~~~ OPEN SOURCE ~~~"))
        MainWindow.setWhatsThis(_translate("MainWindow", "This is an installer."))
        self.label.setText(_translate("MainWindow", "Youtube-Downloader Installation-Manager | by blackspace.cf"))
        self.accept.setText(_translate("MainWindow", "Accept"))
        self.instbtn.setText(_translate("MainWindow", "Install"))
        self.label_2.setText(_translate("MainWindow", "Installation folder:"))






    def acceptbox(self, state):

        if state == QtCore.Qt.Checked:
            print("Accepted terms/conditions...")
            self.log.append("Accepted terms/conditions...")

            return True
        else:
            print("You need to accept terms/conditions...")
            self.log.append("You need to accept terms/conditions...")

            return False
