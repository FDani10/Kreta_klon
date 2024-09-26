import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
import ctypes
import math

diakID = "1237658"

con = mysql.connector.connect( host="localhost", user="root", password="", database="kreta_klon")
cursor = con.cursor()

main = tk.Tk()
main.geometry("800x700")
main.resizable(False, False)
main.title("Kréta")

image_btn=Image.open(f'./pics/uzenetBG.png')
img_btn=image_btn.resize((700, 530))
uzenetBG=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/uzenetTartalom.png')
img_btn=image_btn.resize((650, 95))
uzenetTartalom=ImageTk.PhotoImage(img_btn)
image_btn=Image.open(f'./pics/uzenetFejlec.png')
img_btn=image_btn.resize((700, 75))
uzenetFejlec=ImageTk.PhotoImage(img_btn)

canvas_uzenetDiak = tk.Canvas(main,bg="#FAFAFA",width=800,height=700)
canvas_uzenetDiak.place(x=0,y=0)

fejlec = tk.Label(canvas_uzenetDiak,image=uzenetFejlec,bg="#FAFAFA")
fejlec.place(x=50,y=11)

HatterCanvas = tk.Label(canvas_uzenetDiak,image=uzenetBG,bg="#FAFAFA")
HatterCanvas.place(x=50,y=130)

frame=tk.Frame(canvas_uzenetDiak,width=660,height=480,bg="#D9D9D9")
frame.pack(expand=True, fill="both", padx=72, pady=155) #.grid(row=0,column=0)
canvas=tk.Canvas(frame,width=660,height=480,scrollregion=(0,0,500,1500),bg="#D9D9D9",borderwidth=0,highlightthickness=0)
vbar=tk.Scrollbar(frame,orient="vertical")
vbar.pack(side="right",fill="y")
vbar.config(command=canvas.yview)
canvas.config(width=660,height=480)
canvas.config(yscrollcommand=vbar.set)
canvas.pack(side="left",expand=True,fill="both")

querry = f"SELECT tanar.tanar_nev,uzenet.uzenet_targy, LEFT(uzenet.uzenet_text,70) FROM `diak` inner join osztaly on osztaly.osztaly_id = diak.diak_osztaly INNER JOIN uzenetkinek on uzenetkinek.osztaly_id = osztaly.osztaly_id inner JOIN uzenet on uzenet.uzenet_id = uzenetkinek.uzenet_id inner JOIN tanar on tanar.tanar_id = uzenet.tanar_id WHERE diak_id = {diakID};"
cursor.execute(querry)
uzenetek = cursor.fetchall()
for i in range(0,len(uzenetek)):
    uzenet = tk.Label(canvas,image=uzenetTartalom,bg="#D9D9D9")
    canvas.create_window(328, 70+i*120, window=uzenet)

    uzenet_targy = tk.Label(canvas,bg="#F4F3F3",text=f"{uzenetek[i][0]} | {uzenetek[i][1]}",font=('Inter',20,'bold'))
    canvas.create_window(20, 50+i*120, window=uzenet_targy,anchor="w")

    uzenet_targy = tk.Label(canvas,bg="#F4F3F3",text=f"{uzenetek[i][2]}",font=('Inter',12))
    canvas.create_window(20, 80+i*120, window=uzenet_targy,anchor="w")
    if len(uzenetek[i][2]) == 70:
        uzenet_targy["text"] = f"{uzenetek[i][2]}..."
canvas["scrollregion"]=(0,0,500,len(uzenetek)*120+70)

main.mainloop()