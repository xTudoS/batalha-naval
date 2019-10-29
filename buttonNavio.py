import tkinter as tk

class ButtonNavio(tk.Button):
    
    def __init__(self, master=None, *args, **kw):
        super().__init__(master, *args, **kw)
        self.navio = False