from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root=Tk()
root.title("Forza Horizon Auction House")
root.geometry("1150x850+150+10")

#開啟圖片
img=Image.open("./Project/Img/ForzaLogo.png")
#轉換為 tk 圖片物件
tk_img=ImageTk.PhotoImage(img)
#設定程式Icon
root.iconphoto(True, tk_img)

S2_Class_CarInfo = {"pic":["./Project/Img/KoenigseggJesko.png", "./Project/Img/MercedesAMGOne.png", "./Project/Img/HennesseyVenomF5.png", "./Project/Img/LamborghiniSestoElemento.png"], "name":["Koenigsegg Jesko", "Mercedes AMG One", "Hennessey Venom F5", "Lamborghini Sesto Elemento"], "price":["2,800,000 CR", "2,700,000 CR", "3,000,000 CR", "2,500,000 CR"], "engine":["5.0L Twin-Turbocharged V8"+'\n'+"                                  1280 bhp (954 kW), 883 lb⋅ft (1197 N·m)", "1.6L Turbocharged Hybrid V6"+'\n'+"877 bhp (654 kW), 535 lb⋅ft (725 N·m)", "6.6L Twin-Turbocharged V8"+'\n'+"1817 bhp (1355 kW), 1193 lb⋅ft (1617 N·m)", "5.2L Naturally-Aspirated V10"+'\n'+"571 bhp (426 kW), 398 lb⋅ft (540 N·m)"], "layout":["Mid-Engined, Rear-Wheel Drive"+'\n'+"9-speed Transmission", "Mid-Engined, All-Wheel Drive"+'\n'+"8-speed Transmission", "Mid-Engined, Rear-Wheel Drive"+'\n'+"7-speed Transmission", "Mid-Engined, All-Wheel Drive"+'\n'+"6-speed Transmission"], "weight":["3131 lbs (1420 kg)", "3737 lbs (1695 kg)", "3053 lbs (1385 kg)", "2202 lbs (999 kg)"]}
S1_Class_CarInfo = {"pic":["./Project/Img/PorscheCarreraGT.png", "./Project/Img/McLaren720SSpider.png", "./Project/Img/FerrariEnzo.png", "./Project/Img/BugattiEB110.png"], "name":["Porsche Carrera GT", "McLaren 720S Spider", "Ferrari Enzo", "Bugatti EB110"], "price":["1,000,000 CR", "340,000 CR", "2,800,000 CR", "1,700,000 CR"], "engine":["5.0L Twin-Turbocharged V8"+'\n'+"                                  1280 bhp (954 kW), 883 lb⋅ft (1197 N·m)", "1.6L Turbocharged Hybrid V6"+'\n'+"877 bhp (654 kW), 535 lb⋅ft (725 N·m)", "6.6L Twin-Turbocharged V8"+'\n'+"1817 bhp (1355 kW), 1193 lb⋅ft (1617 N·m)", "5.2L Naturally-Aspirated V10"+'\n'+"571 bhp (426 kW), 398 lb⋅ft (540 N·m)"], "layout":["Mid-Engined, Rear-Wheel Drive"+'\n'+"9-speed Transmission", "Mid-Engined, All-Wheel Drive"+'\n'+"8-speed Transmission", "Mid-Engined, Rear-Wheel Drive"+'\n'+"7-speed Transmission", "Mid-Engined, All-Wheel Drive"+'\n'+"6-speed Transmission"], "weight":["3131 lbs (1420 kg)", "3737 lbs (1695 kg)", "3053 lbs (1385 kg)", "2202 lbs (999 kg)"]}
A_Class_CarInfo = {"pic":["./Project/Img/LamborghiniCountach.png", "./Project/Img/Porsche911GT2.png", "./Project/Img/ToyotaSupraRZ.png", "./Project/Img/Mercedes-BenzE63AMG.png"], "name":["Lamborghini Countach", "Porsche 911 GT2", "Toyota Supra RZ", "Mercedes-Benz E63 AMG"], "price":["220,000 CR", "550,000 CR", "38,000 CR", "105,000 CR"], "engine":["5.0L Twin-Turbocharged V8"+'\n'+"                                  1280 bhp (954 kW), 883 lb⋅ft (1197 N·m)", "1.6L Turbocharged Hybrid V6"+'\n'+"877 bhp (654 kW), 535 lb⋅ft (725 N·m)", "6.6L Twin-Turbocharged V8"+'\n'+"1817 bhp (1355 kW), 1193 lb⋅ft (1617 N·m)", "5.2L Naturally-Aspirated V10"+'\n'+"571 bhp (426 kW), 398 lb⋅ft (540 N·m)"], "layout":["Mid-Engined, Rear-Wheel Drive"+'\n'+"9-speed Transmission", "Mid-Engined, All-Wheel Drive"+'\n'+"8-speed Transmission", "Mid-Engined, Rear-Wheel Drive"+'\n'+"7-speed Transmission", "Mid-Engined, All-Wheel Drive"+'\n'+"6-speed Transmission"], "weight":["3131 lbs (1420 kg)", "3737 lbs (1695 kg)", "3053 lbs (1385 kg)", "2202 lbs (999 kg)"]}
Eco_Friendly_CarInfo = {"pic":["./Project/Img/LotusEvija.png", "./Project/Img/RimacConceptTwo.png", "./Project/Img/PorscheTaycanTurboS.png", "./Project/Img/FordMustangMachE1400.png"], "name":["Koenigsegg Jesko", "Mercedes AMG One", "Hennessey Venom F5", "Lamborghini Sesto Elemento"], "price":["2,800,000 CR", "2,700,000 CR", "3,000,000 CR", "2,500,000 CR"], "engine":["5.0L Twin-Turbocharged V8"+'\n'+"                                  1280 bhp (954 kW), 883 lb⋅ft (1197 N·m)", "1.6L Turbocharged Hybrid V6"+'\n'+"877 bhp (654 kW), 535 lb⋅ft (725 N·m)", "6.6L Twin-Turbocharged V8"+'\n'+"1817 bhp (1355 kW), 1193 lb⋅ft (1617 N·m)", "5.2L Naturally-Aspirated V10"+'\n'+"571 bhp (426 kW), 398 lb⋅ft (540 N·m)"], "layout":["Mid-Engined, Rear-Wheel Drive"+'\n'+"9-speed Transmission", "Mid-Engined, All-Wheel Drive"+'\n'+"8-speed Transmission", "Mid-Engined, Rear-Wheel Drive"+'\n'+"7-speed Transmission", "Mid-Engined, All-Wheel Drive"+'\n'+"6-speed Transmission"], "weight":["3131 lbs (1420 kg)", "3737 lbs (1695 kg)", "3053 lbs (1385 kg)", "2202 lbs (999 kg)"]}

