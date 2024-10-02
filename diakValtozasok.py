#region Változtatások funkciók
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def UjEmail():
    global emailEntry
    global canvas_email
    if(re.fullmatch(regex, emailEntry.get())):
        print("Valid Email")
        print(diakID)
    else:
        invalid = tk.Label(canvas_email,text="Rendes email címet adjon meg!",fg="red",bg="#F1F1F1",font=('Inter',10))
        invalid.place(x=65,y=185)

def emailValtoztatas():
    global emailEntry
    global canvas_email
    
    valemailmain = tk.Tk()
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

    valemailmain.mainloop()