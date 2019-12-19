class Menu:

    def __init__(self, canvas):
        self.is_game_start = False
        self.is_quit = False
        self.pivod = 0

        self.canvas = canvas
        self.start_game_btn_id = self.canvas.create_text(250, 200, text="Start", font=('Courier', 25), fill='green')
        self.quit_btn_id = self.canvas.create_text(250, 260, text="Quit", font=('Courier', 25), fill='red')
        self.pivod_id = canvas.create_rectangle(200, 195, 205, 200, fill='yellow')

        self.canvas.bind_all('<KeyPress-Up>', self.menu_up)
        self.canvas.bind_all('<KeyPress-Down>', self.menu_down)
        self.canvas.bind_all('<KeyPress-Return>', self.check)

    def __update_controls(self):
        self.canvas.bind_all('<KeyPress-Up>', self.menu_up)
        self.canvas.bind_all('<KeyPress-Down>', self.menu_down)

    def show(self):
        self.start_game_btn_id = self.canvas.create_text(250, 200, text="Start", font=('Courier', 25), fill='green')
        self.quit_btn_id = self.canvas.create_text(250, 260, text="Quit", font=('Courier', 25), fill='red')
        self.pivod_id = self.canvas.create_rectangle(200, 195, 205, 200, fill='yellow')
        self.pivod = 0

    def hide(self):
        self.canvas.delete(self.start_game_btn_id)
        self.canvas.delete(self.quit_btn_id)
        self.canvas.delete(self.pivod_id)

    def stop_game_mode(self):
        self.is_game_start = False
        self.__update_controls()
        self.show()

    def is_exit(self):
        return self.is_quit

    def is_game_mode(self):
        return self.is_game_start

    def check(self, event):
        if self.pivod == 0:
            self.is_game_start = True
            self.hide()
        elif self.pivod == 1:
            self.is_quit = True

    def menu_up(self, event):
        if self.pivod > 0:
            self.pivod -= 1
            self.canvas.move(self.pivod_id, 0, -60)
    
    def menu_down(self, event):
        if self.pivod < 1:
            self.pivod += 1
            self.canvas.move(self.pivod_id, 0, 60)