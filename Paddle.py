import random
class Paddle:

     # Описание платформы для игры

    def __init__(self, canvas, color, pos_x, command_up_key, command_down_key):

        # canvas означает, что платформа будет нарисована на нашем изначальном холсте
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 10, 100, fill=color)

        self.starting_point_x = pos_x
        self.canvas.move(self.id, self.starting_point_x, 200)

        self.vy = 0
        self.canvas_height = self.canvas.winfo_height() #высота окна
        #обработка жмяканий
        self.canvas.bind_all(command_up_key, self.turn_up)
        self.canvas.bind_all(command_down_key, self.turn_down)
        # '<KeyPress-Left>'


    def turn_up(self, event):
        self.vy = -4

    def turn_down(self, event):
        self.vy = 4

    def draw(self):#движение платформы
        pos = self.canvas.coords(self.id)#координаты
        if pos[1] <= 0 and self.vy < 0:                     # крайние положения - верх
            self.vy = 0
        elif pos[3] >= self.canvas_height and self.vy > 0:   # низ
            self.vy = 0

        self.canvas.move(self.id, 0, self.vy)