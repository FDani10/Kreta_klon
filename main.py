import tkinter as tk
from tkinter import messagebox 
from PIL import Image, ImageTk
import mysql.connector
import ctypes
import math
import re

diakID = ""
tanarID = ""
lines = []
numbers = []

con = mysql.connector.connect( host="localhost", user="root", password="", database="kreta_klon")
cursor = con.cursor()

#region Diák funkciók
def visszaOrakra():
    global canvas_balSC
    global canvas_jobbSc

    canvas_jobbSc.delete("all")
    canvas_balSC.delete("all")

    canvas_orakDiak.place(x=200,y=0)
    canvas_tanora.place(x=1000,y=0)

def oraMegjelenites(oraId):
    tantargyLekerdezes = f"SELECT tantargy.tantargy_nev,tanar.tanar_nev,tanar.tanar_email,tanar.tanar_telefon FROM `tanora` inner JOIN tanar on tanar.tanar_id = tanora.tanar_id inner JOIN tantargy on tantargy.tantargy_id = tanora.tantargy_id WHERE tanora_id = {oraId};"
    cursor.execute(tantargyLekerdezes)
    Tanora = cursor.fetchall()

    szamonkeresekLekerdez = f"SELECT szamonkeres.szamonkeres_text,szamonkeres.szamonkeres_datum FROM `osztaly` inner JOIN tanora on tanora.osztaly_id = osztaly.osztaly_id inner JOIN szamonkeres on szamonkeres.tanora_id = tanora.tanora_id where tanora.tanora_id = {oraId};"
    cursor.execute(szamonkeresekLekerdez)
    Szamonkeresek = cursor.fetchall()

    hianyzasLekerdez = f"SELECT hianyzas_datum FROM `hianyzasok` where diak_id = {diakID} and tanora_id = {oraId} ORDER BY hianyzas_datum DESC"
    cursor.execute(hianyzasLekerdez)
    Hianyzasok = cursor.fetchall()

    tanNev["text"] = Tanora[0][0]
    tanarAdatok["text"] = f"{Tanora[0][1]}\n{Tanora[0][2]}\n{Tanora[0][3]}"

    if len(Hianyzasok) > 0:
        for i in range(0,len(Hianyzasok)):
            hianyBG = tk.Label(canvas_balSC,image=hianyzasBlokk,bg="#DBE8FF")
            canvas_balSC.create_window(0,0+(i*60),window=hianyBG,anchor="nw")

            hianySzoveg = tk.Label(canvas_balSC,text=Hianyzasok[i][0],font=('Inter',20,'bold'),bg="#D9D9D9",fg="#414141")
            canvas_balSC.create_window(80,10+(i*60),window=hianySzoveg,anchor="nw")
    else:
        nincsHiany = tk.Label(canvas_balSC,text="Jelenleg nincs\nhiányzás beírva!",font=('Inter',20,'bold'),bg="#DBE8FF",fg="#414141")
        canvas_balSC.create_window(160,50,window=nincsHiany)

    if len(Szamonkeresek) > 0:
        for i in range(0,len(Szamonkeresek)):
            hianyBG = tk.Label(canvas_jobbSc,image=hianyzasBlokk,bg="#DBE8FF")
            canvas_jobbSc.create_window(0,0+(i*60),window=hianyBG,anchor="nw")
            
            szamonSzoveg = tk.Label(canvas_jobbSc,text=Szamonkeresek[i][0],font=('Inter',20,'bold'),bg="#D9D9D9",fg="#414141")
            canvas_jobbSc.create_window(120,27+(i*60),window=szamonSzoveg)
            if len(Szamonkeresek[i][0])>15:
                szamonSzoveg["text"] = f"{Szamonkeresek[i][0][:12]}..."

            szamonDatum = tk.Label(canvas_jobbSc,text=Szamonkeresek[i][1],font=('Inter',10,'bold'),bg="#D9D9D9",fg="#414141")
            canvas_jobbSc.create_window(210,17+(i*60),window=szamonDatum,anchor="nw")
    else:
        nincsHiany = tk.Label(canvas_jobbSc,text="Jelenleg nincs\nszámonkérés beírva!",font=('Inter',20,'bold'),bg="#DBE8FF",fg="#414141")
        canvas_jobbSc.create_window(160,50,window=nincsHiany)


    canvas_balSC["scrollregion"]=(0,0,500,len(Hianyzasok)*60)
    canvas_balSC.pack(side="left",expand=True,fill="both")

    canvas_jobbSc["scrollregion"]=(0,0,500,len(Szamonkeresek)*60)
    canvas_jobbSc.pack(side="left",expand=True,fill="both")

    canvas_orakDiak.place(x=1000,y=0)
    canvas_tanora.place(x=200,y=0)

