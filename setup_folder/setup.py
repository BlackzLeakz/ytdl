import os
import sys
import subprocess
import platform
import setupui
import datetime
from setupui import *
from git import Repo
from datetime import datetime
#from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
from os.path import *

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

    def load_opt1():
        currdir = os.getcwd()
        print(currdir)
        self.log.append("\nGot current working directory: " + currdir + "\n" + current_time)
        #os.system("cd")
        os.system('mkdir youtubedl')
        self.log.append("\nDownloading requiremnts from blackzspace.org server...\n " + current_time)

    #    proc = subprocess.run('ping blackzspace.org', stdout=subprocess.PIPE)
#        output = proc.communicate()
        #print(output)
        Repo.clone_from("https://github.com/BlackLeakz96/youtubedl/", "youtubedl")
        self.log.append("\n cloning repository from grithub: git clone https://github.com/BlackLeakz96/youtubedl/ " + current_time)


    def load_opt2():
        self.log.append("\nDownloading requirements over python3-console.\n" + current_time)

        os.system('python3 -m pip install PySide2')
        self.log.append("\nInstalling PySide2 using python3 -m pip *** --" + current_time)
        os.system('python3 -m pip install PySide6')
        self.log.append("\nInstalling PySide6 using python3 -m pip *** --" + current_time)
        os.system('python3 -m pip install GitPython')
        self.log.append("\nInstalling GitPython using python3 -m pip *** --" + current_time)
        os.system('python3 -m pip install pyqt5')
        self.log.append("\nInstalling pyqt5 using python3 -m pip *** --" + current_time)
        os.system('python3 -m pip install PyQt5')
        self.log.append("\nInstalling PyQt5 using python3 -m pip *** --" + current_time)
        os.system('python3 -m pip install youtube_dl')
        self.log.append("\nInstalling youtube_dl using python3 -m pip *** --" + current_time)

    #    detdir = self.inpdir.text()
        #os.system('')
        currdir = os.getcwd()
        print(currdir)
        self.log.append("\nGot current working directory: " + currdir + "\n" + current_time)
        #os.system("cd")
        os.system('mkdir youtubedl')
    #    os.system('cd youtubedl')
    #    os.system('cd C:\Users\Public')
        #subprocess.call('cd %appdata%')
    #    subprocess.call('mkdir youtubedl')

        #os.system('mkdir youtubedl')
        #os.system
        #os.system('cd yo')
#        dirx = self.inpdir.setText("C:\Users\Public")
        getdir = self.inpdir.text()
        if getdir == '':
            self.log.append("\nInstallationpath is empty, trying to install to tmp path...\n" + current_time)
        #else kommt gleich



        Repo.clone_from("https://github.com/BlackLeakz96/youtubedl.git", "youtubedl")
        #Repo.clone_from("https://github.com/BlackLeakz96/youtubedl/", '%appdata%')
        #self.log.append("\nDownloaded repository to %appdata%...\n" + current_time)
        self.log.append("\nDownloaded repository to : " + currdir + " youtubedl\n" + current_time)
        self.log.append("\nStarting now the main-app!...\n" + current_time)
        os.system("python3 main.py")

    def install(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        checkx = self.accept.isChecked()
        if checkx == True:
            self.log.append("\nStarting installation....\n" + current_time)
            ossys = platform.system()
            self.log.append("\nDetected OverdriveSystem: " + ossys + "\n" + current_time)
            self.log.append("\nConfiguring setup for your system....\n" + current_time)
            if ossys == 'Windows':
                load_opt1()
            if current_time == 'Linux':
                self.log.append("How do you run an windows executable file without emulating windows on linux?lel, u wonder me <3 this is only the windows.exe installmanager <33" + current_time)
        else:
            self.log.append("You need to accept the terms/conditions---" + current_time)
            return False
    #    while True:







def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
