import os
import sys
import platform
import youtube_dl
import platform
import datetime
import mainwindow
from mainwindow import *
from builtins import *
from datetime import date
from PyQt5 import QtCore, QtGui, QtWidgets


now = datetime.now()
current_time = now.strftime("%H:%M:%S")





class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)






    def load(self):

        def my_hook(d):
            if d['status'] == 'finished':
                print('Done downloading, now converting ...')
                self.console.append('Done downloading, now converting ...')

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(id)s',
            'noplaylist' : True,
            'progress_hooks': [my_hook],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            gettext = self.inpuri.text()
            ydl.download([gettext])

        detectos()



    def detectos(self):
        osy = platform.system()
        archx = platform.machine()
        ver = platform.version()

        print("Your system: " + osy)
        print("Your machine: " + archx)
        print("Your system version: " + ver)

        self.console.append("Your system: " + osy)
        self.console.append("Your machine: " + archx)
        self.console.append("Your system version: " + ver)





def initxcon():
    print("\n===============================================\n")
    print("This is a python-console-log(Verbose-level:> 2)")
    print("\nYoutube-Downloader - v0.1a | by BlackLeakz\n")
    print("\n===============================================\n")
    print("\nCurrent Time =", current_time)
    print("\nconsolelog@oClock " + current_time)
    print("\n===============================================\n")








def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()



if __name__ == '__main__':
    initxcon()
    main()
