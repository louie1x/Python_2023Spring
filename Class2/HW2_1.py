from tkinter import *
# 引入 tkscrolledframe module
from tkscrolledframe import ScrolledFrame
root=Tk()
root.title("HW2_1")
root.geometry("300x100")

# Create scrollframe widget
sframe1 = ScrolledFrame(root, width=300, height=100)
sframe1.pack()
# Bind arrow keys and scroll wheel
sframe1.bind_arrow_keys(root)
sframe1.bind_scroll_wheel(root)
# Create a frame within the ScrolledFrame
inner_frame = sframe1.display_widget(Frame)


food = Label(inner_frame, text= "請選擇食物種類：")
food.grid(row=0, column=0, sticky=W)
def clicked1():
    text = (val1.get())+" "+(val2.get())+" "+(val3.get())+" "+(val4.get())+" "+(val5.get())+" "+(val6.get())
    statusbar["text"] = text
val1 = StringVar()
val2 = StringVar()
val3 = StringVar()
checkbutton1 = Checkbutton(inner_frame, text="和牛", variable=val1, onvalue="和牛", offvalue="", command=clicked1)
checkbutton1.grid(row=1, column=0, sticky=W)
checkbutton2 = Checkbutton(inner_frame, text="伊比利豬", variable=val2, onvalue="伊比利豬", offvalue="", command=clicked1)
checkbutton2.grid(row=1, column=1, sticky=W)
checkbutton3 = Checkbutton(inner_frame, text="海鮮", variable=val3, onvalue="海鮮", offvalue="", command=clicked1)
checkbutton3.grid(row=1, column=2, sticky=W)

drink = Label(inner_frame, text= "請選擇飲料種類：")
drink.grid(row=3, column=0, sticky=W)
val4 = StringVar()
val5 = StringVar()
val6 = StringVar()
checkbutton4 = Checkbutton(inner_frame, text="莊園咖啡", variable=val4, onvalue="莊園咖啡", offvalue="", command=clicked1)
checkbutton4.grid(row=4, column=0, sticky=W)
checkbutton5 = Checkbutton(inner_frame, text="日月潭蜜香紅茶", variable=val5, onvalue="日月潭蜜香紅茶", offvalue="", command=clicked1)
checkbutton5.grid(row=4, column=1, sticky=W)
checkbutton6= Checkbutton(inner_frame, text="伯爵奶茶", variable=val6, onvalue="伯爵奶茶", offvalue="", command=clicked1)
checkbutton6.grid(row=4, column=2, sticky=W)
statusbar = Label(inner_frame, text="", relief="sunken", bg="White", fg="Black", anchor=W)
statusbar.grid(row=5, column=0, columnspan=3, sticky=W+N+E)

root.mainloop()