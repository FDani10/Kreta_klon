import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
import ctypes
import math


# tanar id bejelentkezeshez : AAAAAAA


con = mysql.connector.connect( host="localhost", user="root", password="", database="kreta_klon")
cursor = con.cursor()

tanarID = ""

tanarok= tk.Tk()


# oldal menü képek
image_btn=Image.open(f'./pics/kretalogo.png')
img_btn=image_btn.resize((41, 39))
kretaLogo=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/fooldalBtn.png')
img_btn=image_btn.resize((108, 25))
fooldalBtn=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/fooldal_selected.png')
img_btn=image_btn.resize((155, 45))
fooldal_selected=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/infokBtn.png')
img_btn=image_btn.resize((121, 25))
infokBtn=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/infok_selected.png')
img_btn=image_btn.resize((155, 45))
infok_selected=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/jegyekBtn.png')
img_btn=image_btn.resize((102, 25))
jegyekBtn=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/jegyek_selected.png')
img_btn=image_btn.resize((155, 45))
jegyek_selected=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/orakBtn.png')
img_btn=image_btn.resize((82, 25))
orakBtn=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/orak_selected.png')
img_btn=image_btn.resize((155, 45))
orak_selected=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/profilBtn.png')
img_btn=image_btn.resize((137, 25))
profilBtn=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/profil_selected.png')
img_btn=image_btn.resize((155, 45))
profil_selected=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/kijelentBtn.png')
img_btn=image_btn.resize((158, 25))
kijelentBtn=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/jegyBeirBtn.png')
img_btn=image_btn.resize((146, 25))
jegyBeir=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/hianyBeirBtn.png')
img_btn=image_btn.resize((146, 25))
hianyBeir=ImageTk.PhotoImage(img_btn)



# főoldal képek
imagehead=Image.open(f'./pics/fooldalFejlec.png')
img_btn=imagehead.resize((700, 75))
foOlfdalFejlec=ImageTk.PhotoImage(img_btn)



def tanarBej():
    global tanarID
    ut = username_t.get()
    pt = password_t.get()
    if(ut == "" or pt == ""):
        print("Kérem töltsön ki minden mezőt!")
    else:
        tanarInTable = 'SELECT tanar_felnev FROM tanar WHERE tanar_felnev LIKE "'+ut+'" AND tanar_jelszo = "'+pt+'";'
        cursor.execute(tanarInTable)
        table = cursor.fetchall()
        if(len(table) == 1):
            tanarID = ut
        canvas_tanarFo.place(x=0, y=0)
        canvas_bej.place(x=0, y=1000)
        canvas_oldalMenu.place(x=0, y=0)

def hianyzasok():    #hianyz
    osztalyTanar = f'SELECT osztaly.osztaly_nev FROM osztaly join tanora on tanora.osztaly_id = osztaly.osztaly_id join tanar on tanora.tanar_id = tanar.tanar_id where tanar.tanar_felnev LIKE "{ut}" '
    cursor.execute(osztalyTanar)
    osztalyok = cursor.fetchall()
    for i in range(0,len(osztalyok)):
        tanId = str(osztalyok[i][0])
        if i%2 == 0:
            osztalyGomb = tk.Button("",image=osztalyGombKep,command= lambda :print("jo"))
            osztalyGomb["bg"] = "#FAFAFA"
            osztalyGomb["activebackground"] = "#FAFAFA"
            osztalyGomb["border"] = "0"
            osztalyGomb.place(x=70,y=100+math.floor(i/2)*130)
            osztalyNev = tk.Label("",bg="#DBE8FF",foreground="black",text=osztalyok[i][0],font=('Inter',20,'bold'))
            osztalyNev.place(x=84,y=120+math.floor(i/2)*130,width=208,height=28)
            osztalyNev.bind("<Button-1>", lambda :print("jo"))
            atlagKep = tk.Label("",bg="#DBE8FF")
            atlagKep.place(x=300,y=107+math.floor(i/2)*130)
            atlagKep.bind("<Button-1>", lambda :print("jo"))

        else:
            osztalyGomb = tk.Button("",image=osztalyGombKep,command=lambda :print("jo"))
            osztalyGomb["bg"] = "#FAFAFA"
            osztalyGomb["activebackground"] = "#FAFAFA"
            osztalyGomb["border"] = "0"
            osztalyGomb.place(x=418,y=100+math.floor(i/2)*130)
            osztalyNev = tk.Label("",bg="#DBE8FF",foreground="black",text=osztalyok[i][0],font=('Inter',20,'bold'))
            osztalyNev.place(x=432,y=120+math.floor(i/2)*130,width=208,height=28)
            osztalyNev.bind("<Button-1>", lambda :print("jo"))
            atlagKep = tk.Label("",bg="#DBE8FF")
            atlagKep.place(x=648,y=107+math.floor(i/2)*130)
            atlagKep.bind("<Button-1>", lambda :print("jo"))