def info(newWindow, data1):
    global S2_Class_CarInfo
    newWindow.iconify()
    infoWindow = Toplevel(root)
    infoWindow.geometry("970x600+100+100")
    buttonQuit = Button(infoWindow, text = "Quit", font=("Playfair Display", 18), fg="#1E1E1E", bg="#ECE8E7",  width=30, command=lambda:closewindow1(infoWindow, newWindow))
    buttonQuit.grid(pady=2, padx=5, column=1, row=0, columnspan=8)

    spacing = Label(infoWindow, text="     ", font=("Playfair Display", 18))
    spacing.grid(pady=20, column=1, row=1)

    nameLabel = Label(infoWindow, text="𝐍𝐚𝐦𝐞: "+data1["name"][0], font=("Playfair Display", 18))
    nameLabel.grid(pady=20, column=1, row=2)

    priceLabel = Label(infoWindow, text="𝐏𝐫𝐢𝐜𝐞: "+data1["price"][0], font=("Playfair Display", 18))
    priceLabel.grid(column=1, row=3)

    spacing = Label(infoWindow, text="     ", font=("Playfair Display", 18))
    spacing.grid(pady=30, column=1, row=4)

    engineLabel = Label(infoWindow, text="𝐄𝐧𝐠𝐢𝐧𝐞: "+data1["engine"][0], font=("Playfair Display", 18))
    engineLabel.grid(column=1, row=5)

    priceLabel = Label(infoWindow, text="𝐋𝐚𝐲𝐨𝐮𝐭: "+data1["layout"][0], font=("Playfair Display", 18))
    priceLabel.grid(pady=20, column=1, row=6)

    priceLabel = Label(infoWindow, text="𝐖𝐞𝐢𝐠𝐡𝐭: "+data1["weight"][0], font=("Playfair Display", 18))
    priceLabel.grid(column=1, row=7)

    img=Image.open(str(data1["pic"][0]))
    resized_CarInfoImg1=img.resize((500,300))
    global tk_CarInfoImg1
    tk_CarInfoImg1=ImageTk.PhotoImage(resized_CarInfoImg1)
    CarInfoImg1label=Label(infoWindow, image=tk_CarInfoImg1)
    CarInfoImg1label.grid(column=3, row=1, rowspan=4, columnspan=3)





