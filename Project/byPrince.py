from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import pygsheets
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from pathlib import Path
from email.mime.multipart import MIMEMultipart
import pandas as pd
import smtplib
from email import encoders
import json

root=Tk()
root.title("Forza Horizon Auction House")
root.geometry("1150x850+150+10")

#開啟圖片
img=Image.open("./Project/Img/ForzaLogo.png")
#轉換為 tk 圖片物件
tk_img=ImageTk.PhotoImage(img)
#設定程式Icon
root.iconphoto(True, tk_img)


userEmail = ""

S2_Class_CarInfo = {"pic":["./Project/Img/KoenigseggJesko.png", "./Project/Img/MercedesAMGOne.png", "./Project/Img/HennesseyVenomF5.png", "./Project/Img/LamborghiniSestoElemento.png"], "name":["Koenigsegg Jesko", "Mercedes AMG One", "Hennessey Venom F5", "Lamborghini Sesto Elemento"], "price":["2,800,000 CR", "2,700,000 CR", "3,000,000 CR", "2,500,000 CR"], "engine":["5.0L Twin-Turbocharged V8"+'\n'+"                                  1280 bhp (954 kW), 883 lb⋅ft (1197 N·m)", "1.6L Turbocharged Hybrid V6"+'\n'+"877 bhp (654 kW), 535 lb⋅ft (725 N·m)", "6.6L Twin-Turbocharged V8"+'\n'+"1817 bhp (1355 kW), 1193 lb⋅ft (1617 N·m)", "5.2L Naturally-Aspirated V10"+'\n'+"571 bhp (426 kW), 398 lb⋅ft (540 N·m)"], "layout":["Mid-Engined, Rear-Wheel Drive"+'\n'+"9-speed Transmission", "Mid-Engined, All-Wheel Drive"+'\n'+"8-speed Transmission", "Mid-Engined, Rear-Wheel Drive"+'\n'+"7-speed Transmission", "Mid-Engined, All-Wheel Drive"+'\n'+"6-speed Transmission"], "weight":["3131 lbs (1420 kg)", "3737 lbs (1695 kg)", "3053 lbs (1385 kg)", "2202 lbs (999 kg)"]}

S1_Class_CarInfo = {"pic":["./Project/Img/PorscheCarreraGT.png", "./Project/Img/McLaren720SSpider.png", "./Project/Img/FerrariEnzo.png", "./Project/Img/BugattiEB110.png"], "name":["Porsche Carrera GT", "McLaren 720S Spider", "Ferrari Enzo", "Bugatti EB110"], "price":["1,000,000 CR", "340,000 CR", "2,800,000 CR", "1,700,000 CR"], "engine":["5.0L Twin-Turbocharged V8"+'\n'+"                                  1280 bhp (954 kW), 883 lb⋅ft (1197 N·m)", "1.6L Turbocharged Hybrid V6"+'\n'+"877 bhp (654 kW), 535 lb⋅ft (725 N·m)", "6.6L Twin-Turbocharged V8"+'\n'+"1817 bhp (1355 kW), 1193 lb⋅ft (1617 N·m)", "5.2L Naturally-Aspirated V10"+'\n'+"571 bhp (426 kW), 398 lb⋅ft (540 N·m)"], "layout":["Mid-Engined, Rear-Wheel Drive"+'\n'+"9-speed Transmission", "Mid-Engined, All-Wheel Drive"+'\n'+"8-speed Transmission", "Mid-Engined, Rear-Wheel Drive"+'\n'+"7-speed Transmission", "Mid-Engined, All-Wheel Drive"+'\n'+"6-speed Transmission"], "weight":["3131 lbs (1420 kg)", "3737 lbs (1695 kg)", "3053 lbs (1385 kg)", "2202 lbs (999 kg)"]}

