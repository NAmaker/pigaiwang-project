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

    def clicked2(self, ):
        self.x = 2

# trans = Gui_trans("你输入是作文是英文还是中文？1是英文，2是中文")
# trans=trans.x
