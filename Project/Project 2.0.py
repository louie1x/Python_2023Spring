from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root=Tk()
root.title("Forza Horizon Auction House")
root.geometry("1080x800")

#開啟圖片
img=Image.open("./Project/Img/ForzaLogo.png")
#轉換為 tk 圖片物件
tk_img=ImageTk.PhotoImage(img)
#設定程式Icon
root.iconphoto(True, tk_img)
{"pic":[],}

def new():
    newWindow = Toplevel(root)
    newWindow.geometry("700x665")
    img=Image.open("./Project/Img/ForzaLogo.png")
    resized_logoimg=img.resize((55,55))
    tk_logoimg=ImageTk.PhotoImage(resized_logoimg)
    logolabel=Label(newWindow, image=tk_logoimg)
    logolabel.grid(column=0, row=0, sticky=W)

    #Buttons
    buttonQuit = Button(newWindow, text = "Quit", font=("Inter", 18), fg="#1E1E1E", bg="#ECE8E7", command=newWindow.destroy)
    buttonQuit.grid(pady=2, padx=5, column=4, row=0, columnspan=2, sticky=E+W)



    #Row 1 Banner
    img=Image.open("./Project/Img/S2 Class.png")
    resized_bannerimg=img.resize((252,298))
    tk_bannerimg=ImageTk.PhotoImage(resized_bannerimg)
    bannerlabel=Label(newWindow, image=tk_bannerimg)
    bannerlabel.grid(column=4, row=1, rowspan=4, columnspan=2, sticky=S+W+E)

    #Row 2 Car Image
    img=Image.open("./Project/Img/RimacConceptTwo.png")
    resized_RimacConceptTwoimg=img.resize((222,140))
    RimacConceptTwoimg=ImageTk.PhotoImage(resized_RimacConceptTwoimg)
    RimacConceptTwolabel=Label(newWindow, image=RimacConceptTwoimg, width=202, height=200)
    RimacConceptTwolabel.grid(column=0, row=1, columnspan=4, pady=5, sticky=W)

    img=Image.open("./Project/Img/MercedesAMGOne.png")
    resized_MercedesAMGOneimg=img.resize((222,140))
    MercedesAMGOneimg=ImageTk.PhotoImage(resized_MercedesAMGOneimg)
    MercedesAMGOnelabel=Label(newWindow, image=MercedesAMGOneimg, width=202, height=200)
    MercedesAMGOnelabel.grid(column=0, row=4, columnspan=4, pady=5, sticky=W)

    img=Image.open("./Project/Img/HennesseyVenomF5.png")
    resized_HennesseyVenomF5img=img.resize((222,140))
    HennesseyVenomF5img=ImageTk.PhotoImage(resized_HennesseyVenomF5img)
    HennesseyVenomF5label=Label(newWindow, image=HennesseyVenomF5img, width=202, height=200)
    HennesseyVenomF5label.grid(column=6, row=1, columnspan=4, pady=5, sticky=W)

    img=Image.open("./Project/Img/AstonMartinValhalla.png")
    resized_AstonMartinValhallaimg=img.resize((222,140))
    AstonMartinValhallaimg=ImageTk.PhotoImage(resized_AstonMartinValhallaimg)
    AstonMartinValhallalabel=Label(newWindow, image=AstonMartinValhallaimg, width=202, height=200)
    AstonMartinValhallalabel.grid(column=6, row=4, columnspan=4, padx=5, sticky=W)

    #Row 3 Product Name Label
    productname1=Label(newWindow, text="Rimac Concept Two", font=("Playfair Display", 11), fg="White")
    productname1.grid(column=0, row=2, columnspan=4, padx=5, sticky=W)

    productname2=Label(newWindow, text="Mercedes AMG One", font=("Playfair Display", 11), fg="White")
    productname2.grid(column=0, row=5, columnspan=4, padx=5, sticky=W)

    productname3=Label(newWindow, text="Hennessey Venom F5", font=("Playfair Display", 11), fg="White")
    productname3.grid(column=6, row=2, columnspan=4, padx=5, sticky=W)

    productname4=Label(newWindow, text="Aston Martin Valhalla", font=("Playfair Display", 11), fg="White")
    productname4.grid(column=6, row=5, columnspan=4, padx=5, sticky=W)

    #Row 4 Product Price Label
    productprice1=Label(newWindow, text="2,000,000 CR", font=("Playfair Display", 10), fg="White")
    productprice1.grid(column=0, row=3, padx=5, sticky=W)

    productprice2=Label(newWindow, text="2,700,000 CR", font=("Playfair Display", 10), fg="White")
    productprice2.grid(column=0, row=6, padx=5, sticky=W)

    productprice3=Label(newWindow, text="3,000,000 CR", font=("Playfair Display", 10), fg="White")
    productprice3.grid(column=6, row=3, padx=5, sticky=W)

    productprice4=Label(newWindow, text="1,150,000 CR", font=("Playfair Display", 10), fg="White")
    productprice4.grid(column=6, row=6, padx=5, sticky=W)

    #Row 4 Product Number Label+Buttons
    productnumber1=Label(newWindow, text="0", font=("Playfair Display", 12, "bold"), fg="White", width=7)
    productAddbutton1=Button(newWindow, text="+", font=("Playfair Display", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: add(productnumber1, productprice1))
    productMinusbutton1=Button(newWindow, text="-", font=("Playfair Display", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: minus(productnumber1, productprice1))
    productnumber1.grid(column=2, row=3, sticky=W+E+S+N)
    productAddbutton1.grid(column=3, row=3, sticky=E)
    productMinusbutton1.grid(column=1, row=3, sticky=W)

    productnumber2=Label(newWindow, text="0", font=("Playfair Display", 12, "bold"), fg="White", width=7)
    productAddbutton2=Button(newWindow, text="+", font=("Playfair Display", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: add(productnumber2, productprice2))
    productMinusbutton2=Button(newWindow, text="-", font=("Playfair Display", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: minus(productnumber2, productprice2))
    productnumber2.grid(column=2, row=6, sticky=W+E+S+N)
    productAddbutton2.grid(column=3, row=6, sticky=E)
    productMinusbutton2.grid(column=1, row=6, sticky=W)

    productnumber3=Label(newWindow, text="0", font=("Playfair Display", 12, "bold"), fg="White", width=7)
    productAddbutton3=Button(newWindow, text="+", font=("Playfair Display", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: add(productnumber3, productprice3))
    productMinusbutton3=Button(newWindow, text="-", font=("Playfair Display", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: minus(productnumber3, productprice3))
    productnumber3.grid(column=8, row=3, sticky=W+E+S+N)
    productAddbutton3.grid(column=9, row=3, sticky=E)
    productMinusbutton3.grid(column=7, row=3, sticky=W)

    productnumber4=Label(newWindow, text="0", font=("Playfair Display", 12, "bold"), fg="White", width=7)
    productAddbutton4=Button(newWindow, text="+", font=("Playfair Display", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: add(productnumber4, productprice4))
    productMinusbutton4=Button(newWindow, text="-", font=("Playfair Display", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: minus(productnumber4, productprice4))
    productnumber4.grid(column=8, row=6, sticky=W+E+S+N)
    productAddbutton4.grid(column=9, row=6, sticky=E)
    productMinusbutton4.grid(column=7, row=6, sticky=W)

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

#Big Forza Banner
img=Image.open("./Project/Img/ForzaHorizon5Banner.jpeg")
resized_bannerimg=img.resize((652,400))
tk_bannerimg=ImageTk.PhotoImage(resized_bannerimg)
bannerlabel=Label(root, image=tk_bannerimg)
bannerlabel.grid(column=2, row=1, columnspan=8, sticky=N+E+S+W)

#Car Image
img=Image.open("./Project/Img/BugattiChiron.png")
resized_bugattichironimg=img.resize((202,120))
bugattichironimg=ImageTk.PhotoImage(resized_bugattichironimg)
bugattichironlabel=Label(root, image=bugattichironimg, width=202, height=200)
bugattichironlabel.grid(column=1, row=2, rowspan=2, pady=0, sticky=W)

img=Image.open("./Project/Img/Ferrarif40.png")
resized_Ferrarif40img=img.resize((202,120))
Ferrarif40img=ImageTk.PhotoImage(resized_Ferrarif40img)
Ferrarif40label=Label(root, image=Ferrarif40img, width=202, height=200)
Ferrarif40label.grid(column=1, row=4, rowspan=2, pady=0, sticky=W)

img=Image.open("./Project/Img/LamborghiniCentenario.png")
resized_LamborghiniCentenarioimg=img.resize((242,160))
LamborghiniCentenarioimg=ImageTk.PhotoImage(resized_LamborghiniCentenarioimg)
LamborghiniCentenariolabel=Label(root, image=LamborghiniCentenarioimg, width=202, height=200)
LamborghiniCentenariolabel.grid(column=10, row=2, rowspan=2, padx=0, sticky=W)

img=Image.open("./Project/Img/LotusEvija.png")
resized_LotusEvijaimg=img.resize((202,120))
LotusEvijaimg=ImageTk.PhotoImage(resized_LotusEvijaimg)
LotusEvijalabel=Label(root, image=LotusEvijaimg, width=202, height=200)
LotusEvijalabel.grid(column=10, row=4, rowspan=2, padx=0, sticky=W)


S2classbutton=Button(root, text="S2 Class", font=("Playfair Display", 18, "bold"), fg="#1E1E1E", bg="#ECE8E7", height=2, width=10, command = new)
S2classbutton.grid(column=2, row=2, pady=80, padx=50)

Aclassbutton=Button(root, text="A Class", font=("Playfair Display", 18, "bold"), fg="#1E1E1E", bg="#ECE8E7", height=2, width=10)
Aclassbutton.grid(column=2, row=4, pady=80, padx=50)

S1classbutton=Button(root, text="S1 Class", font=("Playfair Display", 18, "bold"), fg="#1E1E1E", bg="#ECE8E7", height=2, width=10)
S1classbutton.grid(column=9, row=2, pady=80, padx=50)

EcoFriendlyclassbutton=Button(root, text="Eco-Friendly", font=("Playfair Display", 18, "bold"), fg="#1E1E1E", bg="#ECE8E7", height=2, width=10)
EcoFriendlyclassbutton.grid(column=9, row=4, pady=80, padx=50)

totalval = StringVar()
totalval.set("共消費: 0 CR")
totallabel=Label(root, textvariable=totalval, font=("Inter", 18), fg="Black")
totallabel.grid(column=5, row=5, columnspan=2, sticky=W+S)

root.mainloop()