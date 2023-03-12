from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

root=Tk()
root.title("Class3")
root.geometry("500x300")

def choose():   
    filePath = filedialog.askopenfilename(title = "選取照片", initialdir = "/Users/Louie/Downloads", multiple = False)

    img=Image.open(filePath)
    resized_img=img.resize((150, 100))
    global tk_img
    tk_img = ImageTk.PhotoImage(resized_img)
    imagelabel["image"] = tk_img

choose = Button(root, text = "Choose", command = choose)
choose.grid(row = 0, column = 0, sticky = W)

imagelabel = Label(root)
imagelabel.grid(row = 1, column = 0, rowspan = 2, columnspan = 2)

root.mainloop()