osztalyK_btn=Image.open(f'./pics/osztalyGomb.png')
osztaly_btn=osztalyK_btn.resize((320, 120))
osztalyGombKep=ImageTk.PhotoImage(osztaly_btn)

tanarok.geometry("1000x700")
tanarok.title("Kérta - Tanári Felület")

# bejelentketés

canvas_bej = tk.Canvas(tanarok,bg="#3479FF",width=1000,height=700)
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

reg_btn1 = tk.Button(canvas_bej,image=my_img21)
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

reg_btn2 = tk.Button(canvas_bej,image=my_img21,command=tanarBej)
reg_btn2["bg"] = "#3479FF"
reg_btn2["activebackground"] = "#3479FF"
reg_btn2["border"] = "0"
reg_btn2.place(x=630,y=544)


# fő oldal tanárokhoz


canvas_tanarFo = tk.Canvas(tanarok, height=700, width=1000)
canvas_tanarFo.place(x=1000, y=1000)

# fő oldal tanárokhoz


canvas_tanarFoCon = tk.Canvas(canvas_tanarFo, height=700, width=800, bg="#FAFAFA")
canvas_tanarFoCon.place(x=200, y=0)
foOlfdalHeader = tk.Label(canvas_tanarFoCon, image=foOlfdalFejlec, width=700, height=75)
foOlfdalHeader.place(x=50, y=20)
def fohoz ():
    canvas_tanarFoCon.place(x=200, y=0)
    canvas_hianyzas.place(x=100000,y=100000)
    canvas_tanarFo.place(x=100000,y=100000)
    canvas_jegybeir.place(x=100000,y=100000)
    canvas_uzeno.place(x=100000,y=100000)
    canvas_profil.place(x=100000,y=100000)
    
    


#hianyzások oldal
canvas_hianyzas = tk.Canvas(canvas_tanarFo, height=700, width=800, bg="#FAFAFA")



def hianyhoz ():
    canvas_hianyzas.place(x=200, y=0)
    canvas_tanarFo.place(x=100000,y=100000)
    canvas_jegybeir.place(x=100000,y=100000)
    canvas_uzeno.place(x=100000,y=100000)
    canvas_profil.place(x=100000,y=100000)
    canvas_tanarFoCon.place(x=100000,y=100000)

    

test2 = tk.Label(canvas_hianyzas, text="b")
test2.place(x=100, y=100)

#jegybeiros olda
canvas_jegybeir = tk.Canvas(canvas_tanarFo, height=700, width=800, background="#FAFAFA")
test1 = tk.Label(canvas_jegybeir, text="a")


def jegyekhez ():
    canvas_jegybeir.place(x=200, y=0)
    canvas_tanarFo.place(x=100000,y=100000)
    canvas_uzeno.place(x=100000,y=100000)
    canvas_profil.place(x=100000,y=100000)
    canvas_hianyzas.place(x=100000,y=100000)
    canvas_tanarFoCon.place(x=100000,y=100000)

