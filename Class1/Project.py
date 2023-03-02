from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.ttk as ttk
root=Tk()
root.title("KubeTech Shop")
root.geometry("900x700")

#開啟圖片
img=Image.open("/Users/Louie/Documents/Python_2023Spring/Class1/logo_tree.png")
#轉換為 tk 圖片物件
tk_img=ImageTk.PhotoImage(img)
#設定程式Icon
root.iconphoto(True, tk_img)

def menu():
    newWindow = Toplevel(root)
    newWindow.geometry("1000x300")
    table=ttk.Treeview(newWindow, columns=["Product Name", "Unit Price", "Quantity", "Subtotal"])
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


    subtotal1 = int(productnumber1['text']) * int(productprice1["text"].replace(",", "").replace("CR", "").strip())
    table.insert('',index='end',text=productname1['text'],values=(productprice1['text'],productnumber1['text'], subtotal1))

    subtotal2 = int(productnumber2['text']) * int(productprice2["text"].replace(",", "").replace("CR", "").strip())
    table.insert('',index='end',text=productname2['text'],values=(productprice2['text'],productnumber2['text'], subtotal2))

    subtotal3 = int(productnumber3['text']) * int(productprice3["text"].replace(",", "").replace("CR", "").strip())
    table.insert('',index='end',text=productname3['text'],values=(productprice3['text'],productnumber3['text'], subtotal3))

    subtotal4 = int(productnumber4['text']) * int(productprice4["text"].replace(",", "").replace("CR", "").strip())
    table.insert('',index='end',text=productname4['text'],values=(productprice4['text'],productnumber4['text'], subtotal4))

    total = subtotal1+subtotal2+subtotal3+subtotal4
    table.insert('',index='end',text='Total',values=['','', total], tags=('totalcolor'))

    table.pack()

    newWindow.mainloop()

def createNewWindow():
    newWindow = Toplevel(root)
    newWindow.geometry("300x200")
    mylabel = Label(newWindow, text = "已結帳完成!")
    mylabel.pack()
    newWindow.mainloop()


