from tkinter import *
from tkinter import ttk
root=Tk()
root.title("Class3")
root.geometry("500x300")

def currentcar():
    label["text"]=str(box.current()+1)+". "+box.get()


brand = Label(root, text = "廠牌：")
brand.grid(row = 0, column = 0, sticky = W)
label = Label(root, text = "")
label.grid(row = 0 , column= 1, sticky = W)
# 建立下拉式選單 ComboBox
box = ttk.Combobox(root, values = ["BMW", "Mercedes Benz", "Audi"])
box.grid(row = 1, column = 0, columnspan = 3)
ok = Button(root, text = "Ok", command = currentcar)
ok.grid(row = 2, column = 0, sticky = W)



def choose():
    statusbar["text"] = listbox.get(listbox.curselection())

# 宣告用於ListBox的文字變數
listVar = StringVar()

# 建立list BMW
BMW=["1 Series (F40)","1 Series (F52)","2 Series Gran Coupé","2 Series","3 Series","4 Series","5 Series","6 Series","7 Series","8 Series","X1","X2","X3","X4","X5","X6","X7","Z4","2 Series Active Tourer","i3 (G28)","i4","i7","iX1","iX3","iX"]

# 將多個選項內容存人listVar
listVar.set(BMW)

# 建立清單列表 Listbox
listbox = Listbox(root, selectmode = "extended", listvariable = listVar)
listbox.grid(row = 0, column = 0)

choose = Button(root, text = "Choose", command = choose)
choose.grid(row = 1, column = 0, sticky = W)

statusbar = Label(root, text="", relief="sunken", bg="White", fg="Black", anchor=W)
statusbar.grid(row = 2, column = 0, sticky = W+N+E+S)

root.mainloop()