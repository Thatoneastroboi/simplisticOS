#generator
import tkinter
root = tkinter.Tk()

def generateWindow():
    import beans

generate = tkinter.Button(root, text="generate window", command=generateWindow)
generate.pack()

root.mainloop()