def new():
    newWindow = Toplevel(root)
    newWindow.geometry("880x650")
    img=Image.open("/Users/louie/Documents/Python_2022Autumn/Class10/Forza5Logo.png")
    resized_logoimg=img.resize((55,55))
    tk_logoimg=ImageTk.PhotoImage(resized_logoimg)
    logolabel=Label(newWindow, image=tk_logoimg)
    logolabel.grid(column=0, row=0, sticky=W)

    #Buttons
    S2classbutton=Button(newWindow, text="S2 Class", font=("Inter", 18), fg="#1E1E1E", bg="#ECE8E7", width=5)
    S2classbutton.grid(pady=2, padx=5, column=1, row=0, sticky=E+W)

    S1classbutton=Button(newWindow, text="S1 Class", font=("Inter", 18), fg="#1E1E1E", bg="#ECE8E7", width=5)
    S1classbutton.grid(pady=2, padx=5, column=2, row=0, sticky=E+W)

    Aclassbutton=Button(newWindow, text="A Class", font=("Inter", 18), fg="#1E1E1E", bg="#ECE8E7", width=5)
    Aclassbutton.grid(pady=2, padx=5, column=3, row=0, sticky=E+W)

    buttonQuit = Button(newWindow, text = "Quit", font=("Inter", 18), fg="#1E1E1E", bg="#ECE8E7", width=12, command=newWindow.destroy)
    buttonQuit.grid(pady=2, padx=5, column=7, row=0, sticky=E)



    #Row 1 Banner
    img=Image.open("/Users/louie/Documents/Python_2022Autumn/Class10/forza-banner.jpeg")
    resized_bannerimg=img.resize((852,298))
    tk_bannerimg=ImageTk.PhotoImage(resized_bannerimg)
    bannerlabel=Label(newWindow, image=tk_bannerimg)
    bannerlabel.grid(column=0, row=1, columnspan=8, sticky=N+E+S+W)

    #Row 2 Sofa Image
    img=Image.open("/Users/louie/Documents/Python_2022Autumn/Class10/Screen Shot 2022-12-17 at 1.17.34 PM.png")
    resized_sofa1img=img.resize((202,200))
    tk_sofa1img=ImageTk.PhotoImage(resized_sofa1img)
    sofa1label=Label(newWindow, image=tk_sofa1img, width=202, height=200)
    sofa1label.grid(column=0, row=2, columnspan=2, pady=5, sticky=W)

    img=Image.open("/Users/louie/Documents/Python_2022Autumn/Class10/Screen Shot 2022-12-17 at 1.02.56 PM.png")
    resized_sofa2img=img.resize((202,200))
    tk_sofa2img=ImageTk.PhotoImage(resized_sofa2img)
    sofa2label=Label(newWindow, image=tk_sofa2img, width=202, height=200)
    sofa2label.grid(column=2, row=2, columnspan=2, pady=5, sticky=W)

    img=Image.open("/Users/louie/Documents/Python_2022Autumn/Class10/Screen Shot 2022-12-18 at 3.50.00 PM.png")
    resized_sofa3img=img.resize((202,200))
    tk_sofa3img=ImageTk.PhotoImage(resized_sofa3img)
    sofa3label=Label(newWindow, image=tk_sofa3img, width=202, height=200)
    sofa3label.grid(column=4, row=2, columnspan=2, pady=5, sticky=W)

    img=Image.open("/Users/louie/Documents/Python_2022Autumn/Class10/Screen Shot 2022-12-18 at 3.52.57 PM.png")
    resized_sofa4img=img.resize((202,200))
    tk_sofa4img=ImageTk.PhotoImage(resized_sofa4img)
    sofa4label=Label(newWindow, image=tk_sofa4img, width=202, height=200)
    sofa4label.grid(column=6, row=2, columnspan=2, padx=5, sticky=W)

    #Row 3 Product Name Label
    productname1=Label(newWindow, text="Porsche Taycan Turbo S", font=("Inter", 11), fg="Black")
    productname1.grid(column=0, row=3, columnspan=2, padx=5, sticky=W)

    productname2=Label(newWindow, text="Nissan GT-R Black Edition", font=("Inter", 11), fg="Black")
    productname2.grid(column=2, row=3, columnspan=2, padx=5, sticky=W)

    productname3=Label(newWindow, text="Mercedes-AMG GT-R", font=("Inter", 11), fg="Black")
    productname3.grid(column=4, row=3, columnspan=2, padx=5, sticky=W)

    productname4=Label(newWindow, text="Acura NSX", font=("Inter", 11), fg="Black")
    productname4.grid(column=6, row=3, columnspan=2, padx=5, sticky=W)

    #Row 4 Product Price Label
    productprice1=Label(newWindow, text="185,000 CR", font=("Inter", 10), fg="Black")
    productprice1.grid(column=0, row=4, padx=5, sticky=W)

    productprice2=Label(newWindow, text="250,000 CR", font=("Inter", 10), fg="Black")
    productprice2.grid(column=2, row=4, padx=5, sticky=W)

    productprice3=Label(newWindow, text="295,000 CR", font=("Inter", 10), fg="Black")
    productprice3.grid(column=4, row=4, padx=5, sticky=W)

    productprice4=Label(newWindow, text="170,000 CR", font=("Inter", 10), fg="Black")
    productprice4.grid(column=6, row=4, padx=5, sticky=W)

    #Row 4 Product Number Label+Buttons
    productnumber1=Label(newWindow, text="0", font=("Inter", 12, "bold"), fg="Black", width=7)
    productAddbutton1=Button(newWindow, text="+", font=("Inter", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: add(productnumber1, productprice1))
    productMinusbutton1=Button(newWindow, text="-", font=("Inter", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: minus(productnumber1, productprice1))
    productnumber1.grid(column=1, row=4, sticky=W+E+S+N)
    productAddbutton1.grid(column=1, row=4, sticky=E)
    productMinusbutton1.grid(column=1, row=4, sticky=W)

    productnumber2=Label(newWindow, text="0", font=("Inter", 12, "bold"), fg="Black", width=7)
    productAddbutton2=Button(newWindow, text="+", font=("Inter", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: add(productnumber2, productprice2))
    productMinusbutton2=Button(newWindow, text="-", font=("Inter", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: minus(productnumber2, productprice2))
    productnumber2.grid(column=3, row=4, sticky=W+E+S+N)
    productAddbutton2.grid(column=3, row=4, sticky=E)
    productMinusbutton2.grid(column=3, row=4, sticky=W)

    productnumber3=Label(newWindow, text="0", font=("Inter", 12, "bold"), fg="Black", width=7)
    productAddbutton3=Button(newWindow, text="+", font=("Inter", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: add(productnumber3, productprice3))
    productMinusbutton3=Button(newWindow, text="-", font=("Inter", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: minus(productnumber3, productprice3))
    productnumber3.grid(column=5, row=4, sticky=W+E+S+N)
    productAddbutton3.grid(column=5, row=4, sticky=E)
    productMinusbutton3.grid(column=5, row=4, sticky=W)

    productnumber4=Label(newWindow, text="0", font=("Inter", 12, "bold"), fg="Black", width=7)
    productAddbutton4=Button(newWindow, text="+", font=("Inter", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: add(productnumber4, productprice4))
    productMinusbutton4=Button(newWindow, text="-", font=("Inter", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: add(productnumber4, productprice4))
    productnumber4.grid(column=7, row=4, sticky=W+E+S+N)
    productAddbutton4.grid(column=7, row=4, sticky=E, padx=(0,35))
    productMinusbutton4.grid(column=7, row=4, sticky=W, padx=(35,0))

    newWindow.mainloop()

#Add and Minus Def
def add(numberlabel, pricelabel):
    numberlabel["text"] = int(numberlabel["text"])+1
    price = int(pricelabel["text"].replace(",", "").replace("CR", "").strip())
    total = int(totalval.get().split(":")[1].replace("CR", "").strip())
    totalval.set("共消費: "+str(total+price)+" CR")

def minus(numberlabel, pricelabel):
    if int(numberlabel["text"])>0:
        numberlabel["text"] = int(numberlabel["text"])-1
    else:
        messagebox.showwarning("showwarning", "The number of products can\'t be below 0")
    price = int(pricelabel["text"].replace(",", "").replace("CR", "").strip())
    total = int(totalval.get().split(":")[1].replace("CR", "").strip())
    totalval.set("共消費: "+str(total-price)+" CR")

def new2():
    newWindow2 = Toplevel(root)
    newWindow2.geometry("910x650")
    img=Image.open("/Users/louie/Documents/Python_2022Autumn/Class10/Forza5Logo.png")
    resized_logoimg=img.resize((55,55))
    tk_logoimg=ImageTk.PhotoImage(resized_logoimg)
    logolabel=Label(newWindow2, image=tk_logoimg)
    logolabel.grid(column=0, row=0, sticky=W)

    #Buttons
    S2classbutton=Button(newWindow2, text="S2 Class", font=("Inter", 18), fg="#1E1E1E", bg="#ECE8E7", width=5)
    S2classbutton.grid(pady=2, padx=5, column=1, row=0, sticky=E+W)

    S1classbutton=Button(newWindow2, text="S1 Class", font=("Inter", 18), fg="#1E1E1E", bg="#ECE8E7", width=5)
    S1classbutton.grid(pady=2, padx=5, column=2, row=0, sticky=E+W)

    Aclassbutton=Button(newWindow2, text="A Class", font=("Inter", 18), fg="#1E1E1E", bg="#ECE8E7", width=5)
    Aclassbutton.grid(pady=2, padx=5, column=3, row=0, sticky=E+W)

    buttonQuit = Button(newWindow2, text = "Quit", font=("Inter", 18), fg="#1E1E1E", bg="#ECE8E7", width=12, command=newWindow2.destroy)
    buttonQuit.grid(pady=2, padx=5, column=7, row=0, sticky=E)



    #Row 1 Banner
    img=Image.open("/Users/louie/Documents/Python_2022Autumn/Class10/forza-banner.jpeg")
    resized_bannerimg=img.resize((852,298))
    tk_bannerimg=ImageTk.PhotoImage(resized_bannerimg)
    bannerlabel=Label(newWindow2, image=tk_bannerimg)
    bannerlabel.grid(column=0, row=1, columnspan=8, sticky=N+E+S+W)

    #Row 2 Sofa Image
    img=Image.open("/Users/louie/Documents/Python_2022Autumn/Class10/Screen Shot 2022-12-21 at 9.16.31 PM.png")
    resized_sofa1img=img.resize((202,200))
    tk_sofa1img=ImageTk.PhotoImage(resized_sofa1img)
    sofa1label=Label(newWindow2, image=tk_sofa1img, width=202, height=200)
    sofa1label.grid(column=0, row=2, columnspan=2, pady=5, sticky=W)

    img=Image.open("/Users/louie/Documents/Python_2022Autumn/Class10/Screen Shot 2022-12-21 at 9.31.59 PM.png")
    resized_sofa2img=img.resize((202,200))
    tk_sofa2img=ImageTk.PhotoImage(resized_sofa2img)
    sofa2label=Label(newWindow2, image=tk_sofa2img, width=202, height=200)
    sofa2label.grid(column=2, row=2, columnspan=2, pady=5, sticky=W)

    img=Image.open("/Users/louie/Documents/Python_2022Autumn/Class10/Screen Shot 2022-12-21 at 9.36.26 PM.png")
    resized_sofa3img=img.resize((202,200))
    tk_sofa3img=ImageTk.PhotoImage(resized_sofa3img)
    sofa3label=Label(newWindow2, image=tk_sofa3img, width=202, height=200)
    sofa3label.grid(column=4, row=2, columnspan=2, pady=5, sticky=W)

    img=Image.open("/Users/louie/Documents/Python_2022Autumn/Class10/Screen Shot 2022-12-21 at 9.45.30 PM.png")
    resized_sofa4img=img.resize((202,200))
    tk_sofa4img=ImageTk.PhotoImage(resized_sofa4img)
    sofa4label=Label(newWindow2, image=tk_sofa4img, width=202, height=200)
    sofa4label.grid(column=6, row=2, columnspan=2, padx=5, sticky=W)

    #Row 3 Product Name Label
    productname1=Label(newWindow2, text="Dodge Challenger SRT Demon", font=("Inter", 11), fg="Black")
    productname1.grid(column=0, row=3, columnspan=2, padx=5, sticky=W)

    productname2=Label(newWindow2, text="Porsche Cayenne Turbo", font=("Inter", 11), fg="Black")
    productname2.grid(column=2, row=3, columnspan=2, padx=5, sticky=W)

    productname3=Label(newWindow2, text="Toyota GR Supra", font=("Inter", 11), fg="Black")
    productname3.grid(column=4, row=3, columnspan=2, padx=5, sticky=W)

    productname4=Label(newWindow2, text="Lamborghini Gallardo LP 570-4 Spyder Performante", font=("Inter", 11), fg="Black")
    productname4.grid(column=6, row=3, columnspan=2, padx=5, sticky=W)

    #Row 4 Product Price Label
    productprice1=Label(newWindow2, text="150,000 CR", font=("Inter", 10), fg="Black")
    productprice1.grid(column=0, row=4, padx=5, sticky=W)

    productprice2=Label(newWindow2, text="220,000 CR", font=("Inter", 10), fg="Black")
    productprice2.grid(column=2, row=4, padx=5, sticky=W)

    productprice3=Label(newWindow2, text="55,000 CR", font=("Inter", 10), fg="Black")
    productprice3.grid(column=4, row=4, padx=5, sticky=W)

    productprice4=Label(newWindow2, text="280,000 CR", font=("Inter", 10), fg="Black")
    productprice4.grid(column=6, row=4, padx=5, sticky=W)

    #Row 4 Product Number Label+Buttons
    productnumber1=Label(newWindow2, text="0", font=("Inter", 12, "bold"), fg="Black", width=7)
    productAddbutton1=Button(newWindow2, text="+", font=("Inter", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: add(productnumber1, productprice1))
    productMinusbutton1=Button(newWindow2, text="-", font=("Inter", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: minus(productnumber1, productprice1))
    productnumber1.grid(column=1, row=4, sticky=W+E+S+N)
    productAddbutton1.grid(column=1, row=4, sticky=E)
    productMinusbutton1.grid(column=1, row=4, sticky=W)

    productnumber2=Label(newWindow2, text="0", font=("Inter", 12, "bold"), fg="Black", width=7)
    productAddbutton2=Button(newWindow2, text="+", font=("Inter", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: add(productnumber2, productprice2))
    productMinusbutton2=Button(newWindow2, text="-", font=("Inter", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: minus(productnumber2, productprice2))
    productnumber2.grid(column=3, row=4, sticky=W+E+S+N)
    productAddbutton2.grid(column=3, row=4, sticky=E)
    productMinusbutton2.grid(column=3, row=4, sticky=W)

    productnumber3=Label(newWindow2, text="0", font=("Inter", 12, "bold"), fg="Black", width=7)
    productAddbutton3=Button(newWindow2, text="+", font=("Inter", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: add(productnumber3, productprice3))
    productMinusbutton3=Button(newWindow2, text="-", font=("Inter", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: minus(productnumber3, productprice3))
    productnumber3.grid(column=5, row=4, sticky=W+E+S+N)
    productAddbutton3.grid(column=5, row=4, sticky=E)
    productMinusbutton3.grid(column=5, row=4, sticky=W)

    productnumber4=Label(newWindow2, text="0", font=("Inter", 12, "bold"), fg="Black", width=7)
    productAddbutton4=Button(newWindow2, text="+", font=("Inter", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: add(productnumber4, productprice4))
    productMinusbutton4=Button(newWindow2, text="-", font=("Inter", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: add(productnumber4, productprice4))
    productnumber4.grid(column=7, row=4, sticky=W+E+S+N)
    productAddbutton4.grid(column=7, row=4, sticky=E, padx=(0,35))
    productMinusbutton4.grid(column=7, row=4, sticky=W, padx=(35,0))

    newWindow2.mainloop()

#Row 0 Logo
img=Image.open("/Users/louie/Documents/Python_2022Autumn/Class10/Forza5Logo.png")
resized_logoimg=img.resize((55,55))
tk_logoimg=ImageTk.PhotoImage(resized_logoimg)
logolabel=Label(root, image=tk_logoimg)
logolabel.grid(column=0, row=0, sticky=W)

#Buttons
S2classbutton=Button(root, text="S2 Class", font=("Inter", 18), fg="#1E1E1E", bg="#ECE8E7", width=5)
S2classbutton.grid(pady=2, padx=5, column=1, row=0, sticky=E+W)

S1classbutton=Button(root, text="S1 Class", font=("Inter", 18), fg="#1E1E1E", bg="#ECE8E7", width=5, command=new)
S1classbutton.grid(pady=2, padx=5, column=2, row=0, sticky=E+W)

Aclassbutton=Button(root, text="A Class", font=("Inter", 18), fg="#1E1E1E", bg="#ECE8E7", width=5, command=new2)
Aclassbutton.grid(pady=2, padx=5, column=3, row=0, sticky=E+W)

loginbutton=Button(root, text="會員登入/註冊", font=("Inter", 18), fg="#1E1E1E", bg="#ECE8E7", width=12)
loginbutton.grid(pady=2, padx=5, column=7, row=0, sticky=E)



#Row 1 Banner
img=Image.open("/Users/louie/Documents/Python_2022Autumn/Class10/forza-banner.jpeg")
resized_bannerimg=img.resize((852,298))
tk_bannerimg=ImageTk.PhotoImage(resized_bannerimg)
bannerlabel=Label(root, image=tk_bannerimg)
bannerlabel.grid(column=0, row=1, columnspan=8, sticky=N+E+S+W)

#Row 2 Sofa Image
img=Image.open("/Users/louie/Documents/Python_2022Autumn/Class10/Screen Shot 2022-12-18 at 3.16.36 PM.png")
resized_sofa1img=img.resize((202,200))
tk_sofa1img=ImageTk.PhotoImage(resized_sofa1img)
sofa1label=Label(root, image=tk_sofa1img, width=202, height=200)
sofa1label.grid(column=0, row=2, columnspan=2, pady=5, sticky=W)

img=Image.open("/Users/louie/Documents/Python_2022Autumn/Class10/Screen Shot 2022-12-18 at 3.18.47 PM.png")
resized_sofa2img=img.resize((202,200))
tk_sofa2img=ImageTk.PhotoImage(resized_sofa2img)
sofa2label=Label(root, image=tk_sofa2img, width=202, height=200)
sofa2label.grid(column=2, row=2, columnspan=2, pady=5, sticky=W)

img=Image.open("/Users/louie/Documents/Python_2022Autumn/Class10/Screen Shot 2022-12-17 at 1.11.33 PM.png")
resized_sofa3img=img.resize((202,200))
tk_sofa3img=ImageTk.PhotoImage(resized_sofa3img)
sofa3label=Label(root, image=tk_sofa3img, width=202, height=200)
sofa3label.grid(column=4, row=2, columnspan=2, pady=5, sticky=W)

img=Image.open("/Users/louie/Documents/Python_2022Autumn/Class10/Screen Shot 2022-12-18 at 3.14.37 PM.png")
resized_sofa4img=img.resize((202,200))
tk_sofa4img=ImageTk.PhotoImage(resized_sofa4img)
sofa4label=Label(root, image=tk_sofa4img, width=202, height=200)
sofa4label.grid(column=6, row=2, columnspan=2, padx=5, sticky=W)

#Row 3 Product Name Label
productname1=Label(root, text="Pagani Huayra BC", font=("Inter", 11), fg="Black")
productname1.grid(column=0, row=3, columnspan=2, padx=5, sticky=W)

productname2=Label(root, text="Pagani Zonda R", font=("Inter", 11), fg="Black")
productname2.grid(column=2, row=3, columnspan=2, padx=5, sticky=W)

productname3=Label(root, text="PORSCHE 918 SPYDER", font=("Inter", 11), fg="Black")
productname3.grid(column=4, row=3, columnspan=2, padx=5, sticky=W)

productname4=Label(root, text="Bugatti Divo", font=("Inter", 11), fg="Black")
productname4.grid(column=6, row=3, columnspan=2, padx=5, sticky=W)

#Row 4 Product Price Label
productprice1=Label(root, text="2,700,000 CR", font=("Inter", 10), fg="Black")
productprice1.grid(column=0, row=4, padx=5, sticky=W)

productprice2=Label(root, text="1,800,000 CR", font=("Inter", 10), fg="Black")
productprice2.grid(column=2, row=4, padx=5, sticky=W)

productprice3=Label(root, text="850,000 CR", font=("Inter", 10), fg="Black")
productprice3.grid(column=4, row=4, padx=5, sticky=W)

productprice4=Label(root, text="3,000,000 CR", font=("Inter", 10), fg="Black")
productprice4.grid(column=6, row=4, padx=5, sticky=W)

#Row 4 Product Number Label+Buttons
productnumber1=Label(root, text="0", font=("Inter", 12, "bold"), fg="Black", width=7)
productAddbutton1=Button(root, text="+", font=("Inter", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: add(productnumber1, productprice1))
productMinusbutton1=Button(root, text="-", font=("Inter", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: minus(productnumber1, productprice1))
productnumber1.grid(column=1, row=4, sticky=W+E+S+N)
productAddbutton1.grid(column=1, row=4, sticky=E)
productMinusbutton1.grid(column=1, row=4, sticky=W)

productnumber2=Label(root, text="0", font=("Inter", 12, "bold"), fg="Black", width=7)
productAddbutton2=Button(root, text="+", font=("Inter", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: add(productnumber2, productprice2))
productMinusbutton2=Button(root, text="-", font=("Inter", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: minus(productnumber2, productprice2))
productnumber2.grid(column=3, row=4, sticky=W+E+S+N)
productAddbutton2.grid(column=3, row=4, sticky=E)
productMinusbutton2.grid(column=3, row=4, sticky=W)

productnumber3=Label(root, text="0", font=("Inter", 12, "bold"), fg="Black", width=7)
productAddbutton3=Button(root, text="+", font=("Inter", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: add(productnumber3, productprice3))
productMinusbutton3=Button(root, text="-", font=("Inter", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: minus(productnumber3, productprice3))
productnumber3.grid(column=5, row=4, sticky=W+E+S+N)
productAddbutton3.grid(column=5, row=4, sticky=E)
productMinusbutton3.grid(column=5, row=4, sticky=W)

productnumber4=Label(root, text="0", font=("Inter", 12, "bold"), fg="Black", width=7)
productAddbutton4=Button(root, text="+", font=("Inter", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: add(productnumber4, productprice4))
productMinusbutton4=Button(root, text="-", font=("Inter", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: add(productnumber4, productprice4))
productnumber4.grid(column=7, row=4, sticky=W+E+S+N)
productAddbutton4.grid(column=7, row=4, sticky=E, padx=(0,35))
productMinusbutton4.grid(column=7, row=4, sticky=W, padx=(35,0))

#Row 5 Layout
root.rowconfigure(5, weight=2)
detaillistbutton=Button(root, text="詳細清單", font=("Inter", 18), fg="Black", bg="#ECEDE7", command=menu)
detaillistbutton.grid(row=5, column=0, sticky=W+S, padx=5, pady=1)

img=Image.open("/Users/louie/Documents/Python_2022Autumn/Class10/Shopping Cart.png")
resized_shoppingcartimg=img.resize((30,30))
tk_shoppingcartimg=ImageTk.PhotoImage(resized_shoppingcartimg)
shoppingcartlabel=Label(root, image=tk_shoppingcartimg)
shoppingcartlabel.grid(column=4, row=5, sticky=E+S)

totalval = StringVar()
totalval.set("共消費: 0 CR")
totallabel=Label(root, textvariable=totalval, font=("Inter", 18), fg="Black")
totallabel.grid(column=5, row=5, columnspan=2, sticky=W+S)

checkoutbutton=Button(root, text="結帳", font=("Inter", 18), fg="Black", bg="#ECEDE7", command=createNewWindow)
checkoutbutton.grid(row=5, column=7, sticky=E+S)

root.mainloop()