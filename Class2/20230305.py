from tkinter import *
# 引入 tkscrolledframe module
from tkscrolledframe import ScrolledFrame
root=Tk()
root.title("Flight Ticket")
root.geometry("270x300")

#-------------------------------------------------------------------------------------------------

# destination = Label(root, text= "目的地：")
# destination.grid(row=0, column=0, sticky=E)
# def clicked1():
#     statusbar["textvariable"]=val
# def clicked2():
#     statusbar["textvariable"]=val
# def clicked3():
#     statusbar["textvariable"]=val
# val = StringVar()
# radiobtn1 = Radiobutton(root, text="東京", variable=val, value="東京", command=clicked1)
# radiobtn1.grid(row=1, column=0, sticky=E)
# radiobtn1.select()
# radiobtn2 = Radiobutton(root, text="德國", variable=val, value="德國", command=clicked2)
# radiobtn2.grid(row=1, column=1, sticky=E)
# radiobtn3 = Radiobutton(root, text="紐約", variable=val, value="紐約", command=clicked3)
# radiobtn3.grid(row=1, column=2, sticky=E)
# statusbar = Label(root, textvariable=val, relief="sunken", bg="White", fg="Black", anchor=W)
# statusbar.grid(row=2, column=0, columnspan=3, sticky=W+N+E)

#-------------------------------------------------------------------------------------------------

# turnplane = Label(root, text= "轉機次數：")
# turnplane.grid(row=0, column=0, sticky=W)
# def clicked1():
#     text = (val1.get())+" "+(val2.get())+" "+(val3.get())
#     statusbar["text"] = text
# val1 = StringVar()
# val2 = StringVar()
# val3 = StringVar()
# checkbutton1 = Checkbutton(root, text="直飛", variable=val1, onvalue="直飛", offvalue="", command=clicked1)
# checkbutton1.grid(row=1, column=0, sticky=W)
# checkbutton2 = Checkbutton(root, text="轉機一次", variable=val2, onvalue="轉機一次", offvalue="", command=clicked1)
# checkbutton2.grid(row=1, column=1, sticky=W)
# checkbutton3 = Checkbutton(root, text="轉機兩次以上", variable=val3, onvalue="轉機兩次以上", offvalue="", command=clicked1)
# checkbutton3.grid(row=1, column=2, sticky=W)
# statusbar = Label(root, text="", relief="sunken", bg="White", fg="Black", anchor=W)
# statusbar.grid(row=2, column=0, columnspan=3, sticky=W+N+E)

#-------------------------------------------------------------------------------------------------

# Create scrollframe widget
sframe1 = ScrolledFrame(root, width=300, height=300)
sframe1.pack()
# Bind arrow keys and scroll wheel
sframe1.bind_arrow_keys(root)
sframe1.bind_scroll_wheel(root)
# Create a frame within the ScrolledFrame
inner_frame = sframe1.display_widget(Frame)

button1 = Button(inner_frame, text="1", height=5)
button1.grid(row = 0, column = 0)
button2 = Button(inner_frame, text="2", height=5)
button2.grid(row = 1, column = 0)
button3 = Button(inner_frame, text="3", height=5)
button3.grid(row = 2, column = 0)
button4 = Button(inner_frame, text="4", height=5)
button4.grid(row = 3, column = 0)
button5= Button(inner_frame, text="5", height=5)
button5.grid(row = 4, column = 0)


root.mainloop()