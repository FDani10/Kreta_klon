import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
import ctypes
import math

diakID = "1237658"
oraId = "1"

con = mysql.connector.connect( host="localhost", user="root", password="", database="kreta_klon")
cursor = con.cursor()

main = tk.Tk()
main.geometry("800x700")
main.resizable(False, False)
main.title("Kréta")

image_btn=Image.open(f'./pics/tantargyKocka.png')
img_btn=image_btn.resize((312, 67))
tantargyKocka=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/hetifeladatKocka.png')
img_btn=image_btn.resize((347, 230))
haziKocka=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/hianyzasSzamonkeresKocka.png')
img_btn=image_btn.resize((731, 230))
szamonkeresKocka=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/tantargyFejlec.png')
img_btn=image_btn.resize((765, 70))
tantargyFejlec=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/tantargyTanarkep.png')
img_btn=image_btn.resize((229, 224))
tantargyTanarkep=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/visszaBtn.png')
img_btn=image_btn.resize((186, 58))
visszaBtn=ImageTk.PhotoImage(img_btn)

tantargyLekerdezes = f"SELECT tantargy.tantargy_nev,tanar.tanar_nev,tanar.tanar_email,tanar.tanar_telefon FROM `tanora` inner JOIN tanar on tanar.tanar_id = tanora.tanar_id inner JOIN tantargy on tantargy.tantargy_id = tanora.tantargy_id WHERE tanora_id = {oraId};"
cursor.execute(tantargyLekerdezes)
Tanora = cursor.fetchall()

szamonkeresekLekerdez = f"SELECT szamonkeres.szamonkeres_text,szamonkeres.szamonkeres_datum FROM `osztaly` inner JOIN tanora on tanora.osztaly_id = osztaly.osztaly_id inner JOIN szamonkeres on szamonkeres.tanora_id = tanora.tanora_id where tanora.tanora_id = {oraId};"
cursor.execute(szamonkeresekLekerdez)
Szamonkeresek = cursor.fetchall()



canvas_tanora = tk.Canvas(main,bg="#FAFAFA",width=800,height=700,borderwidth=0,highlightthickness=0)
canvas_tanora.place(x=0,y=0)
tanFejlec = tk.Label(canvas_tanora,image=tantargyFejlec,bg="#FAFAFA")
tanFejlec.place(x=18,y=21)
tanNev = tk.Label(canvas_tanora,text=Tanora[0][0],bg="#3479FF",fg="white",font=('Inter',38,'bold'),anchor="center")
tanNev.place(x=36,y=26,width=730,height=61)

tanarProfilkep = tk.Label(canvas_tanora,image=tantargyTanarkep,bg="#FAFAFA")
tanarProfilkep.place(x=96,y=106)
tanarAdatok = tk.Label(canvas_tanora,text=f"{Tanora[0][1]}\n{Tanora[0][2]}\n{Tanora[0][3]}",bg="#FAFAFA",font=('Inter',25),anchor="center")
tanarAdatok.place(x=383,y=106,width=383,height=224)

alsoKockak = tk.Label(canvas_tanora,image=szamonkeresKocka)
alsoKockak.place(x=36,y=365)

tantargyGomb = tk.Button(canvas_tanora,image=visszaBtn,command= lambda :print("Vissza"))
tantargyGomb["bg"] = "#FAFAFA"
tantargyGomb["activebackground"] = "#FAFAFA"
tantargyGomb["border"] = "0"
tantargyGomb.place(x=307,y=620)


main.mainloop()