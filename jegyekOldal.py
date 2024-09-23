import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
import ctypes
import math

diakID = ""

con = mysql.connector.connect( host="localhost", user="root", password="", database="kreta_klon")
cursor = con.cursor()

lines = []
numbers = []

def backToJegyek():
    global canvas_jegyek
    global lines
    global canvas

    canvas_jegyek.delete("all")
    canvas.delete("all")
    
    for i in range(0,len(lines)):
        canvas_jegyek.delete(lines[i])

    for i in range(0,len(numbers)):
        numbers[i].destroy()

    canvas_jegyDiak.place(x=0,y=0)
    canvas_jegyek.place(x=1000,y=0)


def skidaddle(tanId):
    tanuloTanJegyek = f"SELECT beirt_jegy,jegy_ido FROM `jegy` inner join tanora on tanora.tanora_id = jegy.tanora_id where jegy.diak_id = 1237658 and tanora.tantargy_id = {tanId} ORDER BY jegy.jegy_ido DESC;"
    cursor.execute(tanuloTanJegyek)
    TanJegyek = cursor.fetchall()
    nums = []
    for i in range(0,len(TanJegyek)): 
        nums.append(TanJegyek[i][0])
        label1 = tk.Label(canvas,image=jegyekBeirva,bg="#ACC8FF")
        canvas.create_window(300, 50+i*70, window=label1)

        jegyLabel = tk.Label(canvas,font=('Inter',20,'bold'),text=TanJegyek[i][1],bg="#D9D9D9")
        canvas.create_window(150, 50+i*70, window=jegyLabel)

        jegyElvImg = tk.Label(canvas, image=jegyElvalaszto,bg="#D9D9D9")
        canvas.create_window(250, 50+i*70, window=jegyElvImg)

        jegyElvImg2 = tk.Label(canvas, image=jegyElvalaszto,bg="#D9D9D9")
        canvas.create_window(450, 50+i*70, window=jegyElvImg2)

        jegyNum = tk.Label(canvas,font=('Inter',20,'bold'),text=TanJegyek[i][0],bg="#D9D9D9")
        canvas.create_window(500, 50+i*70, window=jegyNum)

    canvas_jegyek.create_image(74,15,anchor="nw",image=nagyKocka)

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

    canvas["scrollregion"]=(0,0,500,40+len(TanJegyek)*70)
    canvas.pack(side="left",expand=True,fill="both")

    visszaBtn = tk.Button(canvas_jegyek,text="Vissza",command=backToJegyek)
    visszaBtn.place(x=350,y=620,width=100,height=50)

    canvas_jegyDiak.place(x=1000,y=0)
    canvas_jegyek.place(x=0,y=0)

main = tk.Tk()
main.geometry("800x700")
main.resizable(False, False)
main.title("Kréta")

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

canvas_jegyDiak = tk.Canvas(main,bg="#3479FF",width=800,height=700)
canvas_jegyDiak.place(x=0,y=0)

masikOldal_jegyDiak = tk.Label(canvas_jegyDiak,bg="#ACC8FF")
masikOldal_jegyDiak.place(x=0,y=0,width=800,height=700)

