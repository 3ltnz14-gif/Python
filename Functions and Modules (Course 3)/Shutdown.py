import os

shutdown = input("do you wish to shutdown your computer y/n ")

if shutdown == "n":
    exit()
else:
    os.system("shutdown /s /t 1")