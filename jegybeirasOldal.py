import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
import ctypes
import math

con = mysql.connector.connect( host="localhost", user="root", password="", database="kreta_klon")
cursor = con.cursor()

jegyek = []

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

var1 = tk.StringVar()
var1.set(None)

canvas_Jegyiras = tk.Canvas(main,bg="#FAFAFA")
canvas_Jegyiras.place(x=0,y=0,width=800,height=700)

jegy1 = tk.Radiobutton(canvas_Jegyiras,image=jegy1_unS,variable=var1,value=1,command=lambda:print(1),indicatoron=0,borderwidth=0,highlightthickness=0)
jegy1["bg"] = "#FAFAFA"
jegy1["activebackground"] = "#FAFAFA"
jegy1["border"] = "0"
jegy1.place(x=100,y=100)

csik1 = tk.Label(canvas_Jegyiras,image=jegyCsik,borderwidth=0,highlightthickness=0)
csik1.place(x=155,y=102)

jegy2 = tk.Radiobutton(canvas_Jegyiras,image=jegy2_unS,variable=var1,value=2,command=lambda:print(2),indicatoron=0,borderwidth=0,highlightthickness=0)
jegy2["bg"] = "#FAFAFA"
jegy2["activebackground"] = "#FAFAFA"
jegy2["border"] = "0"
jegy2.place(x=157,y=100)

csik2 = tk.Label(canvas_Jegyiras,image=jegyCsik,borderwidth=0,highlightthickness=0)
csik2.place(x=214,y=102)

jegy3 = tk.Radiobutton(canvas_Jegyiras,image=jegy3_unS,variable=var1,value=3,command=lambda:print(3),indicatoron=0,borderwidth=0,highlightthickness=0)
jegy3["bg"] = "#FAFAFA"
jegy3["activebackground"] = "#FAFAFA"
jegy3["border"] = "0"
jegy3.place(x=216,y=100)

csik3 = tk.Label(canvas_Jegyiras,image=jegyCsik,borderwidth=0,highlightthickness=0)
csik3.place(x=271,y=102)

jegy4 = tk.Radiobutton(canvas_Jegyiras,image=jegy4_unS,variable=var1,value=4,command=lambda:print(4),indicatoron=0,borderwidth=0,highlightthickness=0)
jegy4["bg"] = "#FAFAFA"
jegy4["activebackground"] = "#FAFAFA"
jegy4["border"] = "0"
jegy4.place(x=273,y=100)

csik4 = tk.Label(canvas_Jegyiras,image=jegyCsik,borderwidth=0,highlightthickness=0)
csik4.place(x=328,y=102)

jegy5 = tk.Radiobutton(canvas_Jegyiras,image=jegy5_unS,variable=var1,value=5,command=lambda:print(5),indicatoron=0,borderwidth=0,highlightthickness=0)
jegy5["bg"] = "#FAFAFA"
jegy5["activebackground"] = "#FAFAFA"
jegy5["border"] = "0"
jegy5.place(x=330,y=100)

jegyek.append(jegy1)

main.mainloop()