def DiakBej():
    global diakID
    ud = username_d.get()
    pd = password_d.get()
    if(ud == "" or pd == ""):
        print("Kérem töltsön ki minden mezőt!")
    else:
        diakInTable = 'SELECT diak_id,diak_osztaly FROM diak WHERE diak_id LIKE "'+ud+'" AND diak_jelszo = "'+pd+'";'
        cursor.execute(diakInTable)
        table = cursor.fetchall()
        if(len(table) == 1):
            diakID = ud

            #Legutolsó 3 jegy
            utolso3jegy = "SELECT tantargy.tantargy_nev,beirt_jegy FROM `jegy` INNER JOIN tanora on tanora.tanora_id = jegy.tanora_id inner JOIN tantargy on tantargy.tantargy_id = tanora.tantargy_id where jegy.diak_id = "+ud+" ORDER BY jegy_ido DESC limit 3;"
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
                case atlag if 2<=atlag<3:
                    atlagNagy.config(foreground="red")
                case atlag if 3<=atlag<4:
                    atlagNagy.config(foreground="lightgreen")
                case atlag if 4<=atlag<4.5:
                    atlagNagy.config(foreground="green")
                case atlag if 4.4 < atlag:
                    atlagNagy.config(foreground="darkgreen")

            #Legutolsó 3 üzenet
            utolso3uzenet = f"SELECT tanar.tanar_nev,uzenet.uzenet_text FROM `diak` INNER JOIN uzenetkinek on uzenetkinek.osztaly_id = diak.diak_osztaly inner join uzenet on uzenetkinek.uzenet_id = uzenet.uzenet_id inner JOIN tanar on tanar.tanar_id = uzenet.tanar_id where diak.diak_id = {diakID} order by uzenet.uzenet_id DESC limit 3;"
            cursor.execute(utolso3uzenet)
            utolsoUzenetek = cursor.fetchall()
            if len(utolsoUzenetek) > 0:
                mess1["text"] = utolsoUzenetek[0][0]
                mess1Text["text"] = utolsoUzenetek[0][1]
                if len(utolsoUzenetek[0][1]) > 27:
                    mess1Text["text"] = f"{utolsoUzenetek[0][1][:25]}..."
            if len(utolsoUzenetek) > 1:
                mess2["text"] = utolsoUzenetek[1][0]
                mess2Text["text"] = utolsoUzenetek[1][1]
                if len(utolsoUzenetek[1][1]) > 27:
                    mess2Text["text"] = f"{utolsoUzenetek[1][1][:25]}..."
            if len(utolsoUzenetek) > 2:
                mess3["text"] = utolsoUzenetek[2][0]
                mess3Text["text"] = utolsoUzenetek[2][1]
                if len(utolsoUzenetek[2][1]) > 27:
                    mess3Text["text"] = f"{utolsoUzenetek[2][1][:25]}..."


            #Jegyek oldal megcsinálása
            tanuloTantargyak = f"SELECT tantargy.tantargy_id, tantargy.tantargy_nev, tanora.tanora_id FROM `diak` inner join osztaly on osztaly.osztaly_id = diak.diak_osztaly INNER JOIN tanora on tanora.osztaly_id = osztaly.osztaly_id inner join tantargy on tantargy.tantargy_id = tanora.tantargy_id where diak.diak_id = {diakID};"
            cursor.execute(tanuloTantargyak)
            Tantargyak = cursor.fetchall()
            for i in range(0,len(Tantargyak)):
                tanId = str(Tantargyak[i][0])
                oraId = Tantargyak[i][2]
                if i%2 == 0:
                    tantargyGomb = tk.Button(canvas_jegyDiak,image=tantargyKocka,command= lambda e = tanId:jegyreKattint(e))
                    tantargyGomb["bg"] = "#ACC8FF"
                    tantargyGomb["activebackground"] = "#ACC8FF"
                    tantargyGomb["border"] = "0"
                    tantargyGomb.place(x=70,y=100+math.floor(i/2)*130)
                    tantargyNev = tk.Label(canvas_jegyDiak,bg="#DBE8FF",foreground="black",text=Tantargyak[i][1],font=('Inter',20,'bold'))
                    tantargyNev.place(x=84,y=120+math.floor(i/2)*130,width=208,height=28)
                    tantargyNev.bind("<Button-1>", lambda e,id = tanId : jegyreKattint(id))
                    atlagKep = tk.Label(canvas_jegyDiak,bg="#DBE8FF")
                    atlagKep.place(x=300,y=107+math.floor(i/2)*130)
                    atlagKep.bind("<Button-1>", lambda e,id = tanId : jegyreKattint(id))

                    tanuloTanAtlag = f"SELECT ROUND(AVG(beirt_jegy),1) FROM `jegy` inner join tanora on tanora.tanora_id = jegy.tanora_id where jegy.diak_id = {diakID} and tanora.tantargy_id = {tanId};"
                    cursor.execute(tanuloTanAtlag)
                    TanAtlag = cursor.fetchall()
                    atlag = TanAtlag[0][0]
                    atlagText = tk.Label(canvas_jegyDiak,text=atlag,font=('Inter',18,'bold'))
                    atlagText.place(x=309,y=119+math.floor(i/2)*130)
                    atlagText.bind("<Button-1>", lambda e,id = tanId : jegyreKattint(id))
                    match atlag:
                            case atlag if 2 > atlag:
                                atlagKep["image"] = jegyElegtelen
                                atlagText["bg"] = "#ab1400"
                            case atlag if 2<=atlag<3:
                                atlagKep["image"] = jegyElegseges
                                atlagText["bg"] = "#fd1e00"
                            case atlag if 3<=atlag<4:
                                atlagKep["image"] = jegyKozepes
                                atlagText["bg"] = "#00ef18"
                            case atlag if 4<=atlag<4.5:
                                atlagKep["image"] = jegyJo
                                atlagText["bg"] = "#00ac11"
                            case atlag if 4.4 < atlag:
                                atlagKep["image"] = jegyKivalo
                                atlagText["bg"] = "#005e09"

                    #Órák oldal bal része
                    tantargyGomb = tk.Button(canvas_orakDiak,image=tantargyKocka,command= lambda e = oraId : oraMegjelenites(e))
                    tantargyGomb["bg"] = "#ACC8FF"
                    tantargyGomb["activebackground"] = "#ACC8FF"
                    tantargyGomb["border"] = "0"
                    tantargyGomb.place(x=70,y=100+math.floor(i/2)*130)
                    tantargyNev = tk.Label(canvas_orakDiak,bg="#DBE8FF",foreground="black",text=Tantargyak[i][1],font=('Inter',20,'bold'))
                    tantargyNev.bind("<Button-1>", lambda e,id = oraId : oraMegjelenites(id))
                    tantargyNev.place(x=124,y=120+math.floor(i/2)*130,width=208,height=28)

                else:
                    tantargyGomb = tk.Button(canvas_jegyDiak,image=tantargyKocka,command=lambda e = tanId:jegyreKattint(e))
                    tantargyGomb["bg"] = "#ACC8FF"
                    tantargyGomb["activebackground"] = "#ACC8FF"
                    tantargyGomb["border"] = "0"
                    tantargyGomb.place(x=418,y=100+math.floor(i/2)*130)
                    tantargyNev = tk.Label(canvas_jegyDiak,bg="#DBE8FF",foreground="black",text=Tantargyak[i][1],font=('Inter',20,'bold'))
                    tantargyNev.place(x=432,y=120+math.floor(i/2)*130,width=208,height=28)
                    tantargyNev.bind("<Button-1>", lambda e,id = tanId : jegyreKattint(id))
                    atlagKep = tk.Label(canvas_jegyDiak,bg="#DBE8FF")
                    atlagKep.place(x=648,y=107+math.floor(i/2)*130)
                    atlagKep.bind("<Button-1>", lambda e,id = tanId : jegyreKattint(id))

                    tanuloTanAtlag = f"SELECT ROUND(AVG(beirt_jegy),1) FROM `jegy` inner join tanora on tanora.tanora_id = jegy.tanora_id where jegy.diak_id = {diakID} and tanora.tantargy_id = {tanId};"
                    cursor.execute(tanuloTanAtlag)
                    TanAtlag = cursor.fetchall()
                    atlag = TanAtlag[0][0]
                    atlagText = tk.Label(canvas_jegyDiak,text=atlag,font=('Inter',18,'bold'))
                    atlagText.place(x=657,y=119+math.floor(i/2)*130)
                    atlagText.bind("<Button-1>", lambda e,id = tanId : jegyreKattint(id))
                    match atlag:
                            case atlag if 2 > atlag:
                                atlagKep["image"] = jegyElegtelen
                                atlagText["bg"] = "#ab1400"
                            case atlag if 2<=atlag<3:
                                atlagKep["image"] = jegyElegseges
                                atlagText["bg"] = "#fd1e00"
                            case atlag if 3<=atlag<4:
                                atlagKep["image"] = jegyKozepes
                                atlagText["bg"] = "#00ef18"
                            case atlag if 4<=atlag<4.5:
                                atlagKep["image"] = jegyJo
                                atlagText["bg"] = "#00ac11"
                            case atlag if 4.4 < atlag:
                                atlagKep["image"] = jegyKivalo
                                atlagText["bg"] = "#005e09"
                    
                    #Órák oldal jobb része
                    tantargyGomb = tk.Button(canvas_orakDiak,image=tantargyKocka,command= lambda e = oraId : oraMegjelenites(e))
                    tantargyGomb["bg"] = "#ACC8FF"
                    tantargyGomb["activebackground"] = "#ACC8FF"
                    tantargyGomb["border"] = "0"
                    tantargyGomb.place(x=418,y=100+math.floor(i/2)*130)
                    tantargyNev = tk.Label(canvas_orakDiak,bg="#DBE8FF",foreground="black",text=Tantargyak[i][1],font=('Inter',20,'bold'))
                    tantargyNev.bind("<Button-1>", lambda e,id = oraId : oraMegjelenites(id))
                    tantargyNev.place(x=472,y=120+math.floor(i/2)*130,width=208,height=28)
                    

            #Saját profil oldal megcsinálása
            utolso3jegy = f"SELECT diak_jelszo,diak_email,diak_telefon FROM diak WHERE diak_id LIKE '{ud}' AND diak_jelszo = '{pd}'"
            cursor.execute(utolso3jegy)
            tableAdatok = cursor.fetchall()
            pSz["text"] = tableAdatok[0][1]
            pT["text"] = tableAdatok[0][2]
            pJ["text"] = f"{tableAdatok[0][0][0]}{((len(tableAdatok[0][0]))-2)*'*'}{tableAdatok[0][0][(len(tableAdatok[0][0]))-1]}"

            canvas_bej.place(x=1000,y=0)
            canvas_kezdDiak.place(x=200,y=0)
            canvas_oldalMenu.place(x=0,y=0)

            #Üzenetek oldal megcsinálása
            querry = f"SELECT tanar.tanar_nev,uzenet.uzenet_targy, LEFT(uzenet.uzenet_text,70) FROM `diak` inner join osztaly on osztaly.osztaly_id = diak.diak_osztaly INNER JOIN uzenetkinek on uzenetkinek.osztaly_id = osztaly.osztaly_id inner JOIN uzenet on uzenet.uzenet_id = uzenetkinek.uzenet_id inner JOIN tanar on tanar.tanar_id = uzenet.tanar_id WHERE diak_id = {diakID};"
            cursor.execute(querry)
            uzenetek = cursor.fetchall()
            for i in range(0,len(uzenetek)):
                uzenet = tk.Label(canvas_uziScroll,image=uzenetTartalom,bg="#D9D9D9")
                canvas_uziScroll.create_window(328, 70+i*120, window=uzenet)

                uzenet_targy = tk.Label(canvas_uziScroll,bg="#F4F3F3",text=f"{uzenetek[i][0]} | {uzenetek[i][1]}",font=('Inter',20,'bold'))
                canvas_uziScroll.create_window(20, 50+i*120, window=uzenet_targy,anchor="w")

                uzenet_targy = tk.Label(canvas_uziScroll,bg="#F4F3F3",text=f"{uzenetek[i][2]}",font=('Inter',12))
                canvas_uziScroll.create_window(20, 80+i*120, window=uzenet_targy,anchor="w")
                if len(uzenetek[i][2]) == 70:
                    uzenet_targy["text"] = f"{uzenetek[i][2]}..."
            canvas_uziScroll["scrollregion"]=(0,0,500,len(uzenetek)*120+70)

            #Órák oldal megcsinálása
            

        else:
            print("Rossz név vagy jelszó!")
    
