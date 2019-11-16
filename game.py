import tkinter as tk
from buttonNavio import ButtonNavio
from tkinter import messagebox


class Game(tk.Frame):
    
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.controller = master
        self.navio_num = 0
        self.change_wids = []
        self.colors = 'cyan', 'blue' # Informe aqui as cores dos retângulos
        self.navios = [5, 4, 9, 3, 2] # Informe aqui o tamanho dos navios
        self.create_widgets()
        
    def create_widgets(self):
        for x in range(10):
            for y in range(10):
                b = ButtonNavio(master=self, bg=self.colors[(x+y)%2], width=4, height=2)
                b.grid(column=x, row=y)
                b.bind('<Enter>', self.motion)
                b.bind('<ButtonPress>', self.press)
    
    def press(self, event):
        for wid in self.change_wids:
            if wid[0].navio:
                return None
            wid[0].navio = True
            
        self.navio_num += 1

        wid = event.widget
        wid['bg'] = 'green' if wid.navio else 'black'
        if self.win():
            messagebox.showinfo("Title", f"Parabéns, Marinheiro! Você afundou todos os {len(self.navios)} navios estrangeiros!")

            self.controller.changeScreen(Game(self.controller))
            self.destroy()
    
    def motion(self, event):
        if self.navio_num <= len(self.navios):
            for wid, color in self.change_wids:
                wid['bg'] = color
            
            while len(self.change_wids) > 0:
                self.change_wids.pop()

            widget = event.widget
            info = widget.grid_info()
            try:
                navio = self.navios[self.navio_num]
            except IndexError:
                navio = 0
            c = -1
            for x in range(navio):
                wid = self.find_in_grid(info['row'], info['column']+x)
                if wid == None:
                    wid = self.find_in_grid(info['row'], info['column']+c)
                    c -= 1
                self.change_wids.append((wid, wid['bg']))
                
                wid['bg'] = 'white'        
 

    def find_in_grid(self, row, column):
        for children in self.children.values():
            info = children.grid_info()
            if info['row'] == row and info['column'] == column:
                return children

    def win(self):
        total_navios = 0
        total_widgets_verdes = 0
        for wid in self.children.values():
 
            if wid.navio:
                total_navios += 1
            if wid['bg'] == 'green':
                total_widgets_verdes += 1
            
        if total_navios == total_widgets_verdes:
            return True
        return False
