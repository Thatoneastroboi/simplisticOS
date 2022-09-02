#imports modules
import tkinter
import time
from PIL import Image,ImageTk
#starts window

root = tkinter.Tk()


root.title("simplisticOS")
root.geometry("1000x1000")
bank = Image.open("bg.png")
bankdisplay =  ImageTk.PhotoImage(bank)
label = tkinter.Label(root, image=bankdisplay)
label.pack()
import loginpage
root.mainloop()