import tkinter as tk
from tkinter import messagebox 
from PIL import Image, ImageTk
import mysql.connector
import ctypes
import math
import re

from main import DiakBej

con = mysql.connector.connect( host="localhost", user="root", password="", database="kreta_klon")
cursor = con.cursor()

bejAblak = tk.Tk()
ctypes.windll.shcore.SetProcessDpiAwareness(1)
bejAblak.geometry("1000x700")
bejAblak.resizable(False, False)
bejAblak.title("Kréta - Bejelentkezés")

canvas_bej = tk.Canvas(bejAblak,bg="#3479FF",width=1000,height=700)
canvas_bej.place(x=0,y=0)
kreta = tk.Label(canvas_bej,bg="#3479FF",foreground="white",text="KRÉTA",font=('Inter',65,'bold'))
kreta.place(x=339,y=32,width=322,height=100)

bej = tk.Label(canvas_bej,bg="#3479FF",foreground="white",text="Bejelentkezés",font=('Inter',30))
bej.place(x=365,y=190,width=269,height=44)

canvas_bej.create_line(500, 256, 500, 670,fill="white")

diak = tk.Label(canvas_bej,bg="#3479FF",foreground="white",text="Diák",font=('Inter',30))
diak.place(x=227,y=247,width=89,height=45)

tanar = tk.Label(canvas_bej,bg="#3479FF",foreground="white",text="Tanár",font=('Inter',30))
tanar.place(x=684,y=247,width=109,height=45)

image_btn=Image.open(f'./pics/formInput.png')
img_btn=image_btn.resize((350, 60))
formInputBG=ImageTk.PhotoImage(img_btn)

image21=Image.open(f'./pics/bej_btn.png')
img21=image21.resize((240, 90))
my_img21=ImageTk.PhotoImage(img21)

nev_1 = tk.Label(canvas_bej,bg="#3479FF",foreground="white",text="Azonosító:",font=('Inter',20))
nev_1.place(x=107,y=301,width=130,height=34)
ent_diakNev = tk.Label(canvas_bej,image=formInputBG,bg="#3479FF")
ent_diakNev.place(x=96,y=335,width=350,height=60)
username_d = tk.Entry(canvas_bej,font=('Ariel',20),bg="#D9D9D9",border=0)
username_d.place(x=110,y=340,width=330,height=50)

jelszo_1 = tk.Label(canvas_bej,bg="#3479FF",foreground="white",text="Jelszó:",font=('Inter',20))
jelszo_1.place(x=107,y=409,width=80,height=34)
ent_diakJelszo = tk.Label(canvas_bej,image=formInputBG,bg="#3479FF")
ent_diakJelszo.place(x=96,y=443,width=350,height=60)
password_d = tk.Entry(canvas_bej,font=('Ariel',20),bg="#D9D9D9",border=0,show="*")
password_d.place(x=110,y=448,width=330,height=50)

reg_btn1 = tk.Button(canvas_bej,image=my_img21,command= lambda ud = username_d.get(), pd = password_d.get() : DiakBej(ud,pd))
reg_btn1["bg"] = "#3479FF"
reg_btn1["activebackground"] = "#3479FF"
reg_btn1["border"] = "0"
reg_btn1.place(x=151,y=544)



nev_2 = tk.Label(canvas_bej,bg="#3479FF",foreground="white",text="Név:",font=('Inter',20))
nev_2.place(x=578,y=301,width=56,height=34)
ent_tanarNev = tk.Label(canvas_bej,image=formInputBG,bg="#3479FF")
ent_tanarNev.place(x=564,y=335,width=350,height=60)
username_t = tk.Entry(canvas_bej,font=('Ariel',20),bg="#D9D9D9",border=0)
username_t.place(x=570,y=340,width=330,height=50)

jelszo_2 = tk.Label(canvas_bej,bg="#3479FF",foreground="white",text="Jelszó:",font=('Inter',20))
jelszo_2.place(x=578,y=409,width=80,height=34)
ent_tanarJelszo = tk.Label(canvas_bej,image=formInputBG,bg="#3479FF")
ent_tanarJelszo.place(x=564,y=443,width=350,height=60)
password_t = tk.Entry(canvas_bej,font=('Ariel',20),bg="#D9D9D9",border=0,show="*")
password_t.place(x=570,y=448,width=330,height=50)

reg_btn2 = tk.Button(canvas_bej,image=my_img21)
reg_btn2["bg"] = "#3479FF"
reg_btn2["activebackground"] = "#3479FF"
reg_btn2["border"] = "0"
reg_btn2.place(x=630,y=544)