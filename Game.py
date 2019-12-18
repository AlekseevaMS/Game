from tkinter import *
from Ball import *
from Paddle import *
from score import *
from Brick import *
import time
tk = Tk()
tk.title('Game')
canvas = Canvas(tk, width=500, height=400, highlightthickness=0, bg ='black')
canvas.pack()
tk.update()

score = Score(canvas, 'green')
paddle = Paddle(canvas, 'yellow')
brick = Brick(canvas, 'red')
ball = Ball(canvas, paddle, score, brick, 'white')

while not ball.hit_bottom:
    if paddle.started == True:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
time.sleep(1)


#lbl = Label(tk, text="Вы достигли дна", font=("Arial Bold", 50))
#lbl.draw()
#tk.update_idletasks()
#tk.update()