S2_Class = {"banner":["./Project/Img/S2 Class.png"], "pic":["./Project/Img/KoenigseggJesko.png", "./Project/Img/MercedesAMGOne.png", "./Project/Img/HennesseyVenomF5.png", "./Project/Img/LamborghiniSestoElemento.png"], "name":["Koenigsegg Jesko", "Mercedes AMG One", "Hennessey Venom F5", "Lamborghini Sesto Elemento"], "price":["2,800,000 CR", "2,700,000 CR", "3,000,000 CR", "2,500,000 CR"]}
S1_Class = {"banner":["./Project/Img/S1 Class.png"], "pic":["./Project/Img/PorscheCarreraGT.png", "./Project/Img/McLaren720SSpider.png", "./Project/Img/FerrariEnzo.png", "./Project/Img/BugattiEB110.png"], "name":["Porsche Carrera GT", "McLaren 720S Spider", "Ferrari Enzo", "Bugatti EB110"], "price":["1,000,000 CR", "340,000 CR", "2,800,000 CR", "1,700,000 CR"]}
A_Class = {"banner":["./Project/Img/A Class.png"], "pic":["./Project/Img/LamborghiniCountach.png", "./Project/Img/Porsche911GT2.png", "./Project/Img/ToyotaSupraRZ.png", "./Project/Img/Mercedes-BenzE63AMG.png"], "name":["Lamborghini Countach", "Porsche 911 GT2", "Toyota Supra RZ", "Mercedes-Benz E63 AMG"], "price":["220,000 CR", "550,000 CR", "38,000 CR", "105,000 CR"]}
Eco_Friendly = {"banner":["./Project/Img/Eco-Friendly.png"], "pic":["./Project/Img/LotusEvija.png", "./Project/Img/RimacConceptTwo.png", "./Project/Img/PorscheTaycanTurboS.png", "./Project/Img/FordMustangMachE1400.png"], "name":["Lotus Evija", "Rimac Concept Two", "Porsche Taycan Turbo S", "Ford Mustang Mach-E 1400"], "price":["2,500,000 CR", "2,000,000 CR", "185,000 CR", "750,000 CR"]}

def new(data):
    root.iconify()
    global S2_Class
    global S1_Class
    global A_Class
    global Eco_Friendly
    newWindow = Toplevel(root)
    newWindow.geometry("700x600+350+150")
    img=Image.open("./Project/Img/ForzaLogo.png")
    resized_logoimg=img.resize((55,55))
    tk_logoimg=ImageTk.PhotoImage(resized_logoimg)
    logolabel=Label(newWindow, image=tk_logoimg)
    logolabel.grid(column=0, row=0, sticky=W)

    #Buttons
    buttonQuit = Button(newWindow, text = "Quit", font=("Playfair Display", 18), fg="#1E1E1E", bg="#ECE8E7", command=lambda:closewindow(newWindow))
    buttonQuit.grid(pady=2, padx=5, column=4, row=0, columnspan=2, sticky=E+W)

    #Row 1 Banner
    img=Image.open(data["banner"][0])
    resized_bannerimg=img.resize((252,298))
    tk_bannerimg=ImageTk.PhotoImage(resized_bannerimg)
    bannerlabel=Label(newWindow, image=tk_bannerimg)
    bannerlabel.grid(column=4, row=1, rowspan=4, columnspan=2, sticky=S+N+E)

    #Row 2 Car Image
    img=Image.open(data["pic"][0])
    resized_CarImg1=img.resize((222,140))
    CarImg1=ImageTk.PhotoImage(resized_CarImg1)
    CarLabel1=Button(newWindow, image=CarImg1, width=202, height=200, command = lambda:info(newWindow, S2_Class_CarInfo))
    CarLabel1.grid(column=0, row=1, columnspan=4, pady=5, sticky=W)

    img=Image.open(data["pic"][1])
    resized_CarImg2=img.resize((222,140))
    CarImg2=ImageTk.PhotoImage(resized_CarImg2)
    CarLabel2=Button(newWindow, image=CarImg2, width=202, height=200, command = lambda:info(newWindow, S1_Class_CarInfo))
    CarLabel2.grid(column=0, row=4, columnspan=4, pady=5, sticky=W)

    img=Image.open(data["pic"][2])
    resized_CarImg3=img.resize((222,140))
    CarImg3=ImageTk.PhotoImage(resized_CarImg3)
    CarLabel3=Button(newWindow, image=CarImg3, width=202, height=200, command = lambda:info(newWindow, A_Class_CarInfo))
    CarLabel3.grid(column=6, row=1, columnspan=4, pady=5, sticky=W)

    img=Image.open(data["pic"][3])
    resized_CarImg4=img.resize((222,140))
    CarImg4=ImageTk.PhotoImage(resized_CarImg4)
    CarLabel4=Button(newWindow, image=CarImg4, width=202, height=200, command = lambda:info(newWindow, Eco_Friendly_CarInfo))
    CarLabel4.grid(column=6, row=4, columnspan=4, padx=5, sticky=W)

    #Row 3 Product Name Label
    productname1=Label(newWindow, text=data["name"][0], font=("Playfair Display", 11), fg="White")
    productname1.grid(column=0, row=2, columnspan=4, padx=5, sticky=W)

    productname2=Label(newWindow, text=data["name"][1], font=("Playfair Display", 11), fg="White")
    productname2.grid(column=0, row=5, columnspan=4, padx=5, sticky=W)

    productname3=Label(newWindow, text=data["name"][2], font=("Playfair Display", 11), fg="White")
    productname3.grid(column=6, row=2, columnspan=4, padx=5, sticky=W)

    productname4=Label(newWindow, text=data["name"][3], font=("Playfair Display", 11), fg="White")
    productname4.grid(column=6, row=5, columnspan=4, padx=5, sticky=W)

    #Row 4 Product Price Label
    productprice1=Label(newWindow, text=data["price"][0], font=("Playfair Display", 10), fg="White")
    productprice1.grid(column=0, row=3, padx=5, sticky=W)

    productprice2=Label(newWindow, text=data["price"][1], font=("Playfair Display", 10), fg="White")
    productprice2.grid(column=0, row=6, padx=5, sticky=W)

    productprice3=Label(newWindow, text=data["price"][2], font=("Playfair Display", 10), fg="White")
    productprice3.grid(column=6, row=3, padx=5, sticky=W)

    productprice4=Label(newWindow, text=data["price"][3], font=("Playfair Display", 10), fg="White")
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

