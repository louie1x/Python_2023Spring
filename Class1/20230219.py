from tkinter import *
# 引入 Pillow Module
from PIL import Image, ImageTk
root=Tk()
root.geometry("1000x300")
root.title("Class1")

#開啟圖片
img=Image.open("/Users/Louie/Documents/Python_2023Spring/Class1/logo_tree.png")
#轉換為 tk 圖片物件
tk_img=ImageTk.PhotoImage(img)
#設定程式Icon
root.iconphoto(True, tk_img)

#--------------------------------------------------------------------------------------------------

# #建立 Label
# label1=Label(root, text="flat", relief="flat")
# #加入視窗
# label1.pack()
# label2=Label(root, text="flat", relief="groove")
# label2.pack()
# label3=Label(root, text="flat", relief="raised")
# label3.pack()
# label4=Label(root, text="flat", relief="ridge")
# label4.pack()
# label5=Label(root, text="flat", relief="solid")
# label5.pack()
# label6=Label(root, text="flat", relief="sunken")
# label6.pack()

#--------------------------------------------------------------------------------------------------

# #方法一 (靜態)
# def buttonstart():
#     statusbar["text"]="processing..."
# def buttondone():
#     statusbar["text"]="Done"

# buttonstart=Button(root, text="Start", command=buttonstart)
# buttonstart.pack()
# buttonstart=Button(root, text="Done", command=buttondone)
# buttonstart.pack()
# statusbar=Label(root, text="Initialization...", relief="sunken", bg="White", fg="Black", anchor=W, bd=2)
# statusbar.pack(fill=X, side=BOTTOM)

# #方法二 (動態)
# # statusBar
# # start button function
# def start():
#     mystringvar.set("processing...")
# # stop button function
# def stop():
#     mystringvar.set("Done")
# # start button object
# Start=Button(text="Start", commmand=start)
# Start.pack()
# #stop button object
# Stop=Button(text="Stop", command=stop)
# Stop.pack()
# # 建立StringVar
# mystringvar=StringVar()
# mystringvar.set("Initialization...")

# #建立 Label
# statusBar=Label(root, textvariable=mystringvar, fg="black", bg="white", anchor=W, relief="sunken", bd=2)
# #加入視窗
# statusBar.pack(side="bottom", fill="x")

#--------------------------------------------------------------------------------------------------

import tkinter.ttk as ttk

table=ttk.Treeview(root, columns=["Product Name", "Unit Price", "Quantity", "Subtotal"])
# create columns title
table.heading("#0", text="Product name")
table.heading("#1", text="Unit Price")
table.heading("#2", text="Quantity")
table.heading("#3", text="Subtotal")

table.column("#0", width=250, anchor=CENTER)
table.column("#1", anchor=CENTER)
table.column("#2", anchor=CENTER)
table.column("#3", anchor=CENTER)

table.tag_configure("totalcolor", background="#E7E2E2")
table.insert("", index="end", text="Sofa", values=("20000", "2", "40000"))

table.pack()

#--------------------------------------------------------------------------------------------------

root.mainloop()