def jegyreKattint(tanId):
    global diakID
    tanuloTanJegyek = f"SELECT beirt_jegy,jegy_ido FROM `jegy` inner join tanora on tanora.tanora_id = jegy.tanora_id where diak_id = {diakID} and tanora.tantargy_id = {tanId} ORDER BY jegy_ido DESC;"
    cursor.execute(tanuloTanJegyek)
    TanJegyek = cursor.fetchall()
    nums = []
    for i in range(0,len(TanJegyek)): 
        nums.append(TanJegyek[i][0])
        label1 = tk.Label(canvasScrollable,image=jegyekBeirva,bg="#ACC8FF")
        canvasScrollable.create_window(300, 50+i*70, window=label1)

        jegyLabel = tk.Label(canvasScrollable,font=('Inter',20,'bold'),text=TanJegyek[i][1],bg="#D9D9D9")
        canvasScrollable.create_window(150, 50+i*70, window=jegyLabel)

        jegyElvImg = tk.Label(canvasScrollable, image=jegyElvalaszto,bg="#D9D9D9")
        canvasScrollable.create_window(250, 50+i*70, window=jegyElvImg)

        jegyElvImg2 = tk.Label(canvasScrollable, image=jegyElvalaszto,bg="#D9D9D9")
        canvasScrollable.create_window(450, 50+i*70, window=jegyElvImg2)

        jegyNum = tk.Label(canvasScrollable,font=('Inter',20,'bold'),text=TanJegyek[i][0],bg="#D9D9D9")
        canvasScrollable.create_window(500, 50+i*70, window=jegyNum)

    canvas_jegyek.create_image(74,15,anchor="nw",image=nagyKocka)

    nums = nums[::-1]
    ugras = 500/len(nums)
    l = nums[0]
    for i in range(1,len(nums)+1):
        ujl = round(sum(nums[:i])/len(nums[:i]),2)
        line = canvas_jegyek.create_line(ugras*i+100,320-l*50,ugras*(i+1)+100,320-ujl*50,fill="red")
        lines.append(line)
        avgNum = tk.Label(canvas_jegyek,bg="#DBE8FF",foreground="black",text=str(ujl),font=('Inter',10))
        avgNum.place(x=ugras*(i+1)+80,y=290-ujl*50)
        numbers.append(avgNum)
        l=sum(nums[:i])/len(nums[:i])

    canvasScrollable["scrollregion"]=(0,0,500,40+len(TanJegyek)*70)
    canvasScrollable.pack(side="left",expand=True,fill="both")

    visszaBtn = tk.Button(canvas_jegyek,text="Vissza",command=backToJegyek)
    visszaBtn.place(x=350,y=620,width=100,height=50)

    canvas_jegyDiak.place(x=1000,y=0)
    canvas_jegyek.place(x=200,y=0)

def backToJegyek():
    global canvas_jegyek
    global lines
    global canvasScrollable

    canvas_jegyek.delete("all")
    canvasScrollable.delete("all")
    
    for i in range(0,len(lines)):
        canvas_jegyek.delete(lines[i])

    for i in range(0,len(numbers)):
        numbers[i].destroy()

    canvas_jegyDiak.place(x=200,y=0)
    canvas_jegyek.place(x=1000,y=0)

def DiakKezd():
    canvas_jegyDiak.place(x=1000,y=0)
    canvas_kezdDiak.place(x=200,y=0)
    canvas_profDiak.place(x=1000,y=0)
    canvas_jegyek.place(x=1000,y=0)
    canvas_uzenetDiak.place(x=1000,y=0)
    canvas_orakDiak.place(x=1000,y=0)
    canvas_tanora.place(x=1000,y=1000)

    fooldal_btn["image"] = fooldal_selected
    orak_btn["image"] = orakBtn
    jegyek_btn["image"] = jegyekBtn
    infok_btn["image"] = infokBtn
    profil_btn["image"] = profilBtn

