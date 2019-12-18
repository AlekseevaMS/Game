class Score:

    # Описание счета для игры(мало ли кому-то интересно)

    def __init__(self, canvas, color):
        self.score = 0#обнуляем
        self.canvas = canvas
        self.id = canvas.create_text(450, 10, text=self.score, font=('Courier', 15), fill=color)

    #Касание платформы

    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)