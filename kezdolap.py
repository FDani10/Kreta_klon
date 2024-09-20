import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
import ctypes


main = tk.Tk()
ctypes.windll.shcore.SetProcessDpiAwareness(1)
main.geometry("1000x700")
main.resizable(False, False)
main.title("Kréta - Kezdőlap")

#Képek bekérése
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


canvas_bej = tk.Canvas(main,bg="#3479FF",width=1000,height=700)
canvas_bej.place(x=0,y=0)

valasztoFelulet = tk.Label(canvas_bej,bg="#3479FF")
valasztoFelulet.place(x=0,y=0,width=200,height=700)

kretaLogoLabel = tk.Label(canvas_bej, image=kretaLogo,bg="#3479FF")
kretaLogoLabel.place(x=13,y=18)

kretaLogoText = tk.Label(canvas_bej,bg="#3479FF",foreground="white",text="KRÉTA",font=('Inter',26,'bold'))
kretaLogoText.place(x=54,y=18,width=121,height=39)

fooldal_btn = tk.Button(canvas_bej,image=fooldal_selected)
fooldal_btn["bg"] = "#3479FF"
fooldal_btn["activebackground"] = "#3479FF"
fooldal_btn["border"] = "0"
fooldal_btn.place(x=20,y=122)
orak_btn = tk.Button(canvas_bej,image=orakBtn)
orak_btn["bg"] = "#3479FF"
orak_btn["activebackground"] = "#3479FF"
orak_btn["border"] = "0"
orak_btn.place(x=29,y=187)
jegyek_btn = tk.Button(canvas_bej,image=jegyekBtn)
jegyek_btn["bg"] = "#3479FF"
jegyek_btn["activebackground"] = "#3479FF"
jegyek_btn["border"] = "0"
jegyek_btn.place(x=29,y=242)
infok_btn = tk.Button(canvas_bej,image=infokBtn)
infok_btn["bg"] = "#3479FF"
infok_btn["activebackground"] = "#3479FF"
infok_btn["border"] = "0"
infok_btn.place(x=29,y=297)
profil_btn = tk.Button(canvas_bej,image=profilBtn)
profil_btn["bg"] = "#3479FF"
profil_btn["activebackground"] = "#3479FF"
profil_btn["border"] = "0"
profil_btn.place(x=29,y=351)
kijelent_btn = tk.Button(canvas_bej,image=kijelentBtn)
kijelent_btn["bg"] = "#3479FF"
kijelent_btn["activebackground"] = "#3479FF"
kijelent_btn["border"] = "0"
kijelent_btn.place(x=20,y=659)

masikOldal = tk.Label(canvas_bej,bg="#ACC8FF")
masikOldal.place(x=200,y=0,width=800,height=700)

#Első kicsi kocka
kretaLogoLabel = tk.Label(canvas_bej, image=kicsiKocka,bg="#ACC8FF")
kretaLogoLabel.place(x=252,y=62)

kretaLogoLabel = tk.Label(canvas_bej, image=kkKisvonal,bg="#DBE8FF")
kretaLogoLabel.place(x=268,y=111)
kretaLogoLabel = tk.Label(canvas_bej, image=kkNagyvonal,bg="#DBE8FF")
kretaLogoLabel.place(x=293,y=181)
kretaLogoLabel = tk.Label(canvas_bej, image=kkNagyvonal,bg="#DBE8FF")
kretaLogoLabel.place(x=293,y=244)