def DiakJegy():
    canvas_kezdDiak.place(x=1000,y=0)
    canvas_jegyDiak.place(x=200,y=0)
    canvas_profDiak.place(x=1000,y=0)
    canvas_jegyek.place(x=1000,y=0)
    canvas_uzenetDiak.place(x=1000,y=0)
    canvas_orakDiak.place(x=1000,y=0)
    canvas_tanora.place(x=1000,y=1000)

    fooldal_btn["image"] = fooldalBtn
    orak_btn["image"] = orakBtn
    jegyek_btn["image"] = jegyek_selected
    infok_btn["image"] = infokBtn
    profil_btn["image"] = profilBtn

def DiakProfil():
    canvas_kezdDiak.place(x=1000,y=0)
    canvas_jegyDiak.place(x=1000,y=0)
    canvas_profDiak.place(x=200,y=0)
    canvas_jegyek.place(x=1000,y=0)
    canvas_uzenetDiak.place(x=1000,y=0)
    canvas_orakDiak.place(x=1000,y=0)
    canvas_tanora.place(x=1000,y=1000)

    fooldal_btn["image"] = fooldalBtn
    orak_btn["image"] = orakBtn
    jegyek_btn["image"] = jegyekBtn
    infok_btn["image"] = infokBtn
    profil_btn["image"] = profil_selected

def DiakUzenet():
    canvas_kezdDiak.place(x=1000,y=0)
    canvas_jegyDiak.place(x=1000,y=0)
    canvas_profDiak.place(x=1000,y=0)
    canvas_jegyek.place(x=1000,y=0)
    canvas_uzenetDiak.place(x=200,y=0)
    canvas_orakDiak.place(x=1000,y=0)
    canvas_tanora.place(x=1000,y=1000)

    fooldal_btn["image"] = fooldalBtn
    orak_btn["image"] = orakBtn
    jegyek_btn["image"] = jegyekBtn
    infok_btn["image"] = infok_selected
    profil_btn["image"] = profilBtn

def DiakOrak():
    canvas_kezdDiak.place(x=1000,y=0)
    canvas_jegyDiak.place(x=1000,y=0)
    canvas_profDiak.place(x=1000,y=0)
    canvas_jegyek.place(x=1000,y=0)
    canvas_uzenetDiak.place(x=1000,y=0)
    canvas_orakDiak.place(x=200,y=0)
    canvas_tanora.place(x=1000,y=1000)

    fooldal_btn["image"] = fooldalBtn
    orak_btn["image"] = orak_selected
    jegyek_btn["image"] = jegyekBtn
    infok_btn["image"] = infokBtn
    profil_btn["image"] = profilBtn

def KijelentkezesDiak():
    diakID = ""
    tanarID = ""

    username_d.delete(0,tk.END)
    username_t.delete(0,tk.END)
    password_d.delete(0,tk.END)
    password_t.delete(0,tk.END)
    canvas_oldalMenu.place(x=1000,y=1000)
    canvas_kezdDiak.place(x=1000,y=0)
    canvas_jegyDiak.place(x=1000,y=0)
    canvas_profDiak.place(x=1000,y=0)
    canvas_jegyek.place(x=1000,y=0)
    canvas_uzenetDiak.place(x=1000,y=0)
    canvas_orakDiak.place(x=1000,y=0)
    canvas_tanora.place(x=1000,y=1000)
    canvas_bej.place(x=0,y=0)

#region Változtatások funkciók
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def UjEmail():
    global emailEntry
    global canvas_email
    global pSz
    if(re.fullmatch(regex, emailEntry.get())):
        emailvaltozquerry = f"UPDATE `diak` SET `diak_email`='{emailEntry.get()}' WHERE `diak_id` = {diakID}"
        cursor.execute(emailvaltozquerry)
        con.commit()
        messagebox.showinfo("showinfo", "Email cím sikeresen megváltoztatva!")
        pSz["text"] = emailEntry.get()
        valemailmain.destroy()

    else:
        invalid = tk.Label(canvas_email,text="Rendes email címet adjon meg!",fg="red",bg="#F1F1F1",font=('Inter',10))
        invalid.place(x=65,y=185)

def emailValtoztatas():
    global emailEntry
    global canvas_email
    global valemailmain
    
    valemailmain = tk.Toplevel()
    #ctypes.windll.shcore.SetProcessDpiAwareness(1)
    valemailmain.geometry("500x350")
    valemailmain.resizable(False, False)
    valemailmain.title("Kréta - email változtatás")

    canvas_email = tk.Canvas(valemailmain,bg="#F1F1F1")
    canvas_email.place(x=0,y=0,width=500,height=350)

    emailText = tk.Label(canvas_email,text="Új email cím:",font=('Inter',16,'bold'))
    emailText.place(x=57,y=91)

    emailEntryBG = tk.Label(canvas_email,image=valtoztatasEntry,bg="#F1F1F1")
    emailEntryBG.place(x=57,y=131,width=386,height=50)

    emailEntry = tk.Entry(canvas_email,bg="#D9D9D9",font=('Inter',12),border=0)
    emailEntry.place(x=70,y=140,width=360,height=30)

    valBtn = tk.Button(canvas_email,image=valtoztatasBtn,command= UjEmail)
    valBtn["bg"] = "#F1F1F1"
    valBtn["activebackground"] = "#F1F1F1"
    valBtn["border"] = "0"
    valBtn.place(x=162,y=217)

    megBtn = tk.Button(canvas_email,image=megseBtn,command= valemailmain.destroy)
    megBtn["bg"] = "#F1F1F1"
    megBtn["activebackground"] = "#F1F1F1"
    megBtn["border"] = "0"
    megBtn.place(x=162,y=277)

    valemailmain.grab_set()

    valemailmain.mainloop()

def UjTelefon():
    global telefonEntry
    global canvas_telefon
    global pT
    if(telefonEntry.get().isdigit()):
        telefonvaltozquerry = f"UPDATE `diak` SET `diak_telefon`='{telefonEntry.get()}' WHERE `diak_id` = {diakID}"
        cursor.execute(telefonvaltozquerry)
        con.commit()
        messagebox.showinfo("showinfo", "Telefonszám sikeresen megváltoztatva!")
        pT["text"] = telefonEntry.get()
        valtelefonmain.destroy()

    else:
        invalid = tk.Label(canvas_telefon,text="Rendes telefonszámot adjon meg!",fg="red",bg="#F1F1F1",font=('Inter',10))
        invalid.place(x=65,y=185)

