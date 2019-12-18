from tkinter import *
import random
import time
from Game import *
from Easy import *



tk = Tk()
tk.title("Game 1.0")
tk.geometry('600x400')
lbl = Label(tk, text="MENU", font=("Arial Bold", 50))
lbl.grid(column=4, row=0)


#canvas = Canvas(tk, highlightthickness=0)
#canvas.pack()
#у каждого видимого элемента будут свои отдельные координаты


btn = Button(tk, text="easy", width=30, height=5, fg='green')
btn.grid(column=5, row=2)
btn.bind("<Button-1>", easy)
btn = Button(tk, text="mid", width=30, height=5, fg='orange')
btn.grid(column=5, row=4)
btn.bind("<Button-1>", mid)
btn = Button(tk, text="hard", width=30, height=5, fg='red')
btn.grid(column=5, row=6)
btn.bind("<Button-1>", hard)
tk.mainloop()

