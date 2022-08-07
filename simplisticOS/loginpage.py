#imports libs
import math
import tkinter
import time
#establishes tkinter
root = tkinter.Tk()
#instatiates login page
label = tkinter.Label(root, text="welcome to simplistic OS!")
label2 = tkinter.Label(root, text="please enter a passcode.")
passwordInput = tkinter.Entry(root)
submitButton = tkinter.Button(root, width = 10, text="submit")
for i in 20:
    print(passwordInput)
    time.sleep(2)
label.pack()
label2.pack()
passwordInput.pack()
submitButton.pack()
#starts tk
root.mainloop()
