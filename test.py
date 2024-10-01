import tkinter as tk

root = tk.Tk()

# Create a Canvas
canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

# Create the first frame
frame1 = tk.Frame(canvas, width=100, height=100, bg='blue')
canvas.create_window(50, 100, window=frame1)  # Place frame1 at (50, 100)

# Create the second frame
frame2 = tk.Frame(canvas, width=100, height=100, bg='red')
canvas.create_window(150, 100, window=frame2)  # Place frame2 at (150, 100)

root.mainloop()