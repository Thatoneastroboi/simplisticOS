#imports modules
import tkinter
import time
from PIL import Image,ImageTk
#starts window

root = tkinter.Tk()


root.title("simplisticOS")
root.geometry("1000x1000")
bank = Image.open("bg.png")
activityBar = Image.open("activitybar.png")
bankdisplay =  ImageTk.PhotoImage(bank)
activitybardisplay =  ImageTk.PhotoImage(activityBar)
label = tkinter.Label(root, image=bankdisplay)
label.pack()
label2 = tkinter.Label(root, image=activitybardisplay)
label2.pack()
import loginpage
root.mainloop()