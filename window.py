from tkinter import *

window = Tk()
window.title("Game 1.0")
window.geometry('800x600')


lbl = Label(window, text="MENU", font=("Arial Bold", 50))
lbl.grid(column=4, row=0)
btn = Button(window, text="easy", fg='green')
btn.grid(column=4, row=2)
btn = Button(window, text="mid", fg='orange')
btn.grid(column=4, row=4)
btn = Button(window, text="hard", fg='red')
btn.grid(column=4, row=6)
window.mainloop()