def telefonValtoztatas():
    global telefonEntry
    global canvas_telefon
    global valtelefonmain
    
    valtelefonmain = tk.Toplevel()
    #ctypes.windll.shcore.SetProcessDpiAwareness(1)
    valtelefonmain.geometry("500x350")
    valtelefonmain.resizable(False, False)
    valtelefonmain.title("Kréta - telefonszám változtatás")

    canvas_telefon = tk.Canvas(valtelefonmain,bg="#F1F1F1")
    canvas_telefon.place(x=0,y=0,width=500,height=350)

    telefonText = tk.Label(canvas_telefon,text="Új telefonszám:",font=('Inter',16,'bold'))
    telefonText.place(x=57,y=91)

    telefonEntryBG = tk.Label(canvas_telefon,image=valtoztatasEntry,bg="#F1F1F1")
    telefonEntryBG.place(x=57,y=131,width=386,height=50)

    telefonEntry = tk.Entry(canvas_telefon,bg="#D9D9D9",font=('Inter',12),border=0)
    telefonEntry.place(x=70,y=140,width=360,height=30)

    valBtn = tk.Button(canvas_telefon,image=valtoztatasBtn,command= UjTelefon)
    valBtn["bg"] = "#F1F1F1"
    valBtn["activebackground"] = "#F1F1F1"
    valBtn["border"] = "0"
    valBtn.place(x=162,y=217)

    megBtn = tk.Button(canvas_telefon,image=megseBtn,command= valtelefonmain.destroy)
    megBtn["bg"] = "#F1F1F1"
    megBtn["activebackground"] = "#F1F1F1"
    megBtn["border"] = "0"
    megBtn.place(x=162,y=277)

    valtelefonmain.grab_set()

    valtelefonmain.mainloop()

def UjJelszo():
    global jelszoEntry
    global canvas_jelszo
    global pJ
    jelszovaltozquerry = f"UPDATE `diak` SET `diak_jelszo`='{jelszoEntry.get()}' WHERE `diak_id` = {diakID}"
    cursor.execute(jelszovaltozquerry)
    con.commit()
    messagebox.showinfo("showinfo", "Jelszó sikeresen megváltoztatva!")
    pJ["text"] = f"{jelszoEntry.get()[0]}{((len(jelszoEntry.get()))-2)*'*'}{jelszoEntry.get()[(len(jelszoEntry.get()))-1]}"
    valjelszomain.destroy()

def jelszoValtoztatas():
    global jelszoEntry
    global canvas_jelszo
    global valjelszomain
    
    valjelszomain = tk.Toplevel()
    #ctypes.windll.shcore.SetProcessDpiAwareness(1)
    valjelszomain.geometry("500x350")
    valjelszomain.resizable(False, False)
    valjelszomain.title("Kréta - jelszó változtatás")

    canvas_jelszo = tk.Canvas(valjelszomain,bg="#F1F1F1")
    canvas_jelszo.place(x=0,y=0,width=500,height=350)

    jelszoText = tk.Label(canvas_jelszo,text="Új jelszó:",font=('Inter',16,'bold'))
    jelszoText.place(x=57,y=91)

    jelszoEntryBG = tk.Label(canvas_jelszo,image=valtoztatasEntry,bg="#F1F1F1")
    jelszoEntryBG.place(x=57,y=131,width=386,height=50)

    jelszoEntry = tk.Entry(canvas_jelszo,bg="#D9D9D9",font=('Inter',12),border=0)
    jelszoEntry.place(x=70,y=140,width=360,height=30)

    valBtn = tk.Button(canvas_jelszo,image=valtoztatasBtn,command= UjJelszo)
    valBtn["bg"] = "#F1F1F1"
    valBtn["activebackground"] = "#F1F1F1"
    valBtn["border"] = "0"
    valBtn.place(x=162,y=217)

    megBtn = tk.Button(canvas_jelszo,image=megseBtn,command= valjelszomain.destroy)
    megBtn["bg"] = "#F1F1F1"
    megBtn["activebackground"] = "#F1F1F1"
    megBtn["border"] = "0"
    megBtn.place(x=162,y=277)

    valjelszomain.grab_set()

    valjelszomain.mainloop()
#endregion

#endregion

#region Tanár funkciók
def TanarBej():
    global tanarID
    ut = username_t.get()
    pt = password_t.get()
    if(ut == "" or pt == ""):
        print("Kérem töltsön ki minden mezőt!")
    else:
        tanarInTable = f"SELECT tanar_id FROM tanar WHERE tanar_felnev LIKE '{ut}'"
        cursor.execute(tanarInTable)
        table = cursor.fetchall()
        if(len(table) == 1):
            tanarID = table[0][0]

            #Jegybeírás oldal megcsinálása
            tanarOsztalyok = f"SELECT tanora.tanora_id, tantargy.tantargy_nev, osztaly.osztaly_nev FROM `tanora` inner join osztaly on osztaly.osztaly_id = tanora.osztaly_id inner join tantargy on tantargy.tantargy_id = tanora.tantargy_id where tanar_id = {tanarID};"
            cursor.execute(tanarOsztalyok)
            Osztalyok = cursor.fetchall()
            for i in range(0,len(Osztalyok)):
                tanId = Osztalyok[i][0]
                oszID = Osztalyok[i][2]
                if i%2 == 0:
                    #Órák oldal bal része
                    oszGomb = tk.Button(canvasScrollable_TJegy,image=osztalyGomb,command= lambda tid = tanId, oid = oszID:print(f"{tid}, {oid}"))
                    oszGomb["bg"] = "#FAFAFA"
                    oszGomb["activebackground"] = "#FAFAFA"
                    oszGomb["border"] = "0"
                    canvasScrollable_TJegy.create_window(50,10+math.floor(i/2)*150,window=oszGomb,anchor="nw")
                    osztalyNev = tk.Label(canvasScrollable_TJegy,bg="#C1D8FF",foreground="black",text=Osztalyok[i][2],font=('Inter',38,'bold'))
                    osztalyNev.bind("<Button-1>",lambda e,tid = tanId, oid = oszID:print(f"{tid}, {oid}"))
                    canvasScrollable_TJegy.create_window(55,35+math.floor(i/2)*150,window=osztalyNev,width=79,height=67,anchor="nw")

                else:
                    #Órák oldal jobb része
                    oszGomb = tk.Button(canvasScrollable_TJegy,image=osztalyGomb,command= lambda tid = tanId, oid = oszID:print(f"{tid}, {oid}"))
                    oszGomb["bg"] = "#FAFAFA"
                    oszGomb["activebackground"] = "#FAFAFA"
                    oszGomb["border"] = "0"
                    canvasScrollable_TJegy.create_window(430,10+math.floor(i/2)*150,window=oszGomb,anchor="nw")
                    osztalyNev = tk.Label(canvasScrollable_TJegy,bg="#C1D8FF",foreground="black",text=Osztalyok[i][2],font=('Inter',38,'bold'))
                    osztalyNev.bind("<Button-1>",lambda e,tid = tanId, oid = oszID:print(f"{tid}, {oid}"))
                    canvasScrollable_TJegy.create_window(438,35+math.floor(i/2)*150,window=osztalyNev,width=79,height=67,anchor="nw")
            
            canvasScrollable_TJegy["scrollregion"]=(0,0,700,len(Osztalyok)*150/2)
            canvasScrollable_TJegy.pack(side="left",expand=True,fill="both")

            canvas_bej.place(x=1000,y=0)
            canvas_TKezdolap.place(x=200,y=0)
            canvas_ToldalMenu.place(x=0,y=0)
            print(tanarID)

def TanarJegybeiras():
    canvas_TKezdolap.place(x=1000,y=0)
    canvas_TJegy.place(x=200,y=0)
#endregion

