import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
import ctypes
import math

diakID = "1237658"

con = mysql.connector.connect( host="localhost", user="root", password="", database="kreta_klon")
cursor = con.cursor()


def oraMegjelenites(oraId):
    tantargyLekerdezes = f"SELECT tantargy.tantargy_nev,tanar.tanar_nev,tanar.tanar_email,tanar.tanar_telefon FROM `tanora` inner JOIN tanar on tanar.tanar_id = tanora.tanar_id inner JOIN tantargy on tantargy.tantargy_id = tanora.tantargy_id WHERE tanora_id = {oraId};"
    cursor.execute(tantargyLekerdezes)
    Tanora = cursor.fetchall()

    szamonkeresekLekerdez = f"SELECT szamonkeres.szamonkeres_text,szamonkeres.szamonkeres_datum FROM `osztaly` inner JOIN tanora on tanora.osztaly_id = osztaly.osztaly_id inner JOIN szamonkeres on szamonkeres.tanora_id = tanora.tanora_id where tanora.tanora_id = {oraId};"
    cursor.execute(szamonkeresekLekerdez)
    Szamonkeresek = cursor.fetchall()
    print(oraId)

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

canvas_jegyDiak = tk.Canvas(main,bg="#ACC8FF",width=800,height=700,borderwidth=0,highlightthickness=0)
canvas_jegyDiak.place(x=0,y=0)

tanuloTantargyak = f"SELECT tanora.tanora_id, tantargy.tantargy_nev FROM `diak` inner join osztaly on osztaly.osztaly_id = diak.diak_osztaly INNER JOIN tanora on tanora.osztaly_id = osztaly.osztaly_id inner join tantargy on tantargy.tantargy_id = tanora.tantargy_id where diak.diak_id = {diakID};"
cursor.execute(tanuloTantargyak)
Tantargyak = cursor.fetchall()
for i in range(0,len(Tantargyak)):
    oraId = Tantargyak[i][0]
    if i%2 == 0:
        tantargyGomb = tk.Button(canvas_jegyDiak,image=tantargyKocka,command= lambda e = oraId : oraMegjelenites(e))
        tantargyGomb["bg"] = "#ACC8FF"
        tantargyGomb["activebackground"] = "#ACC8FF"
        tantargyGomb["border"] = "0"
        tantargyGomb.place(x=70,y=100+math.floor(i/2)*130)
        tantargyNev = tk.Label(canvas_jegyDiak,bg="#DBE8FF",foreground="black",text=Tantargyak[i][1],font=('Inter',20,'bold'))
        tantargyNev.bind("<Button-1>", lambda e,id = oraId : oraMegjelenites(id))
        tantargyNev.place(x=124,y=120+math.floor(i/2)*130,width=208,height=28)
    else:
        tantargyGomb = tk.Button(canvas_jegyDiak,image=tantargyKocka,command= lambda e = oraId : oraMegjelenites(e))
        tantargyGomb["bg"] = "#ACC8FF"
        tantargyGomb["activebackground"] = "#ACC8FF"
        tantargyGomb["border"] = "0"
        tantargyGomb.place(x=418,y=100+math.floor(i/2)*130)
        tantargyNev = tk.Label(canvas_jegyDiak,bg="#DBE8FF",foreground="black",text=Tantargyak[i][1],font=('Inter',20,'bold'))
        tantargyNev.bind("<Button-1>", lambda e,id = oraId : oraMegjelenites(id))
        tantargyNev.place(x=472,y=120+math.floor(i/2)*130,width=208,height=28)

canvas_tanora = tk.Canvas(main,bg="#FAFAFA",width=800,height=700,borderwidth=0,highlightthickness=0)
canvas_tanora.place(x=1000,y=0)


main.mainloop()