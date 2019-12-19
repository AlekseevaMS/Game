import random
class Brick:

     # Описание кирпича для игры

     #def __init__(self, cx, cy, ccolor, r=10):
         #self.x = cx
         #self.y = cy
         #self.r = r
         #self.color = ccolor
         #self.live = 1

    def __init__(self, canvas, color):

        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 50, 10, fill=color)
        #self.live = live
        start_1 = []# список возможных стартовых положений
        for i in range(50):
            start_1.append(random.randint(60, 340))
        random.shuffle(start_1)
        self.starting_point_x = start_1[0]#стартовое положение
        start_2 = []# список возможных стартовых положений
        for i in range(50):
            start_2.append(random.randint(60, 140))
        random.shuffle(start_2)
        self.starting_point_y = start_2[0]
        self.canvas.move(self.id, self.starting_point_x, self.starting_point_y)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_width = self.canvas.winfo_width()


#    def draw(self):#движение кирпич
#        self.canvas.move(self.id, self.x, 0)
#        pos = self.canvas.coords(self.id)#координаты
#        if pos[0] <= 0:#крайние положения - левая стена
#            self.x = 2
#        elif pos[2] >= self.canvas_width:#правая
#            self.x = -2

