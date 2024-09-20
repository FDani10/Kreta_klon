import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
import ctypes

con = mysql.connector.connect( host="localhost", user="root", password="", database="kreta_klon")
cursor = con.cursor()
def DiakBej():
    ud = username_d.get()
    pd = password_d.get()
    if(ud == "" or pd == ""):
        print("Kérem töltsön ki minden mezőt!")
    else:
        diakInTable = 'SELECT diak_id,diak_osztaly FROM diak WHERE diak_id LIKE "'+ud+'" AND diak_jelszo = "'+pd+'";'
        cursor.execute(diakInTable)
        table = cursor.fetchall()
        if(len(table) == 1):
            #Legutolsó 3 jegy
            utolso3jegy = "SELECT tantargy.tantargy_nev,beirt_jegy FROM `jegy` INNER JOIN tanora on tanora.tanora_id = jegy.tanora_id inner JOIN tantargy on tantargy.tantargy_id = tanora.tantargy_id where jegy.diak_id = "+ud+" ORDER BY jegy_id DESC limit 3;"
            cursor.execute(utolso3jegy)
            table2 = cursor.fetchall()
            jegy1Text.config(text=table2[0][0])
            jegy1Num.config(text=table2[0][1])
            jegy2Text.config(text=table2[1][0])
            jegy2Num.config(text=table2[1][1])
            jegy3Text.config(text=table2[2][0])
            jegy3Num.config(text=table2[2][1])

            #Tanuló átlaga
            tanuloAtlag = "SELECT round(AVG(beirt_jegy),1) FROM `jegy` where diak_id = "+ud+";"
            cursor.execute(tanuloAtlag)
            table3 = cursor.fetchall()
            atlag = float(table3[0][0])
            atlagNagy.config(text=str(atlag))

            # 1,0 - 1,9 darkred
            # 2,0 - 2,9 red
            # 3,0 - 3,9 lightgreen
            # 4,0 - 4,4 green
            # 4,5 - 5,0 darkgreen
            match atlag:
                case atlag if 2 > atlag:
                    atlagNagy.config(foreground="darkred")
                case atlag if 2<atlag<3:
                    atlagNagy.config(foreground="red")
                case atlag if 3<atlag<4:
                    atlagNagy.config(foreground="lightgreen")
                case atlag if 4<atlag<4.5:
                    atlagNagy.config(foreground="green")
                case atlag if 4.4 < atlag:
                    atlagNagy.config(foreground="darkgreen")

            canvas_bej.place(x=1000,y=0)
            canvas_kezdDiak.place(x=0,y=0)
        else:
            print("Rossz név vagy jelszó!")
    

main = tk.Tk()
ctypes.windll.shcore.SetProcessDpiAwareness(1)
main.geometry("1000x700")
main.resizable(False, False)
main.title("Kréta")

#region Képek beolvasása
image_btn=Image.open(f'./pics/kretalogo.png')
img_btn=image_btn.resize((41, 39))
kretaLogo=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/fooldal_selected.png')
img_btn=image_btn.resize((155, 45))
fooldal_selected=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/infokBtn.png')
img_btn=image_btn.resize((82, 25))
infokBtn=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/jegyekBtn.png')
img_btn=image_btn.resize((102, 25))
jegyekBtn=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/kijelentBtn.png')
img_btn=image_btn.resize((158, 25))
kijelentBtn=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/orakBtn.png')
img_btn=image_btn.resize((82, 25))
orakBtn=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/profilBtn.png')
img_btn=image_btn.resize((137, 25))
profilBtn=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/kicsiKocka.png')
img_btn=image_btn.resize((300, 275))
kicsiKocka=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/nagyKocka.png')
img_btn=image_btn.resize((672, 275))
nagyKocka=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/kkKisvonal.png')
img_btn=image_btn.resize((269, 5))
kkKisvonal=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/kkNagyvonal.png')
img_btn=image_btn.resize((213, 3))
kkNagyvonal=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/nkKisvonal.png')
img_btn=image_btn.resize((640, 5))
nkKisvonal=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/nkNagyvonal.png')
img_btn=image_btn.resize((580, 3))
nkNagyvonal=ImageTk.PhotoImage(img_btn)
#endregion

#region Bejelentkezés ablak
canvas_bej = tk.Canvas(main,bg="#3479FF",width=1000,height=700)
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

reg_btn1 = tk.Button(canvas_bej,image=my_img21,command=DiakBej)
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
#endregion

#region Kezdőlap diáknak
canvas_kezdDiak = tk.Canvas(main,bg="#3479FF",width=1000,height=700)
canvas_kezdDiak.place(x=1000,y=0)

valasztoFelulet = tk.Label(canvas_kezdDiak,bg="#3479FF")
valasztoFelulet.place(x=0,y=0,width=200,height=700)

kretaLogoLabel = tk.Label(canvas_kezdDiak, image=kretaLogo,bg="#3479FF")
kretaLogoLabel.place(x=13,y=18)

kretaLogoText = tk.Label(canvas_kezdDiak,bg="#3479FF",foreground="white",text="KRÉTA",font=('Inter',26,'bold'))
kretaLogoText.place(x=54,y=18,width=121,height=39)

