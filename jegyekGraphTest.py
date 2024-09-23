import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
import ctypes

main = tk.Tk()
ctypes.windll.shcore.SetProcessDpiAwareness(1)
main.geometry("1000x700")
main.resizable(False, False)
main.title("Kréta - Kezdőlap")

nums = [5,1,1,1,3,5,2,4,5,2]

canvas_bej = tk.Canvas(main,bg="#3479FF",width=1000,height=700)
canvas_bej.place(x=0,y=0)

ugras = 800/len(nums)
l = nums[0]
for i in range(1,len(nums)+1):
    print(i)
    ujl = round(sum(nums[:i])/len(nums[:i]),2)
    canvas_bej.create_line(ugras*i+100,600-l*100,ugras*(i+1)+100,600-ujl*100,fill="red")
    avgNum = tk.Label(canvas_bej,bg="#3479FF",foreground="white",text=str(ujl),font=('Inter',10))
    avgNum.place(x=ugras*(i+1)+80,y=560-ujl*100)
    l=sum(nums[:i])/len(nums[:i])

main.mainloop()