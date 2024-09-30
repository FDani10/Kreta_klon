import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
import ctypes
import math


con = mysql.connector.connect( host="localhost", user="root", password="", database="kreta_klon")
cursor = con.cursor()

tanarID = ""



def DiakBej():
    global diakID
    ut = username_t.get()
    pt = password_t.get()
    if(ut == "" or pt == ""):
        print("Kérem töltsön ki minden mezőt!")
    else:
        tanarInTable = 'SELECT tanar_felnev,tanar_osztaly FROM tanar WHERE tanar_felnev LIKE "'+ut+'" AND tanar_jelszo = "'+pt+'";'
        cursor.execute(tanarInTable)
        table = cursor.fetchall()
        if(len(table) == 1):
            tanarID = ut

            #hianyzasok
            osztalyTanar = f'SELECT osztaly.osztaly_nev FROM osztaly join tanora on tanora.osztaly_id = osztaly.osztaly_id join tanar on tanora.tanar_id = tanar.tanar_id where tanar_id LIKE {ut} '
            cursor.execute(osztalyTanar)
            osztalyok = cursor.fetchall
            for i in range(0,len(osztalyok)):
                tanId = str(osztalyok[i][0])
                if i%2 == 0:
                    osztalyGomb = tk.Button(canvasOsztalyok,image=osztalyGomb,command= lambda e = tanId:jegyreKattint(e))
                    osztalyGomb["bg"] = "#ACC8FF"
                    osztalyGomb["activebackground"] = "#ACC8FF"
                    osztalyGomb["border"] = "0"
                    osztalyGomb.place(x=70,y=100+math.floor(i/2)*130)
                    osztalyNev = tk.Label(canvasOsztalyok,bg="#DBE8FF",foreground="black",text=osztalyok[i][1],font=('Inter',20,'bold'))
                    osztalyNev.place(x=84,y=120+math.floor(i/2)*130,width=208,height=28)
                    osztalyNev.bind("<Button-1>", lambda e,id = tanId : jegyreKattint(id))
                    atlagKep = tk.Label(canvasOsztalyok,bg="#DBE8FF")
                    atlagKep.place(x=300,y=107+math.floor(i/2)*130)
                    atlagKep.bind("<Button-1>", lambda e,id = tanId : jegyreKattint(id))


                    cursor.execute(osztalyok)
                    osztalyNevek = cursor.fetchall()
                    nevek= osztalyNevek
                    osztalyText = tk.Label(canvasOsztalyok,text=nevek,font=('Inter',18,'bold'))
                    osztalyText.place(x=309,y=119+math.floor(i/2)*130)
                    atlagText.bind("<Button-1>", lambda e,id = tanId : jegyreKattint(id))

                else:
                    osztalyGomb = tk.Button(canvasOsztalyok,image=osztalyGomb,command=lambda e = tanId:jegyreKattint(e))
                    osztalyGomb["bg"] = "#ACC8FF"
                    osztalyGomb["activebackground"] = "#ACC8FF"
                    osztalyGomb["border"] = "0"
                    osztalyGomb.place(x=418,y=100+math.floor(i/2)*130)
                    osztalyNev = tk.Label(canvasOsztalyok,bg="#DBE8FF",foreground="black",text=Tantargyak[i][1],font=('Inter',20,'bold'))
                    osztalyNev.place(x=432,y=120+math.floor(i/2)*130,width=208,height=28)
                    osztalyNev.bind("<Button-1>", lambda e,id = tanId : jegyreKattint(id))
                    atlagKep = tk.Label(canvasOsztalyok,bg="#DBE8FF")
                    atlagKep.place(x=648,y=107+math.floor(i/2)*130)
                    atlagKep.bind("<Button-1>", lambda e,id = tanId : jegyreKattint(id))

                    tanuloTanAtlag = f"SELECT ROUND(AVG(beirt_jegy),1) FROM `jegy` inner join tanora on tanora.tanora_id = jegy.tanora_id where jegy.diak_id = {diakID} and tanora.tantargy_id = {tanId};"
                    cursor.execute(tanuloTanAtlag)
                    TanAtlag = cursor.fetchall()
                    atlag = TanAtlag[0][0]
                    atlagText = tk.Label(canvasOsztalyok,text=atlag,font=('Inter',18,'bold'))
                    atlagText.place(x=657,y=119+math.floor(i/2)*130)


hianyzas= tk.Tk()



osztalyK_btn=Image.open(f'./pics/kretalogo.png')
osztaly_btn=osztalyK_btn.resize((320, 120))
osztalyGomb=ImageTk.PhotoImage(osztaly_btn)

hianyzas.geometry("1000x700")
hianyzas.title("hianyzasok")

canvasOsztalyok = tk.Canvas(hianyzas, width=800,height=700, border=0, borderwidth=0, highlightthickness=0, bg="gray")
canvasOsztalyok.place(x=200, y=0)

username_t= tk.Entry(canvasOsztalyok)
username_t.pack()
password_t =tk.Entry(canvasOsztalyok)
password_t.pack()


btnBej = tk.Button(canvasOsztalyok, width=10, height=10, command=DiakBej)
btnBej.pack()


hianyzas.mainloop()