fooldal_btn = tk.Button(canvas_kezdDiak,image=fooldal_selected)
fooldal_btn["bg"] = "#3479FF"
fooldal_btn["activebackground"] = "#3479FF"
fooldal_btn["border"] = "0"
fooldal_btn.place(x=20,y=122)
orak_btn = tk.Button(canvas_kezdDiak,image=orakBtn)
orak_btn["bg"] = "#3479FF"
orak_btn["activebackground"] = "#3479FF"
orak_btn["border"] = "0"
orak_btn.place(x=29,y=187)
jegyek_btn = tk.Button(canvas_kezdDiak,image=jegyekBtn)
jegyek_btn["bg"] = "#3479FF"
jegyek_btn["activebackground"] = "#3479FF"
jegyek_btn["border"] = "0"
jegyek_btn.place(x=29,y=242)
infok_btn = tk.Button(canvas_kezdDiak,image=infokBtn)
infok_btn["bg"] = "#3479FF"
infok_btn["activebackground"] = "#3479FF"
infok_btn["border"] = "0"
infok_btn.place(x=29,y=297)
profil_btn = tk.Button(canvas_kezdDiak,image=profilBtn)
profil_btn["bg"] = "#3479FF"
profil_btn["activebackground"] = "#3479FF"
profil_btn["border"] = "0"
profil_btn.place(x=29,y=351)
kijelent_btn = tk.Button(canvas_kezdDiak,image=kijelentBtn)
kijelent_btn["bg"] = "#3479FF"
kijelent_btn["activebackground"] = "#3479FF"
kijelent_btn["border"] = "0"
kijelent_btn.place(x=20,y=659)

masikOldal = tk.Label(canvas_kezdDiak,bg="#ACC8FF")
masikOldal.place(x=200,y=0,width=800,height=700)

#Első kicsi kocka
kretaLogoLabel = tk.Label(canvas_kezdDiak, image=kicsiKocka,bg="#ACC8FF")
kretaLogoLabel.place(x=252,y=62)

kretaLogoLabel = tk.Label(canvas_kezdDiak, image=kkKisvonal,bg="#DBE8FF")
kretaLogoLabel.place(x=268,y=111)
kretaLogoLabel = tk.Label(canvas_kezdDiak, image=kkNagyvonal,bg="#DBE8FF")
kretaLogoLabel.place(x=293,y=181)
kretaLogoLabel = tk.Label(canvas_kezdDiak, image=kkNagyvonal,bg="#DBE8FF")
kretaLogoLabel.place(x=293,y=244)

szoveg1 = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="black",text="Új beírt jegyek:",font=('Inter',18,'bold'))
szoveg1.place(x=269,y=76,width=179,height=29)
jegy1Text = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="#1E1E1E",text="Matematika",font=('Inter',16,'bold'),anchor='w')
jegy1Text.place(x=308,y=140,width=200,height=21)
jegy1Num = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="black",text="3",font=('Inter',16,'bold'))
jegy1Num.place(x=479,y=140,width=14,height=21)
jegy2Text = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="#1E1E1E",text="Informatika",font=('Inter',16,'bold'),anchor='w')
jegy2Text.place(x=308,y=202,width=200,height=21)
jegy2Num = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="black",text="5",font=('Inter',16,'bold'))
jegy2Num.place(x=479,y=202,width=14,height=21)
jegy3Text = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="#1E1E1E",text="Kémia",font=('Inter',16,'bold'),anchor='w')
jegy3Text.place(x=308,y=264,width=200,height=21)
jegy3Num = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="black",text="2",font=('Inter',16,'bold'))
jegy3Num.place(x=479,y=264,width=14,height=21)

#Második kicsi kocka
kretaLogoLabel = tk.Label(canvas_kezdDiak, image=kicsiKocka,bg="#ACC8FF")
kretaLogoLabel.place(x=624,y=62)

szoveg1 = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="black",text="Átlag:",font=('Inter',18,'bold'))
szoveg1.place(x=738,y=76,width=72,height=29)

atlagNagy = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="green",text="4,2",font=('Inter',80,'bold'),anchor="center")
atlagNagy.place(x=693,y=144,width=163,height=118)


#Alsó nagy kocka
kretaLogoLabel = tk.Label(canvas_kezdDiak, image=nagyKocka,bg="#ACC8FF")
kretaLogoLabel.place(x=252,y=376)

kretaLogoLabel = tk.Label(canvas_kezdDiak, image=nkKisvonal,bg="#DBE8FF")
kretaLogoLabel.place(x=265,y=433)
kretaLogoLabel = tk.Label(canvas_kezdDiak, image=nkNagyvonal,bg="#DBE8FF")
kretaLogoLabel.place(x=297,y=496)
kretaLogoLabel = tk.Label(canvas_kezdDiak, image=nkNagyvonal,bg="#DBE8FF")
kretaLogoLabel.place(x=297,y=559)

mess1 = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="black",text="Új információk:",font=('Inter',18,'bold'),anchor='w')
mess1.place(x=269,y=393,width=179,height=29)

mess1 = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="#1E1E1E",text="Juhász Magdolna",font=('Inter',16,'bold'),anchor='w')
mess1.place(x=310,y=460,width=242,height=23)
mess2 = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="#1E1E1E",text="Nagy Pál",font=('Inter',16,'bold'),anchor='w')
mess2.place(x=310,y=519,width=242,height=23)
mess3 = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="#1E1E1E",text="Kis László",font=('Inter',16,'bold'),anchor='w')
mess3.place(x=310,y=581,width=242,height=23)

mess1Text = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="black",text="Beiratkozás információ",font=('Inter',16),anchor='w')
mess1Text.place(x=578,y=460,width=242,height=23)
mess2Text = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="black",text="Változás az órarendben",font=('Inter',16),anchor='w')
mess2Text.place(x=578,y=519,width=242,height=23)
mess3Text = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="black",text="Dolgozat információ",font=('Inter',16),anchor='w')
mess3Text.place(x=578,y=581,width=242,height=23)

#endregion

main.mainloop()