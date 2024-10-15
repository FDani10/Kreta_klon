import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
import ctypes
import math
import tkinter.ttk as ttk
from datetime import date
from tkinter import messagebox 

tanarID = "A7Z9T3B"
oid = "2"
tid = "1"

con = mysql.connector.connect( host="localhost", user="root", password="", database="kreta_klon")
cursor = con.cursor()

gyerekekLekerdezes = f"SELECT diak_nev,diak_id FROM `diak` where diak_osztaly = {oid};"
cursor.execute(gyerekekLekerdezes)
diakokLekerd = cursor.fetchall()

radios = []
varok = []
def jegyKatt(sor,jegy):
    radios[sor][0]["image"] = jegy1_unS
    radios[sor][1]["image"] = jegy2_unS
    radios[sor][2]["image"] = jegy3_unS
    radios[sor][3]["image"] = jegy4_unS
    radios[sor][4]["image"] = jegy5_unS

    match jegy:
        case 1:
            radios[sor][0]["image"] = jegy1_Sel
        case 2:
            radios[sor][1]["image"] = jegy2_Sel
        case 3:
            radios[sor][2]["image"] = jegy3_Sel
        case 4:
            radios[sor][3]["image"] = jegy4_Sel
        case 5:
            radios[sor][4]["image"] = jegy5_Sel

def visszavon(sor):
    varok[sor].set(None)

    radios[sor][0]["image"] = jegy1_unS
    radios[sor][1]["image"] = jegy2_unS
    radios[sor][2]["image"] = jegy3_unS
    radios[sor][3]["image"] = jegy4_unS
    radios[sor][4]["image"] = jegy5_unS

    radios[sor][0].deselect()
    radios[sor][1].deselect()
    radios[sor][2].deselect()
    radios[sor][3].deselect()
    radios[sor][4].deselect()

def Jegybeiras():
    for i in range(0,len(varok)):
        if varok[i][0].get() != "None":
            emailvaltozquerry = f"INSERT INTO `jegy`(`tanora_id`, `diak_id`, `beirt_jegy`, `jegy_ido`) VALUES ('{tid}','{varok[i][1]}','{varok[i].get()}','{date.today()}')"
            cursor.execute(emailvaltozquerry)
            con.commit()
        messagebox.showinfo("showinfo", "Diákok jegyei sikeresen beírva!")

    

main = tk.Tk()
main.geometry("800x700")
main.resizable(False, False)
main.title("Kréta")

image_btn=Image.open(f'./pics/jegy1_unS.png')
img_btn=image_btn.resize((55, 35))
jegy1_unS=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/jegy2_unS.png')
img_btn=image_btn.resize((55, 35))
jegy2_unS=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/jegy3_unS.png')
img_btn=image_btn.resize((55, 35))
jegy3_unS=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/jegy4_unS.png')
img_btn=image_btn.resize((55, 35))
jegy4_unS=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/jegy5_unS.png')
img_btn=image_btn.resize((55, 35))
jegy5_unS=ImageTk.PhotoImage(img_btn)

image_btn=Image.open(f'./pics/jegyCsik.png')
img_btn=image_btn.resize((2, 35))
jegyCsik=ImageTk.PhotoImage(img_btn)

image_btn=Image.open(f'./pics/jegy1_Sel.png')
img_btn=image_btn.resize((55, 35))
jegy1_Sel=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/jegy2_Sel.png')
img_btn=image_btn.resize((55, 35))
jegy2_Sel=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/jegy3_Sel.png')
img_btn=image_btn.resize((55, 35))
jegy3_Sel=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/jegy4_Sel.png')
img_btn=image_btn.resize((55, 35))
jegy4_Sel=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/jegy5_Sel.png')
img_btn=image_btn.resize((55, 35))
jegy5_Sel=ImageTk.PhotoImage(img_btn)

image_btn=Image.open(f'./pics/visszavonasBtn.png')
img_btn=image_btn.resize((131, 41))
visszavonasBtn=ImageTk.PhotoImage(img_btn)

image_btn=Image.open(f'./pics/diakJegyBG.png')
img_btn=image_btn.resize((650, 70))
diakJegyBG=ImageTk.PhotoImage(img_btn)

image_btn=Image.open(f'./pics/diakokJegybeirasBG.png')
img_btn=image_btn.resize((700, 570))
diakokJegybeirasBG=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/kukaBtn.png')
img_btn=image_btn.resize((50, 50))
kukaBtn=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/jegybeirasBtn.png')
img_btn=image_btn.resize((250, 50))
jegybeirasBtn=ImageTk.PhotoImage(img_btn)

canvas_Jegyiras = tk.Canvas(main,bg="#EFEFEF")
canvas_Jegyiras.place(x=0,y=0,width=800,height=700)

diakokBG = tk.Label(canvas_Jegyiras,image=diakokJegybeirasBG,bg="#EFEFEF")
diakokBG.place(x=50,y=105)

frameDiakJegy=tk.Frame(canvas_Jegyiras,width=700,height=300,bg="#D9D9D9")
frameDiakJegy.pack(expand=True, fill="both", padx=50, pady=(150,100))

