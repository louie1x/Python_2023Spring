from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Class3")
root.geometry("500x300")

def currentcar():
    if box.get() == "BMW":
        listVar.set(BMW)
    elif box.get() == "Mercedes Benz":
        listVar.set(Mercedes)
    else:
        listVar.set(Audi)
    label["text"]="廠牌："+str(box.current()+1)+". "+box.get()

def choose():
    statusbar["text"] = listbox.get(listbox.curselection())

label = Label(root, text = "廠牌：")
label.grid(row = 0 , column= 0, sticky = W)

box = ttk.Combobox(root, values = ["BMW", "Mercedes Benz", "Audi"])
box.grid(row = 1, column = 0, sticky = W)

ok = Button(root, text = "Ok", command = currentcar)
ok.grid(row = 2, column = 0, sticky = W)

listVar = StringVar()

BMW=["1 Series (F40)","1 Series (F52)","2 Series Gran Coupé","2 Series","3 Series","4 Series","5 Series","6 Series","7 Series","8 Series","X1","X2","X3","X4","X5","X6","X7","Z4","2 Series Active Tourer","i3 (G28)","i4","i7","iX1","iX3","iX"]
Mercedes=["A-Class(Hatchbacks)","A-Class(Sedans)","C-Class","CLA","CLS","E-Class","EQE","EQS","S-Class","C-Class","CLA","E-Class","E-Class","EQA","EQB","EQC","G-Class","GLA","GLB","GLC","GLE","GLS","AMG GT","AMG GT 4-Door Coupé","AMG SL","AMG One","B-Class","Citan Van","Viano","EQV"]
Audi=["A1","A3","A4","A5","A6","A7","A8","e-tron GT","TT","R8","Q2","Q3","2019","Q4 e-tron","2021","Q5","Q5 e-tron","Q6","Q7","Q8","e-tron"]

listVar.set(Audi)

listbox = Listbox(root, selectmode = "extended", listvariable = listVar)
listbox.grid(row = 4, column = 0, sticky = W)

choose = Button(root, text = "Choose", command = choose)
choose.grid(row = 5, column = 0, sticky = W)

statusbar = Label(root, text="", relief="sunken", bg="White", fg="Black", anchor=W)
statusbar.grid(row = 6, column = 0, sticky = W+N+E+S)

root.mainloop()