main = tk.Tk()
#ctypes.windll.shcore.SetProcessDpiAwareness(1)
main.geometry("1000x700")
main.resizable(False, False)
main.title("Kréta")

#region Képbeolvasás
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
image_btn=Image.open(f'./pics/tantargyKocka.png')
img_btn=image_btn.resize((312, 67))
tantargyKocka=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/jegyKivalo.png')
img_btn=image_btn.resize((53, 53))
jegyKivalo=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/jegyJo.png')
img_btn=image_btn.resize((53, 53))
jegyJo=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/jegyKozepes.png')
img_btn=image_btn.resize((53, 53))
jegyKozepes=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/jegyElegseges.png')
img_btn=image_btn.resize((53, 53))
jegyElegseges=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/jegyElegtelen.png')
img_btn=image_btn.resize((53, 53))
jegyElegtelen=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/jegyekBeirva.png')
img_btn=image_btn.resize((503, 59))
jegyekBeirva=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/nagyKocka.png')
img_btn=image_btn.resize((672, 265))
nagyKocka=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/jegyElvalaszto.png')
img_btn=image_btn.resize((3, 26))
jegyElvalaszto=ImageTk.PhotoImage(img_btn)
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
image_btn=Image.open(f'./pics/uzenetBG.png')
img_btn=image_btn.resize((700, 530))
uzenetBG=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/uzenetTartalom.png')
img_btn=image_btn.resize((650, 95))
uzenetTartalom=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/uzenetFejlec.png')
img_btn=image_btn.resize((700, 75))
uzenetFejlec=ImageTk.PhotoImage(img_btn)
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
image_btn=Image.open(f'./pics/megseBtn.png')
img_btn=image_btn.resize((163, 43))
megseBtn=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/valtoztatasBtn.png')
img_btn=image_btn.resize((163, 43))
valtoztatasBtn=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/valtoztatasEntry.png')
img_btn=image_btn.resize((386, 50))
valtoztatasEntry=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/megseBtn.png')
img_btn=image_btn.resize((163, 43))
megseBtn=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/valtoztatasBtn.png')
img_btn=image_btn.resize((163, 43))
valtoztatasBtn=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/valtoztatasEntry.png')
img_btn=image_btn.resize((386, 50))
valtoztatasEntry=ImageTk.PhotoImage(img_btn)

#Csak a tanár résznél használtak:
image_btn=Image.open(f'./pics/dogakBtn.png')
img_btn=image_btn.resize((96, 25))
dogakBtn=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/dogak_selected.png')
img_btn=image_btn.resize((155, 45))
dogak_selected=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/hianyzasBtn.png')
img_btn=image_btn.resize((121, 25))
hianyzasBtn=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/hianyzas_selected.png')
img_btn=image_btn.resize((155, 45))
hianyzas_selected=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/osztalyGomb.png')
img_btn=image_btn.resize((320, 120))
osztalyGomb=ImageTk.PhotoImage(img_btn)


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

reg_btn2 = tk.Button(canvas_bej,image=my_img21,command=TanarBej)
reg_btn2["bg"] = "#3479FF"
reg_btn2["activebackground"] = "#3479FF"
reg_btn2["border"] = "0"
reg_btn2.place(x=630,y=544)
#endregion

#region Diák oldal

#region Oldalmenü
canvas_oldalMenu = tk.Canvas(main,bg="#3479FF",width=200,height=700)
canvas_oldalMenu.place(x=1000,y=0)

valasztoFelulet = tk.Label(canvas_oldalMenu,bg="#3479FF")
valasztoFelulet.place(x=0,y=0,width=200,height=700)

kretaLogoLabel = tk.Label(canvas_oldalMenu, image=kretaLogo,bg="#3479FF")
kretaLogoLabel.place(x=13,y=18)

kretaLogoText = tk.Label(canvas_oldalMenu,bg="#3479FF",foreground="white",text="KRÉTA",font=('Inter',26,'bold'))
kretaLogoText.place(x=54,y=18,width=121,height=39)

fooldal_btn = tk.Button(canvas_oldalMenu,image=fooldal_selected,command=DiakKezd)
fooldal_btn["bg"] = "#3479FF"
fooldal_btn["activebackground"] = "#3479FF"
fooldal_btn["border"] = "0"
fooldal_btn.place(x=29,y=122)
orak_btn = tk.Button(canvas_oldalMenu,image=orakBtn,command=DiakOrak)
orak_btn["bg"] = "#3479FF"
orak_btn["activebackground"] = "#3479FF"
orak_btn["border"] = "0"
orak_btn.place(x=29,y=187)
jegyek_btn = tk.Button(canvas_oldalMenu,image=jegyekBtn,command=DiakJegy)
jegyek_btn["bg"] = "#3479FF"
jegyek_btn["activebackground"] = "#3479FF"
jegyek_btn["border"] = "0"
jegyek_btn.place(x=29,y=242)
infok_btn = tk.Button(canvas_oldalMenu,image=infokBtn,command=DiakUzenet)
infok_btn["bg"] = "#3479FF"
infok_btn["activebackground"] = "#3479FF"
infok_btn["border"] = "0"
infok_btn.place(x=29,y=297)
profil_btn = tk.Button(canvas_oldalMenu,image=profilBtn,command=DiakProfil)
profil_btn["bg"] = "#3479FF"
profil_btn["activebackground"] = "#3479FF"
profil_btn["border"] = "0"
profil_btn.place(x=29,y=351)
kijelent_btn = tk.Button(canvas_oldalMenu,image=kijelentBtn,command=KijelentkezesDiak)
kijelent_btn["bg"] = "#3479FF"
kijelent_btn["activebackground"] = "#3479FF"
kijelent_btn["border"] = "0"
kijelent_btn.place(x=20,y=659)

#endregion

#region Kezdőlap diáknak

canvas_kezdDiak = tk.Canvas(main,bg="#3479FF",width=800,height=700)
canvas_kezdDiak.place(x=1000,y=0)

masikOldal = tk.Label(canvas_kezdDiak,bg="#ACC8FF")
masikOldal.place(x=000,y=0,width=800,height=700)

#Első kicsi kocka
kretaLogoLabel = tk.Label(canvas_kezdDiak, image=kicsiKocka,bg="#ACC8FF")
kretaLogoLabel.place(x=52,y=62)

kretaLogoLabel = tk.Label(canvas_kezdDiak, image=kkKisvonal,bg="#DBE8FF")
kretaLogoLabel.place(x=68,y=111)
kretaLogoLabel = tk.Label(canvas_kezdDiak, image=kkNagyvonal,bg="#DBE8FF")
kretaLogoLabel.place(x=93,y=181)
kretaLogoLabel = tk.Label(canvas_kezdDiak, image=kkNagyvonal,bg="#DBE8FF")
kretaLogoLabel.place(x=93,y=244)

