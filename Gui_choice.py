from tkinter import *


class Gui_choice():
    x = None

    rad2 = None
    rad1 = None
    rad3 = None
    rad4 = None
    rad5 = None

    def __init__(self, fi):
        window = Tk()
        f = IntVar()
        f.set(0)
        self.window = window
        self.window.title(fi)
        self.window.geometry("350x200")
        rad1 = Radiobutton(self.window, text="第一篇", var=f, value=1, width=10, command=self.clicked1)
        rad2 = Radiobutton(self.window, text="第二篇", var=f, value=2, width=10, command=self.clicked2)
        rad3 = Radiobutton(self.window, text="第三篇", var=f, value=3, width=10, command=self.clicked3)
        rad4 = Radiobutton(self.window, text="第四篇", var=f, value=4, width=10, command=self.clicked4)
        rad5 = Radiobutton(self.window, text="第五篇", var=f, value=5, width=10, command=self.clicked5)
        rad1.grid(column=0, row=0)
        rad2.grid(column=1, row=0)
        rad3.grid(column=3, row=0)
        rad4.grid(column=0, row=1)
        rad5.grid(column=1, row=1)
        self.rad1 = rad1
        self.rad3 = rad3
        self.rad2 = rad2
        self.rad4 = rad4
        self.rad5 = rad5
        self.window.mainloop()

    def clicked1(self, ):
        self.x = 1

    def clicked2(self, ):
        self.x = 2

    def clicked3(self, ):
        self.x = 3

    def clicked4(self, ):
        self.x = 4

    def clicked5(self, ):
        self.x = 5

which = Gui_choice("输入你想写的文章数，第一篇第二篇？1，2,3,4,5")
which = which.x