tanuloTantargyak = "SELECT tantargy.tantargy_id, tantargy.tantargy_nev FROM `diak` inner join osztaly on osztaly.osztaly_id = diak.diak_osztaly INNER JOIN tanora on tanora.osztaly_id = osztaly.osztaly_id inner join tantargy on tantargy.tantargy_id = tanora.tantargy_id where diak.diak_id = 1237658;"
cursor.execute(tanuloTantargyak)
Tantargyak = cursor.fetchall()
for i in range(0,len(Tantargyak)):
    tanId = str(Tantargyak[i][0])
    if i%2 == 0:
        tantargyGomb = tk.Button(canvas_jegyDiak,image=tantargyKocka,command= lambda e = tanId:skidaddle(e))
        tantargyGomb["bg"] = "#ACC8FF"
        tantargyGomb["activebackground"] = "#ACC8FF"
        tantargyGomb["border"] = "0"
        tantargyGomb.place(x=70,y=100+math.floor(i/2)*130)
        tantargyNev = tk.Label(canvas_jegyDiak,bg="#DBE8FF",foreground="black",text=Tantargyak[i][1],font=('Inter',20,'bold'))
        tantargyNev.place(x=84,y=120+math.floor(i/2)*130,width=208,height=28)
        tantargyNev.bind("<Button-1>", lambda e,id = tanId : skidaddle(id))
        atlagKep = tk.Label(canvas_jegyDiak,bg="#DBE8FF")
        atlagKep.place(x=300,y=107+math.floor(i/2)*130)
        atlagKep.bind("<Button-1>", lambda e,id = tanId : skidaddle(id))

        tanuloTanAtlag = f"SELECT ROUND(AVG(beirt_jegy),1) FROM `jegy` inner join tanora on tanora.tanora_id = jegy.tanora_id where jegy.diak_id = 1237658 and tanora.tantargy_id = {tanId};"
        cursor.execute(tanuloTanAtlag)
        TanAtlag = cursor.fetchall()
        atlag = TanAtlag[0][0]
        atlagText = tk.Label(canvas_jegyDiak,text=atlag,font=('Inter',18,'bold'))
        atlagText.place(x=309,y=119+math.floor(i/2)*130)
        atlagText.bind("<Button-1>", lambda e,id = tanId : skidaddle(id))
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

    else:
        tantargyGomb = tk.Button(canvas_jegyDiak,image=tantargyKocka,command=lambda e = tanId:skidaddle(e))
        tantargyGomb["bg"] = "#ACC8FF"
        tantargyGomb["activebackground"] = "#ACC8FF"
        tantargyGomb["border"] = "0"
        tantargyGomb.place(x=418,y=100+math.floor(i/2)*130)
        tantargyNev = tk.Label(canvas_jegyDiak,bg="#DBE8FF",foreground="black",text=Tantargyak[i][1],font=('Inter',20,'bold'))
        tantargyNev.place(x=432,y=120+math.floor(i/2)*130,width=208,height=28)
        tantargyNev.bind("<Button-1>", lambda e,id = tanId : skidaddle(id))
        atlagKep = tk.Label(canvas_jegyDiak,bg="#DBE8FF")
        atlagKep.place(x=648,y=107+math.floor(i/2)*130)
        atlagKep.bind("<Button-1>", lambda e,id = tanId : skidaddle(id))

        tanuloTanAtlag = f"SELECT ROUND(AVG(beirt_jegy),1) FROM `jegy` inner join tanora on tanora.tanora_id = jegy.tanora_id where jegy.diak_id = 1237658 and tanora.tantargy_id = {tanId};"
        cursor.execute(tanuloTanAtlag)
        TanAtlag = cursor.fetchall()
        atlag = TanAtlag[0][0]
        atlagText = tk.Label(canvas_jegyDiak,text=atlag,font=('Inter',18,'bold'))
        atlagText.place(x=657,y=119+math.floor(i/2)*130)
        atlagText.bind("<Button-1>", lambda e,id = tanId : skidaddle(id))
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

canvas_jegyek = tk.Canvas(main,bg="#ACC8FF",width=800,height=700)
canvas_jegyek.place(x=1000,y=0)

frame=tk.Frame(canvas_jegyek,width=600,height=300,borderwidth=0,highlightthickness=0)
frame.pack(expand=True, fill="both", padx=100, pady=300)

canvas=tk.Canvas(frame,width=600,height=300,scrollregion=(0,0,500,1500),bg="#ACC8FF",borderwidth=0,highlightthickness=0)
vbar=tk.Scrollbar(frame,orient="vertical")
vbar.pack(side="right",fill="y")
vbar.config(command=canvas.yview)
canvas.config(width=600,height=300)
canvas.config(yscrollcommand=vbar.set)

main.mainloop()