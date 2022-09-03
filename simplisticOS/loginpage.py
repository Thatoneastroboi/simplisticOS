import tkinter as tk

root = tk.Tk()
root.title("login")


def close():
    root.destroy()

label1 = tk.Label(root, text="please enter a passcode.")
password = tk.Entry(root)
submitbutton = tk.Button(root, text="submit", command=close)
label1.pack()
password.pack()
submitbutton.pack()

root.mainloop()