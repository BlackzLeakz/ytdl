import os
import sys
import subprocess
import platform
from git import Repo
from datetime import datetime


now = datetime.now()
current_time = now.strftime("%H:%M:%S")



def conf():
    dlpath = input("Enter Download-Path:~$ ")



def det():
    sysxx = platform.system()
    if sysxx == 'Windows':
        windows()
    if sysxx == 'Linux':
        linux()

    else:
        print("OS not supported, exit().")
        sys.exit()



def autoinit():
    print("\Auto setup... please wait while trying to setup *\n" + current_time)
    print("\nDetecting now runnin' os... \n")
    det()



def windows():
    print("\nSeting up youtubedl for a Windows system!\n" + current_time)
    conf()
    Repo.clone_from("https://github.com/BlackLeakz96/youtubedl/", dlpath)
    os.system("cd " + dlpath)
    os.system("icacls " + dlpath + " /q /c /t /grant Users:F")
    os.system("python3 -m pip install -r requirements.txt")



def linux():
    print("\nSeting up youtubedl for a linux system!\n" + current_time)
    conf()
    Repo.clone_from("https://github.com/BlackLeakz96/youtubedl/", dlpath)
    os.system("cd " + dlpath)
    os.system("sudo chmod 777 -R ./* && me=$(whoami) && sudo chown $me -hR ./*")
    os.system("python3 -m pip install -r requirements.txt")




#def main():#
    #autoinit()





#if __name__ == '__main__':
#    main()
