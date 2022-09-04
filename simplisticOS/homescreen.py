#imports modules
import tkinter
import time
from PIL import Image,ImageTk
#starts window

root = tkinter.Tk()


root.title("simplisticOS")
root.geometry("2000x2000")
bank = Image.open("bg.png")
activityBar = Image.open("activityBar.png")
bankdisplay =  ImageTk.PhotoImage(bank)
activityBarDisplay = ImageTk.PhotoImage(activityBar)
label = tkinter.Label(root, image=bankdisplay)
label2 = tkinter.Label(root, image=activityBarDisplay)
label.pack()
label2.place(y=785, x=225)
import loginpage
root.mainloop()