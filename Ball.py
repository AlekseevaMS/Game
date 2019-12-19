import random
class Ball:

    # Описание шарика для игры

    def __init__(self, canvas, paddle_list, color):
        self.canvas = canvas
        self.paddle_list = paddle_list
        
        self.id = canvas.create_oval(10,10, 25, 25, fill=color) #создаём круг радиусом 15 пикселей и закрашиваем нужным цветом
        self.canvas.move(self.id, 245, 200)
        starts = [-2, -1, 1, 2] #возможные направлений для старта
        random.shuffle(starts)
        self.vx = starts[0]#направление старта
        starts_2 = [-2, -1, -3] #возможные направлений для старта
        random.shuffle(starts_2)
        self.vy = starts_2[0]
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def destroy(self):
        self.canvas.delete(self.id)


    def hit_paddle(self, paddle, pos):# paddle (платформа)
        paddle_pos = self.canvas.coords(paddle.id)
        center = (pos[0] + pos[2])/2 , (pos[1] + pos[3])/2
        if center[0] >= paddle_pos[0] and center[0] <= paddle_pos[2]:
            if center[1] >= paddle_pos[1] and center[1] <= paddle_pos[3]:
                return True

    def draw(self):#обработка отрисовки
        self.canvas.move(self.id, self.vx, self.vy)

        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.vy *= -1
        if pos[3] >= self.canvas_height:
            self.vy *= -1

        for paddle in self.paddle_list:
            if self.hit_paddle(paddle, pos):
                self.vx *= -1

    def get_coords(self):
        pos = self.canvas.coords(self.id)
        return (pos[0] + pos[2])/2 , (pos[1] + pos[3])/2