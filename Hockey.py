from tkinter import *
from Puck import *
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
puck = Puck(canvas, paddle, paddle2, score, brick, 'white')



while not (puck.hit_bottom or puck.hit_top):
    if (paddle.started or paddle2.started) is True:
        puck.draw()
        paddle.draw()
        paddle2.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
canvas.create_text(250, 200, text='Game over', font=('Courier', 15), fill='Red')
tk.update_idletasks()
tk.update()
time.sleep(1)


#lbl = Label(tk, text="Вы достигли дна", font=("Arial Bold", 50))
#lbl.draw()
#tk.update_idletasks()
#tk.update()
