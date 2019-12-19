from tkinter import *
from Ball import *
from Paddle import *
from score import *
from Brick import *
import time

global start_game

def start(event):
    start_game=True

tk = Tk()
tk.title('Game')
canvas = Canvas(tk, width=500, height=400, highlightthickness=0, bg ='black')
canvas.pack()
tk.update()

score0 = Score(10, canvas, 'turquoise')
score1 = Score(450, canvas, 'turquoise')

PADDLES = []
PADDLES.append(Paddle(canvas, 'yellow', 10, '<KeyPress-w>', '<KeyPress-s>'))
PADDLES.append(Paddle(canvas, 'yellow', 480, '<KeyPress-Up>', '<KeyPress-Down>'))

ball = Ball(canvas, PADDLES, 'white')

start_game = True
canvas.bind_all('<KeyPress-Return>', start)

while True:
    if start_game  is True:
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
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
canvas.create_text(250, 200, text='Вы достигли дна', font=('Courier', 15), fill='Red')
tk.update_idletasks()
tk.update()
time.sleep(3)