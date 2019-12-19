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

score = Score(canvas, 'turquoise')
paddle = Paddle(canvas, 'yellow')
#BRICKS = []
#for i in range(10):
#    BRICKS.append(Brick(canvas, 'red'))
#for i in range(10):
#    brick = BRICKS[i]
brick = Brick(canvas, 'red')
ball = Ball(canvas, paddle, score, brick, 'white')



while not ball.hit_bottom:
    if paddle.started  is True:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
canvas.create_text(250, 200, text='Вы достигли дна', font=('Courier', 15), fill='Red')
tk.update_idletasks()
tk.update()
time.sleep(3)


#lbl = Label(tk, text="Вы достигли дна", font=("Arial Bold", 50))
#lbl.draw()
#tk.update_idletasks()
#tk.update()