szoveg1 = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="black",text="Új beírt jegyek:",font=('Inter',18,'bold'))
szoveg1.place(x=69,y=76,width=179,height=29)
jegy1Text = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="#1E1E1E",text="Matematika",font=('Inter',16,'bold'),anchor='w')
jegy1Text.place(x=108,y=140,width=200,height=21)
jegy1Num = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="black",text="3",font=('Inter',16,'bold'))
jegy1Num.place(x=279,y=140,width=14,height=21)
jegy2Text = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="#1E1E1E",text="Informatika",font=('Inter',16,'bold'),anchor='w')
jegy2Text.place(x=108,y=202,width=200,height=21)
jegy2Num = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="black",text="5",font=('Inter',16,'bold'))
jegy2Num.place(x=279,y=202,width=14,height=21)
jegy3Text = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="#1E1E1E",text="Kémia",font=('Inter',16,'bold'),anchor='w')
jegy3Text.place(x=108,y=264,width=200,height=21)
jegy3Num = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="black",text="2",font=('Inter',16,'bold'))
jegy3Num.place(x=279,y=264,width=14,height=21)

#Második kicsi kocka
kretaLogoLabel = tk.Label(canvas_kezdDiak, image=kicsiKocka,bg="#ACC8FF")
kretaLogoLabel.place(x=424,y=62)

szoveg1 = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="black",text="Átlag:",font=('Inter',18,'bold'))
szoveg1.place(x=538,y=76,width=72,height=29)

atlagNagy = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="green",text="4,2",font=('Inter',80,'bold'),anchor="center")
atlagNagy.place(x=493,y=144,width=163,height=118)


#Alsó nagy kocka
kretaLogoLabel = tk.Label(canvas_kezdDiak, image=nagyKocka,bg="#ACC8FF")
kretaLogoLabel.place(x=52,y=376)

kretaLogoLabel = tk.Label(canvas_kezdDiak, image=nkKisvonal,bg="#DBE8FF")
kretaLogoLabel.place(x=65,y=433)
kretaLogoLabel = tk.Label(canvas_kezdDiak, image=nkNagyvonal,bg="#DBE8FF")
kretaLogoLabel.place(x=97,y=496)
kretaLogoLabel = tk.Label(canvas_kezdDiak, image=nkNagyvonal,bg="#DBE8FF")
kretaLogoLabel.place(x=97,y=559)

mess1 = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="black",text="Új információk:",font=('Inter',18,'bold'),anchor='w')
mess1.place(x=69,y=393,width=179,height=29)

mess1 = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="#1E1E1E",text="",font=('Inter',16,'bold'),anchor='w')
mess1.place(x=110,y=460,width=242,height=23)
mess2 = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="#1E1E1E",text="",font=('Inter',16,'bold'),anchor='w')
mess2.place(x=110,y=519,width=242,height=23)
mess3 = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="#1E1E1E",text="",font=('Inter',16,'bold'),anchor='w')
mess3.place(x=110,y=581,width=242,height=23)

mess1Text = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="black",text="",font=('Inter',16),anchor='w')
mess1Text.place(x=378,y=460,width=242,height=23)
mess2Text = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="black",text="",font=('Inter',16),anchor='w')
mess2Text.place(x=378,y=519,width=242,height=23)
mess3Text = tk.Label(canvas_kezdDiak,bg="#DBE8FF",foreground="black",text="",font=('Inter',16),anchor='w')
mess3Text.place(x=378,y=581,width=242,height=23)

#endregion

#region Jegyek oldal

canvas_jegyDiak = tk.Canvas(main,bg="#3479FF",width=800,height=700)
canvas_jegyDiak.place(x=1000,y=0)

masikOldal_jegyDiak = tk.Label(canvas_jegyDiak,bg="#ACC8FF")
masikOldal_jegyDiak.place(x=0,y=0,width=800,height=700)

canvas_jegyek = tk.Canvas(main,bg="#ACC8FF",width=800,height=700)
canvas_jegyek.place(x=1000,y=0)

frame=tk.Frame(canvas_jegyek,width=600,height=300,borderwidth=0,highlightthickness=0)
frame.pack(expand=True, fill="both", padx=100, pady=300)

canvasScrollable=tk.Canvas(frame,width=600,height=300,scrollregion=(0,0,500,1500),bg="#ACC8FF",borderwidth=0,highlightthickness=0)
vbar=tk.Scrollbar(frame,orient="vertical")
vbar.pack(side="right",fill="y")
vbar.config(command=canvasScrollable.yview)
canvasScrollable.config(width=600,height=300)
canvasScrollable.config(yscrollcommand=vbar.set)

#endregion

#region Saját profil oldal diáknak

canvas_profDiak = tk.Canvas(main,bg="#F1F1F1",width=800,height=700)
canvas_profDiak.place(x=1000,y=0)

fejlec = tk.Label(canvas_profDiak,image=profilFejlec)
fejlec.place(x=50,y=15)

adatok = tk.Label(canvas_profDiak,image=profilAdatok)
adatok.place(x=50,y=117)

valszuletes = tk.Button(canvas_profDiak,image=szuletesnapV,command=emailValtoztatas)
valszuletes["bg"] = "#F1F1F1"
valszuletes["activebackground"] = "#F1F1F1"
valszuletes["border"] = "0"
valszuletes.place(x=244,y=393)

valtelefon = tk.Button(canvas_profDiak,image=telefonV,command=telefonValtoztatas)
valtelefon["bg"] = "#F1F1F1"
valtelefon["activebackground"] = "#F1F1F1"
valtelefon["border"] = "0"
valtelefon.place(x=244,y=476)

valjelszo = tk.Button(canvas_profDiak,image=jelszoV,command=jelszoValtoztatas)
valjelszo["bg"] = "#F1F1F1"
valjelszo["activebackground"] = "#F1F1F1"
valjelszo["border"] = "0"
valjelszo.place(x=244,y=555)

kisbetusresz = tk.Label(canvas_profDiak,text="Probléma esetén kérjük küldjenek levelet az\nadmin@kamukreta.com email címre.",font=('Inter',8))
kisbetusresz.place(x=272,y=644)


profilNev = tk.Label(canvas_profDiak,bg="#C7C7C7",text="",font=('Inter',20,'bold'))
profilNev.place(x=400,y=136)

profilSzuletes = tk.Label(canvas_profDiak,bg="#C7C7C7",text="Email: ",font=('Inter',16,'bold'))
profilSzuletes.place(x=300,y=190)
profilTelefon = tk.Label(canvas_profDiak,bg="#C7C7C7",text="Telefonszám: ",font=('Inter',16,'bold'))
profilTelefon.place(x=300,y=240)
profilJelszo = tk.Label(canvas_profDiak,bg="#C7C7C7",text="Jelszó: ",font=('Inter',16,'bold'))
profilJelszo.place(x=300,y=290)

pSz = tk.Label(canvas_profDiak,bg="#C7C7C7",text="",font=('Inter',16))
pSz.place(x=380,y=190)
pT = tk.Label(canvas_profDiak,bg="#C7C7C7",text="",font=('Inter',16))
pT.place(x=450,y=240)
pJ = tk.Label(canvas_profDiak,bg="#C7C7C7",text="",font=('Inter',16),anchor="nw")
pJ.place(x=380,y=290)
#endregion

#region Üzenőfal oldal diáknak
canvas_uzenetDiak = tk.Canvas(main,bg="#FAFAFA",width=800,height=700)
canvas_uzenetDiak.place(x=1000,y=0)

