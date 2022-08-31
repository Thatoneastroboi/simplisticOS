#loads libraries
import math
import time
#generates hardware/global variables
cache = "test"
powerButton = True
#bootloader code
def bootScreen():
    print("what would you like to do?")
    print("bios check or boot os")
    startQuestion = input()
    if startQuestion == "bios check":
        inputTest = input()
        print(inputTest)
        bootScreen()
    if startQuestion == "boot os":
        import loginpage
    else: 
        bootScreen()
        

def boot():
    test = True
    print("system booting")
    bootScreen()
 #checks if system/internalOS is on  
if powerButton == True:
    boot()
#instatiates the scheduler
def scheduler():
    processes = ["testprocess1", "testprocess2", "testprocess3"]
scheduler()