import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
import ctypes
import math

diakID = ""

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

frame=tk.Frame(canvas_uzenetDiak,width=650,height=480,bg="#D9D9D9")
frame.pack(expand=True, fill="both", padx=72, pady=155) #.grid(row=0,column=0)
canvas=tk.Canvas(frame,width=650,height=480,scrollregion=(0,0,500,1500),bg="#D9D9D9",borderwidth=0,highlightthickness=0)
vbar=tk.Scrollbar(frame,orient="vertical")
vbar.pack(side="right",fill="y")
vbar.config(command=canvas.yview)
canvas.config(width=650,height=480)
canvas.config(yscrollcommand=vbar.set)
canvas.pack(side="left",expand=True,fill="both")

main.mainloop()