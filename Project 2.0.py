from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.ttk as ttk
root=Tk()
root.title("KubeTech Shop")
root.geometry("1100x800")

#開啟圖片
img=Image.open("/Users/Louie/Documents/Python_2023Spring/Class1/logo_tree.png")
#轉換為 tk 圖片物件
tk_img=ImageTk.PhotoImage(img)
#設定程式Icon
root.iconphoto(True, tk_img)


#Big Forza Banner
img=Image.open("/Users/Louie/Documents/Python_2023Spring/ForzaHorizon5Banner.jpeg")
resized_bannerimg=img.resize((652,400))
tk_bannerimg=ImageTk.PhotoImage(resized_bannerimg)
bannerlabel=Label(root, image=tk_bannerimg)
bannerlabel.grid(column=2, row=1, columnspan=8, sticky=N+E+S+W)

#Car Image
img=Image.open("/Users/Louie/Documents/Python_2023Spring/BugattiChiron.png")
resized_bugattichironimg=img.resize((202,120))
bugattichironimg=ImageTk.PhotoImage(resized_bugattichironimg)
bugattichironlabel=Label(root, image=bugattichironimg, width=202, height=200)
bugattichironlabel.grid(column=1, row=2, rowspan=2, pady=0, sticky=W)

img=Image.open("/Users/Louie/Documents/Python_2023Spring/Ferrarif40.png")
resized_Ferrarif40img=img.resize((202,120))
Ferrarif40img=ImageTk.PhotoImage(resized_Ferrarif40img)
Ferrarif40label=Label(root, image=Ferrarif40img, width=202, height=200)
Ferrarif40label.grid(column=1, row=4, rowspan=2, pady=0, sticky=W)

img=Image.open("/Users/Louie/Documents/Python_2023Spring/LamborghiniCentenario.png")
resized_LamborghiniCentenarioimg=img.resize((242,160))
LamborghiniCentenarioimg=ImageTk.PhotoImage(resized_LamborghiniCentenarioimg)
LamborghiniCentenariolabel=Label(root, image=LamborghiniCentenarioimg, width=202, height=200)
LamborghiniCentenariolabel.grid(column=10, row=2, rowspan=2, padx=0, sticky=W)

img=Image.open("/Users/Louie/Documents/Python_2023Spring/LotusEvija.png")
resized_LotusEvijaimg=img.resize((202,120))
LotusEvijaimg=ImageTk.PhotoImage(resized_LotusEvijaimg)
LotusEvijalabel=Label(root, image=LotusEvijaimg, width=202, height=200)
LotusEvijalabel.grid(column=10, row=4, rowspan=2, padx=0, sticky=W)


S2classbutton=Button(root, text="S2 Class", font=("Calibri", 18), fg="#1E1E1E", bg="#ECE8E7", height=2, width=10)
S2classbutton.grid(column=2, row=2, pady=80, padx=50)

Aclassbutton=Button(root, text="A Class", font=("Playfair", 18), fg="#1E1E1E", bg="#ECE8E7", height=2, width=10)
Aclassbutton.grid(column=2, row=4, pady=80, padx=50)

S1classbutton=Button(root, text="S1 Class", font=("Playfair", 18), fg="#1E1E1E", bg="#ECE8E7", height=2, width=10)
S1classbutton.grid(column=9, row=2, pady=80, padx=50)

EcoFriendlyclassbutton=Button(root, text="Eco-Friendly", font=("Playfair", 18), fg="#1E1E1E", bg="#ECE8E7", height=2, width=10)
EcoFriendlyclassbutton.grid(column=9, row=4, pady=80, padx=50)


root.mainloop()