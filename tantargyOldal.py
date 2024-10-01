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
image_btn=Image.open(f'./pics/hianyzasBlokk.png')
img_btn=image_btn.resize((300, 48))
hianyzasBlokk=ImageTk.PhotoImage(img_btn)

tantargyLekerdezes = f"SELECT tantargy.tantargy_nev,tanar.tanar_nev,tanar.tanar_email,tanar.tanar_telefon FROM `tanora` inner JOIN tanar on tanar.tanar_id = tanora.tanar_id inner JOIN tantargy on tantargy.tantargy_id = tanora.tantargy_id WHERE tanora_id = {oraId};"
cursor.execute(tantargyLekerdezes)
Tanora = cursor.fetchall()

szamonkeresekLekerdez = f"SELECT szamonkeres.szamonkeres_text,szamonkeres.szamonkeres_datum FROM `osztaly` inner JOIN tanora on tanora.osztaly_id = osztaly.osztaly_id inner JOIN szamonkeres on szamonkeres.tanora_id = tanora.tanora_id where tanora.tanora_id = {oraId};"
cursor.execute(szamonkeresekLekerdez)
Szamonkeresek = cursor.fetchall()

hianyzasLekerdez = f"SELECT hianyzas_datum FROM `hianyzasok` where diak_id = {diakID} and tanora_id = {oraId} ORDER BY hianyzas_datum DESC"
cursor.execute(hianyzasLekerdez)
Hianyzasok = cursor.fetchall()

canvas_tanora = tk.Canvas(main,bg="#FAFAFA",borderwidth=0,highlightthickness=0)
canvas_tanora.place(x=0,y=0,width=800,height=700)
tanFejlec = tk.Label(canvas_tanora,image=tantargyFejlec,bg="#FAFAFA")
tanFejlec.place(x=18,y=21)
tanNev = tk.Label(canvas_tanora,text=Tanora[0][0],bg="#3479FF",fg="white",font=('Inter',38,'bold'),anchor="center")
tanNev.place(x=36,y=26,width=730,height=61)

tanarProfilkep = tk.Label(canvas_tanora,image=tantargyTanarkep,bg="#FAFAFA")
tanarProfilkep.place(x=96,y=106)
tanarAdatok = tk.Label(canvas_tanora,text=f"{Tanora[0][1]}\n{Tanora[0][2]}\n{Tanora[0][3]}",bg="#FAFAFA",font=('Inter',25),anchor="center")
tanarAdatok.place(x=383,y=106,width=383,height=224)

alsoKockak = tk.Label(canvas_tanora,image=szamonkeresKocka,bg="#FAFAFA")
alsoKockak.place(x=36,y=365)

tantargyGomb = tk.Button(canvas_tanora,image=visszaBtn,command= lambda :print("Vissza"))
tantargyGomb["bg"] = "#FAFAFA"
tantargyGomb["activebackground"] = "#FAFAFA"
tantargyGomb["border"] = "0"
tantargyGomb.place(x=307,y=620)

canvas_bal = tk.Canvas(canvas_tanora,bg="#DBE8FF",borderwidth=0,highlightthickness=0)
canvas_tanora.create_window(45,430,window=canvas_bal,width=335,height=150,anchor="nw")
frame_hiany=tk.Frame(canvas_bal,width=335,height=150,borderwidth=0,highlightthickness=0,bg="#DBE8FF")
frame_hiany.pack(expand=True, fill="both", padx=0, pady=0)
canvas_balSC=tk.Canvas(frame_hiany,width=335,height=150,scrollregion=(0,0,500,1500),bg="#DBE8FF",borderwidth=0,highlightthickness=0)
vbar=tk.Scrollbar(frame_hiany,orient="vertical")
vbar.pack(side="right",fill="y")
vbar.config(command=canvas_balSC.yview)
canvas_balSC.config(width=335,height=150)
canvas_balSC.config(yscrollcommand=vbar.set)

canvas_jobb = tk.Canvas(canvas_tanora,bg="#DBE8FF",borderwidth=0,highlightthickness=0)
canvas_tanora.create_window(430,430,window=canvas_jobb,width=335,height=150,anchor="nw")
fr=tk.Frame(canvas_jobb,width=330,height=160,borderwidth=0,highlightthickness=0,bg="#DBE8FF")
fr.pack(expand=True, fill="both")
canvas_jobbSc=tk.Canvas(fr,width=330,height=160,scrollregion=(0,0,500,1500),bg="#DBE8FF",borderwidth=0,highlightthickness=0)
vbar=tk.Scrollbar(fr,orient="vertical")
vbar.pack(side="right",fill="y")
vbar.config(command=canvas_jobbSc.yview)
canvas_jobbSc.config(width=330,height=160)
canvas_jobbSc.config(yscrollcommand=vbar.set)

if len(Hianyzasok) > 0:
    for i in range(0,len(Hianyzasok)):
        print(Hianyzasok[i][0])
        hianyBG = tk.Label(canvas_balSC,image=hianyzasBlokk,bg="#DBE8FF")
        canvas_balSC.create_window(0,0+(i*60),window=hianyBG,anchor="nw")

        hianySzoveg = tk.Label(canvas_balSC,text=Hianyzasok[i][0],font=('Inter',20,'bold'),bg="#D9D9D9",fg="#414141")
        canvas_balSC.create_window(80,10+(i*60),window=hianySzoveg,anchor="nw")
else:
    nincsHiany = tk.Label(canvas_balSC,text="Jelenleg nincs\nhiányzás beírva!",font=('Inter',20,'bold'),bg="#DBE8FF",fg="#414141")
    canvas_balSC.create_window(160,50,window=nincsHiany)

if len(Szamonkeresek) > 0:
    for i in range(0,len(Szamonkeresek)):
        print(Szamonkeresek[i][0])
        hianyBG = tk.Label(canvas_jobbSc,image=hianyzasBlokk,bg="#DBE8FF")
        canvas_jobbSc.create_window(0,0+(i*60),window=hianyBG,anchor="nw")
        
        Szoveg = tk.Label(canvas_jobbSc,text=Szamonkeresek[i][0],font=('Inter',20,'bold'),bg="#D9D9D9",fg="#414141")
        canvas_jobbSc.create_window(120,27+(i*60),window=hianySzoveg)
else:
    nincsHiany = tk.Label(canvas_jobbSc,text="Jelenleg nincs\nszámonkérés beírva!",font=('Inter',20,'bold'),bg="#DBE8FF",fg="#414141")
    canvas_jobbSc.create_window(160,50,window=nincsHiany)


canvas_balSC["scrollregion"]=(0,0,500,len(Hianyzasok)*60)
canvas_balSC.pack(side="left",expand=True,fill="both")

canvas_jobbSc["scrollregion"]=(0,0,500,len(Szamonkeresek)*60)
canvas_jobbSc.pack(side="left",expand=True,fill="both")

main.mainloop()