A_Class_CarInfo = {"pic":["./Project/Img/LamborghiniCountach.png", "./Project/Img/Porsche911GT2.png", "./Project/Img/ToyotaSupraRZ.png", "./Project/Img/Mercedes-BenzE63AMG.png"], "name":["Lamborghini Countach", "Porsche 911 GT2", "Toyota Supra RZ", "Mercedes-Benz E63 AMG"], "price":["220,000 CR", "550,000 CR", "38,000 CR", "105,000 CR"], "engine":["5.0L Twin-Turbocharged V8"+'\n'+"                                  1280 bhp (954 kW), 883 lb⋅ft (1197 N·m)", "1.6L Turbocharged Hybrid V6"+'\n'+"877 bhp (654 kW), 535 lb⋅ft (725 N·m)", "6.6L Twin-Turbocharged V8"+'\n'+"1817 bhp (1355 kW), 1193 lb⋅ft (1617 N·m)", "5.2L Naturally-Aspirated V10"+'\n'+"571 bhp (426 kW), 398 lb⋅ft (540 N·m)"], "layout":["Mid-Engined, Rear-Wheel Drive"+'\n'+"9-speed Transmission", "Mid-Engined, All-Wheel Drive"+'\n'+"8-speed Transmission", "Mid-Engined, Rear-Wheel Drive"+'\n'+"7-speed Transmission", "Mid-Engined, All-Wheel Drive"+'\n'+"6-speed Transmission"], "weight":["3131 lbs (1420 kg)", "3737 lbs (1695 kg)", "3053 lbs (1385 kg)", "2202 lbs (999 kg)"]}

Eco_Friendly_CarInfo = {"pic":["./Project/Img/LotusEvija.png", "./Project/Img/RimacConceptTwo.png", "./Project/Img/PorscheTaycanTurboS.png", "./Project/Img/FordMustangMachE1400.png"], "name":["Koenigsegg Jesko", "Mercedes AMG One", "Hennessey Venom F5", "Lamborghini Sesto Elemento"], "price":["2,800,000 CR", "2,700,000 CR", "3,000,000 CR", "2,500,000 CR"], "engine":["5.0L Twin-Turbocharged V8"+'\n'+"                                  1280 bhp (954 kW), 883 lb⋅ft (1197 N·m)", "1.6L Turbocharged Hybrid V6"+'\n'+"877 bhp (654 kW), 535 lb⋅ft (725 N·m)", "6.6L Twin-Turbocharged V8"+'\n'+"1817 bhp (1355 kW), 1193 lb⋅ft (1617 N·m)", "5.2L Naturally-Aspirated V10"+'\n'+"571 bhp (426 kW), 398 lb⋅ft (540 N·m)"], "layout":["Mid-Engined, Rear-Wheel Drive"+'\n'+"9-speed Transmission", "Mid-Engined, All-Wheel Drive"+'\n'+"8-speed Transmission", "Mid-Engined, Rear-Wheel Drive"+'\n'+"7-speed Transmission", "Mid-Engined, All-Wheel Drive"+'\n'+"6-speed Transmission"], "weight":["3131 lbs (1420 kg)", "3737 lbs (1695 kg)", "3053 lbs (1385 kg)", "2202 lbs (999 kg)"]}

S2_Class = {"banner":["./Project/Img/S2 Class.png"], "pic":["./Project/Img/KoenigseggJesko.png", "./Project/Img/MercedesAMGOne.png", "./Project/Img/HennesseyVenomF5.png", "./Project/Img/LamborghiniSestoElemento.png"], "name":["Koenigsegg Jesko", "Mercedes AMG One", "Hennessey Venom F5", "Lamborghini Sesto Elemento"], "price":["2,800,000 CR", "2,700,000 CR", "3,000,000 CR", "2,500,000 CR"], "priceNumber":[0, 0, 0, 0]}

S1_Class = {"banner":["./Project/Img/S1 Class.png"], "pic":["./Project/Img/PorscheCarreraGT.png", "./Project/Img/McLaren720SSpider.png", "./Project/Img/FerrariEnzo.png", "./Project/Img/BugattiEB110.png"], "name":["Porsche Carrera GT", "McLaren 720S Spider", "Ferrari Enzo", "Bugatti EB110"], "price":["1,000,000 CR", "340,000 CR", "2,800,000 CR", "1,700,000 CR"], "priceNumber":[0, 0, 0, 0]}

A_Class = {"banner":["./Project/Img/A Class.png"], "pic":["./Project/Img/LamborghiniCountach.png", "./Project/Img/Porsche911GT2.png", "./Project/Img/ToyotaSupraRZ.png", "./Project/Img/Mercedes-BenzE63AMG.png"], "name":["Lamborghini Countach", "Porsche 911 GT2", "Toyota Supra RZ", "Mercedes-Benz E63 AMG"], "price":["220,000 CR", "550,000 CR", "38,000 CR", "105,000 CR"], "priceNumber":[0, 0, 0, 0]}

