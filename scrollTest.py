# 3 órámba telt, mire rájöttem hogy kell ezt. No cap.

from tkinter import *
root=Tk()
root.geometry("800x700")

canvasKulso=Canvas(root,width=600,height=300,scrollregion=(0,0,500,1500))
canvasKulso.place(x=0,y=0)


frame=Frame(canvasKulso,width=600,height=300)
frame.pack(expand=True, fill=BOTH, padx=100, pady=250) #.grid(row=0,column=0)

canvas=Canvas(frame,width=600,height=300,scrollregion=(0,0,500,1500))
vbar=Scrollbar(frame,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)
canvas.config(width=600,height=300)
canvas.config(yscrollcommand=vbar.set)
canvas.pack(side=LEFT,expand=True,fill=BOTH)

label1 = Label(canvas, text="I'm gonna cry", font=("bold", 20))
canvas.create_window(160, 350, window=label1)

root.mainloop()