import tkinter as tk
from game import Game

class BatalhaNaval(tk.Tk):
    def __init__(self, *args, **kw):
        tk.Tk.__init__(self, *args, **kw)
        game = Game(self)
        game.pack()

    def changeScreen(self, screen):
        self.screen = screen
        self.screen.pack()
                

if __name__ == "__main__":
    game = BatalhaNaval()
    game.title('Batalha Naval')    
    game.mainloop()