import subprocess
import sys
import os
import time

def install(package):    
    os.system("pip install "+ str(package))
    os.system("pip3 install "+ str(package))
    
    print("\n" + "Installed " + package.upper() + "\n")

os.system("clear" or "cls")
print("Checking Requirements")
time.sleep(2)
install("git+https://gitlab.com/obuilds/public/pytube@ob-v1 --upgrade")
install("ffmpeg")
print("Requirements Installed Completed")
time.sleep(2)