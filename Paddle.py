import random
class Paddle:

     # Описание платформы для игры

    def __init__(self, canvas, color):

        # canvas означает, что платформа будет нарисована на нашем изначальном холсте

        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        start_1 = [40, 60, 90, 120, 150, 180, 200]# список возможных стартовых положений платформы
        random.shuffle(start_1)
        self.starting_point_x = start_1[0]#стартовое положение
        self.canvas.move(self.id, self.starting_point_x, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()#ширина платформы
        #обработка жмяканий
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)

        self.started = False
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)


    def turn_right(self, event):
        self.x = 4


    def turn_left(self, event):
        self.x = -4
        self.x = -4



    def start_game(self, event):#запуск игры
        self.started = True



    def draw(self):#движение платформы
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)#координаты
        if pos[0] <= 0:#крайние положения - левая стена
            self.x = 0
        elif pos[2] >= self.canvas_width:#правая
            self.x = 0