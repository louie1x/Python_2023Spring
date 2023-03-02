from tkinter import *
# 引入 Pillow Module
from PIL import Image, ImageTk
import tkinter.ttk as ttk
root=Tk()
root.geometry("1000x300")
root.title("Class1")

#開啟圖片
img=Image.open("/Users/Louie/Documents/Python_2023Spring/Class1/logo_tree.png")
#轉換為 tk 圖片物件
tk_img=ImageTk.PhotoImage(img)
#設定程式Icon
root.iconphoto(True, tk_img)

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

root.mainloop()