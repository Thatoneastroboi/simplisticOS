#loads libraries
import tkinter
#generates hardware/global variables
cache = "test"
powerButton = True
#bootloader code
def bootScreen():
    print("what would you like to do?")
    print("bios check or boot os")
    startQuestion = input()
    if startQuestion == "bios check":
        bioscheck = input()
        root = tkinter.Tk()
        def close():
            root.destroy()
        label = tkinter.Label(root, text=bioscheck)
        stop = tkinter.Button(root, text="close", command=close)
        root.geometry("100x100")
        label.pack()
        stop.pack()
        root.mainloop()
        bootScreen()
    if startQuestion == "boot os":
        import homescreen
    else: 
        bootScreen()
        

 #checks if system/internalOS is on  
if powerButton == True:
    bootScreen()
#instatiates the scheduler
def scheduler():
    processes = ["testprocess1", "testprocess2", "testprocess3"]
scheduler()