def closewindow(newWindow):
    newWindow.destroy()
    root.deiconify()

def closewindow1(infoWindow, newWindow):
    infoWindow.destroy()
    newWindow.deiconify()

def createNewWindow():
    newWindow = Toplevel(root)
    newWindow.geometry("300x200")
    mylabel = Label(newWindow, text = "Successfully purchased!")
    mylabel.pack()
    newWindow.mainloop()

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


S2classbutton=Button(root, text="S2 Class", font=("Playfair Display", 18, "bold"), fg="#1E1E1E", bg="#ECE8E7", height=2, width=10, command = lambda:new(S2_Class))
S2classbutton.grid(column=2, row=2, pady=80, padx=50)

Aclassbutton=Button(root, text="A Class", font=("Playfair Display", 18, "bold"), fg="#1E1E1E", bg="#ECE8E7", height=2, width=10, command = lambda:new(A_Class))
Aclassbutton.grid(column=2, row=4, pady=80, padx=50)

S1classbutton=Button(root, text="S1 Class", font=("Playfair Display", 18, "bold"), fg="#1E1E1E", bg="#ECE8E7", height=2, width=10, command = lambda:new(S1_Class))
S1classbutton.grid(column=9, row=2, pady=80, padx=50)

EcoFriendlyclassbutton=Button(root, text="Eco-Friendly", font=("Playfair Display", 18, "bold"), fg="#1E1E1E", bg="#ECE8E7", height=2, width=10, command = lambda:new(Eco_Friendly))
EcoFriendlyclassbutton.grid(column=9, row=4, pady=80, padx=50)

totalval = StringVar()
totalval.set("共消費: 0 CR")
totallabel=Label(root, textvariable=totalval, font=("Inter", 18), fg="White")
# totallabel.grid(column=1, row=0, columnspan=8, sticky=W+S)

Menubutton=Button(root, text="Menu", font=("Playfair Display", 18, "bold"), fg="#1E1E1E", bg="#ECE8E7", height=2, width=10, command=createNewWindow)
Menubutton.grid(column=10, row=1, pady=80, padx=50, sticky=N)

Buyoutbutton=Button(root, text="Buyout", font=("Playfair Display", 18, "bold"), fg="#1E1E1E", bg="#ECE8E7", height=2, width=10, command=createNewWindow)
Buyoutbutton.grid(column=10, row=1, pady=80, padx=50, sticky=W)

Buyoutbutton=Button(root, text="Quit", font=("Playfair Display", 18, "bold"), fg="#1E1E1E", bg="#ECE8E7", height=5, width=10, command=createNewWindow)
Buyoutbutton.grid(column=1, row=1, pady=80, padx=50, sticky=N)


root.mainloop()