Eco_Friendly = {"banner":["./Project/Img/Eco-Friendly.png"], "pic":["./Project/Img/LotusEvija.png", "./Project/Img/RimacConceptTwo.png", "./Project/Img/PorscheTaycanTurboS.png", "./Project/Img/FordMustangMachE1400.png"], "name":["Lotus Evija", "Rimac Concept Two", "Porsche Taycan Turbo S", "Ford Mustang Mach-E 1400"], "price":["2,500,000 CR", "2,000,000 CR", "185,000 CR", "750,000 CR"], "priceNumber":[0, 0, 0, 0]}



def info(newWindow, data1, number):
    global S2_Class_CarInfo
    global S1_Class_CarInfo
    global A_Class_CarInfo
    global Eco_Friendly_CarInfo
    newWindow.iconify()
    infoWindow = Toplevel(root)
    infoWindow.geometry("970x600+100+100")
    buttonQuit = Button(infoWindow, text = "Quit", font=("Playfair Display", 18), fg="#1E1E1E", bg="#ECE8E7",  width=30, command=lambda:closewindow1(infoWindow, newWindow))
    buttonQuit.grid(pady=2, padx=5, column=1, row=0, columnspan=8)

    # Group 1
    spacing = Label(infoWindow, text="     ", font=("Playfair Display", 18))
    spacing.grid(pady=20, column=1, row=1)

    nameLabel = Label(infoWindow, text="𝐍𝐚𝐦𝐞: "+data1["name"][number], font=("Playfair Display", 18))
    nameLabel.grid(pady=20, column=1, row=2)

    priceLabel = Label(infoWindow, text="𝐏𝐫𝐢𝐜𝐞: "+data1["price"][number], font=("Playfair Display", 18))
    priceLabel.grid(column=1, row=3)

    spacing = Label(infoWindow, text="     ", font=("Playfair Display", 18))
    spacing.grid(pady=30, column=1, row=4)

    engineLabel = Label(infoWindow, text="𝐄𝐧𝐠𝐢𝐧𝐞: "+data1["engine"][number], font=("Playfair Display", 18))
    engineLabel.grid(column=1, row=5)

    priceLabel = Label(infoWindow, text="𝐋𝐚𝐲𝐨𝐮𝐭: "+data1["layout"][number], font=("Playfair Display", 18))
    priceLabel.grid(pady=20, column=1, row=6)

    priceLabel = Label(infoWindow, text="𝐖𝐞𝐢𝐠𝐡𝐭: "+data1["weight"][number], font=("Playfair Display", 18))
    priceLabel.grid(column=1, row=7)

    img=Image.open(str(data1["pic"][number]))
    resized_CarInfoImg1=img.resize((500,300))
    global tk_CarInfoImg1
    tk_CarInfoImg1=ImageTk.PhotoImage(resized_CarInfoImg1)
    CarInfoImg1label=Label(infoWindow, image=tk_CarInfoImg1)
    CarInfoImg1label.grid(column=3, row=1, rowspan=4, columnspan=3)




