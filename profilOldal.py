import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
import ctypes
import math

diakID = ""

con = mysql.connector.connect( host="localhost", user="root", password="", database="kreta_klon")
cursor = con.cursor()

main = tk.Tk()
main.geometry("800x700")
main.resizable(False, False)
main.title("Kréta")

image_btn=Image.open(f'./pics/szuletesnapV.png')
img_btn=image_btn.resize((300, 51))
szuletesnapV=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/jelszoV.png')
img_btn=image_btn.resize((300, 51))
jelszoV=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/telefonV.png')
img_btn=image_btn.resize((300, 51))
telefonV=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/profilFejlec.png')
img_btn=image_btn.resize((700, 75))
profilFejlec=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/profilAdatok.png')
img_btn=image_btn.resize((700, 230))
profilAdatok=ImageTk.PhotoImage(img_btn)

canvas_profDiak = tk.Canvas(main,bg="#F1F1F1",width=800,height=700)
canvas_profDiak.place(x=0,y=0)

fejlec = tk.Label(canvas_profDiak,image=profilFejlec)
fejlec.place(x=50,y=15)

adatok = tk.Label(canvas_profDiak,image=profilAdatok)
adatok.place(x=50,y=117)

valszuletes = tk.Button(canvas_profDiak,image=szuletesnapV,command=lambda : print("Szuletes"))
valszuletes["bg"] = "#F1F1F1"
valszuletes["activebackground"] = "#F1F1F1"
valszuletes["border"] = "0"
valszuletes.place(x=244,y=393)

valtelefon = tk.Button(canvas_profDiak,image=telefonV,command=lambda : print("Telefon"))
valtelefon["bg"] = "#F1F1F1"
valtelefon["activebackground"] = "#F1F1F1"
valtelefon["border"] = "0"
valtelefon.place(x=244,y=476)

valjelszo = tk.Button(canvas_profDiak,image=jelszoV,command=lambda : print("Jelszo"))
valjelszo["bg"] = "#F1F1F1"
valjelszo["activebackground"] = "#F1F1F1"
valjelszo["border"] = "0"
valjelszo.place(x=244,y=555)

kisbetusresz = tk.Label(canvas_profDiak,text="Probélma esetén kérjük küldjenek levelet az\nadmin@kamukreta.com email címre.",font=('Inter',8))
kisbetusresz.place(x=272,y=644)

profilNev = tk.Label(canvas_profDiak,bg="#C7C7C7",text="Abdul Ödön",font=('Inter',20,'bold'))
profilNev.place(x=400,y=136)

profilSzuletes = tk.Label(canvas_profDiak,bg="#C7C7C7",text="Születésnap: ",font=('Inter',16,'bold'))
profilSzuletes.place(x=300,y=190)
profilTelefon = tk.Label(canvas_profDiak,bg="#C7C7C7",text="Telefonszám: ",font=('Inter',16,'bold'))
profilTelefon.place(x=300,y=240)
profilJelszo = tk.Label(canvas_profDiak,bg="#C7C7C7",text="Jelszó: ",font=('Inter',16,'bold'))
profilJelszo.place(x=300,y=290)

pSz = tk.Label(canvas_profDiak,bg="#C7C7C7",text="2018-12-10",font=('Inter',16))
pSz.place(x=440,y=190)
pT = tk.Label(canvas_profDiak,bg="#C7C7C7",text="06402345674",font=('Inter',16))
pT.place(x=450,y=240)
pJ = tk.Label(canvas_profDiak,bg="#C7C7C7",text="********",font=('Inter',16))
pJ.place(x=380,y=290)

main.mainloop()