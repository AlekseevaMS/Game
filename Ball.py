import random
class Ball:

    # Описание шарика для игры

    def __init__(self, canvas, paddle, score, brick , color):
        self.canvas = canvas
        self.paddle = paddle
        self.brick = brick
        self.score = score
        self.id = canvas.create_oval(10,10, 25, 25, fill=color)#создаём круг радиусом 15 пикселей и закрашиваем нужным цветом
        self.canvas.move(self.id, 245, 100)
        starts = [-2, -1, 1, 2] #возможные направлений для старта
        random.shuffle(starts)
        self.x = starts[0]#направление старта
        starts_2 = [-2, -1, -3] #возможные направлений для старта
        random.shuffle(starts_2)
        self.y = starts_2[0]
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False#Вы достигли дна

    #касание платформы(4 координаты шарика в переменной pos (левая верхняя и правая нижняя точки))




    def hit_paddle(self, pos):# paddle (платформа)
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:# координаты касания совпадают с координатами платформы
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.score.hit()
                #коснулись
                return True



    def hit_brick(self, pos):# brick
        brick_pos = self.canvas.coords(self.brick.id)
        if (pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]) :# координаты касания совпадают с координатами платформы
            if pos[1] <= brick_pos[3] and pos[1] >= brick_pos[1]:
                self.score.hit()
                #коснулись
                return True
            if pos[3] >= brick_pos[1] and pos[3] <= brick_pos[3]:#счет
                self.score.hit()
                return True







    def draw(self):#обработка отрисовки
        self.canvas.move(self.id, self.x, self.y)
        #новые координаты шарика
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:# шарик падает сверху
            self.y *= -1#  падение
        if pos[3] >= self.canvas_height:# касание правым нижним углом дна
            self.hit_bottom = True


        if self.hit_paddle(pos) == True:#касание платформы
            self.y *= -1#шарик летит наверх



        if self.hit_brick(pos) == True:#касание кирпича
            self.y *= -1#шарик летит в противоположную сторону

        if pos[0] <= 0:#левая стенка
            self.x *= -1
        if pos[2] >= self.canvas_width:#правая
            self.x *= -1