szoveg1 = tk.Label(canvas_bej,bg="#DBE8FF",foreground="black",text="Új beírt jegyek:",font=('Inter',18,'bold'))
szoveg1.place(x=269,y=76,width=179,height=29)
jegy1Text = tk.Label(canvas_bej,bg="#DBE8FF",foreground="#1E1E1E",text="Matematika",font=('Inter',16,'bold'),anchor='w')
jegy1Text.place(x=308,y=140,width=118,height=21)
jegy1Num = tk.Label(canvas_bej,bg="#DBE8FF",foreground="black",text="3",font=('Inter',16,'bold'))
jegy1Num.place(x=479,y=140,width=14,height=21)
jegy2Text = tk.Label(canvas_bej,bg="#DBE8FF",foreground="#1E1E1E",text="Informatika",font=('Inter',16,'bold'),anchor='w')
jegy2Text.place(x=308,y=202,width=118,height=21)
jegy2Num = tk.Label(canvas_bej,bg="#DBE8FF",foreground="black",text="5",font=('Inter',16,'bold'))
jegy2Num.place(x=479,y=202,width=14,height=21)
jegy3Text = tk.Label(canvas_bej,bg="#DBE8FF",foreground="#1E1E1E",text="Kémia",font=('Inter',16,'bold'),anchor='w')
jegy3Text.place(x=308,y=264,width=118,height=21)
jegy3Num = tk.Label(canvas_bej,bg="#DBE8FF",foreground="black",text="2",font=('Inter',16,'bold'))
jegy3Num.place(x=479,y=264,width=14,height=21)

#Második kicsi kocka
kretaLogoLabel = tk.Label(canvas_bej, image=kicsiKocka,bg="#ACC8FF")
kretaLogoLabel.place(x=624,y=62)

szoveg1 = tk.Label(canvas_bej,bg="#DBE8FF",foreground="black",text="Átlag:",font=('Inter',18,'bold'))
szoveg1.place(x=738,y=76,width=72,height=29)

# 1,0 - 1,9 darkred
# 2,0 - 2,9 red
# 3,0 - 3,9 lightgreen
# 4,0 - 4,4 green
# 4,5 - 5,0 darkgreen
szoveg1 = tk.Label(canvas_bej,bg="#DBE8FF",foreground="green",text="4,2",font=('Inter',80,'bold'),anchor="center")
szoveg1.place(x=693,y=144,width=163,height=118)


#Alsó nagy kocka
kretaLogoLabel = tk.Label(canvas_bej, image=nagyKocka,bg="#ACC8FF")
kretaLogoLabel.place(x=252,y=376)

kretaLogoLabel = tk.Label(canvas_bej, image=nkKisvonal,bg="#DBE8FF")
kretaLogoLabel.place(x=265,y=433)
kretaLogoLabel = tk.Label(canvas_bej, image=nkNagyvonal,bg="#DBE8FF")
kretaLogoLabel.place(x=297,y=496)
kretaLogoLabel = tk.Label(canvas_bej, image=nkNagyvonal,bg="#DBE8FF")
kretaLogoLabel.place(x=297,y=559)

mess1 = tk.Label(canvas_bej,bg="#DBE8FF",foreground="black",text="Új információk:",font=('Inter',18,'bold'),anchor='w')
mess1.place(x=269,y=393,width=179,height=29)

mess1 = tk.Label(canvas_bej,bg="#DBE8FF",foreground="#1E1E1E",text="Juhász Magdolna",font=('Inter',16,'bold'),anchor='w')
mess1.place(x=310,y=460,width=242,height=23)
mess2 = tk.Label(canvas_bej,bg="#DBE8FF",foreground="#1E1E1E",text="Nagy Pál",font=('Inter',16,'bold'),anchor='w')
mess2.place(x=310,y=519,width=242,height=23)
mess3 = tk.Label(canvas_bej,bg="#DBE8FF",foreground="#1E1E1E",text="Kis László",font=('Inter',16,'bold'),anchor='w')
mess3.place(x=310,y=581,width=242,height=23)

mess1Text = tk.Label(canvas_bej,bg="#DBE8FF",foreground="black",text="Beiratkozás információ",font=('Inter',16),anchor='w')
mess1Text.place(x=578,y=460,width=242,height=23)
mess2Text = tk.Label(canvas_bej,bg="#DBE8FF",foreground="black",text="Változás az órarendben",font=('Inter',16),anchor='w')
mess2Text.place(x=578,y=519,width=242,height=23)
mess3Text = tk.Label(canvas_bej,bg="#DBE8FF",foreground="black",text="Dolgozat információ",font=('Inter',16),anchor='w')
mess3Text.place(x=578,y=581,width=242,height=23)

main.mainloop()