canvas_scrollJegyDiak=tk.Canvas(frameDiakJegy,width=700,height=300,scrollregion=(0,0,500,1500),bg="#D9D9D9",border=0,highlightthickness=0)
vbar=tk.Scrollbar(frameDiakJegy,orient="vertical")
vbar.pack(side="right",fill="y")
vbar.config(command=canvas_scrollJegyDiak.yview)
canvas_scrollJegyDiak.config(width=700,height=300)
canvas_scrollJegyDiak.config(yscrollcommand=vbar.set)

for i in range(0,len(diakokLekerd)):
    diakBG = tk.Label(canvas_scrollJegyDiak,image=diakJegyBG,bg="#D9D9D9")
    canvas_scrollJegyDiak.create_window(15,i*100, window=diakBG,anchor="nw")

    diakNev = tk.Label(canvas_scrollJegyDiak,text=diakokLekerd[i][0],font=('Inter',20,'bold'),bg="#A5A5A5")
    canvas_scrollJegyDiak.create_window(25,20+i*100, window=diakNev,anchor="nw")

    var = tk.StringVar()
    var.set(None)

    style = {"indicatoron": 0,
             "borderwidth": 0,
             "border":0,
             "bg":"#A5A5A5",
             "activebackground":"#A5A5A5",
             "highlightthickness":0,
             "selectcolor":"#A5A5A5",
             "relief":"flat"}


    jegyek = []

    jegy1 = tk.Radiobutton(canvas_scrollJegyDiak,image=jegy1_unS,variable=var,value=1,command=lambda sor = i:jegyKatt(sor,1), **style)
    canvas_scrollJegyDiak.create_window(300, 20+i*100, window=jegy1,anchor="nw")

    csik1 = tk.Label(canvas_scrollJegyDiak,image=jegyCsik,borderwidth=0,highlightthickness=0)
    canvas_scrollJegyDiak.create_window(355, 20+i*100, window=csik1,anchor="nw")

    jegy2 = tk.Radiobutton(canvas_scrollJegyDiak,image=jegy2_unS,variable=var,value=2,command=lambda sor = i:jegyKatt(sor,2),**style)
    canvas_scrollJegyDiak.create_window(357, 20+i*100, window=jegy2,anchor="nw")

    csik2 = tk.Label(canvas_scrollJegyDiak,image=jegyCsik,borderwidth=0,highlightthickness=0)
    canvas_scrollJegyDiak.create_window(414, 20+i*100, window=csik2,anchor="nw")

    jegy3 = tk.Radiobutton(canvas_scrollJegyDiak,image=jegy3_unS,variable=var,value=3,command=lambda sor = i:jegyKatt(sor,3), **style)
    canvas_scrollJegyDiak.create_window(416, 20+i*100, window=jegy3,anchor="nw")

    csik3 = tk.Label(canvas_scrollJegyDiak,image=jegyCsik,borderwidth=0,highlightthickness=0)
    canvas_scrollJegyDiak.create_window(471, 20+i*100, window=csik3,anchor="nw")

    jegy4 = tk.Radiobutton(canvas_scrollJegyDiak,image=jegy4_unS,variable=var,value=4,command=lambda sor = i:jegyKatt(sor,4), **style)
    canvas_scrollJegyDiak.create_window(473, 20+i*100, window=jegy4,anchor="nw")

    csik4 = tk.Label(canvas_scrollJegyDiak,image=jegyCsik,borderwidth=0,highlightthickness=0)
    canvas_scrollJegyDiak.create_window(528, 20+i*100, window=csik4,anchor="nw")

    jegy5 = tk.Radiobutton(canvas_scrollJegyDiak,image=jegy5_unS,variable=var,value=5,command=lambda sor = i:jegyKatt(sor,5), **style)
    canvas_scrollJegyDiak.create_window(530, 20+i*100, window=jegy5,anchor="nw")

    visszavonGomb = tk.Button(canvas_scrollJegyDiak,image=kukaBtn,command=lambda sor = i:visszavon(sor),borderwidth=0,highlightthickness=0)
    visszavonGomb["bg"] = "#A5A5A5"
    visszavonGomb["activebackground"] = "#A5A5A5"
    visszavonGomb["border"] = "0"
    canvas_scrollJegyDiak.create_window(600, 15+i*100, window=visszavonGomb,anchor="nw")

    jegyek.append(jegy1)
    jegyek.append(jegy2)
    jegyek.append(jegy3)
    jegyek.append(jegy4)
    jegyek.append(jegy5)

    radios.append(jegyek)

    varMegNev = []
    varMegNev.append(var)
    varMegNev.append(diakokLekerd[i][1])

    varok.append(varMegNev)

canvas_scrollJegyDiak["scrollregion"]=(0,0,500,len(diakokLekerd)*100)
canvas_scrollJegyDiak.pack(side="left",expand=True,fill="both")

jegyiras = tk.Button(canvas_Jegyiras,image=jegybeirasBtn,command=Jegybeiras,borderwidth=0,highlightthickness=0)
jegyiras["bg"] = "#D9D9D9"
jegyiras["activebackground"] = "#D9D9D9"
jegyiras["border"] = "0"
jegyiras.place(x=300,y=620)

main.mainloop()