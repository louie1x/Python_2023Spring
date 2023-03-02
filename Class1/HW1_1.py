from tkinter import *
# 引入 Pillow Module
from PIL import Image, ImageTk
root=Tk()
root.geometry("1000x300")
root.title("Class1")

def buttonstart():
    statusbar["text"]="processing..."
def buttondone():
    statusbar["text"]="Done"

buttonstart=Button(root, text="Start", command=buttonstart)
buttonstart.pack()
buttonstart=Button(root, text="Done", command=buttondone)
buttonstart.pack()
statusbar=Label(root, text="Initialization...", relief="sunken", bg="White", fg="Black", anchor=W, bd=2)
statusbar.pack(fill=X, side=BOTTOM)


root.mainloop()