from tkinter import *


class Gui_trans():
    x = None

    def __init__(self, fi):
        window = Tk()
        f = IntVar()
        f.set(0)
        self.window = window
        self.window.title(fi)
        self.window.geometry("350x200")
        rad1 = Radiobutton(self.window, text="英文", var=f, value=1, width=10, command=self.clicked1)
        rad2 = Radiobutton(self.window, text="中文", var=f, value=2, width=10, command=self.clicked2)
        rad1.grid(column=0, row=0)
        rad2.grid(column=1, row=0)
        self.rad1 = rad1
        self.rad2 = rad2
        self.window.mainloop()

    def clicked1(self, ):
        self.x = 1
        self.window.destroy()

    def clicked2(self, ):
        self.x = 2
        self.window.destroy()

