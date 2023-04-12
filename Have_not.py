
from tkinter import *



class Have_not():
    x = None

    def __init__(self):

        window = Tk()
        f = IntVar()
        f.set(0)
        self.window = window
        self.window.title("是已经完成还是没完成？")
        self.window.geometry("700x250")
        rad1 = Radiobutton(self.window, text="完成", var=f, value=1, width=10, command=self.clicked1)
        rad2 = Radiobutton(self.window, text="未完成", var=f, value=2, width=10, command=self.clicked2)
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