test1.place(x=100, y=100)

#uzenofal
canvas_uzeno = tk.Canvas(canvas_tanarFo, height=700, width=800, bg="#FAFAFA")


def uzeneshez ():
    canvas_jegybeir.place(x=100000,y=100000)
    canvas_tanarFo.place(x=100000,y=100000)
    canvas_uzeno.place(x=200, y=0)
    canvas_profil.place(x=100000,y=100000)
    canvas_hianyzas.place(x=100000,y=100000)
    canvas_tanarFoCon.place(x=100000,y=100000)

test3 = tk.Label(canvas_uzeno, text="c")
test3.place(x=100, y=100)
#sajatprofil

canvas_profil = tk.Canvas(canvas_tanarFo, height=700, width=800, bg="#FAFAFA")

def profilhoz ():
    canvas_jegybeir.place(x=100000,y=100000)
    canvas_tanarFo.place(x=100000,y=100000)
    canvas_uzeno.place(x=100000,y=100000)
    canvas_profil.place(x=200, y=0)
    canvas_hianyzas.place(x=100000,y=100000)
    canvas_tanarFoCon.place(x=100000,y=100000)

test4 = tk.Label(canvas_profil, text="d")
test4.place(x=100, y=100)


# oldal menü

canvas_oldalMenu = tk.Canvas(tanarok,bg="#3479FF",width=200,height=700)
canvas_oldalMenu.place(x=1000,y=0)

valasztoFelulet = tk.Label(canvas_oldalMenu,bg="#3479FF")
valasztoFelulet.place(x=0,y=0,width=200,height=700)

kretaLogoLabel = tk.Label(canvas_oldalMenu, image=kretaLogo,bg="#3479FF")
kretaLogoLabel.place(x=13,y=18)

kretaLogoText = tk.Label(canvas_oldalMenu,bg="#3479FF",foreground="white",text="KRÉTA",font=('Inter',26,'bold'))
kretaLogoText.place(x=54,y=18,width=121,height=39)

fooldal_btn = tk.Button(canvas_oldalMenu,image=fooldal_selected,command=fohoz)
fooldal_btn["bg"] = "#3479FF"
fooldal_btn["activebackground"] = "#3479FF"
fooldal_btn["border"] = "0"
fooldal_btn.place(x=29,y=122)
hianyzas = tk.Button(canvas_oldalMenu,image=hianyBeir,command=hianyhoz)
hianyzas["bg"] = "#3479FF"
hianyzas["activebackground"] = "#3479FF"
hianyzas["border"] = "0"
hianyzas.place(x=29,y=187)
jegyek_btn = tk.Button(canvas_oldalMenu,image=jegyBeir,command=jegyekhez)
jegyek_btn["bg"] = "#3479FF"
jegyek_btn["activebackground"] = "#3479FF"
jegyek_btn["border"] = "0"
jegyek_btn.place(x=29,y=242)
infok_btn = tk.Button(canvas_oldalMenu,image=infokBtn,command=uzeneshez)
infok_btn["bg"] = "#3479FF"
infok_btn["activebackground"] = "#3479FF"
infok_btn["border"] = "0"
infok_btn.place(x=29,y=297)
profil_btn = tk.Button(canvas_oldalMenu,image=profilBtn,command=profilhoz)
profil_btn["bg"] = "#3479FF"
profil_btn["activebackground"] = "#3479FF"
profil_btn["border"] = "0"
profil_btn.place(x=29,y=351)
kijelent_btn = tk.Button(canvas_oldalMenu,image=kijelentBtn,command="")
kijelent_btn["bg"] = "#3479FF"
kijelent_btn["activebackground"] = "#3479FF"
kijelent_btn["border"] = "0"
kijelent_btn.place(x=20,y=659)





tanarok.mainloop()