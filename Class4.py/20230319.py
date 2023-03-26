from tkinter import *
root=Tk()
root.title("Class4")
root.geometry("500x300")

#---------------------------------------------------------------------------------------------------------------------------------------

# def getValue(e):
#     value.set("年齡： "+str(year_scale.get()))

# # 建議標題 Label
# titlelabel = Label(root, text = "請選擇年齡：")
# titlelabel.grid(row = 0, column = 0, columnspan = 2, sticky = W)

# # 建立 Scale 元件
# year_scale = Scale(root, length = 300, from_ = 0, to = 100, orient = HORIZONTAL, resolution = 1, showvalue = True, command =getValue)
# year_scale.grid(row = 1, column = 0, columnspan = 3)

# # 建立字串變數
# value = StringVar()
# value.set("年齡： 0")

# # 建立Label
# statusbar = Label(root, textvariable = value, text="年齡："+str(year_scale.get()), relief="sunken", bg="White", fg="Black", anchor=W)
# statusbar.grid(row = 2, column = 0, columnspan = 3, sticky = W+E+S)

#---------------------------------------------------------------------------------------------------------------------------------------

# def getValue():
#     value.set("身高： "+str(height.get()))

# # 建立標題 Label
# value = StringVar()
# value.set("身高： 0")

# # 建立標題 Label
# titlelabel = Label(root, text = "身高：", textvariable = value)
# titlelabel.grid(row = 0, column = 0, columnspan = 2, sticky = W)

# # 建立標題 Spinboxx 
# height = Spinbox(root, from_ = 0, to = 100, command = getValue)
# height.grid(row = 1, column = 0, columnspan = 3)

#---------------------------------------------------------------------------------------------------------------------------------------

root.mainloop()