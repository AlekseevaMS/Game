from tkinter import *
from Ball import *
from Paddle import *
from score import *
from Brick import *
from menu import *
import time

tk = Tk()
tk.title('Game')
canvas = Canvas(tk, width=500, height=400, highlightthickness=0, bg ='black')
canvas.pack()
tk.update()


score0 = Score(10, canvas, 'turquoise')
score1 = Score(450, canvas, 'turquoise')

PADDLES = []
PADDLES.append(Paddle(canvas, 'yellow', 20, '<KeyPress-w>', '<KeyPress-s>'))
PADDLES.append(Paddle(canvas, 'yellow', 480, '<KeyPress-Up>', '<KeyPress-Down>'))

ball = Ball(canvas, PADDLES, 'white')
menu = Menu(canvas)

while not menu.is_exit():
    if menu.is_game_mode()  is True:
        for p in PADDLES:
            p.update_controls()

        ball.draw()
        PADDLES[0].draw()
        PADDLES[1].draw()

        pos = ball.get_coords()
        if pos[0] <= 0:
            score1.hit()
            ball.destroy()
            ball = Ball(canvas, PADDLES, 'white')
        
        if pos[0] >= 500:
            score0.hit()
            ball.destroy()
            ball = Ball(canvas, PADDLES, 'white')

        if score0.score >= 5:
            text0 = canvas.create_text(250, 250, text="Левый игрок победил", font=('Courier', 25), fill='green')
            text1 = canvas.create_text(250, 300, text="Правый игрок на дне", font=('Courier', 15), fill='red')

            tk.update_idletasks()
            tk.update()
            time.sleep(3)
            canvas.delete(text0, text1)
            menu.stop_game_mode()
            score0.score = score1.score = 0
        if score1.score >= 5:
            text0 = canvas.create_text(250, 250, text="Правый игрок победил", font=('Courier', 25), fill='green')
            text1 = canvas.create_text(250, 300, text="Левый игрок на дне", font=('Courier', 15), fill='red')

            tk.update_idletasks()
            tk.update()
            time.sleep(3)
            canvas.delete(text0, text1)
            menu.stop_game_mode()
            score0.score = score1.score = 0

    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

tk.update_idletasks()
tk.update()
time.sleep(3)