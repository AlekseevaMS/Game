from tkinter import *
from Ball import *
from Paddle import *
from score import *
from Brick import *
import time
tk = Tk()
tk.title('Game')
canvas = Canvas(tk, width=500, height=400, highlightthickness=0)
canvas.pack()
tk.update()

score = Score(canvas, 'green')
paddle = Paddle(canvas, 'White')
brick = Brick(canvas, 'orange')
ball = Ball(canvas, paddle, score, brick, 'red')

while not ball.hit_bottom:
    if paddle.started == True:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)


lbl = Label(tk, text="Вы достигли дна", font=("Arial Bold", 50))
tk.update_idletasks()
tk.update()
time.sleep(3)