def new(data, dataInfo):
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
    CarLabel1=Button(newWindow, image=CarImg1, width=202, height=200, command = lambda:info(newWindow, dataInfo,0))
    CarLabel1.grid(column=0, row=1, columnspan=4, pady=5, sticky=W)

    img=Image.open(data["pic"][1])
    resized_CarImg2=img.resize((222,140))
    CarImg2=ImageTk.PhotoImage(resized_CarImg2)
    CarLabel2=Button(newWindow, image=CarImg2, width=202, height=200, command = lambda:info(newWindow, dataInfo,1))
    CarLabel2.grid(column=0, row=4, columnspan=4, pady=5, sticky=W)

    img=Image.open(data["pic"][2])
    resized_CarImg3=img.resize((222,140))
    CarImg3=ImageTk.PhotoImage(resized_CarImg3)
    CarLabel3=Button(newWindow, image=CarImg3, width=202, height=200, command = lambda:info(newWindow, dataInfo,2))
    CarLabel3.grid(column=6, row=1, columnspan=4, pady=5, sticky=W)

    img=Image.open(data["pic"][3])
    resized_CarImg4=img.resize((222,140))
    CarImg4=ImageTk.PhotoImage(resized_CarImg4)
    CarLabel4=Button(newWindow, image=CarImg4, width=202, height=200, command = lambda:info(newWindow, dataInfo,3))
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
    productnumber1=Label(newWindow, text=data["priceNumber"][0], font=("Playfair Display", 12, "bold"), fg="White", width=7)
    productAddbutton1=Button(newWindow, text="+", font=("Playfair Display", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: add(productnumber1, productprice1,data,0))
    productMinusbutton1=Button(newWindow, text="-", font=("Playfair Display", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: minus(productnumber1, productprice1,data,0))
    productnumber1.grid(column=2, row=3, sticky=W+E+S+N)
    productAddbutton1.grid(column=3, row=3, sticky=E)
    productMinusbutton1.grid(column=1, row=3, sticky=W)

    productnumber2=Label(newWindow, text=data["priceNumber"][1], font=("Playfair Display", 12, "bold"), fg="White", width=7)
    productAddbutton2=Button(newWindow, text="+", font=("Playfair Display", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: add(productnumber2, productprice2,data,1))
    productMinusbutton2=Button(newWindow, text="-", font=("Playfair Display", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: minus(productnumber2, productprice2,data,1))
    productnumber2.grid(column=2, row=6, sticky=W+E+S+N)
    productAddbutton2.grid(column=3, row=6, sticky=E)
    productMinusbutton2.grid(column=1, row=6, sticky=W)

    productnumber3=Label(newWindow, text=data["priceNumber"][2], font=("Playfair Display", 12, "bold"), fg="White", width=7)
    productAddbutton3=Button(newWindow, text="+", font=("Playfair Display", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: add(productnumber3, productprice3,data,2))
    productMinusbutton3=Button(newWindow, text="-", font=("Playfair Display", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: minus(productnumber3, productprice3,data,2))
    productnumber3.grid(column=8, row=3, sticky=W+E+S+N)
    productAddbutton3.grid(column=9, row=3, sticky=E)
    productMinusbutton3.grid(column=7, row=3, sticky=W)

    productnumber4=Label(newWindow, text=data["priceNumber"][3], font=("Playfair Display", 12, "bold"), fg="White", width=7)
    productAddbutton4=Button(newWindow, text="+", font=("Playfair Display", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: add(productnumber4, productprice4,data,3))
    productMinusbutton4=Button(newWindow, text="-", font=("Playfair Display", 10, "bold"), fg="Black", bg="#E7E2E2", command=lambda: minus(productnumber4, productprice4,data,3))
    productnumber4.grid(column=8, row=6, sticky=W+E+S+N)
    productAddbutton4.grid(column=9, row=6, sticky=E)
    productMinusbutton4.grid(column=7, row=6, sticky=W)

    newWindow.mainloop()

#Add and Minus Def
def add(numberlabel, pricelabel, data, position):
    data['priceNumber'][position] = data['priceNumber'][position]+1
    numberlabel["text"] = int(numberlabel["text"])+1
    price = int(pricelabel["text"].replace(",", "").replace("CR", "").strip())
    total = int(totalval.get().split(":")[1].replace("CR", "").strip())
    totalval.set("共消費: "+str(total+price)+" CR")

def minus(numberlabel, pricelabel, data, position):
    data['priceNumber'][position] = data['priceNumber'][position]-1
    if int(numberlabel["text"])>0:
        numberlabel["text"] = int(numberlabel["text"])-1
    else:
        messagebox.showwarning("showwarning", "The number of products can't be below 0")
    price = int(pricelabel["text"].replace(",", "").replace("CR", "").strip())
    total = int(totalval.get().split(":")[1].replace("CR", "").strip())
    totalval.set("共消費: "+str(total-price)+" CR")

def closewindow(newWindow):
    newWindow.destroy()
    root.deiconify()

def closewindow1(infoWindow, newWindow):
    infoWindow.destroy()
    newWindow.deiconify()
    
def destroyWindow():
    global userEmail
    with open("Project/userData.json", "w") as f:
        data = {userEmail :{"S2_Class_CarInfo":S2_Class_CarInfo,"S1_Class_CarInfo":S1_Class_CarInfo,"A_Class_CarInfo":A_Class_CarInfo,"Eco_Friendly_CarInfo":Eco_Friendly_CarInfo,"S2_Class":S2_Class,"S1_Class":S1_Class,"A_Class":A_Class,"Eco_Friendly":Eco_Friendly}}
        json.dump(data, f)
    root.destroy()

def menu():
    menuWindow = Toplevel(root)
    menuWindow.geometry("1000x300+230+220")
    table=ttk.Treeview(menuWindow, columns=["Product Name", "Unit Price", "Quantity", "Subtotal"])
    # create columns title
    table.heading("#0", text="Product name")
    table.heading("#1", text="Unit Price")
    table.heading("#2", text="Quantity")
    table.heading("#3", text="Subtotal")

    table.column("#0", width=250, anchor=CENTER)
    table.column("#1", anchor=CENTER)
    table.column("#2", anchor=CENTER)
    table.column("#3", anchor=CENTER)

    table.tag_configure("totalcolor", background="#C0C2C0")

    subtotal1 = int(S2_Class["priceNumber"][0]) * int(S2_Class["price"][0].replace(",", "").replace("CR", "").strip())
    table.insert('',index='end',text=S2_Class["name"][0],values=(S2_Class["price"][0],S2_Class["priceNumber"][0], subtotal1))

    subtotal2 = int(S2_Class["priceNumber"][1]) * int(S2_Class["price"][1].replace(",", "").replace("CR", "").strip())
    table.insert('',index='end',text=S2_Class["name"][1],values=(S2_Class["price"][1],S2_Class["priceNumber"][1], subtotal2))

    subtotal3 = int(S2_Class["priceNumber"][2]) * int(S2_Class["price"][2].replace(",", "").replace("CR", "").strip())
    table.insert('',index='end',text=S2_Class["name"][2],values=(S2_Class["price"][2],S2_Class["priceNumber"][2], subtotal3))

    subtotal4 = int(S2_Class["priceNumber"][3]) * int(S2_Class["price"][3].replace(",", "").replace("CR", "").strip())
    table.insert('',index='end',text=S2_Class["name"][3],values=(S2_Class["price"][3],S2_Class["priceNumber"][3], subtotal4))

    # S1 Class
    subtotal5 = int(S1_Class["priceNumber"][0]) * int(S1_Class["price"][0].replace(",", "").replace("CR", "").strip())
    table.insert('',index='end',text=S1_Class["name"][0],values=(S1_Class["price"][0],S1_Class["priceNumber"][0], subtotal5))

    subtotal6 = int(S1_Class["priceNumber"][1]) * int(S1_Class["price"][1].replace(",", "").replace("CR", "").strip())
    table.insert('',index='end',text=S1_Class["name"][1],values=(S1_Class["price"][1],S1_Class["priceNumber"][1], subtotal6))

    subtotal7 = int(S1_Class["priceNumber"][2]) * int(S1_Class["price"][2].replace(",", "").replace("CR", "").strip())
    table.insert('',index='end',text=S1_Class["name"][2],values=(S1_Class["price"][2],S1_Class["priceNumber"][2], subtotal7))

    subtotal8 = int(S1_Class["priceNumber"][3]) * int(S1_Class["price"][3].replace(",", "").replace("CR", "").strip())
    table.insert('',index='end',text=S1_Class["name"][3],values=(S1_Class["price"][3],S1_Class["priceNumber"][3], subtotal8))

    # A Class
    subtotal9 = int(A_Class["priceNumber"][0]) * int(A_Class["price"][0].replace(",", "").replace("CR", "").strip())
    table.insert('',index='end',text=A_Class["name"][0],values=(A_Class["price"][0],A_Class["priceNumber"][0], subtotal9))

    subtotal10 = int(A_Class["priceNumber"][1]) * int(A_Class["price"][1].replace(",", "").replace("CR", "").strip())
    table.insert('',index='end',text=A_Class["name"][1],values=(A_Class["price"][1],A_Class["priceNumber"][1], subtotal10))

    subtotal11 = int(A_Class["priceNumber"][2]) * int(A_Class["price"][2].replace(",", "").replace("CR", "").strip())
    table.insert('',index='end',text=A_Class["name"][2],values=(A_Class["price"][2],A_Class["priceNumber"][2], subtotal11))

    subtotal12 = int(A_Class["priceNumber"][3]) * int(A_Class["price"][3].replace(",", "").replace("CR", "").strip())
    table.insert('',index='end',text=A_Class["name"][3],values=(A_Class["price"][3],A_Class["priceNumber"][3], subtotal12))

    # Eco_Friendly
    subtotal13 = int(Eco_Friendly["priceNumber"][0]) * int(Eco_Friendly["price"][0].replace(",", "").replace("CR", "").strip())
    table.insert('',index='end',text=Eco_Friendly["name"][0],values=(Eco_Friendly["price"][0],Eco_Friendly["priceNumber"][0], subtotal13))

    subtotal14 = int(Eco_Friendly["priceNumber"][1]) * int(Eco_Friendly["price"][1].replace(",", "").replace("CR", "").strip())
    table.insert('',index='end',text=Eco_Friendly["name"][1],values=(Eco_Friendly["price"][1],Eco_Friendly["priceNumber"][1], subtotal14))

    subtotal15 = int(Eco_Friendly["priceNumber"][2]) * int(Eco_Friendly["price"][2].replace(",", "").replace("CR", "").strip())
    table.insert('',index='end',text=Eco_Friendly["name"][2],values=(Eco_Friendly["price"][2],Eco_Friendly["priceNumber"][2], subtotal15))

    subtotal16 = int(Eco_Friendly["priceNumber"][3]) * int(Eco_Friendly["price"][3].replace(",", "").replace("CR", "").strip())
    table.insert('',index='end',text=Eco_Friendly["name"][3],values=(Eco_Friendly["price"][3],Eco_Friendly["priceNumber"][3], subtotal16))

    total = subtotal1+subtotal2+subtotal3+subtotal4+subtotal5+subtotal6+subtotal7+subtotal8+subtotal9+subtotal10+subtotal11+subtotal12+subtotal13+subtotal14+subtotal15+subtotal16
    table.insert('',index='end',text='Total',values=['','', total], tags=('totalcolor'))

    table.pack()

    menuWindow.mainloop()

def loginWindow():
    gc = pygsheets.authorize(service_file="Project/causal-scarab-383206-d3edf987cf5e.json")
    sht = gc.open_by_url("https://docs.google.com/spreadsheets/d/1mpgr_6vPS_pSIxFawYWXU9czJPpZq4Q-c9j7y5wlYHM/edit#gid=0")
    ws = sht[0]
    ws = sht.worksheet_by_title("Project")
    def signup(email, password):
        global userEmail
        df = pd.DataFrame(ws.get_all_records())
        df.loc[len(df.index)] = [str(email), str(password)]
        ws.set_dataframe(df, 'A1') #從欄位 A1 開始
        messagebox.showwarning("showwarning", "Sign Up Success!")
        userEmail = email
        loginWindow.destroy()
    def login(email,password):
        global userEmail
        global S2_Class_CarInfo
        global S1_Class_CarInfo
        global A_Class_CarInfo
        global Eco_Friendly_CarInfo
        global S2_Class
        global S1_Class
        global A_Class
        global Eco_Friendly
        df = pd.DataFrame(ws.get_all_records())
        df_result = df[df["電子郵件："] == email]
        if (len(df_result) >= 1):
            if (str(list(df_result["密碼："])[0]) == password):
                # 成功登陸
                messagebox.showwarning("showwarning", "Login Success!")
                userEmail = email
                with open('Project/userData.json','r') as f:
                    data = json.load(f)
                    if userEmail in list(data.keys()):
                        print(userEmail in list(data.keys()))
                        data = data[userEmail]
                        S2_Class_CarInfo = data["S2_Class_CarInfo"]
                        S1_Class_CarInfo = data["S1_Class_CarInfo"]
                        A_Class_CarInfo = data["A_Class_CarInfo"]
                        Eco_Friendly_CarInfo = data["Eco_Friendly_CarInfo"]
                        S2_Class = data["S2_Class"]
                        S1_Class = data["S1_Class"]
                        A_Class = data["A_Class"]
                        Eco_Friendly = data["Eco_Friendly"]
                loginWindow.destroy()
            else:
                # 密碼錯誤
                messagebox.showwarning("showwarning", "Password is wrong, please try again.")
        else:
            # 電子郵件錯誤
            messagebox.showwarning("showwarning", "Email or password is wrong, please try again or create a new account.")

    loginWindow=Toplevel()
    loginWindow.title("Login")
    loginWindow.geometry("400x300+150+50")

    loginLabel=Label(loginWindow, text="L o g i n", font=("Playfair Display", 25, "bold"))
    loginLabel.grid(column=0, row=0, pady=10, sticky=W)

    emailLabel=Label(loginWindow, text="Email:", font=("Playfair Display", 18))
    emailLabel.grid(column=0, row=1, pady=10, sticky=W)

    emailEntry=Entry(loginWindow)
    emailEntry.grid(column=1, row=1, pady=10, sticky=W)

    passwordLabel=Label(loginWindow, text="Password:", font=("Playfair Display", 18))
    passwordLabel.grid(column=0, row=2, pady=10, sticky=W)

    passwordEntry=Entry(loginWindow, show="*")
    passwordEntry.grid(column=1, row=2, pady=10, sticky=W)

    signupButton=Button(loginWindow, text="Sign Up", font=("Playfair Display", 18), command=lambda:signup(emailEntry.get(), passwordEntry.get()))
    signupButton.grid(column=0, row=3, pady=10, sticky=W)


    loginButton=Button(loginWindow, text="Login", font=("Playfair Display", 18), command=lambda:login(emailEntry.get(), passwordEntry.get()))
    loginButton.grid(column=1, row=3, pady=10, sticky=W)

    loginWindow.mainloop()

def buyoutWindow():

    global userEmail

    buyoutWindow = Toplevel(root)
    buyoutWindow.geometry("450x80+550+300")
    shoppinglist = [[S2_Class_CarInfo["name"][0], S2_Class_CarInfo["price"][0], S2_Class["priceNumber"][0]],[S2_Class_CarInfo["name"][1], S2_Class_CarInfo["price"][1], S2_Class["priceNumber"][1]],[S2_Class_CarInfo["name"][2], S2_Class_CarInfo["price"][2], S2_Class["priceNumber"][2]],[S2_Class_CarInfo["name"][3], S2_Class_CarInfo["price"][3], S2_Class["priceNumber"][3]],[S1_Class_CarInfo["name"][0], S1_Class_CarInfo["price"][0], S1_Class["priceNumber"][0]],[S1_Class_CarInfo["name"][1], S1_Class_CarInfo["price"][1], S1_Class["priceNumber"][1]],[S1_Class_CarInfo["name"][2], S1_Class_CarInfo["price"][2], S1_Class["priceNumber"][2]],[S1_Class_CarInfo["name"][3], S1_Class_CarInfo["price"][3], S1_Class["priceNumber"][3]],[A_Class_CarInfo["name"][0], A_Class_CarInfo["price"][0], A_Class["priceNumber"][0]],[A_Class_CarInfo["name"][1], A_Class_CarInfo["price"][1], A_Class["priceNumber"][1]],[A_Class_CarInfo["name"][2], A_Class_CarInfo["price"][2], A_Class["priceNumber"][2]],[A_Class_CarInfo["name"][3], A_Class_CarInfo["price"][3], A_Class["priceNumber"][3]],[Eco_Friendly_CarInfo["name"][0], Eco_Friendly_CarInfo["price"][0], Eco_Friendly["priceNumber"][0]],[Eco_Friendly_CarInfo["name"][1], Eco_Friendly_CarInfo["price"][1], Eco_Friendly["priceNumber"][1]],[Eco_Friendly_CarInfo["name"][2], Eco_Friendly_CarInfo["price"][2], Eco_Friendly["priceNumber"][2]],[Eco_Friendly_CarInfo["name"][3], Eco_Friendly_CarInfo["price"][3], Eco_Friendly["priceNumber"][3]]]
    df_shoppinglist = pd.DataFrame(shoppinglist, columns = ["name", "price", "number"])
    df_shoppinglist.to_excel("./Project/ShoppingList.xlsx")
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("./Project/ShoppingList.xlsx", "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="ShoppingList.xlsx"')

    if userEmail == "":
        messagebox.showwarning("showwarning", "Please login first!")
    else:
        text = MIMEText("內文")
        
        content = MIMEMultipart() 
        content.attach(part)
        content["subject"] = "Forza Auction House Receipt" 
        content["from"] = "louiechiang907@gmail.com" 
        content["to"] = userEmail

        content.attach(text)  


        smtp = smtplib.SMTP(host = "smtp.gmail.com", port = "587")


        with open("./Project/password.txt", "r") as f:
            mailToken = f.read()

        with smtp:
            try:
                smtp.ehlo() 
                smtp.starttls()
                smtp.login("louiechiang907@gmail.com", mailToken)
                smtp.send_message(content) 
                print("Your Email has been successfully sent")
                smtp.quit()
            except Exception as e:
                print("Error message: ", e)
        mylabel = Label(buyoutWindow, text = "Successfully purchased!", font=("Playfair Display", 30))
        mylabel.pack()

        S2_Class["priceNumber"]=[0, 0, 0, 0]
        S1_Class["priceNumber"]=[0, 0, 0, 0]
        A_Class["priceNumber"]=[0, 0, 0, 0]
        Eco_Friendly["priceNumber"]=[0, 0, 0, 0]
        with open("Project/userData.json", "w") as f:
            data = {userEmail :{"S2_Class_CarInfo":S2_Class_CarInfo,"S1_Class_CarInfo":S1_Class_CarInfo,"A_Class_CarInfo":A_Class_CarInfo,"Eco_Friendly_CarInfo":Eco_Friendly_CarInfo,"S2_Class":S2_Class,"S1_Class":S1_Class,"A_Class":A_Class,"Eco_Friendly":Eco_Friendly}}
            json.dump(data, f)

    buyoutWindow.mainloop()

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


S2classbutton=Button(root, text="S2 Class", font=("Playfair Display", 18, "bold"), fg="#1E1E1E", bg="#ECE8E7", height=2, width=10, command = lambda:new(S2_Class, S2_Class_CarInfo))
S2classbutton.grid(column=2, row=2, pady=80, padx=50)

Aclassbutton=Button(root, text="A Class", font=("Playfair Display", 18, "bold"), fg="#1E1E1E", bg="#ECE8E7", height=2, width=10, command = lambda:new(A_Class, A_Class_CarInfo))
Aclassbutton.grid(column=2, row=4, pady=80, padx=50)

S1classbutton=Button(root, text="S1 Class", font=("Playfair Display", 18, "bold"), fg="#1E1E1E", bg="#ECE8E7", height=2, width=10, command = lambda:new(S1_Class, S1_Class_CarInfo))
S1classbutton.grid(column=9, row=2, pady=80, padx=50)

EcoFriendlyclassbutton=Button(root, text="Eco-Friendly", font=("Playfair Display", 18, "bold"), fg="#1E1E1E", bg="#ECE8E7", height=2, width=10, command = lambda:new(Eco_Friendly, Eco_Friendly_CarInfo))
EcoFriendlyclassbutton.grid(column=9, row=4, pady=80, padx=50)

totalval = StringVar()
totalval.set("共消費: 0 CR")
totallabel=Label(root, textvariable=totalval, font=("Inter", 18), fg="White")
# totallabel.grid(column=1, row=0, columnspan=8, sticky=W+S)

Menubutton=Button(root, text="Menu", font=("Playfair Display", 18, "bold"), fg="#1E1E1E", bg="#ECE8E7", height=2, width=10, command=menu)
Menubutton.grid(column=10, row=1, pady=80, padx=50, sticky=N)

Buyoutbutton=Button(root, text="Buyout", font=("Playfair Display", 18, "bold"), fg="#1E1E1E", bg="#ECE8E7", height=2, width=10, command=buyoutWindow)
Buyoutbutton.grid(column=10, row=1, pady=80, padx=50, sticky=W)

quitbutton=Button(root, text="Quit", font=("Playfair Display", 18, "bold"), fg="#1E1E1E", bg="#ECE8E7", height=2, width=10, command=destroyWindow)
quitbutton.grid(column=1, row=1, pady=80, padx=50, sticky=W)

Loginbutton=Button(root, text="Login", font=("Playfair Display", 18, "bold"), fg="#1E1E1E", bg="#ECE8E7", height=2, width=10, command=loginWindow)
Loginbutton.grid(column=1, row=1, pady=80, padx=50, sticky=N)

root.mainloop()