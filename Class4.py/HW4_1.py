from tkinter import *

root = Tk()
root.title("Class4")
root.geometry("500x300")

def getValueR(e):
    valueR.set("R: " + str(year_scaleR.get()))
    update_color()

def getValueB(e):
    valueB.set("B: " + str(year_scaleB.get()))
    update_color()

def getValueG(e):
    valueG.set("G: " + str(year_scaleG.get()))
    update_color()

def update_color():
    r = year_scaleR.get()
    g = year_scaleG.get()
    b = year_scaleB.get()
    color_hex = f"#{r:02x}{g:02x}{b:02x}"
    color_label.config(bg=color_hex)

# 建議標題 Label
title_label = Label(root, text="選擇顏色(R,G,B)")
title_label.grid(row=0, column=0, columnspan=2, sticky=W)

# R E D

# 建立 Scale 元件
year_scaleR = Scale(root, length=300, from_=0, to=256, orient=HORIZONTAL, resolution=1, showvalue=True, command=getValueR)
year_scaleR.grid(row=2, column=0, columnspan=3)

# 建立字串變數
valueR = StringVar()
valueR.set("R: 0")

# 建立Label
statusbarR = Label(root, textvariable=valueR, text="R: " + str(year_scaleR.get()), anchor=W)
statusbarR.grid(row=1, column=0, columnspan=3, sticky=W+E+S)

# B L U E

# 建立 Scale 元件
year_scaleB = Scale(root, length=300, from_=0, to=256, orient=HORIZONTAL, resolution=1, showvalue=True, command=getValueB)
year_scaleB.grid(row=4, column=0, columnspan=3)

# 建立字串變數
valueB = StringVar()
valueB.set("B: 0")

# 建立Label
statusbarB = Label(root, textvariable=valueB, text="B: " + str(year_scaleB.get()), anchor=W)
statusbarB.grid(row=3, column=0, columnspan=3, sticky=W+E+S)

# G R E E N

# 建立 Scale 元件
year_scaleG = Scale(root, length=300, from_=0, to=256, orient=HORIZONTAL, resolution=1, showvalue=True, command=getValueG)
year_scaleG.grid(row=6, column=0, columnspan=3)

# 建立字串變數
valueG = StringVar()
valueG.set("G: 0")

# 建立Label
statusbarG = Label(root, textvariable=valueG, text="G: " + str(year_scaleG.get()), anchor=W)
statusbarG.grid(row=5, column=0, columnspan=3, sticky=W+E+S)

# Color label
color_label = Label(root, text="",relief="sunken", bg="White", fg="Black", anchor=W)
color_label.grid(row=7, column=0, columnspan=3, sticky = W+N+E+S)

root.mainloop()