fejlec = tk.Label(canvas_uzenetDiak,image=uzenetFejlec,bg="#FAFAFA")
fejlec.place(x=50,y=11)

HatterCanvas = tk.Label(canvas_uzenetDiak,image=uzenetBG,bg="#FAFAFA")
HatterCanvas.place(x=50,y=130)

frame=tk.Frame(canvas_uzenetDiak,width=660,height=480,bg="#D9D9D9")
frame.pack(expand=True, fill="both", padx=72, pady=155) #.grid(row=0,column=0)
canvas_uziScroll=tk.Canvas(frame,width=660,height=480,scrollregion=(0,0,500,1500),bg="#D9D9D9",borderwidth=0,highlightthickness=0)
vbar=tk.Scrollbar(frame,orient="vertical")
vbar.pack(side="right",fill="y")
vbar.config(command=canvas_uziScroll.yview)
canvas_uziScroll.config(width=660,height=480)
canvas_uziScroll.config(yscrollcommand=vbar.set)
canvas_uziScroll.pack(side="left",expand=True,fill="both")
#endregion

#region Órák oldal diáknak
canvas_orakDiak = tk.Canvas(main,bg="#ACC8FF",width=800,height=700,borderwidth=0,highlightthickness=0)
canvas_orakDiak.place(x=1000,y=0)

canvas_tanora = tk.Canvas(main,bg="#FAFAFA",borderwidth=0,highlightthickness=0)
canvas_tanora.place(x=1000,y=0,width=800,height=700)
tanFejlec = tk.Label(canvas_tanora,image=tantargyFejlec,bg="#FAFAFA")
tanFejlec.place(x=18,y=21)
tanNev = tk.Label(canvas_tanora,text="",bg="#3479FF",fg="white",font=('Inter',38,'bold'),anchor="center")
tanNev.place(x=36,y=26,width=730,height=61)

tanarProfilkep = tk.Label(canvas_tanora,image=tantargyTanarkep,bg="#FAFAFA")
tanarProfilkep.place(x=96,y=106)
tanarAdatok = tk.Label(canvas_tanora,text="",bg="#FAFAFA",font=('Inter',25),anchor="center")
tanarAdatok.place(x=383,y=106,width=383,height=224)

alsoKockak = tk.Label(canvas_tanora,image=szamonkeresKocka,bg="#FAFAFA")
alsoKockak.place(x=36,y=365)

visszaGomb = tk.Button(canvas_tanora,image=visszaBtn,command=visszaOrakra)
visszaGomb["bg"] = "#FAFAFA"
visszaGomb["activebackground"] = "#FAFAFA"
visszaGomb["border"] = "0"
visszaGomb.place(x=307,y=620)

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
#endregion

#endregion

#region Tanár oldal

#region Tanár oldalmenü
canvas_ToldalMenu = tk.Canvas(main,bg="#3479FF",width=200,height=700)
canvas_ToldalMenu.place(x=1000,y=0)

valasztoFelulet = tk.Label(canvas_ToldalMenu,bg="#3479FF")
valasztoFelulet.place(x=0,y=0,width=200,height=700)

kretaLogoLabel = tk.Label(canvas_ToldalMenu, image=kretaLogo,bg="#3479FF")
kretaLogoLabel.place(x=13,y=18)

kretaLogoText = tk.Label(canvas_ToldalMenu,bg="#3479FF",foreground="white",text="KRÉTA",font=('Inter',26,'bold'))
kretaLogoText.place(x=54,y=18,width=121,height=39)

Tfooldal_btn = tk.Button(canvas_ToldalMenu,image=fooldal_selected)
Tfooldal_btn["activebackground"] = "#3479FF"
Tfooldal_btn["bg"] = "#3479FF"
Tfooldal_btn["border"] = "0"
Tfooldal_btn.place(x=29,y=122)
Thianyzas_btn = tk.Button(canvas_ToldalMenu,image=hianyzasBtn)
Thianyzas_btn["bg"] = "#3479FF"
Thianyzas_btn["activebackground"] = "#3479FF"
Thianyzas_btn["border"] = "0"
Thianyzas_btn.place(x=29,y=187)
Tjegyek_btn = tk.Button(canvas_ToldalMenu,image=jegyekBtn,command=TanarJegybeiras)
Tjegyek_btn["bg"] = "#3479FF"
Tjegyek_btn["activebackground"] = "#3479FF"
Tjegyek_btn["border"] = "0"
Tjegyek_btn.place(x=29,y=242)
Tdogak_btn = tk.Button(canvas_ToldalMenu,image=dogakBtn)
Tdogak_btn["bg"] = "#3479FF"
Tdogak_btn["activebackground"] = "#3479FF"
Tdogak_btn["border"] = "0"
Tdogak_btn.place(x=29,y=297)
Tinfok_btn = tk.Button(canvas_ToldalMenu,image=infokBtn)
Tinfok_btn["bg"] = "#3479FF"
Tinfok_btn["activebackground"] = "#3479FF"
Tinfok_btn["border"] = "0"
Tinfok_btn.place(x=29,y=352)
Tprofil_btn = tk.Button(canvas_ToldalMenu,image=profilBtn)
Tprofil_btn["bg"] = "#3479FF"
Tprofil_btn["activebackground"] = "#3479FF"
Tprofil_btn["border"] = "0"
Tprofil_btn.place(x=29,y=407)
Tkijelent_btn = tk.Button(canvas_ToldalMenu,image=kijelentBtn)
Tkijelent_btn["bg"] = "#3479FF"
Tkijelent_btn["activebackground"] = "#3479FF"
Tkijelent_btn["border"] = "0"
Tkijelent_btn.place(x=20,y=659)
#endregion

#region Tanár kezdőoldal
canvas_TKezdolap = tk.Canvas(main,bg="#FAFAFA",width=800,height=700)
canvas_TKezdolap.place(x=1000,y=0)
#endregion

#region Tanár hiányzás oldal
canvas_THianyzas = tk.Canvas(main,bg="#FAFAFA",width=800,height=700)
canvas_THianyzas.place(x=1000,y=0)
#endregion

#region Tanár jegybeírás oldal
canvas_TJegy = tk.Canvas(main,bg="#FAFAFA")
canvas_TJegy.place(x=1000,y=0,width=800,height=700)

frame_TJegy=tk.Frame(canvas_TJegy,width=700,height=550,borderwidth=0,highlightthickness=0)
frame_TJegy.pack(expand=True, fill="both", padx=10, pady=(100,0))

canvasScrollable_TJegy=tk.Canvas(frame_TJegy,width=700,height=550,scrollregion=(0,0,500,1500),bg="#FAFAFA",borderwidth=0,highlightthickness=0)
vbar=tk.Scrollbar(frame_TJegy,orient="vertical")
vbar.pack(side="right",fill="y")
vbar.config(command=canvasScrollable_TJegy.yview)
canvasScrollable_TJegy.config(width=700,height=550)
canvasScrollable_TJegy.config(yscrollcommand=vbar.set)
#endregion

#endregion

main.mainloop()