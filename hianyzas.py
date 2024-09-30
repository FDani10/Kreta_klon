import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
import ctypes
import math


con = mysql.connector.connect( host="localhost", user="root", password="", database="kreta_klon")
cursor = con.cursor()

tanarID = ""

hianyzas= tk.Tk()

def DiakBej():
    global diakID
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

            #hianyzasok
            osztalyTanar = f'SELECT osztaly.osztaly_nev FROM osztaly join tanora on tanora.osztaly_id = osztaly.osztaly_id join tanar on tanora.tanar_id = tanar.tanar_id where tanar.tanar_felnev LIKE "{ut}" '
            cursor.execute(osztalyTanar)
            osztalyok = cursor.fetchall()
            print(osztalyok[0][0])
            for i in range(0,len(osztalyok)):
                tanId = str(osztalyok[i][0])
                if i%2 == 0:
                    osztalyGomb = tk.Button(canvasOsztalyok,image=osztalyGombKep,command= lambda :print("jo"))
                    osztalyGomb["bg"] = "#ACC8FF"
                    osztalyGomb["activebackground"] = "#ACC8FF"
                    osztalyGomb["border"] = "0"
                    osztalyGomb.place(x=70,y=100+math.floor(i/2)*130)
                    osztalyNev = tk.Label(canvasOsztalyok,bg="#DBE8FF",foreground="black",text=osztalyok[i][0],font=('Inter',20,'bold'))
                    osztalyNev.place(x=84,y=120+math.floor(i/2)*130,width=208,height=28)
                    osztalyNev.bind("<Button-1>", lambda :print("jo"))
                    atlagKep = tk.Label(canvasOsztalyok,bg="#DBE8FF")
                    atlagKep.place(x=300,y=107+math.floor(i/2)*130)
                    atlagKep.bind("<Button-1>", lambda :print("jo"))

                else:
                    osztalyGomb = tk.Button(canvasOsztalyok,image=osztalyGombKep,command=lambda :print("jo"))
                    osztalyGomb["bg"] = "#ACC8FF"
                    osztalyGomb["activebackground"] = "#ACC8FF"
                    osztalyGomb["border"] = "0"
                    osztalyGomb.place(x=418,y=100+math.floor(i/2)*130)
                    osztalyNev = tk.Label(canvasOsztalyok,bg="#DBE8FF",foreground="black",text=osztalyok[i][0],font=('Inter',20,'bold'))
                    osztalyNev.place(x=432,y=120+math.floor(i/2)*130,width=208,height=28)
                    osztalyNev.bind("<Button-1>", lambda :print("jo"))
                    atlagKep = tk.Label(canvasOsztalyok,bg="#DBE8FF")
                    atlagKep.place(x=648,y=107+math.floor(i/2)*130)
                    atlagKep.bind("<Button-1>", lambda :print("jo"))


osztalyK_btn=Image.open(f'./pics/osztalyGomb.png')
osztaly_btn=osztalyK_btn.resize((320, 120))
osztalyGombKep=ImageTk.PhotoImage(osztaly_btn)

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