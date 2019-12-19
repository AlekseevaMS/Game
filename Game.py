from tkinter import *
from Ball import *
from Paddle import *
from score import *
from Brick import *
from rrr import *
import time


tk = Tk()
tk.title('Game')
canvas = Canvas(tk, width=500, height=400, highlightthickness=0, bg ='black')
canvas.pack()
tk.update()

score = Score(canvas, 'turquoise')
paddle = Paddle(canvas, 'yellow')
paddle2 = Paddle2(canvas, 'yellow')
#BRICKS = []
#for i in range(10):
#    BRICKS.append(Brick(canvas, 'red'))
#for i in range(10):
#    brick = BRICKS[i]
brick = Brick(canvas, 'red')
ball = Ball(canvas, paddle, paddle2, score, brick, 'white')



while not ball.hit_bottom and ball.hit_top:
    if (paddle.started and paddle2.started) is True:
        ball.draw()
        paddle.draw()
        paddle2.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
time.sleep(1)


#lbl = Label(tk, text="Вы достигли дна", font=("Arial Bold", 50))
#lbl.draw()
#tk.update_idletasks()
#tk.update()
